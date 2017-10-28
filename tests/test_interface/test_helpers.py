import inspect
from inspect import Parameter

import pytest
from hypothesis.strategies import text, sampled_from

from async_v20 import endpoints
from async_v20 import interface
from async_v20.client import OandaClient
from async_v20.definitions.types import Account
from async_v20.definitions.types import AccountID, OrderRequest
from async_v20.definitions.types import StopLossOrderRequest
from async_v20.endpoints import POSTOrders
from async_v20.endpoints.annotations import Authorization
from async_v20.interface.helpers import _arguments
from async_v20.interface.helpers import _create_request_params
from async_v20.interface.helpers import create_annotation_lookup
from async_v20.interface.helpers import create_body
from async_v20.interface.helpers import create_request_kwargs
from async_v20.interface.helpers import create_url
from .helpers import order_dict
from ..data.json_data import GETAccountID_response

client_attrs = [getattr(OandaClient, attr) for attr in dir(OandaClient)]
client_methods = list(filter(lambda x: hasattr(x, 'endpoint'), client_attrs))


@pytest.fixture
def stop_loss_order():
    order = StopLossOrderRequest(trade_id=1234, price=0.8)
    yield order
    del order


@pytest.fixture
def client():
    client = OandaClient(token='test_token', rest_host='rest_test', stream_host='stream_test')
    client.default_parameters = {}
    yield client
    del client


text_gen = text()
client_signatures = [inspect.signature(method) for method in client_methods]


def bound_args(sig):
    args = [text_gen.example() for param in sig.parameters.values()
            if param.kind not in (Parameter.VAR_KEYWORD, Parameter.VAR_POSITIONAL)]
    bound = sig.bind(*args)
    return sig, bound.arguments, args


annotation_lookup_arguments = [bound_args(sig) for sig in client_signatures]


@pytest.mark.asyncio
@pytest.mark.parametrize('signature, bound_arguments, args', annotation_lookup_arguments)
async def test_create_annotation_lookup(signature, bound_arguments, args):
    """Ensure that the annotation lookup dictionary is built correctly"""
    result = create_annotation_lookup(signature, bound_arguments)
    annotations = [param.annotation for param in signature.parameters.values()]
    correct = zip(annotations, args)
    assert all(map(lambda x: result[x[0]] == x[1], correct))


param_locations = ['header', 'path', 'query']
location = sampled_from(param_locations)
test_arguments_arguments = [(getattr(endpoints, cls), location.example()) for cls in endpoints.__all__]


@pytest.mark.parametrize('endpoint, param_location', test_arguments_arguments)
def test_arguments(endpoint, param_location):
    result = _arguments(endpoint, param_location)
    correct = list(filter(lambda x: x['located'] == param_location, endpoint.parameters))
    assert len(list(result)) == len(list(correct))


test_arguments_arguments = [(getattr(endpoints, cls), location.example(),) for cls in endpoints.__all__]


@pytest.mark.parametrize('interface_method', [method for cls in (getattr(interface, cls) for cls in interface.__all__)
                                              for method in cls.__dict__.values() if hasattr(method, 'endpoint')])
@pytest.mark.asyncio
async def test_create_request_params(client, interface_method):
    """Test that all every argument supplied to an endpoint goes into the HTTP request"""

    endpoint = interface_method.endpoint
    sig = interface_method.__signature__
    print(interface_method.__name__)
    args = tuple(range(len([param for param in sig.parameters.values()
                            if param.kind not in (Parameter.VAR_KEYWORD, Parameter.VAR_POSITIONAL)])))
    bound = dict(sig.bind(*args).arguments)
    arguments = create_annotation_lookup(sig, bound)
    total_params = []
    print(endpoint.request_schema)
    for location in param_locations:
        print('Endpoint: ', endpoint)
        print('Arguments: ', arguments)
        print('Location: ', location)
        result = _create_request_params(client, endpoint, arguments, location)
        print('Possible Arguments', list(_arguments(endpoint, arguments)))
        print(location, ': ', result)
        total_params.extend(result)

    assert len(total_params) == len(arguments) - len(list(endpoint.request_schema)) - 1  # -1 removes 'self'


@pytest.mark.parametrize('endpoint', [getattr(endpoints, cls) for cls in endpoints.__all__])
def test_create_url(client, endpoint):
    path = endpoint.path.path
    arguments = [value for value in path if not isinstance(value, str)]
    values = list(map(lambda x: str(x), range(len(arguments))))
    arguments = dict(zip(arguments, values))
    url = create_url(client, endpoint, arguments)
    path = url.path
    for value in values:
        assert value in path
        path = path[path.index(value):]


@pytest.mark.parametrize('interface_method', [method for cls in (getattr(interface, cls) for cls in interface.__all__)
                                              for method in cls.__dict__.values() if hasattr(method, 'endpoint')])
def test_create_request_kwargs(client, interface_method):
    client.default_parameters.update({AccountID: 'TEST_ID',
                                      Authorization: 'TEST_AUTH'})
    args = list(map(lambda x: str(x), (range(len(interface_method.__signature__.parameters)))))[1:]
    print(interface_method.__name__)
    if interface_method.__name__ == 'create_order':
        args = ((1, 1, 'STOP_LOSS',),)
    elif interface_method.__name__ == 'replace_order':
        args = (12, (1, 1, 'STOP_LOSS'))

    request_kwargs = create_request_kwargs(client,
                                           interface_method.endpoint,
                                           interface_method.__signature__,
                                           *args)
    print("('", request_kwargs['method'], "', '", request_kwargs['url'].path, "')")

    assert 'method' in request_kwargs
    assert 'url' in request_kwargs
    assert 'headers' in request_kwargs
    assert 'params' in request_kwargs
    assert 'json' in request_kwargs

    assert [request_kwargs['method']] in [['POST'], ['GET'], ['PUT'], ['PATCH'], ['DELETE']]
    assert 'Authorization' in request_kwargs['headers']


@pytest.mark.asyncio
async def test_request_body_is_constructed_correctly(stop_loss_order):
    result = create_body(POSTOrders.request_schema,
                         {OrderRequest: stop_loss_order, 'test': Account(), 'arg': 'random_string'})
    correct = {'order': {'tradeID': 1234, 'price': '0.8', 'type': 'STOP_LOSS', 'timeInForce': 'GTC',
                         'triggerCondition': 'DEFAULT'}}
    print('RESULT: \n', result)
    print('CORRECT: \n', correct)
    assert result == correct


@pytest.mark.asyncio
async def test_objects_can_be_converted_between_Model_object_and_json():
    account = Account(**GETAccountID_response['account'])
    response_json_account = GETAccountID_response['account']
    account_to_json = account.json_dict()

    response_json_account = order_dict(response_json_account)
    account_to_json = order_dict(account_to_json)
    print('SERVER DATA')
    print(response_json_account)
    print('ASYNC_20 DATA')
    print(account_to_json)
    assert response_json_account == account_to_json
