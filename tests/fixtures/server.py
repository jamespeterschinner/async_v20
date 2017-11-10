import gzip

import pytest
from aiohttp import web

from .routes import routes


headers = {'Access-Control-Allow-Headers': 'Authorization, Content-Type, Accept-Datetime-Format',
           'Access-Control-Allow-Methods': 'PUT, PATCH, POST, GET, OPTIONS, DELETE', 'Access-Control-Allow-Origin': '*',
           'Content-Type': 'application/json', 'RequestID': '42359369470976686', 'Content-Encoding': 'gzip',
           'Vary': 'Accept-Encoding', 'Connection': 'Keep-Alive'}

status = 200
received  = ''

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

    global received
    received = await request.text()

    return web.Response(body=gzip.compress(bytes(data, encoding='utf8')), headers=headers,
                        status=status)

@pytest.yield_fixture
@pytest.mark.asyncio
async def server(event_loop):
    global status
    status = 200
    server = await event_loop.create_server(web.Server(handler), "127.0.0.1", 8080)
    yield server
    server.close()
