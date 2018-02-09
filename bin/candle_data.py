"""A tool for downloading historical data"""

import argparse
import asyncio
import logging
from datetime import datetime, timedelta
from functools import reduce

from async_v20 import OandaClient

logger = logging.getLogger('async_v20')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

parser = argparse.ArgumentParser()

parser.add_argument('--from-time', help='The date from when to get the date')
parser.add_argument('--to-time', help='Get the required data up to this date', )
parser.add_argument('--instrument', help='The instrument of the data to get')
parser.add_argument('--granularity', help='The width of the candle to get')
parser.add_argument('--out-file', help='The destination of the data')
parser.add_argument('--time_out', help='The request time out period', default=30)

granularity_to_minutes = {
    'S5': 416,
    'S10': 833,
    'S15': 1250,
    'S30': 2500,
    'M1': 5000,
    'M2': 10000,
    'M4': 20000,
    'M5': 25000,
    'M10': 50000,
    'M15': 75000,
    'M30': 150000,
    'H1': 300000,
    'H2': 600000,
    'H3': 900000,
    'H4': 1200000,
    'H6': 1800000,
    'H8': 2400000,
    'H12': 3600000,
    'D': 7200000,
    'W': 50400000,
    'M': 201600000
}

loop = asyncio.get_event_loop()
run = loop.run_until_complete


def rolling(df, window, step):
    count = 0
    df_length = len(df)
    while count < (df_length - window):
        yield count, df[count:window + count]
        count += step


def create_requests(client,
                    instrument_name,
                    granularity,
                    from_time,
                    to_time,
                    price='MBA',
                    count=5000):
    change = timedelta(minutes=granularity_to_minutes[granularity])
    from_time = from_time
    while from_time < to_time:
        yield client.get_candles(instrument_name, price=price, granularity=granularity, count=count,
                                 from_time=from_time)
        from_time = from_time + change


async def worker(coroutines, data_frames):
    while True:
        try:
            coroutine = next(coroutines)
        except StopIteration:
            return
        rsp = await coroutine
        if not rsp.status == 200:
            continue
        df = rsp.candles.dataframe(datetime_format='UNIX')
        df.index = df.time
        data_frames.append(df)


async def get_data(client, instrument_name, granularity, from_time, to_time):
    data_frames = []
    coroutines = create_requests(client, instrument_name, granularity, from_time, to_time)
    await asyncio.gather(*[worker(coroutines, data_frames) for _ in range(5)])
    df = reduce(lambda x, y: x.append(y), data_frames)
    df.sort_index(inplace=True)
    return df


async def execute():
    namespace = parser.parse_args()
    from_time = datetime(*[int(i) for i in namespace.from_time.split('-')])
    to_time = datetime(*[int(i) for i in namespace.to_time.split('-')])
    granularity = namespace.granularity
    out_file = namespace.out_file
    time_out = namespace.time_out
    async with OandaClient(rest_timeout=time_out) as client:
        df = await get_data(client, namespace.instrument, granularity, from_time, to_time)
    df.to_csv(out_file)


loop.run_until_complete(execute())
