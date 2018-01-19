import inspect
import json
import re

import pandas as pd
import pytest

from async_v20 import endpoints
from async_v20.client import OandaClient
from async_v20.definitions.types import Account
from async_v20.definitions.types import DateTime
from async_v20.definitions.types import OrderRequest
from async_v20.definitions.types import StopLossOrderRequest
from async_v20.definitions.types import ArrayInstrument
from async_v20.definitions.types import MarketOrderRequest
from async_v20.endpoints import POSTOrders
from async_v20.endpoints.annotations import Bool
from async_v20.endpoints.annotations import Authorization
from async_v20.endpoints.annotations import SinceTransactionID
from async_v20.endpoints.annotations import LastTransactionID
from async_v20.exceptions import FailedToCreatePath, InvalidOrderRequest
from async_v20.interface.helpers import _create_request_params
from async_v20.interface.helpers import _format_order_request
from async_v20.interface.helpers import construct_arguments
from async_v20.interface.helpers import create_body
from async_v20.interface.helpers import create_request_kwargs
from async_v20.interface.helpers import create_url
from async_v20.interface.helpers import too_many_passed_transactions
from .helpers import order_dict
from ..data.json_data import GETAccountID_response, example_instruments
from ..fixtures.client import client
from ..fixtures.server import server
from ..test_definitions.helpers import get_valid_primitive_data

client_attrs = [getattr(OandaClient, attr) for attr in dir(OandaClient)]
client_methods = list(filter(lambda x: hasattr(x, 'endpoint'), client_attrs))

import logging
logger = logging.getLogger('async_v20')
logger.disabled = True

client = client
server = server


def test_order_dict():
    first = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4, 'f': {'e': 5, 'g': 6}}}
    second = {'c': {'f': {'g': 6, 'e': 5}, 'e': 4, 'd': 3}, 'b': 2, 'a': 1}
    assert order_dict(first) == order_dict(second)


@pytest.fixture
def stop_loss_order():
    order = StopLossOrderRequest(instrument='AUD_USD', trade_id=1234, price=0.8)
    yield order
    del order


client_signatures = [inspect.signature(method) for method in client_methods]


def kwargs(sig):
    args = {name: get_valid_primitive_data(param.annotation) for name, param in sig.parameters.items()
            if name != 'self'}
    return args


annotation_lookup_arguments = [(sig, kwargs(sig)) for sig in client_signatures]


@pytest.mark.asyncio
@pytest.mark.parametrize('signature, arguments', annotation_lookup_arguments)
async def test_construct_arguments(client, server, signature, arguments):
    """Ensure that the annotation lookup dictionary is built correctly"""
    await client.initialize()
    result = construct_arguments(client, signature, **arguments)
    for annotation, instance in result.items():
        if isinstance(instance, bool):
            assert issubclass(annotation, Bool)
        elif isinstance(instance, pd.Timestamp):
            assert issubclass(annotation, DateTime)
        else:
            assert type(instance) == annotation


locations = ['header', 'path', 'query']
test_arguments_arguments = [(getattr(endpoints, cls), location)
                            for location in locations for cls in endpoints.__all__]


@pytest.mark.parametrize('method, signature, kwargs', zip(client_methods, *zip(*annotation_lookup_arguments)))
@pytest.mark.asyncio
async def test_create_request_params(client, method, signature, kwargs):
    """Test that all every argument supplied to an endpoint goes into the HTTP request"""

    endpoint = method.endpoint
    arguments = construct_arguments(client, signature, **kwargs)
    total_params = []
    for location in locations:
        result = _create_request_params(client, endpoint, arguments, location)
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
    if len(endpoint.path) > 3:  # URL TEMPLATES with len > 3 will require addition arguments to be passed
        with pytest.raises(FailedToCreatePath):
            url = create_url(client, endpoint, {})


@pytest.mark.asyncio
@pytest.mark.parametrize('method, signature, kwargs', zip(client_methods, *zip(*annotation_lookup_arguments)))
async def test_create_request_kwargs(client, server, method, signature, kwargs):

    await client.initialize()
    client.format_order_requests = True
    args = construct_arguments(client, signature, **kwargs)
    if OrderRequest in args:
        args.update({OrderRequest: OrderRequest(instrument='AUD_USD', units=1)})

    request_kwargs = create_request_kwargs(client, method.endpoint, args)

    # Make sure args are not empty
    assert request_kwargs.get('method', 1)
    assert request_kwargs.get('url', 1)
    assert request_kwargs.get('headers', 1)
    assert request_kwargs.get('params', 1)
    assert request_kwargs.get('json', 1)

    assert [request_kwargs['method']] in [['POST'], ['GET'], ['PUT'], ['PATCH'], ['DELETE']]

    auth_in_header = 'Authorization' in request_kwargs.get('headers', '')
    if Authorization in method.endpoint.parameters:
        assert auth_in_header
    else:
        assert not auth_in_header


