from inspect import isclass
from .helpers import get_valid_primitive_data
import pytest
from async_v20.definitions import primitives



# Get All user defined class' in primitive package
@pytest.mark.parametrize('primitive', map(lambda x: getattr(primitives,x), primitives.__all__))
def test_all_incorrect_primitive_values_cannot_be_assigned(primitive):
    if isclass(primitive):
        if getattr(primitive, 'values', None):
            for key in primitive.values.keys():
                with pytest.raises(ValueError):
                    primitive(key + '_test')


# Get All user defined class' in primitive package
@pytest.mark.parametrize('primitive', map(lambda x: getattr(primitives,x), primitives.__all__))
def test_primitive_values_have_length_checking(primitive):
    if isclass(primitive):
        if getattr(primitive, 'values', None):
            for key in primitive.values.keys():
                with pytest.raises(ValueError):
                    primitive(key + '_test')


# Get All user defined class' in primitive package
@pytest.mark.parametrize('primitive', map(lambda x: getattr(primitives,x), primitives.__all__))
def test_primitives_enforce_length_checking(primitive):
    if isclass(primitive):
        if getattr(primitive, 'example', None):
            with pytest.raises(ValueError):
                primitive(primitive.example + '_')


@pytest.mark.parametrize('primitive', map(lambda x: getattr(primitives,x), primitives.__all__))
def test_primitives_return_correct_type_when_initialized_with_value(primitive):
    data = get_valid_primitive_data(primitive)
    assert type(primitive(data)) == primitive

def test_PriceValue_rounds_floats_to_the_correct_accuracy():
    assert primitives.PriceValue(0.123456) == 0.12346

def test_Unit_rounds_floats_to_the_correct_accuracy():
    assert primitives.Unit(0.6) == 1
