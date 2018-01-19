import pytest
import asyncio
from async_v20.client import OandaClient


@pytest.yield_fixture
@pytest.mark.asyncio
async def client():
    oanda_client = OandaClient(rest_host='127.0.0.1', rest_port=8080, rest_scheme='http',
                               stream_host='127.0.0.1', stream_port=8080, stream_scheme='http',
                               health_host='127.0.0.1', health_port=8080, health_scheme='http')
    yield oanda_client
    oanda_client.close()
    await asyncio.sleep(0)
