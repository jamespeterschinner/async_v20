import pytest
from tests.fixtures.static import get_account_details_response, get_pricing_response, list_accounts_response
from async_v20.interface.response import Response
from async_v20.definitions.base import Model, Array
from async_v20.definitions.types import ArrayStr
from ..fixtures.client import client
from ..fixtures import server as server_module
from .helpers import sort_json
import asyncio

import logging
logger = logging.getLogger('async_v20')
logger.disabled = True

client = client
server = server_module.server



@pytest.mark.asyncio
async def test_response_creates_correct_json(client, server):
    server_module.status = 200
    async with client as client:
        response = await client.get_account_details()
        resp_json = response.json()

        correct = get_account_details_response.replace(' ', '')
        assert sort_json(resp_json) == sort_json(correct)


@pytest.mark.asyncio
async def test_response_returns_json(client, server):
    async with client as client:
        accounts = await client.list_accounts()
        account_details = await client.get_account_details()
        pricing = await client.get_pricing()

    assert sort_json(accounts.json()) == sort_json(list_accounts_response.replace(' ', ''))
    assert sort_json(account_details.json()) == sort_json(get_account_details_response.replace(' ', ''))
    assert sort_json(pricing.json()) == sort_json(get_pricing_response.replace(' ', ''))

@pytest.mark.asyncio
async def test_response_keys_can_be_accessed_through_dot(client, server):
    async with client as client:
        accounts = await client.list_accounts()
        account_details = await client.get_account_details()
        pricing = await client.get_pricing()

    for response in [accounts, account_details, pricing]:
        for key, value in response.items():
            assert getattr(response, key) == value
            with pytest.raises(AttributeError):
                getattr(response, key+'_test')

def test_response_doesnt_error_when_response_contains_no_data():
    result = Response(None, 400, True, 'UNIX')

@pytest.mark.asyncio
async def test_response_repr(client, server):
    with client as client:
        rsp = await client.get_candles('AUD_USD')
        repr(rsp)

@pytest.mark.asyncio
async def test_response_dict(client, server):
    def check_types(item):
        for value in item.values():
            if isinstance(value, dict):
                check_types(value)
            assert not isinstance(value, (Model, Array))

    async with client as client:
        for rsp in await asyncio.gather(
                client.get_account_details(),
                client.get_candles('AUD_USD'),
                client.list_accounts(),
                client.list_services(),
                client.list_open_trades(),
            ):
            check_types(rsp.dict())

    response = Response({'test': ArrayStr('1','2','3')}, 200, True, 'UNIX')
    check_types(response.dict())