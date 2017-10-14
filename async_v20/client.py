import os
from functools import partial

from yarl import URL

from .definitions.types import AcceptDatetimeFormat
from .endpoints.annotations import Authorization
from .helpers import request_limiter, initialize_client
from .interface import *


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
        application: Optional name of the application using the v20 bindings
        datetime_format: -- The format to request when dealing with times
        poll_timeout: -- The timeout to use when making a polling request with
            the v20 REST server
    """

    default_parameters = {}

    initialized = 0

    account = None

    session = None

    loop = None

    def __init__(self, token=None, rest_host='api-fxpractice.oanda.com', rest_port=443,
                 stream_host='stream-fxpractice.oanda.com', stream_port=None, application='async_v20',
                 datetime_format='UNIX', poll_timeout=2, max_requests_per_second=99, max_simultaneous_connections=10):

        if token is None:
            token = os.environ['OANDA_TOKEN']

        self.application = application

        # V20 REST API URL
        rest_host = partial(URL.build, host=rest_host, port=rest_port, scheme='https')

        # v20 STREAM API URL
        stream_host = partial(URL.build, host=stream_host, port=stream_port, scheme='https')

        self.hosts = {'REST': rest_host, 'STREAM': stream_host}

        # The timeout to use when making a polling request with the
        # v20 REST server
        self.poll_timeout = poll_timeout

        # TODO limit this to > 0
        # Limit new requests to a certain rate
        self.max_requests_per_second = max_requests_per_second

        # TODO limit this to > 0
        # Limit concurrent connections
        self.max_simultaneous_connections = max_simultaneous_connections

        # This is the default parameter dictionary. OandaClient Methods that require certain parameters
        # that are  not explicitly passed will try to find it in this dict
        self.default_parameters.update(
            {Authorization: 'Bearer {}'.format(token),
             AcceptDatetimeFormat: datetime_format}
        )

        self.request = request_limiter(self)

        self.initialize = initialize_client(self)



