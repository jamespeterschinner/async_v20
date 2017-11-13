import asyncio
import os
import ujson as json
from functools import partial
from time import time

import aiohttp
from yarl import URL

from .definitions.types import AcceptDatetimeFormat
from .definitions.types import AccountID
from .endpoints.annotations import Authorization, SinceTransactionID, LastTransactionID
from .interface import *
from .interface.account import AccountInterface


async def sleep(s=0.0):
    await asyncio.sleep(s)


__version__ = '2.0.1a0'


class OandaClient(AccountInterface, InstrumentInterface, OrderInterface, PositionInterface,
                  PricingInterface,
                  TradeInterface,
                  TransactionInterface, UserInterface):
    """
    Create an API context for v20 access

    Args:
        token: -- User generated token from the online account configuration page
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

    # The first step to be called during initialization
    expected_step = None

    # Time to poll initialized when waiting for initialization
    initialization_sleep = 0.5

    account = None

    session = None

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

    def __init__(self, token=None, account_id=None, rest_host='api-fxpractice.oanda.com', rest_port=443,
                 rest_scheme='https',
                 stream_host='stream-fxpractice.oanda.com', stream_port=None, stream_scheme='https',
                 datetime_format='UNIX', poll_timeout=2, max_requests_per_second=99,
                 max_simultaneous_connections=10):
        # TODO: add poll timeout
        self.version = __version__

        self.initialized = False  # when a new client instance is created it must be initialized

        if token is None:
            token = os.environ['OANDA_TOKEN']

        self.account_id = account_id

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

    async def initialize(self, initialization_step=False):
        if self.initialized or self.expected_step == initialization_step:
            print('PASSING INITIALIZATION', self.expected_step, initialization_step)
            pass
        elif self.initializing:
            while not self.initialized:
                await sleep(self.initialization_sleep)
        else:  # Means an initialization is required
            self.initializing = True

            conn = aiohttp.TCPConnector(limit=self.max_simultaneous_connections)

            self.session = aiohttp.ClientSession(
                json_serialize=json.dumps,
                headers=self.headers,
                connector=conn,
                read_timeout=self.poll_timeout
            )

            # Get the first account listed in in accounts
            if self.account_id:
                self.default_parameters.update({AccountID: self.account_id})
            else:  # Get the corresponding AccountID for the provided token
                self.expected_step = 1  # Allow the expected step to pass though
                # initialization
                response = await self.list_accounts()
                if response:
                    self.default_parameters.update({AccountID: response['accounts'][0].id})
                else:
                    self.initializing = False
                    raise ConnectionError(f'Server did not return AccountID during '
                                          f'initialization. {response} {response.json_dict()}')

            # Get Account snapshot and last transaction id
            # last transaction is automatically updated when the
            # response is parsed

            self.expected_step = 2
            response = await self.get_account_details()
            if response:
                self.account = response['account']
            else:
                self.initializing = False
                raise ConnectionError(f'Server did not return Account Details during '
                                      f'initialization. {response} {response.json_dict()}')

            # On initialization the SinceTransactionID needs updated to reflect LastTransactionID
            self.default_parameters.update({SinceTransactionID: self.default_parameters[LastTransactionID]})

            self.initializing = False
            self.initialized = True

        # Always return True when initialization has complete
        return True

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
        except AttributeError:  # In case the client was never initialized
            pass
