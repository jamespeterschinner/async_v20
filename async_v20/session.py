print(__name__)

from async_v20.client import Client
import aiohttp
import asyncio
import ujson as json
import os


session = aiohttp.ClientSession(json_serialize=json.dumps,
                                headers={"Content-Type": "application/json", "OANDA-Agent": "async_v20"})
try:
    oanda = Client(session, token=os.environ['OANDA_TOKEN'], hostname='api-fxpractice.oanda.com')
    co_1 = oanda.list_accounts()
    co_2 = oanda.get_candles('AUD_USD')
    loop = asyncio.get_event_loop()
    resp = loop.run_until_complete(asyncio.gather(co_1, co_2))
finally:
    session.close()