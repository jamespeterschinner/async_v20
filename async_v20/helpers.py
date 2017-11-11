import asyncio
import ujson as json

import aiohttp

from .definitions.types import AccountID


async def sleep(s=0.0):
    await asyncio.sleep(s)


async def initializer(self):
    conn = aiohttp.TCPConnector(limit=self.max_simultaneous_connections)

    headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive',
               'OANDA-Agent': self.application}

    self.session = aiohttp.ClientSession(
        json_serialize=json.dumps,
        headers=headers,
        connector=conn)

    # Get the first account listed in in accounts
    if self.account_id:
        self.default_parameters.update({AccountID: self.account_id})
    else:
        # Get the corresponding AccountID for the provided token
        response = await self.list_accounts()
        if response:
            self.default_parameters.update({AccountID: response['accounts'][0].id})
        else:
            raise ConnectionError(f'Server did not return AccountID during '
                                  f'initialization. {response} {response.json_dict()}')

    # Get Account snapshot and last transaction id
    # last transaction is automatically updated when the
    # response is parsed

    response = await self.get_account_details()
    if response:
        self.account = response['account']
    else:
        raise ConnectionError(f'Server did not return Account Details during '
                              f'initialization. {response} {response.json_dict()}')

    self.initialized = True

    while True:
        yield True
