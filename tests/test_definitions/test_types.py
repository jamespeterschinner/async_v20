import pytest

from async_v20.definitions import types
from async_v20.definitions.base import Model
from async_v20.definitions.base import create_attribute
from tests.test_definitions.helpers import get_valid_primitive_data, create_cls_annotations
import inspect
import re

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

def test_class_default_parameters_contain_parameter_in_preset_arguments():
    # Get the code for the types module
    code = ''.join(inspect.findsource(types)[0])
    # find all the class definitions
    class_definitions = re.findall(r"class[\s\S]*?\*\*{'args_have_been_formatted': True}\)", code)
    # Make sure each class definition is formatted correctly
    for cls in class_definitions:
        # get the __new__ return statement
        return_statement = re.findall(r"return\ssuper\(\)\.__new__\([\s\S]*?\}\)", cls)[0]
        # Find keyword arguments in the return statement
        returned_preset_arguments = re.findall(r"[a-zA-Z]*\S(?=\=)", return_statement)
        # make sure all keyword returned arguments are in the class'
        # _preset_arguments class attribute
        if returned_preset_arguments:
            preset_arguments = re.findall(r"_preset_arguments.*", cls)[0]
            # Debug print out
            print(preset_arguments)
            print(returned_preset_arguments)
            for RPA in returned_preset_arguments:
                assert RPA in preset_arguments