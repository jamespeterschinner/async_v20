from async_v20.definitions.helpers import flatten_dict
from async_v20.definitions.primitives import AccountID, TradeID
from async_v20.endpoints.annotations import Smooth
from .helpers import get_valid_primitive_data
from async_v20.definitions.base import Array

nested_dict = {'a': {'b': 2, 'c': {'d': 4}}}
flattened_dict = {'a_b': 2, 'a_c_d': 4}


def test_flatten_dict():
    result = flatten_dict(nested_dict, delimiter='_')
    assert result == flattened_dict


def test_get_valid_primitive_data_returns_primitive_example():
    assert AccountID.example == get_valid_primitive_data(AccountID)

def test_get_valid_primitive_data_returns_int():
    assert type(get_valid_primitive_data(TradeID)) == int

def test_get_valid_primitive_data_returns_bool():
    assert type(get_valid_primitive_data(Smooth)) == bool

def test_get_valid_primitive_data_returns_Array_example():
    class TestArray(Array):
        _contains = AccountID

    assert (AccountID.example,) == get_valid_primitive_data(TestArray)
