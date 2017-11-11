import pytest

from async_v20.definitions import types
from async_v20.definitions.base import Model
from async_v20.definitions.base import create_attribute
from tests.test_definitions.helpers import get_valid_primitive_data, create_cls_annotations

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
    result = cls(**result.json_dict())
    assert result
    assert type(result) == cls


@pytest.mark.parametrize('cls, data', model_classes_data)
def test_all_types_instantiated_from_dict_with_incorrect_argument_raises_error(cls, data):
    arguments = data.copy()
    arguments.update(this_argument_doesnt_exist='TEST_VALUE')
    with pytest.raises(ValueError):
        cls(**arguments)


@pytest.mark.parametrize('cls, data', model_classes_data)
def test_all_types_can_be_instantiated_from_tuple(cls, data):
    arguments = tuple(data.values())
    # make sure the arguments are in the correct order
    result = cls(*arguments)
    result_json = result.json()
    assert result
    assert type(result) == cls

    for index, argument in enumerate(arguments):
        if isinstance(argument, dict):
            args = list(arguments)
            args[index] = tuple(argument.values())
            assert cls(*args).json() == result_json


@pytest.mark.parametrize('cls, data', model_classes_data)
def test_all_types_can_be_instantiated_from_annotation(cls, data):
    arguments = {k: create_attribute(create_cls_annotations(cls)[k], v)
                 for k, v in data.items()}
    print(arguments)
    assert cls(**arguments)
