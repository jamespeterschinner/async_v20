from inspect import isclass

import pytest
from async_v20.definitions import descriptors
from async_v20.definitions.descriptors.base import IncorrectValue, LengthError
from hypothesis.strategies import text, integers, floats, sampled_from

# Get All user defined class' in descriptor package
@pytest.mark.parametrize('descriptor', map(lambda x: getattr(descriptors,x), descriptors.__all__))
def test_all_correct_descriptor_values_can_be_assigned(descriptor):
    if isclass(descriptor):
        # Create a dummy class to assign attributes to
        class TestClass(object):
            attr = descriptor(name='_attr')

        test_class = TestClass()
        # Test that every key in values can be assigned
        if descriptor.values:
            for key in descriptor.values.keys():
                test_class.attr = key

                assert test_class.attr == key


# Get All user defined class' in descriptor package
@pytest.mark.parametrize('descriptor', map(lambda x: getattr(descriptors,x), descriptors.__all__))
def test_all_incorrect_descriptor_values_cannot_be_assigned(descriptor):
    if isclass(descriptor):
        # Create a dummy class to assign attributes to
        class TestClass(object):
            attr = descriptor(name='_attr')

        test_class = TestClass()
        # Test that every key in values can be assigned
        if descriptor.values:
            for key in descriptor.values.keys():
                with pytest.raises(IncorrectValue):
                    test_class.attr = (key + '_test')


# Get All user defined class' in descriptor package
@pytest.mark.parametrize('descriptor', map(lambda x: getattr(descriptors,x), descriptors.__all__))
def test_descriptor_values_have_length_checking(descriptor):
    if isclass(descriptor):
        # Create a dummy class to assign attributes to
        class TestClass(object):
            attr = descriptor(name='_attr')

        test_class = TestClass()
        # Test that every key in values can be assigned
        if descriptor.values:
            for key in descriptor.values.keys():
                with pytest.raises(IncorrectValue):
                    test_class.attr = (key + '_test')


# Get All user defined class' in descriptor package
@pytest.mark.parametrize('descriptor', map(lambda x: getattr(descriptors,x), descriptors.__all__))
def test_descriptors_enforce_length_checking(descriptor):
    if isclass(descriptor):
        # Create a dummy class to assign attributes to
        class TestClass(object):
            attr = descriptor(name='_attr')

        test_class = TestClass()
        # Test that every key in values can be assigned
        if descriptor.example:
            with pytest.raises(LengthError):
                test_class.attr = (descriptor.example + '_')


# Get All user defined class' in descriptor package
@pytest.mark.parametrize('descriptor', map(lambda x: getattr(descriptors,x), descriptors.__all__))
def test_descriptors_convert_type_to_float(descriptor):
    if isclass(descriptor) and descriptor.typ == float:
        # Create a dummy class to assign attributes to
        class TestClass(object):
            attr = descriptor(name='_attr')

        test_class = TestClass()
        # Test that when a str is passed to a descriptor that requires a float the descriptor will convert it to a float
        test_class.attr = '0.1234'
        assert type(test_class.attr) == float


data_gen = {str: sampled_from([text(), integers(), floats()]), int: sampled_from(['1','-1',3.5]), float: integers()}

@pytest.mark.parametrize('descriptor', map(lambda x: getattr(descriptors,x), descriptors.__all__))
def test_descriptors_return_correct_type_when_initialized_with_value(descriptor):
    typ = descriptor.typ
    gen = data_gen[typ]
    assert all(map(lambda x: type(x) == typ, (descriptor(gen.example()) for _ in range(50))))

def test_PriceValue_rounds_floats_to_the_correct_accuracy():
    class TestClass(object):
        attribute = descriptors.PriceValue(name='_' + 'attribute')

    test_class = TestClass()
    test_class.attribute = 0.123456
    assert test_class.attribute == 0.12346

def test_Unit_rounds_floats_to_the_correct_accuracy():
    class TestClass(object):
        attribute = descriptors.Unit(name='_' + 'attribute')

    test_class = TestClass()
    test_class.attribute = 0.6
    assert test_class.attribute == 1
