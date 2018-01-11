import asyncio
from perftests.helpers import Time, client


print('Running creating_dataframes benchmark with async_v20 version', client.version)
loop = asyncio.get_event_loop()

rsp = loop.run_until_complete(client.get_candles('AUD_USD'))


with Time() as t:
    for _ in range(1000):
        df = rsp.candles.dataframe()