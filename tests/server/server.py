import asyncio
from tests.server.static import *
from aiohttp import web
import gzip
import pytest

from aiohttp.web_server import BaseRequest

loop = asyncio.get_event_loop()
headers = {'Access-Control-Allow-Headers': 'Authorization, Content-Type, Accept-Datetime-Format', 'Access-Control-Allow-Methods': 'PUT, PATCH, POST, GET, OPTIONS, DELETE', 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json', 'RequestID': '42359369470976686', 'Content-Encoding': 'gzip', 'Vary': 'Accept-Encoding', 'Connection': 'Keep-Alive'}

routes = {
    ('GET', '/v3/accounts'): list_accounts_response,
    ('GET', '/v3/accounts/123-123-1234567-123'): get_account_details_response,
    ('GET', '/v3/accounts/123-123-1234567-123/summary'): account_summary_response,
    ('GET', '/v3/accounts/123-123-1234567-123/instruments'): account_instruments_response,
    ('PATCH', '/v3/accounts/123-123-1234567-123/configuration'): None,
    ('GET', '/v3/accounts/123-123-1234567-123/changes'): None,
    ('GET', '/v3/instruments/123-123-1234567-123/candles'): get_candles_response,
    ('POST', '/v3/accounts/123-123-1234567-123/orders'): create_order_response,
    ('GET', '/v3/accounts/123-123-1234567-123/orders'): list_orders_response,
    ('GET', '/v3/accounts/123-123-1234567-123/pendingOrders'): None,
    ('GET', '/v3/accounts/123-123-1234567-123/orders/123-123-1234567-123/'): None,
    ('PUT', '/v3/accounts/123-123-1234567-123/orders/123-123-1234567-123/'): None,
    ('PUT', '/v3/accounts/123-123-1234567-123/orders/123-123-1234567-123/cancel'): None,
    ('PUT', '/v3/accounts/123-123-1234567-123/orders/123-123-1234567-123/clientExtensions'): None,
    ('GET', '/v3/accounts/123-123-1234567-123/positions'): list_positions_response,
    ('GET', '/v3/accounts/123-123-1234567-123/openPositions'): None,
    ('GET', '/v3/accounts/123-123-1234567-123/positions/123-123-1234567-123/'): None,
    ('PUT', '/v3/accounts/123-123-1234567-123/positions/123-123-1234567-123/close'): None,
    ('GET', '/v3/accounts/123-123-1234567-123/pricing'): get_pricing_response,
    ('GET', '/v3/accounts/123-123-1234567-123/pricing/stream'): None,
    ('GET', '/v3/accounts/123-123-1234567-123/trades'): None,
    ('GET', '/v3/accounts/123-123-1234567-123/openTrades'): None,
    ('GET', '/v3/accounts/123-123-1234567-123/trades/123-123-1234567-123'): None,
    ('PUT', '/v3/accounts/123-123-1234567-123/trades/123-123-1234567-123/close'): None,
    ('PUT', '/v3/accounts/123-123-1234567-123/trades/123-123-1234567-123/clientExtensions'): None,
    ('PUT', '/v3/accounts/123-123-1234567-123/trades/123-123-1234567-123/orders'): None,
    ('GET', '/v3/accounts/123-123-1234567-123/transactions'): None,
    ('GET', '/v3/accounts/123-123-1234567-123/transactions/123-123-1234567-123'): None,
    ('GET', '/v3/accounts/123-123-1234567-123/transactions/idrange'): None,
    ('GET', '/v3/accounts/123-123-1234567-123/transactions/sinceid'): None,
    ('GET', '/v3/accounts/123-123-1234567-123/transactions/stream'): None,
    ('GET', '/v3/users/123-123-1234567-123'): None,
    ('GET', '/v3/users/123-123-1234567-123/externalInfo'): None}

received = None

async def handler(request):
    print(request)
    method = request.method
    path = request.path.encode('ascii', 'backslashreplace').decode('ascii')
    data = routes[(method, path)]
    global received
    received = await request.read()
    if data is None:
        data = "null"
    return web.Response(body=gzip.compress(bytes(data, encoding='utf8')), headers=headers)


@pytest.fixture
@pytest.mark.asyncio
async def server(event_loop):
    server = await event_loop.create_server(web.Server(handler), "127.0.0.1", 8080)
    global received
    server.received = received
    yield server
    server.close()




if __name__ == '__main__':


    loop.run_until_complete(server(loop).asend(None))