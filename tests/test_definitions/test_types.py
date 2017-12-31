import pytest

from async_v20.definitions import types
from async_v20.definitions.base import Model
from async_v20.definitions.base import create_attribute
from tests.test_definitions.helpers import get_valid_primitive_data, create_cls_annotations
from async_v20.exceptions import UnknownValue

model_classes = (cls for cls in (getattr(types, typ) for typ in types.__all__) if
                 issubclass(cls, Model))

model_classes_data = [(cls, get_valid_primitive_data(cls)) for cls in model_classes]


@pytest.mark.parametrize('cls, data', model_classes_data)
def test_class_annotations_match_the_parents_class_annotations(cls, data):
    if not cls.__bases__[0] == Model:
        print(cls.__bases__[0].__new__.__annotations__)
        print(cls.__new__.__annotations__)

        for annotation in cls.__new__.__annotations__:
            assert annotation in cls.__bases__[0].__new__.__annotations__


@pytest.mark.parametrize('cls, data', model_classes_data)
def test_all_types_can_be_instantiated_from_dict(cls, data):
    arguments = data
    result = cls(**arguments)
    assert result
    assert type(result) == cls
    # Test class instance can be used to create another instance of the same class
    result = cls(**result.dict())
    assert result
    assert type(result) == cls


@pytest.mark.parametrize('cls, data', model_classes_data)
def test_all_types_instantiated_from_dict_with_incorrect_argument_raises_error(cls, data):
    arguments = data.copy()
    arguments.update(this_argument_doesnt_exist='TEST_VALUE')
    with pytest.raises(UnknownValue):
        cls(**arguments)


@pytest.mark.parametrize('cls, data', model_classes_data)
def test_all_types_can_be_instantiated_from_tuple(cls, data):
    arguments = tuple(data.values())
    # make sure the arguments are in the correct order
    result = cls(*arguments)
    result_json = result.json(datetime_format='UNIX')
    assert result
    assert type(result) == cls

    for index, argument in enumerate(arguments):
        if isinstance(argument, dict):
            args = list(arguments)
            args[index] = tuple(argument.values())
            assert cls(*args).json(datetime_format='UNIX') == result_json


@pytest.mark.parametrize('cls, data', model_classes_data)
def test_all_types_can_be_instantiated_from_annotation(cls, data):
    arguments = {k: create_attribute(create_cls_annotations(cls)[k], v)
                 for k, v in data.items()}
    print(arguments)
    assert cls(**arguments)

@pytest.mark.parametrize('cls, data', model_classes_data)
def test_all_derived_types_have_same_arguments_and_annotations_as_parent(cls, data):
    parent_class = cls.__bases__[0]
    if not parent_class == Model:
        parent_class_parameters = parent_class.__new__.__signature__.parameters
        for name, parameter in cls.__new__.__signature__.parameters.items():
            assert name in parent_class_parameters
            try:
                assert issubclass(parameter.annotation,parent_class_parameters[name].annotation)
            except TypeError:
                # means annotation is async_v20.definitions.helpers.time function
                assert parameter.annotation == parent_class_parameters[name].annotation
