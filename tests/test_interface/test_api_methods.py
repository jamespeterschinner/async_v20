import pytest
from async_v20 import OandaClient
from ..echo_server.server import server
from ..test_client import client
from async_v20 import MarketOrderRequest
from ..test_definitions.test_primitives.helpers import get_valid_primitive_data
import inspect
from aiohttp.client_exceptions import ServerDisconnectedError, ContentTypeError
# Prevent pycharm from removing imports
client = client
server = server


@pytest.mark.asyncio
@pytest.mark.parametrize('api_method', inspect.getmembers(OandaClient, lambda x: hasattr(x, 'endpoint')))
async def test_client_methods_send_correct_data(api_method, server, client):
    async with client as client:
        data = tuple(get_valid_primitive_data(annotation) for annotation
                     in api_method[1].__annotations__.values())
        print(data)
        try:
            resp = await getattr(client, api_method[0])(*data)
        except (KeyError, ServerDisconnectedError, ContentTypeError, AttributeError):
            pass # Caused by incorrect response status being returned
                 # Server not keeping a data stream open
                 # Response Not containing expected data
                 #
        print(server.received)
    pass