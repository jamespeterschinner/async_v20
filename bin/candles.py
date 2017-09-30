import asyncio

from async_v20.client import Client


async def candles():
    client = Client()
    try:
        candles = await client.get_candles('AUD_USD')
    finally:
        client.session.close()
    return candles


loop = asyncio.get_event_loop()
candle_data = loop.run_until_complete(candles())