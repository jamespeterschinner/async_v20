import gzip

import pytest
from aiohttp import web

from ..server.server import routes, headers
from ..server.static import get_account_details_response, get_pricing_response, list_accounts_response
from async_v20 import OandaClient

@pytest.yield_fixture()
def client():
    oanda_client = OandaClient(rest_host='127.0.0.1', rest_port=8080, rest_scheme='http',
                               stream_host='127.0.0.1', stream_port=8080, stream_scheme='http')
    yield oanda_client
    del oanda_client


# prevent pycharm from removing the import

async def handler(request):
    print(request)
    method = request.method
    path = request.path.encode('ascii', 'backslashreplace').decode('ascii')
    data = routes[(method, path)]
    global received
    global status
    received = method
    if data is None:
        data = "null"
    return web.Response(body=gzip.compress(bytes(data, encoding='utf8')), headers=headers, status=status)


@pytest.yield_fixture
@pytest.mark.asyncio
async def server(event_loop):
    global status
    status = 200
    server = await event_loop.create_server(web.Server(handler), "127.0.0.1", 8080)
    yield server
    server.close()
    server.wait_closed()


@pytest.mark.asyncio
async def test_response_creates_correct_json(client, server):
    global status
    status = 200
    async with client as client:
        response = await client.get_account_details()
        resp_json = response.json()
        print(resp_json)
        correct = get_account_details_response.replace(' ', '')
        print(correct)
        assert resp_json == correct


@pytest.mark.asyncio
async def test_response_returns_json(client, server):
    async with client as client:
        accounts = await client.list_accounts()
        account_details = await client.get_account_details()
        pricing = await client.get_pricing()

    assert accounts.json() == list_accounts_response.replace(' ', '')
    assert account_details.json() == get_account_details_response.replace(' ', '')
    assert pricing.json() == get_pricing_response.replace(' ', '')
