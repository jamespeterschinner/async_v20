import pytest

from tests.fixtures.static import get_account_details_response, get_pricing_response, list_accounts_response

from ..fixtures.client import client
from ..fixtures import server as server_module

client = client
server = server_module.server


@pytest.mark.asyncio
async def test_response_creates_correct_json(client, server):
    server_module.status = 200
    async with client as client:
        response = await client.get_account_details()
        resp_json = response.json()
        print(resp_json)
        correct = get_account_details_response.replace(' ', '')
        print(correct)
        assert resp_json == correct


@pytest.mark.asyncio
async def test_response_returns_json(client, server):
    async with client as client:
        accounts = await client.list_accounts()
        account_details = await client.get_account_details()
        pricing = await client.get_pricing()

    assert accounts.json() == list_accounts_response.replace(' ', '')
    assert account_details.json() == get_account_details_response.replace(' ', '')
    assert pricing.json() == get_pricing_response.replace(' ', '')