@pytest.mark.asyncio
async def test_request_body_is_constructed_correctly(client, server, stop_loss_order):
    await client.initialize()
    result = create_body(client, POSTOrders.request_schema,
                         {OrderRequest: stop_loss_order, 'test': Account(), 'arg': 'random_string'})

    correct = {'order': {'instrument':'AUD_USD','tradeID': '1234', 'price': '0.8', 'type': 'STOP_LOSS', 'timeInForce': 'GTC',
                         'triggerCondition': 'DEFAULT'}}


    assert result == correct


@pytest.mark.asyncio
async def test_request_body_does_not_format_order_request_with_no_instrument_parameter(client, server, stop_loss_order):
    await client.initialize()
    client.format_order_requests = True
    create_body(client, POSTOrders.request_schema,
                {OrderRequest: stop_loss_order, 'test': Account(), 'arg': 'random_string'})


@pytest.mark.asyncio
async def test_request_body_raises_error_when_cannot_format_order_request(client, server):
    await client.initialize()
    client.format_order_requests = True
    with pytest.raises(InvalidOrderRequest):
        create_body(client, POSTOrders.request_schema,
                    {OrderRequest: MarketOrderRequest(instrument='NOT AN INSTRUMENT', units=1)})

@pytest.mark.asyncio
async def test_request_body_formats_order_request_when_an_order_request_is_passed(client, server):
    await client.initialize()
    client.format_order_requests = True
    with pytest.raises(InvalidOrderRequest):
        create_body(client, POSTOrders.request_schema,
                    {OrderRequest: MarketOrderRequest(instrument='NOT AN INSTRUMENT', units=1)})

@pytest.mark.asyncio
async def test_request_body_does_not_raise_error_when_an_invalid_order_request_is_passed(client, server):
    await client.initialize()
    client.format_order_requests = True
    body = create_body(client, POSTOrders.request_schema,
                       {OrderRequest: OrderRequest(instrument='AUD_USD', units=0)})
    assert body['order']['units'] == '1.0'

@pytest.mark.asyncio
async def test_objects_can_be_converted_between_Model_object_and_json():
    account = Account(**GETAccountID_response['account'])
    response_json_account = GETAccountID_response['account']
    account_to_json = account.dict(json=True, datetime_format='RFC3339')

    response_json_account = order_dict(response_json_account)
    account_to_json = order_dict(account_to_json)




    assert response_json_account == account_to_json


@pytest.mark.parametrize('instrument', ArrayInstrument(*json.loads(example_instruments)))
def test_format_order_requests_updates_units(instrument):
    order_request = OrderRequest(instrument='AUD_JPY', units=0.123456)


    result = _format_order_request(order_request, instrument, clip=True)
    assert result.units >= instrument.minimum_trade_size


@pytest.mark.parametrize('instrument', ArrayInstrument(*json.loads(example_instruments)))
def test_format_order_requests_raises_error_when_units_less_than_minimum(instrument):
    order_request = OrderRequest(instrument='XPT_USD', units=0.123456)
    with pytest.raises(InvalidOrderRequest):
        _format_order_request(order_request, instrument)


@pytest.mark.parametrize('instrument', ArrayInstrument(*json.loads(example_instruments)))
def test_format_order_requests_applies_correct_precision_to_units(instrument):
    order_request = OrderRequest(instrument=instrument.name, units=50.1234567891234)
    result = _format_order_request(order_request, instrument)


    if instrument.trade_units_precision == 0:
        assert re.findall(r'(?<=\.)\d+', str(result.units))[0] == '0'
    else:
        assert len(re.findall(r'(?<=\.)\d+', str(result.units))[0]) == instrument.trade_units_precision

    order_request = OrderRequest(instrument=instrument.name, units=0.1234567891234)
    result = _format_order_request(order_request, instrument, clip=True)


    if instrument.trade_units_precision == 0:
        assert re.findall(r'(?<=\.)\d+', str(result.units))[0] == '0'
    else:
        assert len(re.findall(r'(?<=\.)\d+', str(result.units))[0]) == instrument.trade_units_precision


@pytest.mark.parametrize('instrument', ArrayInstrument(*json.loads(example_instruments)))
def test_format_order_requests_applies_correct_precision_to_price_price_bound_distance(instrument):
    order_request = OrderRequest(instrument='AUD_USD', price=50.1234567891234, price_bound=1234.123456789,
                                 distance=20.123456789)
    result = _format_order_request(order_request, instrument)
    for attr in (result.price, result.price_bound, result.distance):
        if instrument.display_precision == 0:
            assert re.findall(r'(?<=\.)\d+', str(attr))[0] == '0'
        else:
            assert len(re.findall(r'(?<=\.)\d+', str(attr))[0]) == instrument.display_precision


