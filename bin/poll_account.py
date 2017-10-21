import asyncio

from async_v20 import OandaClient


async def poll_account(poll_interval=6):
    async with OandaClient() as client:
        while True:
            result = await client.account_changes()
            print(result)
            await asyncio.sleep(poll_interval)


loop = asyncio.get_event_loop()
response = loop.run_until_complete(poll_account())
