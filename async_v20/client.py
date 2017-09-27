import json
import os
from functools import partial

import aiohttp
from yarl import URL

from .definitions.types import AcceptDatetimeFormat, AccountID
from .endpoints.annotations import Authorization
from .interface import *


class Client(AccountInterface, InstrumentInterface, OrderInterface, PositionInterface, PricingInterface,
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
        stream_chunk_size: -- The size of each chunk to read when processing a
            stream response
        stream_timeout: -- The timeout to use when making a stream request
            with the v20 REST server
        datetime_format: -- The format to request when dealing with times
        poll_timeout: -- The timeout to use when making a polling request with
            the v20 REST server
    """
    default_parameters = {}

    initialized = False

    account = None

    session = None

    def __init__(self, token=os.environ['OANDA_TOKEN'], rest_host='api-fxpractice.oanda.com', rest_port=443,
                 stream_host='stream-fxpractice.oanda.com', stream_port=None, application="async_v20",
                 stream_chunk_size=512, stream_timeout=10, datetime_format="RFC3339", poll_timeout=2):
        self.application = application

        # V20 REST API URL
        rest_host = partial(URL.build, host=rest_host, port=rest_port, scheme='https')

        # v20 STREAM API URL
        stream_host = partial(URL.build, host=stream_host, port=stream_port, scheme='https')

        self.hosts = {'REST': rest_host, 'STREAM': stream_host}

        # The size of each chunk to read when processing a stream
        # response
        self.stream_chunk_size = stream_chunk_size

        # The timeout to use when making a stream request with the
        # v20 REST server
        self.stream_timeout = stream_timeout

        # The timeout to use when making a polling request with the
        # v20 REST server
        self.poll_timeout = poll_timeout

        # This is the default parameter dictionary. Client Methods that require certain parameters
        # that are  not explicitly passed will try to find it in this dict
        self.default_parameters.update(
            {Authorization: 'Bearer {}'.format(token),
             AcceptDatetimeFormat: datetime_format}
        )

    async def initialize(self):
        if self.initialized:
            return True

        # This needs to be set before calling and endpoints
        # Else initialise will be called multiple times.
        self.initialized = True

        headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive', 'OANDA-Agent': self.application}
        self.session = aiohttp.ClientSession(json_serialize=json.dumps, headers=headers)

        # Get the first account listed in in accounts
        response = await self.list_accounts()

        # Get the corresponding AccountID for the provided token
        self.default_parameters.update({AccountID: response['accounts'][0].id})

        # Get Account snapshot and last transaction id
        # last transaction is automatically updated when the
        # response is parsed
        response = await self.get_account_details()
        self.account = response['account']

        # Get the list of all available instruments for this account
        response = await self.account_instruments()
        self.account_instruments = response['instruments']

        return True

    async def poll_account(self, interval=None):
        response = await self.account_changes()
