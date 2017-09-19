from collections import namedtuple

import pytest
from async_v20.definitions.types import Account
from async_v20.endpoints.account import GETAccountID
from async_v20.interface.parser import _rest_response
from tests.data.json_data import account


class Response(object):
    raw_headers = {}
    status = 200

    async def json(self):
        return account

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


@pytest.mark.asyncio
async def test_rest_response_builds_account_object_from_json_response():
    client = namedtuple('client', ['default_parameters'])
    self = client(dict())
    result = await _rest_response(self, Response(), GETAccountID)
    print(result)
    assert hasattr(result, 'account')
    assert type(result.account) == Account
    assert hasattr(result.account, 'data')
