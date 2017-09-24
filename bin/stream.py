import asyncio

from async_v20.client import client_session

async def stream(instruments):
    client = await client_session()
    try:
        async for data in await client.stream_pricing(instruments):
            price = data.get('PRICE', None)
            if price:
                print(await price.series())
    finally:
        client.session.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(stream('AUD_USD'))
