import asyncio

from async_v20.client import OandaClient


async def candles():
    client = OandaClient()
    try:
        candles_1 = await client.get_candles('AUD_USD')
        candles_2 = await client.get_candles('EUR_USD')
    finally:
        client.session.close()
    return candles_1, candles_2


loop = asyncio.get_event_loop()
candle_data = loop.run_until_complete(candles())