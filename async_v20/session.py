from .endpoints.annotations import Authorization
from .definitions.types import AcceptDatetimeFormat, AccountID
from async_v20.client import Client
import aiohttp
from yarl import URL
import asyncio
import ujson as json
import os


async def client_session(token=os.environ['OANDA_TOKEN'], rest_host='api-fxpractice.oanda.com', rest_port=443,
                         stream_host='stream-fxpractice.oanda.com', stream_port=80, application="async_v20",
                         stream_chunk_size=512, stream_timeout=10, datetime_format="RFC3339", poll_timeout=2):
    """
    Create an API context for v20 access

    Args:
        token -- User generated token from the online account configuration page
        rest_host -- The hostname of the v20 REST server
        rest_port -- The port of the v20 REST server
        stream_host -- The hostname of the v20 REST server
        stream_port -- The port of the v20 REST server
        application: Optional name of the application using the v20 bindings
        stream_chunk_size -- The size of each chunk to read when processing a
            stream response
        stream_timeout -- The timeout to use when making a stream request
            with the v20 REST server
        datetime_format -- The format to request when dealing with times
        poll_timeout -- The timeout to use when making a polling request with
            the v20 REST server
    """

    # Create a client instance
    client = Client()

    headers = {"Content-Type": "application/json", "OANDA-Agent": application}
    client.session = aiohttp.ClientSession(json_serialize=json.dumps, headers=headers)

    # Get the first account listed in in accounts
    account_id = await next(iter(client.get_accounts()['accounts'])).id

    # This parameters is placed here for easy access
    client.account_id = account_id

    # This is the default parameter dictionary. Client Methods that require certain parameters
    # that are  not explicitly passed will try to find it in this dict
    client.default_parameters = {Authorization: 'Bearer {}'.format(token),
                                 AccountID: client.account_id,
                                 AcceptDatetimeFormat: datetime_format}

    # V20 REST API URL
    client.rest_url = URL.build(host=rest_host, port=rest_port, scheme='https')

    # v20 STREAM API URL
    client.stream_url = URL.build(host=stream_host, port=stream_port, scheme='https')

    # The size of each chunk to read when processing a stream
    # response
    client.stream_chunk_size = stream_chunk_size

    # The timeout to use when making a stream request with the
    # v20 REST server
    client.stream_timeout = stream_timeout

    # The timeout to use when making a polling request with the
    # v20 REST server
    client.poll_timeout = poll_timeout
