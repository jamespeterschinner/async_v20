import asyncio
import logging
import os
import ujson as json
from functools import partial
from time import time

import aiohttp
from yarl import URL

from .definitions.types import AcceptDatetimeFormat
from .definitions.types import AccountID
from .definitions.types import ArrayTransaction
from .endpoints.annotations import Authorization, SinceTransactionID, LastTransactionID
from .exceptions import InitializationFailure, ResponseTimeout, CloseAllTradesFailure
from .interface import *
from .interface.helpers import too_many_passed_transactions

logger = logging.getLogger(__name__)


async def sleep(s=0.0):
    await asyncio.sleep(s)


__version__ = '8.0.0b1'


class OandaClient(AccountInterface, InstrumentInterface, OrderInterface, PositionInterface,
                  PricingInterface, TradeInterface, TransactionInterface, UserInterface,
                  HealthInterface):
    """
    Create an API context for v20 access

    Args:
        token: User generated token from the online account configuration page
        account_id: The account id the client will connect to. If None will default to
            the first account number returned by :meth:`~async_v20.OandaClient.list_accounts`
        format_order_requests: True=Format all OrderRequests
            in the context of the orders instrument. False=Do not format OrderRequests,
            raise :class:`~async_v20.exceptions.InvalidOrderRequest` for values outside of allowed range.
        max_transaction_history: Maximum past transactions to store
        rest_host: The hostname of the v20 REST server
        rest_port: The port of the v20 REST server
        stream_host: The hostname of the v20 REST server
        stream_port: The port of the v20 REST server
        rest_scheme: The scheme of the connection to rest server.
        stream_scheme: The scheme of the connection to the stream server.
        health_host: The hostname of the health API server
        health_port: The port of the health server
        health_scheme: The scheme of the connection for the health server.
        datetime_format: The format to request when dealing with times
        rest_timeout: The timeout to use when making a polling request with
            the v20 REST server
        stream_timeout: Period to wait for an new json object during streaming
        max_requests_per_second: Maximum HTTP requests sent per second
        max_simultaneous_connections: Maximum concurrent HTTP requests
        debug: Set to True to log debug messages.

    """
    headers = {'Connection': 'keep-alive',
               'OANDA-Agent': 'async_v20_' + __version__}

    default_parameters = {}

    initialized = False

    initializing = False

    _initialization_step = None  # The first step to be called during initialization

    initialization_sleep = 0.5  # Time to poll initialized when waiting for initialization

    _account = None

    instruments = None

    transactions = ArrayTransaction()

    session = None  # http session will be created during initialization

    _rest_timeout = None  # seconds

    @property
    def max_requests_per_second(self):
        return self._max_requests_per_second

    @max_requests_per_second.setter
    def max_requests_per_second(self, value):
        # Limit maximum concurrent connections
        self._max_requests_per_second = {True: value, False: 1}[value > 0]
        self._min_time_between_requests = 1 / self.max_requests_per_second

    @property
    def max_simultaneous_connections(self):
        return self._max_simultaneous_connections

    @max_simultaneous_connections.setter
    def max_simultaneous_connections(self, value):
        # Limit concurrent connections
        self._max_simultaneous_connections = {True: value, False: 0}[value >= 0]

    @property
    def datetime_format(self):
        return self._datetime_format

    def __init__(self,
                 token=None,
                 account_id=None,
                 format_order_requests=False,
                 max_transaction_history=100,
                 rest_host='api-fxpractice.oanda.com',
                 rest_port=443,
                 rest_scheme='https',
                 stream_host='stream-fxpractice.oanda.com',
                 stream_port=None,
                 stream_scheme='https',
                 health_host='api-status.oanda.com',
                 health_port=80,
                 health_scheme='http',
                 datetime_format='UNIX',
                 rest_timeout=10,
                 stream_timeout=60,
                 max_requests_per_second=99,
                 max_simultaneous_connections=10,
                 debug=False):

        self.version = __version__

        if token is None:
            token = os.environ['OANDA_TOKEN']

        self.account_id = account_id

        self.format_order_requests = format_order_requests

        self.max_transaction_history = max_transaction_history

        # V20 REST API URL
        rest_host = partial(URL.build, host=rest_host, port=rest_port, scheme=rest_scheme)

        # v20 STREAM API URL
        stream_host = partial(URL.build, host=stream_host, port=stream_port, scheme=stream_scheme)

        # V20 API health URL
        health_host = partial(URL.build, host=health_host, port=health_port, scheme=health_scheme)

        self._hosts = {'REST': rest_host, 'STREAM': stream_host, 'HEALTH': health_host}

        # The timeout to use when making a polling request with the
        # v20 REST server
        self.rest_timeout = rest_timeout

        # The timeout to use when waiting for the next object when wait for a stream response
        self.stream_timeout = stream_timeout

        self.max_requests_per_second = max_requests_per_second

        self.max_simultaneous_connections = max_simultaneous_connections

        self._datetime_format = datetime_format

        # This is the default parameter dictionary. OandaClient Methods that require certain parameters
        # that are  not explicitly passed will try to find it in this dict
        self.default_parameters.update(
            {Authorization: 'Bearer {}'.format(token),
             AcceptDatetimeFormat: datetime_format}
        )

        self.debug = debug

    async def account(self):
        """Get updated account

        Returns:

            :class:`~async_v20.Account`
        """
        logger.info('account()')
        if too_many_passed_transactions(self):
            await self.get_account_details()
        else:
            await self.account_changes()
        return self._account

    async def close_all_trades(self):
        """Close all open trades

        Returns:

            :class:`tuple` (:class:`bool`, [:class`~async_v20.interface.response.Response`, ...])

        """

        # Procedure is as follows:
        # - get all open trades
        # - attempt to close all open trades
        # - get all open trades again and check there there are None
        # - return close trade responses

        logger.info('close_all_trades()')
        response = await self.list_open_trades()
        if response:
            close_trade_responses = await asyncio.gather(*[self.close_trade(trade.id)
                                                           for trade in response.trades])
        else:
            msg = f'Could not get open trades. ' \
                  f'Server returned status {response.status}'
            logger.error(msg)
            raise CloseAllTradesFailure(msg)
        # After closing all trades check that all trades have indeed been closed
        response = await self.list_open_trades()
        if response and len(response.trades) == 0:
            pass
        else:
            msg = f'Unable to confirm all trades have been closed! ' \
                  f'Server returned status {response.status}'
            logger.error(msg)
            raise CloseAllTradesFailure(msg)

        return close_trade_responses

    async def _request_limiter(self):
        """Wait for a minimum time interval before creating new request"""
        try:
            self._next_request_time += self._min_time_between_requests
        except AttributeError:
            self._next_request_time = time()
            return

        if self._next_request_time - time() > 0:
            wait_time = self._next_request_time - time()
            if self.debug:
                logger.debug('Request waiting for %s seconds', wait_time)
            await sleep(wait_time)
        return

    async def __aenter__(self):
        await self.initialize()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    def __enter__(self):
        logger.warning('<with> used rather than <async with>')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    async def close(self):
        try:
            await self.session.close()
        except AttributeError:
            # In case the client was never initialized
            pass

    async def initialize_session(self):
        # Create http session this client will use to sent all requests
        logger.info('Initializing session')
        conn = aiohttp.TCPConnector(limit=self.max_simultaneous_connections)

        self.session = aiohttp.ClientSession(
            json_serialize=json.dumps,
            headers=self.headers,
            connector=conn,
            read_timeout=0  # async_v20 will handle timeouts to allow dynamic changing of timeout.
            # after client initialization
        )

    async def initialize(self, initialization_method=False):
        """Initialize client instance

        Args:
            initialization_step: -- Used internally to allow requests to bypass
                                    initialization.

        Returns: True when complete
        """
        if self.initialized or self._initialization_step == initialization_method:
            # Do not initialize or wait for initialization to complete.
            # If it did, due to circular logic, initialization would never
            # complete.
            pass

        elif self.initializing:
            # Wait for current initialization to complete before
            # continuing with request.
            while not self.initialized:
                await sleep(self.initialization_sleep)

        else:  # If it gets this far. An initialization if required.

            msg = ''  # msg is used to create a useful Error msg if Initialization fails
            try:
                logger.info('Initializing client')
                self.initializing = True  # immediately set initializing to make sure
                # Upcoming requests wait for this initialization to complete.

                # V1 REST API is deprecated
                # self._initialization_step = self.list_services.__name__
                # response = await self.list_services()
                # if response:
                #     for service in response.services:
                #         if service.current_event.status.name != 'Up':
                #             logger.warning(f'{service.name} {service.current_event.message}')
                # else:
                #     logging.warning('Server did not return available services')
                #     print(response.json())

                # Get the first account listed in in accounts.
                # If another is desired the account must be configured
                # manually when instantiating the client

                if self.account_id:  # Allow manual assignment of AccountID
                    self.default_parameters.update({AccountID: self.account_id})
                    self.account_id = self.account_id

                else:  # Get the corresponding AccountID for the provided token

                    self._initialization_step = self.list_accounts.__name__
                    response = await self.list_accounts()
                    if response:  # Checks is the response status was the expected status as
                        # defined by OANDA spec.
                        self.default_parameters.update({AccountID: response['accounts'][0].id})
                    else:
                        self.initializing = False
                        msg = f'Server did not return AccountID during initialization'
                        logger.error(msg)
                        raise InitializationFailure(msg)

                # Get Account snapshot and last transaction id
                # last transaction is automatically updated when the
                # response is parsed

                self._initialization_step = self.get_account_details.__name__
                response = await self.get_account_details()
                if response:
                    self._account = response['account']
                else:
                    self.initializing = False
                    msg = f'Server did not return Account Details during initialization.'
                    logger.error(msg)
                    raise InitializationFailure(msg)

                self._initialization_step = self.account_instruments.__name__
                response = await self.account_instruments()
                if response:
                    self.instruments = response['instruments']
                else:
                    self.initializing = False
                    msg = f'Server did not return Account Instruments during initialization'
                    logger.error(msg)
                    raise InitializationFailure(msg)

                # On initialization the SinceTransactionID needs updated to reflect LastTransactionID
                self.default_parameters.update({SinceTransactionID: self.default_parameters[LastTransactionID]})

                self.initializing = False
                self.initialized = True

            except ResponseTimeout:
                self.initializing = False
                self.initialized = False
                msg = f'Initialization step {self._initialization_step} ' \
                      f'took longer than {self.rest_timeout} seconds'
                logger.exception(msg)
                raise InitializationFailure(msg)

            except InitializationFailure:
                self.initializing = False
                self.initialized = False
                logging.exception(msg)
                raise InitializationFailure(msg)

        # Always return True when initialization has complete
        return True
