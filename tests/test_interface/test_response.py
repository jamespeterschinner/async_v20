
import pytest
from ..server.static import get_account_details_response, get_pricing_response, list_accounts_response
from ..test_client import client, server

client = client
server = server
@pytest.mark.asyncio
async def test_response_creates_correct_json(client, server):
    async with client as client:
        response = await client.get_account_details()
        resp_json = response.json()
        print(resp_json)
        correct = get_account_details_response.replace(' ','')
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