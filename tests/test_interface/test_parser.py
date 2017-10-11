from collections import namedtuple

import pytest
from async_v20.definitions.types import Account, AccountSummary, AccountProperties
from async_v20.definitions.types import Price, Position
from async_v20.endpoints.account import GETAccountID, GETAccountIDSummary, GETAccounts
from async_v20.endpoints.annotations import LastTransactionID
from async_v20.endpoints.instrument import GETInstrumentsCandles
from async_v20.endpoints.pricing import GETPricingStream
from async_v20.interface.parser import _create_response
from async_v20.interface.parser import _rest_response
from async_v20.interface.parser import _stream_parser

from tests.data.json_data import GETAccountIDSummary_response
from tests.data.json_data import GETAccountID_response
from tests.data.json_data import GETAccounts_response
from tests.data.json_data import GETInstrumentsCandles_response
from tests.data.stream_data import price_bytes
from .helpers import order_dict


@pytest.fixture
@pytest.mark.asyncio
async def stream_generator():
    """FIXTURE to simulate data stream"""
    async def agen():
        while True:
            yield price_bytes # DATA
    stream = (i async for i in agen())
    yield stream
    del stream

@pytest.mark.asyncio
async def test_response_generator(stream_generator):
    """TEST stream_generator fixture works as intended"""
    result = list()
    result.append(await stream_generator.asend(None))
    result.append(await stream_generator.asend(None))
    assert result == [price_bytes, price_bytes]


@pytest.fixture()
def stream_response(stream_generator):
    """FIXTURE to simulate an `aiohttp` stream response"""
    class StreamResponse:
        content = stream_generator
        status = 200

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            pass
    response = StreamResponse()
    yield response
    del response


@pytest.mark.asyncio
async def test_stream_parser_creates_price_object(stream_response):
    async_gen = _stream_parser(stream_response, GETPricingStream)
    iteration = await async_gen.asend(None)
    assert type(iteration.get('PRICE')) == Price


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


@pytest.fixture
def client_instance():
    """FIXTURE to simulate client object"""
    client = namedtuple('client', ['default_parameters'])
    yield client(dict())


@pytest.mark.asyncio
async def test_rest_response_builds_account_object_from_json_response(client_instance, rest_response):
    result = await _rest_response(client_instance, rest_response(GETAccountID_response), GETAccountID)
    # Ensure the result contains an 'account'
    assert 'account' in result
    # Ensure that 'account' is indeed an Account
    assert type(result['account']) == Account
    # Ensure that the Account has expected attributes
    assert hasattr(result['account'], 'data')
    # Ensure that account.positions is a list and contains a position
    # This tests that the Array object created the correct object
    assert type(result['account'].positions) == list
    assert type(result['account'].positions[0]) == Position

@pytest.mark.asyncio
async def test_rest_response_builds_account_summary_from_json_response(client_instance, rest_response):
    result = await _rest_response(client_instance, rest_response(GETAccountIDSummary_response), GETAccountIDSummary)
    # Ensure the result contains an 'account'
    assert 'account' in result
    # Ensure that 'account' is indeed an Account
    assert type(result['account']) == AccountSummary
    # Ensure that the Account has expected attributes
    assert hasattr(result['account'], 'data')

def test_array_object_creates_list_of_objects():
    array = GETAccounts.responses[200]['accounts']
    result = array(GETAccounts_response['accounts'])
    assert type(result) == list
    assert type(result[0]) == AccountProperties
    assert hasattr(result[0], 'id')


@pytest.mark.asyncio
async def test_rest_response_builds_array_account_properties(client_instance, rest_response):
    result = await _rest_response(client_instance, rest_response(GETAccounts_response), GETAccounts)
    # Ensure the result contains an 'account'
    print(result)
    assert 'accounts' in result
    # Ensure that 'account' is indeed an Account
    assert type(result['accounts']) == list
    assert type(result['accounts'][0]) ==  AccountProperties

@pytest.mark.asyncio
async def test_rest_response_updates_client_default_parameters(client_instance, rest_response):
    await _rest_response(client_instance, rest_response(GETAccountID_response), GETAccountID)
    # Ensure default_parameters is updated
    assert client_instance.default_parameters[LastTransactionID] == str(14)

@pytest.mark.asyncio
@pytest.mark.parametrize('json_body, schema', [(GETInstrumentsCandles_response, GETInstrumentsCandles.responses[200]),
                                               (GETAccounts_response, GETAccounts.responses[200]),
                                               (GETAccountIDSummary_response, GETAccountIDSummary.responses[200])])
async def test_conversion_from_server_json_to_response_object_to_json_equal(json_body, schema):
    response = await _create_response(json_body, schema)
    response_json = response.json_dict()
    pretty_json_body = order_dict(json_body)
    pretty_response_json = order_dict(response_json)
    print('SERVER JSON:\n', pretty_json_body)
    print('Response JSON:\n', pretty_response_json)
    assert response_json == json_body