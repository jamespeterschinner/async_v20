from pandas import Timestamp

from async_v20.definitions.base import Array
from async_v20.definitions.helpers import flatten_dict
from async_v20.definitions.primitives import AccountID, TradeID
from async_v20.endpoints.annotations import Smooth, Count
from .helpers import get_valid_primitive_data

nested_dict = {'a': {'b': 2, 'c': {'d': 4}}}
flattened_dict = {'a_b': 2, 'a_c_d': 4}


def test_flatten_dict():
    result = flatten_dict(nested_dict, delimiter='_')
    assert result == flattened_dict


# def test_time_to_time_stamp_is_RFC3339_UNIX_agnostic():
#     assert time_to_time_stamp('2017-11-19T23:47:30.000000003Z') == time_to_time_stamp('1511135250.000000003')
#
#
# def test_unix_to_datetime64():
#     assert type(time_to_time_stamp('1510937865.000000000')) == \
#            Timestamp
#
#
# def test_rfc3339_to_datetime64():
#     assert type(time_to_time_stamp('2017-11-18T03:57:45.000000000')) == \
#            Timestamp


def test_get_valid_primitive_data_returns_primitive_example():
    assert AccountID.example == get_valid_primitive_data(AccountID)


def test_get_valid_primitive_data_returns_int():
    assert type(get_valid_primitive_data(TradeID)) == int


def test_get_valid_primitive_data_returns_bool():
    assert type(get_valid_primitive_data(Smooth)) == bool


def test_get_valid_primitive_data_returns_default_value():
    assert get_valid_primitive_data(Count) == 500


def test_get_valid_primitive_data_returns_Array_example():
    class TestArray(Array):
        _contains = AccountID

    assert (AccountID.example,) == get_valid_primitive_data(TestArray)
