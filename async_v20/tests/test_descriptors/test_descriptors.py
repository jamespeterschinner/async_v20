from inspect import isclass

import pytest
from async_v20.definitions import descriptors
from async_v20.definitions.descriptors.base import IncorrectValue, LengthError


# Get All user defined class' in descriptor package
@pytest.mark.parametrize('descriptor', filter(lambda x: '__' not in x, dir(descriptors)))
def test_all_correct_descriptor_values_can_be_assigned(descriptor):
    # get the module attribute
    descriptor = getattr(descriptors, descriptor)
    if isclass(descriptor):
        # Create a dummy class to assign attributes to
        class TestClass(object):
            attr = descriptor()

        test_class = TestClass()
        # Test that every key in values can be assigned
        key = None
        if descriptor.values:
            for key in descriptor.values.keys():
                test_class.attr = key

            assert test_class.attr == key


# Get All user defined class' in descriptor package
@pytest.mark.parametrize('descriptor', filter(lambda x: '__' not in x, dir(descriptors)))
def test_all_incorrect_descriptor_values_cannot_be_assigned(descriptor):
    # get the module attribute
    descriptor = getattr(descriptors, descriptor)
    if isclass(descriptor):
        # Create a dummy class to assign attributes to
        class TestClass(object):
            attr = descriptor()

        test_class = TestClass()
        # Test that every key in values can be assigned
        if descriptor.values:
            for key in descriptor.values.keys():
                with pytest.raises(IncorrectValue):
                    test_class.attr = (key + '_test')


# Get All user defined class' in descriptor package
@pytest.mark.parametrize('descriptor', filter(lambda x: '__' not in x, dir(descriptors)))
def test_descriptor_values_have_length_checking(descriptor):
    # get the module attribute
    descriptor = getattr(descriptors, descriptor)
    if isclass(descriptor):
        # Create a dummy class to assign attributes to
        class TestClass(object):
            attr = descriptor()

        test_class = TestClass()
        # Test that every key in values can be assigned
        if descriptor.values:
            for key in descriptor.values.keys():
                with pytest.raises(IncorrectValue):
                    test_class.attr = (key + '_test')


# Get All user defined class' in descriptor package
@pytest.mark.parametrize('descriptor', filter(lambda x: '__' not in x, dir(descriptors)))
def test_descriptors_enforce_length_checking(descriptor):
    # get the module attribute
    descriptor = getattr(descriptors, descriptor)
    if isclass(descriptor):
        # Create a dummy class to assign attributes to
        class TestClass(object):
            attr = descriptor()

        test_class = TestClass()
        # Test that every key in values can be assigned
        if descriptor.example:
            with pytest.raises(LengthError):
                test_class.attr = (descriptor.example + '_')


# Get All user defined class' in descriptor package
@pytest.mark.parametrize('descriptor', filter(lambda x: '__' not in x, dir(descriptors)))
def test_descriptors_convert_type_to_float(descriptor):
    # get the module attribute
    descriptor = getattr(descriptors, descriptor)
    if isclass(descriptor) and descriptor.typ == float:
        # Create a dummy class to assign attributes to
        class TestClass(object):
            attr = descriptor()

        test_class = TestClass()
        # Test that when a str is passed to a descriptor that requires a float the descriptor will convert it to a float
        test_class.attr = '0.1234'
        assert type(test_class.attr) == float
