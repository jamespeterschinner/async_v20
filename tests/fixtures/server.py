import asyncio
import gzip
import re
from inspect import isgenerator
from time import time, sleep
import pytest
from aiohttp import web

from .routes import routes

rest_headers = {'Access-Control-Allow-Headers': 'Authorization, Content-Type, Accept-Datetime-Format',
                'Access-Control-Allow-Methods': 'PUT, PATCH, POST, GET, OPTIONS, DELETE',
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json', 'RequestID': '42359369470976686', 'Content-Encoding': 'gzip',
                'Vary': 'Accept-Encoding', 'Connection': 'Keep-Alive'}

stream_headers = {'Access-Control-Allow-Headers': 'Authorization, Content-Type, Accept-Datetime-Format',
                  'Access-Control-Allow-Methods': 'PUT, PATCH, POST, GET, OPTIONS, DELETE',
                  'Access-Control-Allow-Origin': '*',
                  'Content-Type': 'application/json', 'RequestID': '42359369470976686',
                  'Vary': 'Accept-Encoding', 'Connection': 'Keep-Alive'}

status = 200
received = ''
sleep_time = 0


def get_id_from_path(path):
    print(path)
    try:
        path_id = re.findall(r'(?<=\/)(\d+)(?=(\/|\Z))', path)[0][0]
        path = re.sub(r'(?<=\/)(\d+)(?=(\/|\Z))', '0000', path)
    except:
        return path, None
    else:
        return path, path_id


def get_response_data(method, path, specifier):
    data = 'null'
    try:
        data = routes[(method, path)]
    except KeyError:
        pass
    if isgenerator(data):  # Allows test to mock changing response
        data = next(data)
    if isinstance(data, dict):
        data = data[int(specifier)]

    return data


def get_response_status():
    global status
    try:
        response_status = next(status)
    except:
        response_status = status
    return response_status


async def handler(request):
    method = request.method
    path = request.path.encode('ascii', 'backslashreplace').decode('ascii')
    path, path_id = get_id_from_path(path)
    print('REQUEST HEADERS:\n',
          request.headers)
    print(method, path, path_id)

    response_data = get_response_data(method, path, path_id)

    response_status = get_response_status()

    global received
    received = await request.read()
    print(received)

    if response_data is None:
        response_data = 'null'

    if path == '/v3/accounts/123-123-1234567-123/pricing/stream':
        resp = web.StreamResponse(headers=stream_headers,
                                  status=response_status,
                                  reason='OK')
        await resp.prepare(request)
        while True:
            print('SENDING')
            resp.write(bytes(response_data, encoding='utf8'))
            resp.write(bytes('\n', encoding='utf8'))
            await resp.drain()
            await asyncio.sleep(sleep_time)
    await asyncio.sleep(sleep_time)
    return web.Response(body=gzip.compress(bytes(response_data, encoding='utf8')), headers=rest_headers,
                        status=response_status)


@pytest.yield_fixture
@pytest.mark.asyncio
async def server(event_loop):
    global status, sleep_time
    status = 200
    sleep_time = 0
    server = await event_loop.create_server(web.Server(handler), "127.0.0.1", 8080)
    yield server
    server.close()
