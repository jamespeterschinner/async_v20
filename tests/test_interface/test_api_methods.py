import gzip
import inspect

import pytest
from aiohttp import web
from aiohttp.client_exceptions import ServerDisconnectedError, ContentTypeError

from async_v20 import OandaClient
from tests.test_definitions.helpers import get_valid_primitive_data
from ..server.server import routes, headers

@pytest.yield_fixture()
def client():
    oanda_client = OandaClient(rest_host='127.0.0.1', rest_port=8080, rest_scheme='http',
                               stream_host='127.0.0.1', stream_port=8080, stream_scheme='http')
    yield oanda_client
    del oanda_client

global status
async def handler(request):
    global received
    global status
    print(request)
    method = request.method
    path = request.path.encode('ascii', 'backslashreplace').decode('ascii')
    data = None
    try:
        data = routes[(method, path)]
    except KeyError:
        pass

    received = method

    if data is None:
        data = "null"

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
    await server.wait_closed()

@pytest.mark.asyncio
@pytest.mark.parametrize('method', inspect.getmembers(OandaClient, lambda x: hasattr(x, 'endpoint')))
async def test_client_initializes_automatically_with_every_api_method(method, server, client):
    global received
    global status

    data = tuple(get_valid_primitive_data(param.annotation)
                 for param in method[1].__signature__.parameters.values()
                 if param.name != 'self')
    status = 200
    method = getattr(client, method[0])
    try:
        resp = await method(*data)
    except (KeyError, ServerDisconnectedError, ContentTypeError, AttributeError, ConnectionError):
        pass  # Caused by incorrect response status being returned
        # Server not keeping a data stream open
        # Response Not containing expected data
    assert client.initialized


@pytest.mark.asyncio
@pytest.mark.parametrize('method', inspect.getmembers(OandaClient, lambda x: hasattr(x, 'endpoint')))
async def test_client_methods_send_correct_data(method, server, client):
    global received
    global status

    data = tuple(get_valid_primitive_data(param.annotation)
                 for param in method[1].__signature__.parameters.values()
                 if param.name != 'self')
    status = 200
    async with client as client:  # initialize first
        method = getattr(client, method[0])
        status = next(iter(method.endpoint.responses))
        try:
            resp = await method(*data)
        except (KeyError, ServerDisconnectedError, ContentTypeError, AttributeError):
            pass  # Caused by incorrect response status being returned
            # Server not keeping a data stream open
            # Response Not containing expected data
        # TODO Added meaning full asserts
        print(received)

