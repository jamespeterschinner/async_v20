import asyncio
from async_v20.client import client_session

async def account():
    client = await client_session()
    try:
        await client.get_account_details()
        response = await client.account_changes()
        print(response['state'])
        print(await response['state'].series())
    finally:
        client.session.close()
    return response


loop = asyncio.get_event_loop()
response = loop.run_until_complete(account())
