import pytest
from .fixtures.client import client
from .fixtures.server import server

client = client
server = server

@pytest.mark.asyncio
async def test_list_services_returns_services(client, server):
    async with client as client:
        rsp = await client.list_services()
    print(rsp.services)
    assert getattr(rsp, 'services')