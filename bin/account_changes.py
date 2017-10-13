import asyncio

from async_v20 import OandaClient


async def account():
    client = OandaClient()
    try:
        response = await client.account_changes()
    finally:
        client.session.close()
    return response


loop = asyncio.get_event_loop()
response = loop.run_until_complete(account())

# HTTP response state
print(response['state'])

# JSON data in python dictionary format
print(response['state'].json_dict())

# pandas Series
print(response['state'].series())