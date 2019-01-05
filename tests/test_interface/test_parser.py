import async_timeout
import pytest

from async_v20.definitions.base import Array
from async_v20.definitions.types import Account, AccountSummary, AccountProperties
from async_v20.definitions.types import Position
from async_v20.endpoints.account import GETAccountID, GETAccountIDSummary, GETAccounts
from async_v20.endpoints.annotations import SinceTransactionID, LastTransactionID
from async_v20.endpoints.instrument import GETInstrumentsCandles
from async_v20.exceptions import ResponseTimeout, UnexpectedStatus
from async_v20.interface.parser import _construct_json_body_and_schema
from async_v20.interface.parser import _create_response
from async_v20.interface.parser import _lookup_schema
from async_v20.interface.parser import _rest_response
from tests.data.json_data import GETAccountIDSummary_response
from tests.data.json_data import GETAccountID_response
from tests.data.json_data import GETAccounts_response
from tests.data.json_data import GETInstrumentsCandles_response
from tests.data.json_data import stream_price
from tests.data.json_data import stream_price_heartbeat
from tests.data.json_data import stream_transaction
from tests.data.json_data import stream_transaction_heartbeat
from tests.fixtures import server as server_module
from tests.fixtures.client import client
from tests.fixtures.static import account_changes_response
from tests.test_interface.helpers import order_dict
from async_v20.endpoints.pricing import GETPricingStream
from async_v20.endpoints.transaction import GETTransactionsStream
from async_v20.definitions.types import PricingHeartbeat
from async_v20.definitions.types import TransactionHeartbeat
from async_v20.definitions.types import Price
from async_v20.definitions.types import Transaction
from .helpers import sort_json

import logging
logger = logging.getLogger('async_v20')
logger.disabled = True

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
    result = await _rest_response(client, rest_response(GETAccountID_response), GETAccountID, enable_rest=False,
                                  method_name='test_method')
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
    result = await _rest_response(client, rest_response(GETAccountIDSummary_response), GETAccountIDSummary,
                                  enable_rest=False, method_name='test_method')
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
    result = await _rest_response(client, rest_response(GETAccounts_response), GETAccounts, enable_rest=False,
                                  method_name='test_method')
    # Ensure the result contains an 'account'

    assert 'accounts' in result
    # Ensure that 'account' is indeed an Account
    # assert type(result['accounts']) == tuple # TODO fix
    assert type(result['accounts'][0]) == AccountProperties


@pytest.mark.asyncio
async def test_rest_response_updates_client_default_parameters(client, rest_response):
    await _rest_response(client, rest_response(GETAccountID_response), GETAccountID, enable_rest=False,
                         method_name='test_method')
    # Ensure default_parameters is updated
    assert client.default_parameters[LastTransactionID] == 14


@pytest.mark.asyncio
@pytest.mark.parametrize('json_body, endpoint', [(GETInstrumentsCandles_response, GETInstrumentsCandles),
                                                 (GETAccounts_response, GETAccounts),
                                                 (GETAccountIDSummary_response, GETAccountIDSummary)])
async def test_conversion_from_server_json_to_response_object_to_json_equal(json_body, endpoint):
    response = await _create_response(json_body, endpoint, *_lookup_schema(endpoint, 200), datetime_format='RFC3339')
    response_json = response.dict(json=True, datetime_format='RFC3339')
    pretty_json_body = order_dict(json_body)
    pretty_response_json = order_dict(response_json)


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
    with pytest.raises(UnexpectedStatus):
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


        assert sort_json(response.json()) == sort_json(account_changes_response)

@pytest.mark.asyncio
async def test_stream_parser_creates_response_objects(client, server):
    async with client as client:
        server_module.sleep_time = 0
        client.stream_timeout = 1
        resp = None
        async with async_timeout.timeout(1):
            async for obj in await client.stream_pricing('AUD_USD'):
                resp = obj
                break
        assert resp
        assert resp.status == 200

@pytest.mark.asyncio
async def test_stream_parser_raises_timeout_error(client, server):
    async with client as client:
        server_module.sleep_time = 0.2
        client.stream_timeout = 0.1
        async with async_timeout.timeout(1):
            with pytest.raises(ResponseTimeout):
                async for obj in await client.stream_pricing('AUD_USD'):
                    pass



def test_construct_json_body_and_schema_creates_same_key_for_both_heartbeat_types():
    price_body, price_schema = _construct_json_body_and_schema(
        line=stream_price_heartbeat,
        schema=GETPricingStream.responses[200],
        endpoint=GETPricingStream,
    )
    transaction_body, transaction_schema = _construct_json_body_and_schema(
        line=stream_transaction_heartbeat,
        schema=GETTransactionsStream.responses[200],
        endpoint=GETTransactionsStream,
    )
    assert list(price_body) == list(transaction_body)
    for body_schema in (price_body, price_schema, transaction_body, transaction_schema):
        assert 'heartbeat' in body_schema

    assert type(PricingHeartbeat(**price_body['heartbeat'])) == PricingHeartbeat
    assert type(TransactionHeartbeat(**transaction_body['heartbeat'])) == TransactionHeartbeat

def test_construct_json_body_and_schema_creates_price():
    price_body, price_schema = _construct_json_body_and_schema(
        line=stream_price,
        schema=GETPricingStream.responses[200],
        endpoint=GETPricingStream,
    )
    for body_schema in (price_body, price_schema):
        assert 'price' in body_schema

    assert type(price_schema['price'](**price_body['price'])) == Price

def test_construct_json_body_and_schema_creates_transaction():
    transaction_body, transaction_schema = _construct_json_body_and_schema(
        line=stream_transaction,
        schema=GETTransactionsStream.responses[200],
        endpoint=GETTransactionsStream,
    )
    for body_schema in (transaction_body, transaction_schema):
        assert 'transaction' in body_schema

    assert isinstance(
        transaction_schema['transaction'](**transaction_body['transaction']),
        Transaction
    )

def test_construct_json_body_and_schema_returns_line_and_schema_upon_key_error():
    line = {'errorMessage': "Invalid value specified for 'instruments'"}
    schema = {'errorCode': str, 'errorMessage': str}
    json_body, json_schema = _construct_json_body_and_schema(
        line=line,
        schema=schema,
        endpoint=GETPricingStream,
    )
    assert line == json_body
    assert schema == json_schema