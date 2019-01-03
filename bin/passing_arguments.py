import asyncio

from async_v20 import OandaClient

client = OandaClient()

# This
coroutine_1 = client.create_order('AUD_USD', 10)

# Is the same as this
from async_v20 import InstrumentName, DecimalNumber

coroutine_2 = client.create_order(
    InstrumentName('AUD_USD'), DecimalNumber(10)
)

# Is the same as this
from async_v20 import OrderRequest

coroutine_3 = client.post_order(
    order_request=OrderRequest(
        instrument='AUD_USD', units=10, type='MARKET'
    )
)

loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
        coroutine_1,
        coroutine_2,
        coroutine_3
    )
)
