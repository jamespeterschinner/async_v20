import inspect

import pytest
from aiohttp.client_exceptions import ServerDisconnectedError, ContentTypeError

from async_v20 import OandaClient
from tests.test_definitions.helpers import get_valid_primitive_data
from ..fixtures import server as server_module
from ..fixtures.client import client
from async_v20.exceptions import UnexpectedStatus
client = client
server = server_module.server
received = server_module.received


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
    except (KeyError, ServerDisconnectedError, ContentTypeError, AttributeError, UnexpectedStatus):
        pass  # Caused by incorrect response status being returned
        # Server not keeping a data stream open
        # Response Not containing expected data
    if getattr(method, 'initialize_required', True):
        assert client.initialized
    else:
        assert not client.initialized


@pytest.mark.asyncio
@pytest.mark.parametrize('method', inspect.getmembers(OandaClient, lambda x: hasattr(x, 'endpoint')))
async def test_client_methods_send_correct_data(method, server, client):
    data = tuple(get_valid_primitive_data(param.annotation)
                 for param in method[1].__signature__.parameters.values()
                 if param.name != 'self')
    async with client as client:  # initialize first
        method = getattr(client, method[0])
        server_module.status = next(iter(method.endpoint.responses))
        try:
            resp = await method(*data)
        except (KeyError, ServerDisconnectedError, ContentTypeError, AttributeError):
            pass  # Caused by incorrect response status being returned
            # Server not keeping a data stream open
            # Response Not containing expected data
        # TODO Added meaning full asserts
        print(server_module.received)
        
@pytest.mark.asyncio
@pytest.mark.parametrize('method', inspect.getmembers(OandaClient, lambda x: hasattr(x, 'shortcut')))
async def test_client_methods_shortcut_api_methods(method, server, client):
    data = tuple(get_valid_primitive_data(param.annotation)
                 for param in method[1].__signature__.parameters.values()
                 if param.name not in 'self cls')
    async with client as client:  # initialize first
        method = getattr(client, method[0])
        server_module.status = 201

        print(method)
        try:
            resp = await method(*data)
        except (KeyError, ServerDisconnectedError, ContentTypeError, AttributeError):
            pass  # Caused by incorrect response status being returned
            # Server not keeping a data stream open
            # Response Not containing expected data
        # TODO Added meaning full asserts
        print(server_module.received)


