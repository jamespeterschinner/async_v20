from inspect import isclass

import pytest
from async_v20.definitions import descriptors
from hypothesis.strategies import text, integers, floats, sampled_from



# Get All user defined class' in descriptor package
@pytest.mark.parametrize('descriptor', map(lambda x: getattr(descriptors,x), descriptors.__all__))
def test_all_incorrect_descriptor_values_cannot_be_assigned(descriptor):
    if isclass(descriptor):
        if getattr(descriptor, 'values', None):
            for key in descriptor.values.keys():
                with pytest.raises(ValueError):
                    descriptor(key + '_test')


# Get All user defined class' in descriptor package
@pytest.mark.parametrize('descriptor', map(lambda x: getattr(descriptors,x), descriptors.__all__))
def test_descriptor_values_have_length_checking(descriptor):
    if isclass(descriptor):
        if getattr(descriptor, 'values', None):
            for key in descriptor.values.keys():
                with pytest.raises(ValueError):
                    descriptor(key + '_test')


# Get All user defined class' in descriptor package
@pytest.mark.parametrize('descriptor', map(lambda x: getattr(descriptors,x), descriptors.__all__))
def test_descriptors_enforce_length_checking(descriptor):
    if isclass(descriptor):
        if getattr(descriptor, 'example', None):
            with pytest.raises(ValueError):
                descriptor(descriptor.example + '_')


# # Get All user defined class' in descriptor package
# @pytest.mark.parametrize('descriptor', map(lambda x: getattr(descriptors,x), descriptors.__all__))
# def test_descriptors_convert_type_to_float(descriptor):
#     if isclass(descriptor) and descriptor.typ == float:
#         # Create a dummy class to assign attributes to
#         class TestClass(object):
#             attr = descriptor(name='_attr')
#
#         test_class = TestClass()
#         # Test that when a str is passed to a descriptor that requires a float the descriptor will convert it to a float
#         test_class.attr = '0.1234'
#         assert type(test_class.attr) == float
#

@pytest.mark.parametrize('descriptor', map(lambda x: getattr(descriptors,x), descriptors.__all__))
def test_descriptors_return_correct_type_when_initialized_with_value(descriptor):
    data = None
    try:
        data = descriptor.example
    except AttributeError:
        try:
            data = next(iter(descriptor.values))
        except AttributeError:
            if float in descriptor.__bases__:
                data = '14.0'
            elif int in descriptor.__bases__:
                data = '12345567'
            else:
                data = 'TEST_DATA'
    assert type(descriptor(data)) == descriptor

def test_PriceValue_rounds_floats_to_the_correct_accuracy():
    assert descriptors.PriceValue(0.123456) == 0.12346

def test_Unit_rounds_floats_to_the_correct_accuracy():
    assert descriptors.Unit(0.6) == 1

# def test_delattr():
#     class TestClass(object):
#         attribute = descriptors.Unit(name='_' + 'attribute')
#
#     test_class = TestClass()
#     test_class.attribute = 0.6
#     assert hasattr(test_class, '_attribute')
#     del test_class._attribute
#     assert not hasattr(test_class, '_attribute')