import asyncio
from perftests.helpers import Time, client

print('Running rest_implementation benchmark with async_v20 version', client.version)
async def rest_implementation(repeats):
    for _ in range(repeats):
        account = await client.account()
        account.json()

loop = asyncio.get_event_loop()
with Time() as t:
    loop.run_until_complete(rest_implementation(1000))