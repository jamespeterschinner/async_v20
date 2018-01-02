import asyncio

from async_v20 import OandaClient


async def stream(instruments):
    async with OandaClient() as client:
        async for rsp in await client.stream_pricing(instruments):
            print(rsp.dict(json=True))


loop = asyncio.get_event_loop()
loop.run_until_complete(stream('AUD_USD,EUR_USD'))
