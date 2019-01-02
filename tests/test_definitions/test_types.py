import pytest

from async_v20.definitions import types
from async_v20.definitions.base import Model
from async_v20.definitions.base import create_attribute
from async_v20.definitions.types import OrderRequest
from tests.test_definitions.helpers import get_valid_primitive_data, create_cls_annotations
from async_v20.exceptions import UnknownKeywordArgument, InstantiationFailure
import logging
logger = logging.getLogger('async_v20')
logger.disabled = True

model_classes = (cls for cls in (getattr(types, typ) for typ in types.__all__) if
                 issubclass(cls, Model))

model_classes_data = [(cls, get_valid_primitive_data(cls)) for cls in model_classes]


@pytest.mark.parametrize('cls, data', model_classes_data)
def test_all_order_requests_have_an_instrument_parameter(cls, data):
    if issubclass(cls, OrderRequest):
        assert hasattr(cls, 'instrument')

        result = cls(**data)
        assert getattr(result, 'instrument')

@pytest.mark.parametrize('cls, data', model_classes_data)
def test_class_annotations_match_the_parents_class_annotations(cls, data):
    if not cls.__bases__[0] == Model:



        for annotation in cls.__init__.__annotations__:
            assert annotation in cls.__bases__[0].__init__.__annotations__


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
    with pytest.warns(UnknownKeywordArgument):
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
            result = cls(*args).json(datetime_format='UNIX')


            assert result == result_json


@pytest.mark.parametrize('cls, data', model_classes_data)
def test_all_types_can_be_instantiated_from_annotation(cls, data):
    arguments = {k: create_attribute(create_cls_annotations(cls)[k], v)
                 for k, v in data.items()}

    assert cls(**arguments)

@pytest.mark.parametrize('cls, data', model_classes_data)
def test_all_derived_types_have_same_arguments_and_annotations_as_parent(cls, data):
    parent_class = cls.__bases__[0]
    if not parent_class == Model:
        parent_class_parameters = parent_class.__init__.__signature__.parameters
        for name, parameter in cls.__init__.__signature__.parameters.items():
            assert name in parent_class_parameters
            try:
                assert issubclass(parameter.annotation,parent_class_parameters[name].annotation)
            except TypeError:
                # means annotation is async_v20.definitions.helpers.time function
                assert parameter.annotation == parent_class_parameters[name].annotation

@pytest.mark.parametrize('cls, data', model_classes_data)
def test_instances_are_immutable(cls, data):
    instance = cls(**data)
    with pytest.raises(NotImplementedError):
        setattr(instance, instance._fields[0], None)

    with pytest.raises(NotImplementedError):
        delattr(instance, instance._fields[0])

@pytest.mark.parametrize('cls, data', model_classes_data)
def test_instantiation_failure_when_unknown_kwargs_are_passed(cls, data):
    with pytest.raises(InstantiationFailure):
        try:
            cls(**data, o=1) # doubled up argument for CandlestickData
        except TypeError:
            cls(**data, instrument='AUD_USD')

