import pytest
from async_v20.interface.parser import _rest_response
from collections import namedtuple
from async_v20.endpoints.account import GETAccountID
from ..data.json_data import account_details_endpoint_response
from async_v20.endpoints.annotations import LastTransactionID

class Response(object):
    raw_headers = {}
    status = 200

    async def json(self):
        return account_details_endpoint_response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


@pytest.mark.asyncio
async def test_rest_response_builds_account_object_from_json_response():
    Client = namedtuple('client', ['default_parameters'])
    self = Client({})
    result = await _rest_response(self, Response(), GETAccountID)
    print(result)
    print(self.default_parameters)
    print(self.default_parameters[LastTransactionID])
    assert self.default_parameters[LastTransactionID] == str(14)
