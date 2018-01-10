from inspect import isclass

import pytest

from async_v20.definitions import primitives
from async_v20.definitions.primitives import ClientComment, ClientID, ClientTag, OrderID, TradeID
from async_v20.definitions.primitives import OrderSpecifier, TradeSpecifier, DateTime
from async_v20.definitions.primitives import TransactionID, PriceValue, DecimalNumber
from tests.test_definitions.helpers import get_valid_primitive_data
from async_v20.exceptions import InvalidValue, InvalidFormatArguments
from time import time
from datetime import datetime
import logging
logger = logging.getLogger()
logger.disabled = True

import pandas as pd

def test_date_time_can_be_created_from_time_and_datetime():
    assert DateTime(time())
    assert DateTime(datetime.now())

def test_date_time_can_be_created_from_integer():
    t = time()
    assert DateTime(t).second == DateTime(int(t)).second
    assert DateTime(t).second == DateTime(str(t).replace('.', '')).second

def test_datetime_converts_between_different_representations():
    unix_example = '1502463871.639182000'
    rfc3339_example = '2017-08-11T15:04:31.639182000Z'
    assert DateTime(unix_example) == DateTime(rfc3339_example)
    assert DateTime(rfc3339_example).json('UNIX') == unix_example
    assert DateTime(DateTime(rfc3339_example).json('UNIX')) == DateTime(rfc3339_example)
    assert DateTime(unix_example).json('RFC3339') == rfc3339_example


def test_datetime_format_only_allows_valid_format_string():
    unix_example = '1502463871.639182000'
    with pytest.raises(InvalidValue):
        assert DateTime(unix_example).json(datetime_format='BADVALUE')

@pytest.mark.parametrize('primitive', map(lambda x: getattr(primitives, x), primitives.__all__))
def test_get_valid_primitive_data(primitive):
    """Test the helper function can provide valid data for all primitives"""
    assert get_valid_primitive_data(primitive)


# Get All user defined class' in primitive package
@pytest.mark.parametrize('primitive', map(lambda x: getattr(primitives, x), primitives.__all__))
def test_all_incorrect_primitive_values_cannot_be_assigned(primitive):
    if isclass(primitive):
        if getattr(primitive, 'values', None):
            for key in primitive.values.keys():
                with pytest.raises(InvalidValue):
                    primitive(key + '_test')


# Get All user defined class' in primitive package
@pytest.mark.parametrize('primitive', map(lambda x: getattr(primitives, x), primitives.__all__))
def test_primitive_values_have_length_checking(primitive):
    if isclass(primitive):
        if getattr(primitive, 'values', None):
            for key in primitive.values.keys():
                with pytest.raises(InvalidValue):
                    primitive(key + '_test')


# Get All user defined class' in primitive package
@pytest.mark.parametrize('primitive', map(lambda x: getattr(primitives, x), primitives.__all__))
def test_primitives_enforce_length_checking(primitive):
    if isclass(primitive):
        if getattr(primitive, 'example', None) and primitive not in \
                (OrderSpecifier, ClientComment, ClientID, ClientTag, TransactionID, TradeSpecifier,
                # These are integers and this wouldn't make sense
                 OrderID, TradeID):
            with pytest.raises(InvalidValue):
                primitive(primitive.example + '_')


@pytest.mark.parametrize('primitive', map(lambda x: getattr(primitives, x), primitives.__all__))
def test_primitives_return_correct_type_when_initialized_with_value(primitive):
    if primitive == DateTime:
        assert type(primitive(get_valid_primitive_data(primitive))) == pd.Timestamp
    else:
        assert type(primitive(get_valid_primitive_data(primitive))) == primitive


def test_price_value_cannot_be_created_from_negative_value():
    with pytest.raises(InvalidValue):
        PriceValue(-1)


def test_price_value_format():
    price_value = PriceValue(1234.123456789)

    # Test precision rounding
    assert price_value.format(4) == 1234.1235
    # Check returned value is a float
    assert type(price_value.format(0)) == PriceValue
    # test min limit
    assert price_value.format(5, 2000) == 2000
    # test max limit
    assert price_value.format(3, 0, 100) == 100

    with pytest.raises(InvalidFormatArguments):
        # Min must be greater than max
        price_value.format(4, 300, 150)

    # min_ and max_ can be the same value
    assert price_value.format(4, 100, 100) == 100

    # Precision must be positive
    with pytest.raises(InvalidFormatArguments):
        price_value.format(-1)

def test_decimal_number_format():
    decimal_number = DecimalNumber(1234.123456789)

    # Test precision rounding
    assert decimal_number.format(4) == 1234.1235
    # Check returned value is a float
    assert type(decimal_number.format(0)) == DecimalNumber
    # test min limit
    assert decimal_number.format(5, 2000) == 2000
    # test max limit
    assert decimal_number.format(3, 0, 100) == 100

    with pytest.raises(InvalidFormatArguments):
        # Min must be greater than max
        decimal_number.format(4, 300, 150)

    # min_ and max_ can be the same value
    assert decimal_number.format(4, 100, 100) == 100

    # Precision must be positive
    with pytest.raises(InvalidFormatArguments):
        decimal_number.format(-1)

    # TEST THE SAME WORKS FOR NEGATIVE NUMBERS
    decimal_number = DecimalNumber(-1234.123456789)
    # Test precision rounding
    assert decimal_number.format(4) == -1234.1235
    # Check returned value is a float
    assert type(decimal_number.format(0)) == DecimalNumber
    # test min limit
    assert decimal_number.format(5, 2000) == -2000
    # test max limit
    assert decimal_number.format(3, 0, 100) == -100

    with pytest.raises(InvalidFormatArguments):
        # Min must be greater than max
        decimal_number.format(4, 300, 150)

    # min_ and max_ can be the same value
    assert decimal_number.format(4, 100, 100) == -100


