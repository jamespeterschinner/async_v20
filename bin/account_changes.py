import asyncio
from async_v20 import Client

async def account():
    client = Client()
    try:
        await client.get_account_details()
        response = await client.account_changes()
        print(response['state'])
        print(await response['state'].json_dict())
    finally:
        client.session.close()
    return response


loop = asyncio.get_event_loop()
response = loop.run_until_complete(account())
