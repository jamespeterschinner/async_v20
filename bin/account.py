import asyncio

from async_v20 import OandaClient


async def get_account():
    async with OandaClient() as client:
        return await client.account()


loop = asyncio.get_event_loop()
account = loop.run_until_complete(get_account())

# pandas Series
print(account.series())

# HTTP response state
print(account)

# JSON data in python dictionary format
print(account.dict())
