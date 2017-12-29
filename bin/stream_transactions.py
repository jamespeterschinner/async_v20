import asyncio

from async_v20 import OandaClient


async def stream():
    async with OandaClient() as client:
        async for rsp in await client.stream_transactions():
            if 'HEARTBEAT' not in rsp:
                print(next(iter(rsp.values())).series())


loop = asyncio.get_event_loop()
loop.run_until_complete(stream())
