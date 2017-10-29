import asyncio
from tests.echo_server.static import *
import ujson as json
from aiohttp import web
from functools import partial

loop = asyncio.get_event_loop()

routes = [
    ('GET', '/v3/accounts', list_accounts_response),
    ('GET', '/v3/accounts/TEST_ID', get_account_details_response),
    ('GET', '/v3/accounts/TEST_ID/summary', account_summary_response),
    ('GET', '/v3/accounts/TEST_ID/instruments', account_instruments_response),
    ('PATCH', '/v3/accounts/TEST_ID/configuration'),
    ('GET', '/v3/accounts/TEST_ID/changes'),
    ('GET', '/v3/instruments/123-123-1234567-123/candles', get_candles_response),
    ('POST', '/v3/accounts/TEST_ID/orders', create_order_response),
    ('GET', '/v3/accounts/TEST_ID/orders', list_orders_response),
    ('GET', '/v3/accounts/TEST_ID/pendingOrders'),
    ('GET', '/v3/accounts/TEST_ID/orders/123-123-1234567-123/'),
    ('PUT', '/v3/accounts/TEST_ID/orders/123-123-1234567-123/'),
    ('PUT', '/v3/accounts/TEST_ID/orders/123-123-1234567-123/cancel'),
    ('PUT', '/v3/accounts/TEST_ID/orders/123-123-1234567-123/clientExtensions'),
    ('GET', '/v3/accounts/TEST_ID/positions', get_positions_response),
    ('GET', '/v3/accounts/TEST_ID/openPositions'),
    ('GET', '/v3/accounts/TEST_ID/positions/123-123-1234567-123/'),
    ('PUT', '/v3/accounts/TEST_ID/positions/123-123-1234567-123/close'),
    ('GET', '/v3/accounts/TEST_ID/pricing', get_pricing_response),
    ('GET', '/v3/accounts/TEST_ID/pricing/stream'),
    ('GET', '/v3/accounts/TEST_ID/trades'),
    ('GET', '/v3/accounts/TEST_ID/openTrades'),
    ('GET', '/v3/accounts/TEST_ID/trades/123-123-1234567-123'),
    ('PUT', '/v3/accounts/TEST_ID/trades/123-123-1234567-123/close'),
    ('PUT', '/v3/accounts/TEST_ID/trades/123-123-1234567-123/clientExtensions'),
    ('PUT', '/v3/accounts/TEST_ID/trades/123-123-1234567-123/orders'),
    ('GET', '/v3/accounts/TEST_ID/transactions'),
    ('GET', '/v3/accounts/TEST_ID/transactions/123-123-1234567-123'),
    ('GET', '/v3/accounts/TEST_ID/transactions/idrange'),
    ('GET', '/v3/accounts/TEST_ID/transactions/sinceid'),
    ('GET', '/v3/accounts/TEST_ID/transactions/stream'),
    ('GET', '/v3/users/123-123-1234567-123'),
    ('GET', '/v3/users/123-123-1234567-123/externalInfo')
]


async def echo(request, data=None):
    print(request)
    if data is None:
        data = await request.read()

    js = dict(json.loads(data))
    print('RETURNING', data)
    return web.json_response(js, content_type='application/json')
        # headers=request.headers,


app = web.Application()

route_lookup = {'GET': app.router.add_get,
                'PUT': app.router.add_put,
                'PATCH': app.router.add_patch,
                'POST': app.router.add_post}

for route in routes:
    try:
        handle = partial(echo, data=route[2])
    except IndexError:
        handle = echo
    route_lookup[route[0]](route[1], handle)

loop.run_until_complete(web.run_app(app, host='127.0.0.1', port=8080,
                                    # ssl_context=ssl.create_default_context()
                                    ))
