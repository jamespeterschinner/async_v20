import asyncio
from async_v20.client import client_session


async def server():
    client = await client_session()
    try:
        response = await client.get_accounts()
    finally:
        client.session.close()
    return response, client


loop = asyncio.get_event_loop()
resp = loop.run_until_complete(server())
