import pytest
from async_v20.definitions import types
from async_v20.definitions.base import Model

@pytest.mark.parametrize('cls', [getattr(types, typ) for typ in types.__all__])
def test_class_annotations_match_the_parents_class_annotations(cls):
    if not cls.__bases__[0] == Model:
        print('BASE')
        print(cls.__bases__[0].__new__.__annotations__)
        print('DERIVED')
        print(cls.__new__.__annotations__)

        for annotation in cls.__new__.__annotations__:
            assert annotation in cls.__bases__[0].__new__.__annotations__