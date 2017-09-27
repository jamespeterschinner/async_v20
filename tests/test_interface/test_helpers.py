import inspect

import pytest
from async_v20 import endpoints
from async_v20.client import Client
from async_v20.definitions.types import StopLossOrderRequest, Account
from async_v20.endpoints import POSTOrders
from async_v20.interface.helpers import _arguments
from async_v20.interface.helpers import create_annotation_lookup
from async_v20.interface.helpers import create_body
from async_v20.interface.helpers import make_args_optional
from hypothesis.strategies import text, sampled_from

client_attrs = [getattr(Client, attr) for attr in dir(Client)]
client_methods = list(filter(lambda x: hasattr(x, 'endpoint'), client_attrs))


@pytest.mark.parametrize('method', client_methods)
def test_make_args_optional(method):
    """Ensure that all arguments passed to endpoint's are optional
    """
    result = make_args_optional(inspect.signature(method))

    def check_valid_param(param):
        if param.default != inspect._empty:
            return True
        else:
            print(param)

    assert all(map(check_valid_param, result.parameters.values()))


text_gen = text()
client_signatures = [inspect.signature(method) for method in client_methods]


def bound_args(sig):
    args = [text_gen.example() for _ in range(len(sig.parameters.keys()))]
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


location = sampled_from(['header', 'path', 'query'])
test_arguments_arguments = [(getattr(endpoints, cls), location.example()) for cls in endpoints.__all__]


@pytest.mark.parametrize('endpoint, param_location', test_arguments_arguments)
def test_arguments(endpoint, param_location):
    result = _arguments(endpoint, param_location)
    correct = list(filter(lambda x: x['located'] == param_location, endpoint.parameters))
    assert len(list(result)) == len(list(correct))


@pytest.fixture
def stop_loss_order():
    order = StopLossOrderRequest(trade_id=1234, price=0.8)
    yield order
    del order


@pytest.mark.asyncio
async def test_request_body_is_constructed_correctly(stop_loss_order):
    result = await create_body(POSTOrders.request_schema,
                               {'irrelevant': stop_loss_order, 'test': Account(), 'arg': 'random_string'})
    print(result)
    assert result == {'order': {'tradeID': 'DEFAULT', 'price': 'DEFAULT', 'type': 'DEFAULT', 'timeInForce': 'DEFAULT',
                                'triggerCondition': 'DEFAULT'}}
