import asyncio

from async_v20 import OandaClient


async def account():
    async with OandaClient() as client:
        return await client.account_changes()


loop = asyncio.get_event_loop()
response = loop.run_until_complete(account())

# HTTP response state
print(response['state'])

# JSON data in python dictionary format
print(response['state'].dict())

# pandas Series
print(response['state'].series())
