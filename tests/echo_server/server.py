import asyncio
from tests.echo_server.static import *
from aiohttp import web
from functools import partial
import gzip

loop = asyncio.get_event_loop()
headers = {'Access-Control-Allow-Headers': 'Authorization, Content-Type, Accept-Datetime-Format', 'Access-Control-Allow-Methods': 'PUT, PATCH, POST, GET, OPTIONS, DELETE', 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json', 'RequestID': '42359369470976686', 'Content-Encoding': 'gzip', 'Vary': 'Accept-Encoding', 'Connection': 'Keep-Alive'}

routes = [
    ('GET', '/v3/accounts', list_accounts_response),
    ('GET', '/v3/accounts/123-123-1234567-123', get_account_details_response),
    ('GET', '/v3/accounts/123-123-1234567-123/summary', account_summary_response),
    ('GET', '/v3/accounts/123-123-1234567-123/instruments', account_instruments_response),
    ('PATCH', '/v3/accounts/123-123-1234567-123/configuration'),
    ('GET', '/v3/accounts/123-123-1234567-123/changes'),
    ('GET', '/v3/instruments/123-123-1234567-123/candles', get_candles_response),
    ('POST', '/v3/accounts/123-123-1234567-123/orders', create_order_response),
    ('GET', '/v3/accounts/123-123-1234567-123/orders', list_orders_response),
    ('GET', '/v3/accounts/123-123-1234567-123/pendingOrders'),
    ('GET', '/v3/accounts/123-123-1234567-123/orders/123-123-1234567-123/'),
    ('PUT', '/v3/accounts/123-123-1234567-123/orders/123-123-1234567-123/'),
    ('PUT', '/v3/accounts/123-123-1234567-123/orders/123-123-1234567-123/cancel'),
    ('PUT', '/v3/accounts/123-123-1234567-123/orders/123-123-1234567-123/clientExtensions'),
    ('GET', '/v3/accounts/123-123-1234567-123/positions', get_positions_response),
    ('GET', '/v3/accounts/123-123-1234567-123/openPositions'),
    ('GET', '/v3/accounts/123-123-1234567-123/positions/123-123-1234567-123/'),
    ('PUT', '/v3/accounts/123-123-1234567-123/positions/123-123-1234567-123/close'),
    ('GET', '/v3/accounts/123-123-1234567-123/pricing', get_pricing_response),
    ('GET', '/v3/accounts/123-123-1234567-123/pricing/stream'),
    ('GET', '/v3/accounts/123-123-1234567-123/trades'),
    ('GET', '/v3/accounts/123-123-1234567-123/openTrades'),
    ('GET', '/v3/accounts/123-123-1234567-123/trades/123-123-1234567-123'),
    ('PUT', '/v3/accounts/123-123-1234567-123/trades/123-123-1234567-123/close'),
    ('PUT', '/v3/accounts/123-123-1234567-123/trades/123-123-1234567-123/clientExtensions'),
    ('PUT', '/v3/accounts/123-123-1234567-123/trades/123-123-1234567-123/orders'),
    ('GET', '/v3/accounts/123-123-1234567-123/transactions'),
    ('GET', '/v3/accounts/123-123-1234567-123/transactions/123-123-1234567-123'),
    ('GET', '/v3/accounts/123-123-1234567-123/transactions/idrange'),
    ('GET', '/v3/accounts/123-123-1234567-123/transactions/sinceid'),
    ('GET', '/v3/accounts/123-123-1234567-123/transactions/stream'),
    ('GET', '/v3/users/123-123-1234567-123'),
    ('GET', '/v3/users/123-123-1234567-123/externalInfo')
]


async def echo(request, data=None):
    print(request)
    if data is None:
        data = await request.read()
    return web.Response(body=data, headers=headers)


test_server = web.Application()

route_lookup = {'GET': test_server.router.add_get,
                'PUT': test_server.router.add_put,
                'PATCH': test_server.router.add_patch,
                'POST': test_server.router.add_post}

for route in routes:
    try:
        handle = partial(echo, data=gzip.compress(bytes(route[2], encoding='utf8')))
    except IndexError:
        handle = echo
    route_lookup[route[0]](route[1], handle)

# if __name__ == '__main__':
loop.run_until_complete(web.run_app(test_server, host='127.0.0.1', port=8080))
