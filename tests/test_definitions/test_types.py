import pytest

from async_v20.definitions import types
from async_v20.definitions.base import Model
from async_v20.definitions.base import create_attribute
from tests.test_definitions.helpers import get_valid_primitive_data, create_cls_annotations

model_classes = [cls for cls in (getattr(types, typ) for typ in types.__all__) if
                 issubclass(cls, Model)]


@pytest.mark.parametrize('cls', model_classes)
def test_class_annotations_match_the_parents_class_annotations(cls):
    if not cls.__bases__[0] == Model:
        print(cls.__bases__[0].__new__.__annotations__)
        print(cls.__new__.__annotations__)

        for annotation in cls.__new__.__annotations__:
            assert annotation in cls.__bases__[0].__new__.__annotations__


@pytest.mark.parametrize('cls', model_classes)
def test_all_types_can_be_instantiated_from_dict(cls):
    arguments = get_valid_primitive_data(cls)
    assert cls(**arguments)


@pytest.mark.parametrize('cls', model_classes)
def test_all_types_can_be_instantiated_from_annotation(cls):
    arguments = get_valid_primitive_data(cls)
    arguments = {k: create_attribute(create_cls_annotations(cls)[k], v)
                 for k, v in arguments.items()}
    print(arguments)
    assert cls(**arguments)

@pytest.mark.parametrize('cls', model_classes)
def test_all_types_can_be_instantiated_from_tuple(cls):
    arguments = get_valid_primitive_data(cls).values()
    # make sure the arguments are in the correct order
    arguments = tuple(arguments)
    obj = cls(*arguments)
    obj_json = obj.json()
    assert obj
    for index, argument in enumerate(arguments):
        if isinstance(argument, dict):
            args = list(arguments)
            args[index] = tuple(argument.values())
            assert cls(*args).json() == obj_json