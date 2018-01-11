"""Import and setup ready for user interaction"""

from async_v20 import *
import asyncio
import logging

logger = logging.getLogger('async_v20')
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

client = OandaClient(rest_timeout=40)
loop = asyncio.get_event_loop()
run = loop.run_until_complete