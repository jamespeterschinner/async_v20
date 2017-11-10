import asyncio

from async_v20 import OandaClient

client = OandaClient()

loop = asyncio.get_event_loop()
response = loop.run_until_complete(client.initialize())

# Write your code here

client.close()
