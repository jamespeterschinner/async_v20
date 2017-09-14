import asyncio
from async_v20.client import client_session


async def server():
    client = await client_session()
    try:
        accounts = await client.get_accounts()
        # changes = await client.account_changes()
        # instruments = await client.account_instruments()
        aud_usd = await client.get_candles('AUD_USD')
    finally:
        client.session.close()
    return accounts, aud_usd


loop = asyncio.get_event_loop()
accounts, aud_usd = loop.run_until_complete(server())
