"""Import and setup ready for user interaction"""

from async_v20 import *
client = OandaClient(stream_timeout=4)
import asyncio
loop = asyncio.get_event_loop()
run = loop.run_until_complete