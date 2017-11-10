import pytest

from async_v20.client import OandaClient


@pytest.yield_fixture
@pytest.mark.asyncio
async def client():
    oanda_client = OandaClient(rest_host='127.0.0.1', rest_port=8080, rest_scheme='http',
                               stream_host='127.0.0.1', stream_port=8080, stream_scheme='http')
    yield oanda_client
    await oanda_client.aclose()
    del oanda_client
