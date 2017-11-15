import asyncio

from async_v20 import OandaClient

client = OandaClient()


async def poll_account(poll_interval=6, client=client):
    while True:
        account = await client.account()
        print(account)
        await asyncio.sleep(poll_interval)


async def stream(instruments, client=client):
    async for price in await client.stream_pricing(instruments):
        print(price)


loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(poll_account(), stream('EUR_USD'))
    )
client.close()
