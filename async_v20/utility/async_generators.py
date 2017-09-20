from ..client import client_session
from ..helpers import sleep


async def poll_account(client: client_session(), poll_interval=6):
    # Ensure client has the latest transaction ID before
    await client.get_account_details()
    while True:
        await sleep(1)
        return await client.account_changes()

