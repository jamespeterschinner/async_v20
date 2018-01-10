import asyncio
from time import time
import random
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
    client.get_candles('AUD_USD', from_time=time() - (60 * 10)),
    client.get_order_book('AUD_USD'),
    client.get_position_book('AUD_USD'),
)

for i in rsp:
    print(i.json())

rsp = run(*[client.create_order('AUD_USD', -11) for _ in range(10)])
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

rsp = run(client.close_all_trades())

print(rsp)

rsp = run(*[client.create_order('AUD_USD', 1) for _ in range(10)])

for i in rsp:
    print(i.json())

rsp = run(
    client.list_positions(),
    client.list_open_positions(),
    client.get_position('AUD_USD'),
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
    client.get_transaction(TransactionID(client.default_parameters[LastTransactionID])),

)
for i in rsp:
    print(i.json())

print(run(client.close_all_trades()))

# Test rest functionality

account = run(client.account())

for position in account[0].positions:
    print(position)
    assert position.long.units == 0
    assert position.short.units == 0

trades = [client.create_order(instrument=random.choice(
    list(map(lambda x: x.name, client.instruments))), units=1) for
      _ in range(16)]

rsp = run(*trades)

account = run(client.account())[0]

positions = {r.orderCreateTransaction.instrument: 0 for r in rsp
             if hasattr(r, 'orderFillTransaction')}

for response in rsp:
    fill = getattr(response, 'orderFillTransaction', None)
    if fill is not None:
        positions[fill.instrument] += fill.units

print(positions)
print(account.positions._instrument_index)
print(account.positions._items)
for instrument, units in positions.items():
    assert account.positions.get_instrument(instrument).long.units == units

rsp = run(client.list_open_trades())[0]

assert len(rsp.trades) == len(account.trades)

print(run(client.close_all_trades()))

account = run(client.account())[0]

assert len(account.trades) == 0, f'Account still has trades open {account.trades}'
client.close()
print('TEST SUCCESSFUL!')
