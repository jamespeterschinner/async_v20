import asyncio
from perftests.helpers import Time, client


print('Running creating_dataframe benchmark with async_v20 version', client.version)
loop = asyncio.get_event_loop()

# This will test the speed of the _formatting_order_requests helper function
client.format_order_requests = True

async def place_orders(count):
    await asyncio.gather(*[
        client.create_order(
            'AUD_USD',
            units=0,
            stop_loss_on_fill=0,
            take_profit_on_fill=0,
        trailing_stop_loss_on_fill=0,
        )
    for _ in range(count)])


with Time() as t:
    for _ in range(10):
        loop.run_until_complete(place_orders(500))