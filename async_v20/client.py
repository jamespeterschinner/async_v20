import os
from functools import partial

from yarl import URL

from .definitions.types import AcceptDatetimeFormat
from .endpoints.annotations import Authorization
from .helpers import initializer, sleep
from .interface import *
from .interface.account import AccountInterface
from time import time

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
        application: Optional name of the application using the v20 bindings
        datetime_format: -- The format to request when dealing with times
        poll_timeout: -- The timeout to use when making a polling request with
            the v20 REST server
        max_requests_per_second: -- Maximum HTTP requests sent per second
        max_simultaneous_connections: -- Maximum concurrent HTTP requests

    """

    default_parameters = {}

    initialized = 0

    account = None

    session = None

    loop = None

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
                 application='async_v20', datetime_format='UNIX', poll_timeout=2, max_requests_per_second=99,
                 max_simultaneous_connections=10):
        # TODO: add poll timeout
        self.version = __version__

        self.initialized = False  # when a new client instance is created it must be initialized

        if token is None:
            token = os.environ['OANDA_TOKEN']

        self.account_id = account_id

        self.application = application

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

        self.initialize_client = initializer(self)

    async def request_limiter(self):
        """Wait for the time interval before creating new request"""
        try:
            self._next_request_time += self._min_time_between_requests
        except AttributeError:
            self._next_request_time = time()
            return

        if self._next_request_time - time() > 0:
            await sleep(self._next_request_time - time())
        return


    async def initialize(self):
        """Initialize the client instance"""
        await self.initialize_client.asend(None)

    async def __aenter__(self):
        await self.initialize()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclose()

    def __enter__(self):
        print('Warning: <with> used rather than <async with>')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.close()
        except AttributeError:  # In case the client was never initialized
            pass

    def close(self):
        self.session.close()

    async def aclose(self):
        try:
            self.close()
        except AttributeError:  # In case the client was never initialized
            pass
        else:
            # If the session object exists then then
            # These async gens need to be closed as well
            await self.initialize_client.aclose()

