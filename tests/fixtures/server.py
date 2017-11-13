import gzip

import pytest
from aiohttp import web
import asyncio

from .routes import routes

headers = {'Access-Control-Allow-Headers': 'Authorization, Content-Type, Accept-Datetime-Format',
           'Access-Control-Allow-Methods': 'PUT, PATCH, POST, GET, OPTIONS, DELETE', 'Access-Control-Allow-Origin': '*',
           'Content-Type': 'application/json', 'RequestID': '42359369470976686', 'Content-Encoding': 'gzip',
           'Vary': 'Accept-Encoding', 'Connection': 'Keep-Alive'}

status = 200
received = ''
sleep_time = 0


async def handler(request):
    print(request)
    method = request.method
    path = request.path.encode('ascii', 'backslashreplace').decode('ascii')

    data = None
    try:
        data = routes[(method, path)]
    except KeyError:
        pass

    server.received = method

    if data is None:
        data = "null"
    try:
        response_status = next(status)
    except:
        response_status = status

    global received
    received = await request.text()

    await asyncio.sleep(sleep_time)

    print('RESPONSE STATUS:=', response_status)

    return web.Response(body=gzip.compress(bytes(data, encoding='utf8')), headers=headers,
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
