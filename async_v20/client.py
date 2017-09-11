import requests

from v20.response import Response
from v20.errors import V20ConnectionError, V20Timeout


class Client(object):
    """
    A v20.Context encapuslates a connection to OANDA's v20 REST API
    """

    def __init__(
            self,
            hostname,
            port=443,
            ssl=True,
            application="",
            token=None,
            decimal_number_as_float=True,
            stream_chunk_size=512,
            stream_timeout=10,
            datetime_format="RFC3339",
            poll_timeout=2
    ):
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

        #
        # V20 REST server hostname
        #
        self.hostname = hostname

        #
        # V20 REST server port
        #
        self.port = port

        #
        # The format to use when dealing with times
        #
        self.datetime_format = datetime_format

        #
        # Form the value for the OANDA-Agent header
        #
        extensions = ""

        if application != "":
            extensions = " ({})".format(application)

        oanda_agent = "v20-python/3.0.18{}".format(extensions)

        #
        # Context headers to add to every request sent to the server
        #
        self._headers = {
            "Content-Type": "application/json",
            "OANDA-Agent": oanda_agent,
            "Accept-Datetime-Format": self.datetime_format
        }

        #
        # Current authentication token
        #
        self.token = None

        if token is not None:
            self.set_token(token)

        #
        # The base URL for every request made using the context
        #
        self._base_url = "http{}://{}:{}".format(
            "s" if ssl else "",
            hostname,
            port
        )

        #
        # The session used for communicating with the REST server
        #
        self._session = requests.Session()

        #
        # Flag that controls whether the string representation of floats
        # received from the server should be converted into floats or not
        #
        self.decimal_number_as_float = decimal_number_as_float

        #
        # The size of each chunk to read when processing a stream
        # response
        #
        self.stream_chunk_size = stream_chunk_size

        #
        # The timeout to use when making a stream request with the
        # v20 REST server
        #
        self.stream_timeout = stream_timeout

        #
        # The timeout to use when making a polling request with the
        # v20 REST server
        #
        self.poll_timeout = poll_timeout