@pytest.mark.parametrize('instrument', ArrayInstrument(*json.loads(example_instruments)))
def test_format_order_requests_applies_correct_precision_to_take_profit_on_fill_stop_loss_on_fill(instrument):
    order_request = OrderRequest(instrument=instrument.name, take_profit_on_fill=50.123456789,
                                 stop_loss_on_fill=50.123456789)
    result = _format_order_request(order_request, instrument)
    for attr in (result.stop_loss_on_fill.price, result.take_profit_on_fill):
        if instrument.display_precision == 0:
            assert re.findall(r'(?<=\.)\d+', str(attr))[0] == '0'
        else:
            assert len(re.findall(r'(?<=\.)\d+', str(attr))[0]) == instrument.display_precision


@pytest.mark.parametrize('instrument', ArrayInstrument(*json.loads(example_instruments)))
def test_format_order_requests_applies_correct_precision_to_trailing_stop_loss_on_fill(instrument):
    order_request = OrderRequest(
        instrument=instrument.name,
        trailing_stop_loss_on_fill=instrument.minimum_trailing_stop_distance + 0.123456789
    )
    result = _format_order_request(order_request, instrument)
    attr = result.trailing_stop_loss_on_fill.distance
    if instrument.display_precision == 0:
        assert re.findall(r'(?<=\.)\d+', str(attr))[0] == '0'
    else:
        assert len(re.findall(r'(?<=\.)\d+', str(attr))[0]) == instrument.display_precision


@pytest.mark.parametrize('instrument', ArrayInstrument(*json.loads(example_instruments)))
def test_format_order_requests_limits_trailing_stop_loss_on_fill_to_valid_range(instrument):
    order_request = OrderRequest(
        instrument=instrument.name,
        trailing_stop_loss_on_fill=0
    )
    if instrument.minimum_trailing_stop_distance > 0:
        with pytest.raises(InvalidOrderRequest):
            _format_order_request(order_request, instrument)

    result = _format_order_request(order_request, instrument, clip=True)
    assert result.trailing_stop_loss_on_fill.distance == instrument.minimum_trailing_stop_distance

    order_request = OrderRequest(
        instrument=instrument.name,
        trailing_stop_loss_on_fill=instrument.maximum_trailing_stop_distance + 10
    )

    with pytest.raises(InvalidOrderRequest):
        _format_order_request(order_request, instrument)

    result = _format_order_request(order_request, instrument, clip=True)
    assert result.trailing_stop_loss_on_fill.distance == instrument.maximum_trailing_stop_distance


@pytest.mark.parametrize('instrument', ArrayInstrument(*json.loads(example_instruments)))
def test_format_order_requests_limits_units_to_valid_range(instrument):
    order_request = OrderRequest(
        instrument=instrument.name,
        units=0
    )

    if instrument.minimum_trade_size > 0:
        with pytest.raises(InvalidOrderRequest):
            _format_order_request(order_request, instrument)

    result = _format_order_request(order_request, instrument, clip=True)

    assert result.units == instrument.minimum_trade_size

    order_request = OrderRequest(
        instrument=instrument.name,
        units=instrument.maximum_order_units + 10
    )

    with pytest.raises(InvalidOrderRequest):
        _format_order_request(order_request, instrument)

    result = _format_order_request(order_request, instrument, clip=True)
    assert result.units == instrument.maximum_order_units


@pytest.mark.parametrize('instrument', ArrayInstrument(*json.loads(example_instruments)))
def test_format_order_requests_accepts_negative_values_for_units(instrument):
    order_request = OrderRequest(
        instrument=instrument.name,
        units=-instrument.minimum_trade_size
    )

    result = _format_order_request(order_request, instrument, clip=False)

    assert result.units == -instrument.minimum_trade_size

    result = _format_order_request(order_request, instrument, clip=True)

    assert result.units == -instrument.minimum_trade_size


@pytest.mark.parametrize('instrument', ArrayInstrument(*json.loads(example_instruments)))
def test_ins_context_does_not_add_parameters_to_order_requests(instrument):
    order_request = OrderRequest(
        instrument=instrument.name,
        units=instrument.minimum_trade_size
    )
    result = _format_order_request(order_request, instrument, clip=True)
    assert not hasattr(result, 'price_bound')
    assert not hasattr(result, 'trailing_stop_loss_on_fill')
    assert not hasattr(result, 'stop_loss_on_fill')
    assert not hasattr(result, 'take_profit_on_fill')


def test_too_many_passed_transactions(client):

    client.default_parameters[SinceTransactionID] = 0
    client.default_parameters[LastTransactionID] = 0
    assert not too_many_passed_transactions(client)

    client.default_parameters[SinceTransactionID] = 0
    client.default_parameters[LastTransactionID] = 901
    assert too_many_passed_transactions(client)