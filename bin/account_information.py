import asyncio

from async_v20.client import Client


async def account():
    client = Client()
    try:
        account_snapshot = await client.get_account_details()
        print(account_snapshot)
        print(await account_snapshot['account'].json_dict())
    finally:
        client.session.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(account())
