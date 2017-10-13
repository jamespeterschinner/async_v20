import asyncio

from async_v20.client import OandaClient


async def candles():
    client = OandaClient()
    try:
        response = await client.get_candles('AUD_USD', granularity='M')
    finally:
        client.session.close()
    return response


loop = asyncio.get_event_loop()
response = loop.run_until_complete(candles())

# HTTP response state
print(response['instrument'])

# JSON data in python dictionary format
print(response['candles'][0].json_dict())

# pandas Series
print(response['candles'][0].series())