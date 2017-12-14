import asyncio

from async_v20 import OandaClient, LastTransactionID, OrderSpecifier, TransactionID, TradeSpecifier

loop = asyncio.get_event_loop()

client = OandaClient()

run = lambda *x: loop.run_until_complete(asyncio.gather(*x))

print('RUNNING TEST')

rsp = run(
    client.account(),
    client.list_accounts(),
    client.get_account_details(),
    client.account_summary(),
    client.account_instruments(),
    client.get_candles('AUD_USD'),
    # should be ok
    client.account_instruments(instruments='AUD_USD,EUR_USD,AUD_JPY'),
    # should give error
    client.account_instruments(instruments='AUD_USD EUR_USD'),
    # error
    client.configure_account(margin_rate=200),
    # ok
    client.configure_account(margin_rate=20),
    client.account_changes(),
    client.get_candles('AUD_USD', price='BMA', count=10, granularity='S5',
                       daily_alignment=0, include_first_query=False),
    client.get_order_book('AUD_USD'),
    client.get_position_book('AUD_USD'),
)

for i in rsp:
    print(i.json())

rsp = run(*[client.create_order('AUD_USD', 1) for _ in range(10)])\

for i in rsp:
    print(i.json())

rsp = run(client.list_open_trades())

for i in rsp:
    print(i.json())

rsp = run(client.close_position('AUD_USD', long_units='ALL'))

for i in rsp:
    print(i.json())

rsp = run(*[client.create_order('AUD_USD', 1) for _ in range(10)])

for i in rsp:
    print(i.json())

rsp = run(client.close_position('AUD_USD', long_units='5'))

for i in rsp:
    print(i.json())

rsp = run(client.close_all_trades())

print(rsp)

rsp = run(*[client.create_order('AUD_USD', 1) for _ in range(10)],
    client.list_orders(),
    client.list_pending_orders())

for i in rsp:
    print(i.json())

rsp = run(client.get_order(OrderSpecifier(client.default_parameters[LastTransactionID])))

for i in rsp:
    print(i.json())

rsp = run(client.create_order('AUD_USD', 10))

for i in rsp:
    print(i.json())

rsp = run(client.limit_order('AUD_USD', 10, 0.5))

for i in rsp:
    print(i.json())

rsp = run(client.cancel_order(order_specifier=OrderSpecifier(client.default_parameters[LastTransactionID])))

for i in rsp:
    print(i.json())

rsp = run(client.market_order('EUR_USD', 1))

for i in rsp:
    print(i.json())

rsp =  run(client.close_all_trades())

print(rsp)

rsp = run(*[client.create_order('AUD_USD', 1) for _ in range(10)])

for i in rsp:
    print(i.json())

rsp = run(
    client.list_positions(),
    client.list_open_positions(),
    client.get_positions('AUD_USD'),
    client.close_position('AUD_USD', long_units='ALL'),
    client.get_pricing('AUD_USD'),

)

for i in rsp:
    print(i.json())

rsp = run(*[client.create_order('AUD_JPY', 1) for _ in range(10)])

for i in rsp:
    print(i.json())

rsp = run(
    client.list_open_trades(),
    client.list_trades(),
    client.get_trades(TradeSpecifier(client.default_parameters[LastTransactionID])),
    client.list_transactions(),
    client.get_transactions(TransactionID(client.default_parameters[LastTransactionID])),

)
for i in rsp:
    print(i.json())

print(run(client.close_all_trades()))


print('TEST SUCCESSFUL!')
