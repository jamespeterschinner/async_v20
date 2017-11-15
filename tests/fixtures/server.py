import gzip

import pytest
from aiohttp import web
import asyncio
import re

from .routes import routes

headers = {'Access-Control-Allow-Headers': 'Authorization, Content-Type, Accept-Datetime-Format',
           'Access-Control-Allow-Methods': 'PUT, PATCH, POST, GET, OPTIONS, DELETE', 'Access-Control-Allow-Origin': '*',
           'Content-Type': 'application/json', 'RequestID': '42359369470976686', 'Content-Encoding': 'gzip',
           'Vary': 'Accept-Encoding', 'Connection': 'Keep-Alive'}

status = 200
received = ''
sleep_time = 0

def get_id_from_path(path):
    try:
        path_id = re.findall(r'(?<=\/)(\d+)(?=[/\s])', path)[0]
        path = re.sub(r'(((orders)|(trades)|(transactions))\/)(\d+)', '\g<1>0000', path)
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
    else:
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

    print(method, path, path_id)

    response_data = get_response_data(method, path, path_id)

    response_status = get_response_status()

    global received
    received = await request.text()

    if response_data is None:
        response_data = 'null'

    await asyncio.sleep(sleep_time)
    return web.Response(body=gzip.compress(bytes(response_data, encoding='utf8')), headers=headers,
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
