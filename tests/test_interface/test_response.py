from ..test_client import client, server
import pytest
from ..server.static import get_account_details_response

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

