import asyncio

from async_v20 import OandaClient


async def poll_account(client: OandaClient = OandaClient(), poll_interval=6):
    # Ensure client has the latest transaction ID before
    while True:
        result = await client.account_changes()
        print(result)
        await asyncio.sleep(poll_interval)


loop = asyncio.get_event_loop()
response = loop.run_until_complete(poll_account())
