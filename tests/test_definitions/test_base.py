import pytest
from async_v20.definitions.base import Model, Array, create_attribute
from async_v20.definitions.types import Account, ArrayStr
from async_v20.definitions.helpers import flatten_dict
from async_v20.definitions.primitives import TradeID, AccountID

from ..data.json_data import GETAccountID_response

import ujson as json


@pytest.fixture
def account():
    result = Account(**GETAccountID_response['account'])
    yield result
    del result


def test_account_has_correct_methods(account):
    assert hasattr(account, 'json_dict')
    assert hasattr(account, 'data')
    assert hasattr(account, 'series')


@pytest.fixture
def test_kwargs():
    kwargs = {'type': 'LIST', 'value': 'TEST_VALUE'}
    yield kwargs
    del kwargs


@pytest.fixture
def test_class():
    class TestClass(Model):
        _dispatch = {'type': 'LIST'}

    test_cls = TestClass
    yield test_cls
    del test_cls


def test_base_dispatch_works_correctly():
    pass


def test_json_dict_returns_correct_data_structure(account):
    """Test the result is formatted correctly. There is a requirement for
    json_dict to be able to cast floats to strings, this is necessary when
    serializing objects to send to OANDA. Though when used internally is it more
    natural to leave floats as floats."""

    result = account.json_dict(float_to_string=True)
    # Test result is a dict
    assert type(result) == dict
    flattened_result = flatten_dict(result)
    # Test that all values have the correct data type
    for value in flattened_result:
        assert isinstance(value, (dict, str, int, list))

    result = account.json_dict(float_to_string=False)
    assert type(result) == dict
    flattened_result = flatten_dict(result)
    # Test that all values have the correct data type. Specifically that
    # all floats have not been casted to a string.
    for value in flattened_result:
        assert isinstance(value, (dict, float, str, int, list))
        if isinstance(value, str):
            with pytest.raises(ValueError):
                float(value)

def test_json_data(account):
    result = account.json()
    assert type(result) == str
    assert json.loads(result) == account.json_dict(float_to_string=True)

def test_data(account):
    result = account.data(float_to_string=True)
    for value in result:
        assert isinstance(value, (str, int, list))

    result = account.data(float_to_string=False)
    for value in result:
        print(value)
        assert isinstance(value, (float, str, int, list))
        if isinstance(value, str):
            with pytest.raises(ValueError):
                float(value)

def test_series(account):
    result = account.series()
    print(result)

    for value in result:
        assert isinstance(value, (float, str, int, list, type(None)))
        if isinstance(value, str):
            print(value)
            with pytest.raises(ValueError):
                float(value)

def test_array_returns_type_error():
    class ArrayTest(Array):
        _contains = int

    with pytest.raises(ValueError):
        ArrayTest('ABC', 'DEF')

def test_create_attribute_returns_type_error():
    with pytest.raises(TypeError):
        create_attribute(AccountID, TradeID(123))

    with pytest.raises(TypeError):
        create_attribute(ArrayStr, TradeID(123))