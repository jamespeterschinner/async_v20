import asyncio

from async_v20.client import OandaClient


async def candles():
    client = OandaClient()
    try:
        response = await client.get_candles('AUD_USD')
    finally:
        client.session.close()
    return response


loop = asyncio.get_event_loop()
response = loop.run_until_complete(candles())