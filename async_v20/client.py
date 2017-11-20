import asyncio
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
from .interface import *
from .interface.account import AccountInterface
from aiohttp.client_exceptions import ClientConnectionError


async def sleep(s=0.0):
    await asyncio.sleep(s)


__version__ = '2.2.1b0'


class OandaClient(AccountInterface, InstrumentInterface, OrderInterface, PositionInterface,
                  PricingInterface,
                  TradeInterface,
                  TransactionInterface, UserInterface):
    """
    Create an API context for v20 access

    Args:
        token: -- User generated token from the online account configuration page
        account_id: -- The account id the client will connect to
        max_transaction_history: -- Maximum past transactions to store
        rest_host: -- The hostname of the v20 REST server
        rest_port: -- The port of the v20 REST server
        stream_host: -- The hostname of the v20 REST server
        stream_port: -- The port of the v20 REST server
        rest_scheme: -- The scheme of the connection. Defaults to 'https'
        stream_scheme: -- The scheme of the connection. Defaults to 'https'
        datetime_format: -- The format to request when dealing with times
        poll_timeout: -- The timeout to use when making a polling request with
            the v20 REST server
        max_requests_per_second: -- Maximum HTTP requests sent per second
        max_simultaneous_connections: -- Maximum concurrent HTTP requests

    """
    headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive',
               'OANDA-Agent': 'async_v20_' + __version__}

    default_parameters = {}

    initialized = False

    initializing = False

    expected_step = None  # The first step to be called during initialization

    initialization_sleep = 0.5  # Time to poll initialized when waiting for initialization

    _account = None

    transactions = ArrayTransaction()

    session = None  # http session will be created during initialization

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

    def __init__(self, token=None, account_id=None, max_transaction_history=100,
                 rest_host='api-fxpractice.oanda.com', rest_port=443,
                 rest_scheme='https', stream_host='stream-fxpractice.oanda.com', stream_port=None,
                 stream_scheme='https', datetime_format='UNIX', poll_timeout=4, max_requests_per_second=99,
                 max_simultaneous_connections=10):

        self.version = __version__

        if token is None:
            token = os.environ['OANDA_TOKEN']

        self.account_id = account_id

        self.max_transaction_history = max_transaction_history

        # V20 REST API URL
        rest_host = partial(URL.build, host=rest_host, port=rest_port, scheme=rest_scheme)

        # v20 STREAM API URL
        stream_host = partial(URL.build, host=stream_host, port=stream_port, scheme=stream_scheme)

        self.hosts = {'REST': rest_host, 'STREAM': stream_host}

        # The timeout to use when making a polling request with the
        # v20 REST server
        self.poll_timeout = poll_timeout

        self.max_requests_per_second = max_requests_per_second

        self.max_simultaneous_connections = max_simultaneous_connections

        # This is the default parameter dictionary. OandaClient Methods that require certain parameters
        # that are  not explicitly passed will try to find it in this dict
        self.default_parameters.update(
            {Authorization: 'Bearer {}'.format(token),
             AcceptDatetimeFormat: datetime_format}
        )

    async def account(self):
        """Get updated account

        Returns:

            :class:`~async_v20.definitions.types.Account`
        """
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
        # - return close trade responses and successful/unsuccessful
        all_trades_closed = False
        response = await self.list_open_trades()
        if response:
            close_trade_responses = await asyncio.gather(*[self.close_trade(trade.id)
                                          for trade in response.trades])
        else:
            raise ConnectionError(f'Could not get open trades. '
                                  f'Server returned status {response.status}')
        # After closing all trades check that all trades have indeed been closed
        response = await self.list_open_trades()
        if response:
            if len(response.trades) == 0:
                all_trades_closed = True
        else:
            raise ConnectionError(f'Unable to confirm all trades have been closed! '
                                  f'Server returned status {response.status}')

        return all_trades_closed, close_trade_responses



    async def _request_limiter(self):
        """Wait for a minimum time interval before creating new request"""
        try:
            self._next_request_time += self._min_time_between_requests
        except AttributeError:
            self._next_request_time = time()
            return

        if self._next_request_time - time() > 0:
            await sleep(self._next_request_time - time())
        return

    async def __aenter__(self):
        await self.initialize()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __enter__(self):
        print('Warning: <with> used rather than <async with>')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        try:
            self.session.close()
        except AttributeError:
            # In case the client was never initialized
            pass

    async def initialize(self, initialization_step=False):
        """Initialize client instance

        Args:
            initialization_step: -- Used internally to allow requests to bypass
                                    initialization.

        Returns: True when complete
        """
        if self.initialized or self.expected_step == initialization_step:
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
            try:
                self.initializing = True  # immediately set initializing to make sure
                # Upcoming requests wait for this initialization to complete.

                # Create http session this client will use to sent all requests
                conn = aiohttp.TCPConnector(limit=self.max_simultaneous_connections)

                self.session = aiohttp.ClientSession(
                    json_serialize=json.dumps,
                    headers=self.headers,
                    connector=conn,
                    read_timeout=self.poll_timeout
                )

                # Get the first account listed in in accounts.
                # If another is desired the account must be configured
                # manually when instantiating the client

                if self.account_id:  # Allow manual assignment of AccountID
                    self.default_parameters.update({AccountID: self.account_id})

                else:  # Get the corresponding AccountID for the provided token

                    self.expected_step = 1  # Setting this prevents the request from
                    # waiting for initialization to complete.

                    response = await self.list_accounts()
                    if response:  # Checks is the response status was the expected status as
                        # defined by OANDA spec.
                        self.default_parameters.update({AccountID: response['accounts'][0].id})
                    else:
                        self.initializing = False
                        raise ConnectionError(f'Server did not return AccountID during '
                                              f'initialization. {response} {response.dict()}')

                # Get Account snapshot and last transaction id
                # last transaction is automatically updated when the
                # response is parsed

                self.expected_step = 2
                response = await self.get_account_details()
                if response:
                    self._account = response['account']
                else:
                    self.initializing = False
                    raise ConnectionError(f'Server did not return Account Details during '
                                          f'initialization. {response} {response.dict()}')

                # On initialization the SinceTransactionID needs updated to reflect LastTransactionID
                self.default_parameters.update({SinceTransactionID: self.default_parameters[LastTransactionID]})

                self.initializing = False
                self.initialized = True

            except TimeoutError:
                self.initializing = False
                self.initialized = False
                raise TimeoutError(f'Initialization step {self.expected_step} '
                                   f'took longer than {self.poll_timeout} seconds')
            except (ConnectionError, ClientConnectionError) as e:
                self.initializing = False
                self.initialized = False
                raise ConnectionError(e)

            # Always return True when initialization has complete
        return True