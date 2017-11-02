import pytest
from async_v20.definitions import types
from async_v20.definitions.base import Model
from .test_primitives.helpers import get_valid_primitive_data

@pytest.mark.parametrize('cls', [getattr(types, typ) for typ in types.__all__])
def test_class_annotations_match_the_parents_class_annotations(cls):
    if not cls.__bases__[0] == Model:
        print('BASE')
        print(cls.__bases__[0].__new__.__annotations__)
        print('DERIVED')
        print(cls.__new__.__annotations__)

        for annotation in cls.__new__.__annotations__:
            assert annotation in cls.__bases__[0].__new__.__annotations__



@pytest.mark.parametrize('cls', [getattr(types, typ) for typ in types.__all__])
def test_all_types_can_be_instantiated_from_dict(cls):
        arguments = get_valid_primitive_data(cls)
        assert cls(**arguments)

