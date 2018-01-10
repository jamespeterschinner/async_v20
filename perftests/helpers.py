from time import time
from async_v20 import OandaClient

class Time(object):
    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        print(f'Took {self.end - self.start}')


client = OandaClient(rest_host='127.0.0.1', rest_port=8080, rest_scheme='http',
                     stream_host='127.0.0.1', stream_port=8080, stream_scheme='http',
                     health_host='127.0.0.1', health_port=8080, health_scheme='http',
                     rest_timeout=60, max_simultaneous_connections=1000, max_requests_per_second=99999,
                     token='')