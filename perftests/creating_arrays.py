import asyncio
from perftests.helpers import Time, client

print('Running creating_arrays benchmark with async_v20 version', client.version)
async def creating_arrays(repeats):
    await asyncio.gather(*[client.get_candles('AUD_USD') for _ in range(repeats)])

loop = asyncio.get_event_loop()
with Time() as t:
    loop.run_until_complete(creating_arrays(500))
    loop.run_until_complete(creating_arrays(500))