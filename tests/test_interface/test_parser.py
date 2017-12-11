import pytest

from async_v20.definitions.base import Array
from async_v20.definitions.types import Account, AccountSummary, AccountProperties
from async_v20.definitions.types import Position
from async_v20.endpoints.account import GETAccountID, GETAccountIDSummary, GETAccounts
from async_v20.endpoints.annotations import SinceTransactionID, LastTransactionID
from async_v20.endpoints.instrument import GETInstrumentsCandles
from async_v20.interface.parser import _create_response
from async_v20.interface.parser import _lookup_schema
from async_v20.interface.parser import _rest_response
from tests.data.json_data import GETAccountIDSummary_response
from tests.data.json_data import GETAccountID_response
from tests.data.json_data import GETAccounts_response
from tests.data.json_data import GETInstrumentsCandles_response
from tests.fixtures import server as server_module
from tests.fixtures.client import client
from tests.fixtures.static import account_changes_response
from tests.test_interface.helpers import order_dict
import async_timeout

client = client
server = server_module.server


@pytest.fixture()
def rest_response():
    """FIXTURE to simulate an `aiohttp` rest response"""

    class RestResponse(object):
        raw_headers = {}

        def __init__(self, data, status=200):
            self.data = data
            self.status = status

        async def json(self):
            return self.data

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            pass

    yield RestResponse
    del RestResponse


@pytest.mark.asyncio
async def test_rest_response_builds_account_object_from_json_response(client, rest_response):
    result = await _rest_response(client, rest_response(GETAccountID_response), GETAccountID)
    # Ensure the result contains an 'account'
    assert 'account' in result
    # Ensure that 'account' is indeed an Account
    assert type(result['account']) == Account
    # Ensure that the Account has expected attributes
    assert hasattr(result['account'], 'data')
    # Ensure that account.positions is a list and contains a position
    # This tests that the Array object created the correct object
    # assert type(result['account'].positions) == tuple # TODO fix
    assert type(result['account'].positions[0]) == Position


@pytest.mark.asyncio
async def test_rest_response_builds_account_summary_from_json_response(client, rest_response):
    result = await _rest_response(client, rest_response(GETAccountIDSummary_response), GETAccountIDSummary)
    # Ensure the result contains an 'account'
    assert 'account' in result
    # Ensure that 'account' is indeed an Account
    assert type(result['account']) == AccountSummary
    # Ensure that the Account has expected attributes
    assert hasattr(result['account'], 'data')


def test_array_object_creates_tuple_of_objects():
    array = GETAccounts.responses[200]['accounts']
    result = array(*GETAccounts_response['accounts'])
    assert isinstance(result, Array)
    assert type(result[0]) == AccountProperties
    assert hasattr(result[0], 'id')


@pytest.mark.asyncio
async def test_rest_response_builds_array_account_properties(client, rest_response):
    result = await _rest_response(client, rest_response(GETAccounts_response), GETAccounts)
    # Ensure the result contains an 'account'
    print(result)
    assert 'accounts' in result
    # Ensure that 'account' is indeed an Account
    # assert type(result['accounts']) == tuple # TODO fix
    assert type(result['accounts'][0]) == AccountProperties


@pytest.mark.asyncio
async def test_rest_response_updates_client_default_parameters(client, rest_response):
    await _rest_response(client, rest_response(GETAccountID_response), GETAccountID)
    # Ensure default_parameters is updated
    assert client.default_parameters[LastTransactionID] == 14


@pytest.mark.asyncio
@pytest.mark.parametrize('json_body, endpoint', [(GETInstrumentsCandles_response, GETInstrumentsCandles),
                                                 (GETAccounts_response, GETAccounts),
                                                 (GETAccountIDSummary_response, GETAccountIDSummary)])
async def test_conversion_from_server_json_to_response_object_to_json_equal(json_body, endpoint):
    response = await _create_response(json_body, endpoint, *_lookup_schema(endpoint, 200))
    response_json = response.dict(json=True)
    pretty_json_body = order_dict(json_body)
    pretty_response_json = order_dict(response_json)
    print('SERVER JSON:\n', pretty_json_body)
    print('Response JSON:\n', pretty_response_json)
    assert response_json == json_body


@pytest.mark.asyncio
async def test_parser_returns_correct_boolean_for_response(client, server):
    async with client as client:
        server_module.status = 400  # make this response bad
        response = await client.get_account_details()
        assert bool(response) == False
        server_module.status = 200  # make this response good
        response = await client.get_account_details()
        assert bool(response) == True


@pytest.mark.asyncio
async def test_parser_raises_connection_error_with_bad_http_status(client, server):
    server_module.status = 500
    with pytest.raises(ConnectionError):
        async with client as client:
            pass


@pytest.mark.asyncio
async def test_parser_updates_since_transaction_id(client, server):
    async with client as client:
        # Test server will return response with lastTransactionID
        # Being 10385
        assert client.default_parameters[SinceTransactionID] != 10547
        assert client.default_parameters[SinceTransactionID] == \
               client.default_parameters[LastTransactionID]

        response = await client.account_changes()
        assert client.default_parameters[SinceTransactionID] == 10547
        print(response.json())
        print(account_changes_response)
        assert response.json() == account_changes_response

@pytest.mark.asyncio
async def test_stream_parser_raises_timeout_error(client, server):
    async with client as client:
        server_module.sleep_time = 1
        client.stream_timeout = 0.1
        items = 3
        async with async_timeout.timeout(items*client.stream_timeout+1):
            with pytest.raises(TimeoutError):
                async for obj in await client.stream_pricing('AUD_USD'):
                    items -= 1
                    print(obj)
                    if items <= 0:
                        print('BREAK CALLED')
                        break

