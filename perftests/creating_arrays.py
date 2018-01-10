import asyncio
from time import time

from async_v20 import OandaClient

import json

class Time(object):
    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        self.interval = self.end - self.start


client = OandaClient(rest_host='127.0.0.1', rest_port=8080, rest_scheme='http',
                     stream_host='127.0.0.1', stream_port=8080, stream_scheme='http',
                     health_host='127.0.0.1', health_port=8080, health_scheme='http',
                     rest_timeout=60, max_simultaneous_connections=1000, max_requests_per_second=99999,
                     token='')

loop = asyncio.get_event_loop()

async def benchmark(repeats):
    async with client:
        await asyncio.gather(*[client.get_candles('AUD_USD') for _ in range(repeats)])

print('Running benchmark with async_v20 version', client.version)
with Time() as t:
    loop.run_until_complete(benchmark(1000))
print('Benchmark took ', t.interval)