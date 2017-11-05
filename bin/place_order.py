import asyncio

from async_v20 import OandaClient
from async_v20.definitions.types import MarketOrder

# Create an order to place
order = MarketOrder('AUD_USD', 1)


async def account():
    async with OandaClient() as client:
        return await client.create_order(order_request=order)


loop = asyncio.get_event_loop()
response = loop.run_until_complete(account())

print(response)
