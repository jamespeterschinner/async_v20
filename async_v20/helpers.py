import asyncio
import ujson as json
from time import time

import aiohttp

from .definitions.types import AccountID



async def sleep(s=0.0):
    await asyncio.sleep(s)


async def wait(time_delta, previous_time):
    waited = time() - previous_time
    if waited <= time_delta:
        wait_time = time_delta - waited
        print('WAITING: ', wait_time)
        await sleep(wait_time)
    return True


async def request_limiter(self):
    yield
    time_delta = 1 / self.max_requests_per_second
    while True:
        previous_time = time()
        yield self.session.request
        await wait(time_delta, previous_time)

async def initializer(self):

    # Initialize the request limiter coroutine
    await self.request.asend(None)

    conn = aiohttp.TCPConnector(limit=self.max_simultaneous_connections)

    headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive',
               'OANDA-Agent': self.application}

    self.session = aiohttp.ClientSession(
        json_serialize=json.dumps,
        headers=headers,
        connector=conn)

    # Get the first account listed in in accounts
    response = await self.list_accounts()
    if not response:
        raise ConnectionError(f'Failed to initialize. {response} : {response.json_dict()}')

    # Get the corresponding AccountID for the provided token
    self.default_parameters.update({AccountID: response['accounts'][0].id})

    # Get Account snapshot and last transaction id
    # last transaction is automatically updated when the
    # response is parsed
    response = await self.get_account_details()
    self.account = response['account']

    # Get the list of all available instruments for this account
    response = await self.account_instruments()
    self.available_instruments = response['instruments']

    while True:
        yield True