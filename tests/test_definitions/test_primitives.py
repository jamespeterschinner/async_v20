from inspect import isclass

import pytest

from async_v20.definitions import primitives
from async_v20.definitions.primitives import ClientComment, ClientID, ClientTag
from async_v20.definitions.primitives import OrderSpecifier, TradeSpecifier
from async_v20.definitions.primitives import TransactionID, PriceValue, DecimalNumber
from tests.test_definitions.helpers import get_valid_primitive_data


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
                with pytest.raises(ValueError):
                    primitive(key + '_test')


# Get All user defined class' in primitive package
@pytest.mark.parametrize('primitive', map(lambda x: getattr(primitives, x), primitives.__all__))
def test_primitive_values_have_length_checking(primitive):
    if isclass(primitive):
        if getattr(primitive, 'values', None):
            for key in primitive.values.keys():
                with pytest.raises(ValueError):
                    primitive(key + '_test')


# Get All user defined class' in primitive package
@pytest.mark.parametrize('primitive', map(lambda x: getattr(primitives, x), primitives.__all__))
def test_primitives_enforce_length_checking(primitive):
    if isclass(primitive):
        if getattr(primitive, 'example', None) and primitive not in \
                (OrderSpecifier, ClientComment, ClientID, ClientTag, TransactionID, TradeSpecifier):
            with pytest.raises(ValueError):
                primitive(primitive.example + '_')


@pytest.mark.parametrize('primitive', map(lambda x: getattr(primitives, x), primitives.__all__))
def test_primitives_return_correct_type_when_initialized_with_value(primitive):
    assert type(primitive(get_valid_primitive_data(primitive))) == primitive


def test_price_value_cannot_be_created_from_negative_value():
    with pytest.raises(ValueError):
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

    with pytest.raises(ValueError):
        # Min must be greater than max
        price_value.format(4, 300, 150)

    # min_ and max_ can be the same value
    assert price_value.format(4, 100, 100) == 100

    # Precision must be positive
    with pytest.raises(ValueError):
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

    with pytest.raises(ValueError):
        # Min must be greater than max
        decimal_number.format(4, 300, 150)

    # min_ and max_ can be the same value
    assert decimal_number.format(4, 100, 100) == 100

    # Precision must be positive
    with pytest.raises(ValueError):
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

    with pytest.raises(ValueError):
        # Min must be greater than max
        decimal_number.format(4, 300, 150)

    # min_ and max_ can be the same value
    assert decimal_number.format(4, 100, 100) == -100


