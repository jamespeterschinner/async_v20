from .interface import *
from .endpoints.annotations import Authorization
from .definitions.types import AcceptDatetimeFormat, AccountID

# from v20.response import Response
# from v20.errors import V20ConnectionError, V20Timeout


class Client(AccountInterface, InstrumentInterface, OrderInterface, PositionInterface, PricingInterface, TradeInterface,
             TransactionInterface, UserInterface):
    """
    A Client encapuslates a connection to OANDA's v20 REST API
    """

    default_parameters = {"Content-Type": "application/json", "OANDA-Agent": "async_v20"}

    def __init__(self, session, host, account_id=None, port=443, ssl=True, token=None, decimal_number_as_float=True,
                 stream_chunk_size=512, stream_timeout=10, datetime_format="RFC3339", poll_timeout=2):
        """
        Create an API context for v20 access

        Args:
            hostname: The hostname of the v20 REST server
            port: The port of the v20 REST server
            ssl: Flag to enable/disable SSL
            application: Optional name of the application using the v20 bindings
            token: The authorization token to use when making requests to the
                v20 server
            decimal_number_as_float: Flag that controls whether the string
                representation of floats received from the server should be
                converted into floats or not
            stream_chunk_size: The size of each chunk to read when processing a
                stream response
            stream_timeout: The timeout to use when making a stream request
                with the v20 REST server
            datetime_format: The format to request when dealing with times
            poll_timeout: The timeout to use when making a polling request with
                the v20 REST server
        """

        self.default_parameters.update({Authorization: 'Bearer {}'.format(token)})

        # V20 REST server hostname
        self.host = host

        # V20 REST server port
        self.port = port

        if not account_id:
            account_id = self.run_coroutine(self.get_accounts)['accounts'][0].id

        self.default_parameters.update({AccountID: account_id})

        # The format to use when dealing with times
        self.default_parameters.update({AcceptDatetimeFormat: datetime_format})

        # The base URL for every request made using the context
        self._base_url = "http{}://{}:{}".format(
            "s" if ssl else "",
            host,
            port
        )

        # The session used for communicating with the REST server
        self.session = session

        # Flag that controls whether the string representation of floats
        # received from the server should be converted into floats or not
        self.decimal_number_as_float = decimal_number_as_float

        # The size of each chunk to read when processing a stream
        # response
        self.stream_chunk_size = stream_chunk_size

        # The timeout to use when making a stream request with the
        # v20 REST server
        self.stream_timeout = stream_timeout

        # The timeout to use when making a polling request with the
        # v20 REST server
        self.poll_timeout = poll_timeout

    @staticmethod
    async def run_coroutine(coroutine):
        return await coroutine