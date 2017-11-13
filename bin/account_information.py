import asyncio

from async_v20 import OandaClient


async def account():
    async with OandaClient() as client:
        return await client.get_account_details()


loop = asyncio.get_event_loop()
response = loop.run_until_complete(account())

# pandas Series
print(response['account'].series())

# HTTP response state
print(response['account'])

# JSON data in python dictionary format
print(response['account'].dict())
