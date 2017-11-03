import gzip
import inspect

import pytest
from aiohttp import web
from aiohttp.client_exceptions import ServerDisconnectedError, ContentTypeError

from async_v20 import OandaClient
from tests.test_definitions.helpers import get_valid_primitive_data
from ..server.server import routes, headers
from ..test_client import client

client = client


async def handler(request):
    print(request)
    method = request.method
    path = request.path.encode('ascii', 'backslashreplace').decode('ascii')
    data = routes[(method, path)]
    global received
    received = method
    if data is None:
        data = "null"
    return web.Response(body=gzip.compress(bytes(data, encoding='utf8')), headers=headers)


@pytest.fixture
@pytest.mark.asyncio
async def server(event_loop):
    server = await event_loop.create_server(web.Server(handler), "127.0.0.1", 8080)
    yield server
    server.close()


@pytest.mark.asyncio
@pytest.mark.parametrize('api_method', inspect.getmembers(OandaClient, lambda x: hasattr(x, 'endpoint')))
async def test_client_methods_send_correct_data(api_method, server, client):
    global received
    async with client as client:
        data = tuple(get_valid_primitive_data(annotation) for annotation
                     in api_method[1].__annotations__.values())
        print('CALLING METHOD WITH: ', data)
        try:
            resp = await getattr(client, api_method[0])(*data)
        except (KeyError, ServerDisconnectedError, ContentTypeError, AttributeError):
            pass  # Caused by incorrect response status being returned
            # Server not keeping a data stream open
            # Response Not containing expected data
        # TODO Added meaning full asserts
        print(received)
    pass
