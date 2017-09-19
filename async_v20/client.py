import json
import os
from functools import partial

import aiohttp
from yarl import URL

from .definitions.types import AcceptDatetimeFormat, AccountID
from .endpoints.annotations import Authorization
from .interface import *


class _Client(AccountInterface, InstrumentInterface, OrderInterface, PositionInterface, PricingInterface,
              TradeInterface,
              TransactionInterface, UserInterface):
    """
    A Client encapsulates a connection to OANDA's v20 REST API.
    """

    async def poll_account_changes(self):
        pass

    pass


async def client_session(token=os.environ['OANDA_TOKEN'], rest_host='api-fxpractice.oanda.com', rest_port=443,
                         stream_host='stream-fxpractice.oanda.com', stream_port=None, application="async_v20",
                         stream_chunk_size=512, stream_timeout=10, datetime_format="RFC3339", poll_timeout=2):
    """
    Create an API context for v20 access

    Args:
        token: -- User generated token from the online account configuration page
        rest_host: -- The hostname of the v20 REST server
        rest_port: -- The port of the v20 REST server
        stream_host: -- The hostname of the v20 REST server
        stream_port: -- The port of the v20 REST server
        application: Optional name of the application using the v20 bindings
        stream_chunk_size: -- The size of each chunk to read when processing a
            stream response
        stream_timeout: -- The timeout to use when making a stream request
            with the v20 REST server
        datetime_format: -- The format to request when dealing with times
        poll_timeout: -- The timeout to use when making a polling request with
            the v20 REST server
    """

    # Create a client instance
    client = _Client()

    headers = {'Content-Type': 'application/json', 'key': 'Keep-Alive', 'OANDA-Agent': application}
    client.session = aiohttp.ClientSession(json_serialize=json.dumps, headers=headers)

    # V20 REST API URL
    rest_host = partial(URL.build, host=rest_host, port=rest_port, scheme='https')

    # v20 STREAM API URL
    stream_host = partial(URL.build, host=stream_host, port=stream_port, scheme='https')

    client.hosts = {'REST': rest_host, 'STREAM': stream_host}

    # The size of each chunk to read when processing a stream
    # response
    client.stream_chunk_size = stream_chunk_size

    # The timeout to use when making a stream request with the
    # v20 REST server
    client.stream_timeout = stream_timeout

    # The timeout to use when making a polling request with the
    # v20 REST server
    client.poll_timeout = poll_timeout

    # This is the default parameter dictionary. Client Methods that require certain parameters
    # that are  not explicitly passed will try to find it in this dict
    client.default_parameters = {Authorization: 'Bearer {}'.format(token),
                                 AcceptDatetimeFormat: datetime_format}

    # Get the first account listed in in accounts
    accounts = await client.list_accounts()
    client.default_parameters.update({AccountID: accounts.accounts[0].id})

    return client
