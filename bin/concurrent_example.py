import asyncio

from async_v20 import OandaClient

client = OandaClient()


async def poll_account(poll_interval=6, client=client):
    while True:
        result = await client.account_changes()
        print(result['changes'].json_dict())
        await asyncio.sleep(poll_interval)


async def stream(instruments, client=client):
    async for data in await client.stream_pricing(instruments):
        price = data.get('PRICE', None)
        if price:
            print(price.series())


loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(poll_account(), stream('EUR_USD'))
    )
client.close()
