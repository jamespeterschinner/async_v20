import asyncio

from async_v20.client import client_session

async def stream(instruments):
    client = await client_session()
    try:
        async for price in await client.stream_pricing(instruments):
            print(price)
            if price[0] =='PRICE':
                print(await price[1].data())
    finally:
        client.session.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(stream('AUD_USD'))
