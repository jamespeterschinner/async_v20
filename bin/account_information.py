import asyncio

from async_v20.client import client_session

async def account():
    client = await client_session()
    try:
        account_snapshot = await client.get_account_details()
        print(await account_snapshot.account.data())
    finally:
        client.session.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(account())
