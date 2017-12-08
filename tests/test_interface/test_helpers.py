import inspect

import pytest

from async_v20 import endpoints
from async_v20 import interface
from async_v20.client import OandaClient
from async_v20.definitions.types import Account
from async_v20.definitions.types import AccountID, OrderRequest
from async_v20.definitions.types import StopLossOrderRequest
from async_v20.endpoints import POSTOrders
from async_v20.endpoints.annotations import Authorization
from async_v20.endpoints.annotations import Bool
# noinspection PyProtectedMember
from async_v20.interface.helpers import _arguments
# noinspection PyProtectedMember
from async_v20.interface.helpers import _create_request_params
from async_v20.interface.helpers import construct_arguments
from async_v20.interface.helpers import create_body
from async_v20.interface.helpers import create_request_kwargs
from async_v20.interface.helpers import create_url
from .helpers import order_dict
from ..data.json_data import GETAccountID_response
from ..fixtures.client import client
from ..test_definitions.helpers import get_valid_primitive_data

client_attrs = [getattr(OandaClient, attr) for attr in dir(OandaClient)]
client_methods = list(filter(lambda x: hasattr(x, 'endpoint'), client_attrs))

client = client


def test_order_dict():
    first = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4, 'f': {'e': 5, 'g': 6}}}
    second = {'c': {'f': {'g': 6, 'e': 5}, 'e': 4, 'd': 3}, 'b': 2, 'a': 1}
    assert order_dict(first) == order_dict(second)


@pytest.fixture
def stop_loss_order():
    order = StopLossOrderRequest(trade_id=1234, price=0.8)
    yield order
    del order


client_signatures = [inspect.signature(method) for method in client_methods]


def bound_args(sig):
    args = {name: get_valid_primitive_data(param.annotation) for name, param in sig.parameters.items()}
    bound = sig.bind(**args)
    return sig, bound.arguments, tuple(args.values())


annotation_lookup_arguments = [bound_args(sig) for sig in client_signatures]


@pytest.mark.asyncio
@pytest.mark.parametrize('signature, bound_arguments, args', annotation_lookup_arguments)
async def test_construct_arguments(signature, bound_arguments, args):
    """Ensure that the annotation lookup dictionary is built correctly"""
    result = construct_arguments(signature, bound_arguments)
    for annotation, instance in result.items():
        if isinstance(instance, bool):
            assert issubclass(annotation, Bool)
        else:
            assert type(instance) == annotation


locations = ['header', 'path', 'query']
test_arguments_arguments = [(getattr(endpoints, cls), location)
                            for location in locations for cls in endpoints.__all__]


@pytest.mark.parametrize('endpoint, param_location', test_arguments_arguments)
def test_arguments(endpoint, param_location):
    result = _arguments(endpoint, param_location)
    correct = list(filter(lambda x: x['located'] == param_location, endpoint.parameters))
    assert len(list(result)) == len(list(correct))


@pytest.mark.parametrize('interface_method', [method for cls in (getattr(interface, cls) for cls in interface.__all__)
                                              for method in cls.__dict__.values() if hasattr(method, 'endpoint')])
@pytest.mark.asyncio
async def test_create_request_params(client, interface_method):
    """Test that all every argument supplied to an endpoint goes into the HTTP request"""

    endpoint = interface_method.endpoint
    sig = interface_method.__signature__
    print(interface_method.__name__)
    args = tuple(get_valid_primitive_data(param.annotation)
                 for param in sig.parameters.values() if param.kind == 1)
    bound = dict(sig.bind(*args).arguments)
    arguments = construct_arguments(sig, bound)
    total_params = []
    print(endpoint.request_schema)
    for location in locations:
        print('Endpoint: ', endpoint)
        print('Arguments: ', arguments)
        print('Location: ', location)
        result = _create_request_params(client, endpoint, arguments, location)
        print('Possible Arguments', list(_arguments(endpoint, arguments)))
        print(location, ': ', result)
        total_params.extend(result)

    # These parameters are set by default in the client.
    # They will appear in total_arguments even though they were not passed
    # therefore We will remove them
    for default_param in ['Authorization', 'LastTransactionID', 'Accept-Datetime-Format',
                          'accountID']:
        try:
            total_params.remove(default_param)
        except ValueError:
            continue

    assert len(total_params) == len(arguments) - len(list(endpoint.request_schema))


@pytest.mark.parametrize('endpoint', [getattr(endpoints, cls) for cls in endpoints.__all__])
def test_create_url(client, endpoint):
    template = endpoint.path
    arguments = [value for value in template if not isinstance(value, str)]
    values = list(map(lambda x: str(x), range(len(arguments))))
    arguments = dict(zip(arguments, values))
    url = create_url(client, endpoint, arguments)
    path = url.path
    for value in values:
        assert value in path
        path = path[path.index(value):]

@pytest.mark.parametrize('endpoint', [getattr(endpoints, cls) for cls in endpoints.__all__])
def test_create_url_raises_error_when_missing_arguments(client, endpoint):
    if len(endpoint.path) > 3: # URL TEMPLATES with len > 3 will require addition arguments to be passed
        with pytest.raises(ValueError):
            url = create_url(client, endpoint, {})

@pytest.mark.parametrize('interface_method', [method for cls in (getattr(interface, cls) for cls in interface.__all__)
                                              for method in cls.__dict__.values() if hasattr(method, 'endpoint')])
def test_create_request_kwargs(client, interface_method):
    client.default_parameters.update({AccountID: 'TEST_ID',
                                      Authorization: 'TEST_AUTH'})

    args = []
    for param in interface_method.__signature__.parameters.values():
        args.append(get_valid_primitive_data(param.annotation))

    args = args[1:]

    print(interface_method.__name__)
    if interface_method.__name__ == 'create_order':
        args = ((1, 1, 'STOP_LOSS',),)
    elif interface_method.__name__ == 'replace_order':
        args = (12, (1, 1, 'STOP_LOSS'))
    print('ARGS: ', args)
    request_kwargs = create_request_kwargs(client,
                                           interface_method.endpoint,
                                           interface_method.__signature__,
                                           *args)
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
    account_to_json = account.dict(json=True)

    response_json_account = order_dict(response_json_account)
    account_to_json = order_dict(account_to_json)
    print('SERVER DATA')
    print(response_json_account)
    print('ASYNC_20 DATA')
    print(account_to_json)
    assert response_json_account == account_to_json
