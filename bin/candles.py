import asyncio

from async_v20 import OandaClient


async def candles():
    async with OandaClient() as client:
        return await client.get_candles('AUD_USD', granularity='M')


loop = asyncio.get_event_loop()
response = loop.run_until_complete(candles())

# HTTP response state
print(response['instrument'])

# JSON data in python dictionary format
print(response['candles'][0].json_dict())

# pandas Series
print(response['candles'][0].series())
