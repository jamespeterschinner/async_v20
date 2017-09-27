import inspect

import pytest
from async_v20.definitions import types
from async_v20.definitions.descriptors.base import Descriptor
from async_v20.definitions.helpers import assign_descriptors
from async_v20.definitions.helpers import async_flatten_dict
from async_v20.definitions.helpers import create_signature
from async_v20.definitions.helpers import flatten_dict

nested_dict = {'a': {'b': 2, 'c': {'d': 4}}}
flattened_dict = {'a_b': 2, 'a_c_d': 4}


@pytest.mark.asyncio
async def test_async_flatten_dict():
    result = await async_flatten_dict(nested_dict, delimiter='_')
    assert result == flattened_dict


def test_flatten_dict():
    result = flatten_dict(nested_dict, delimiter='_')
    assert result == flattened_dict


# TODO write test to assert both versions of flatten dict produce same output

@pytest.mark.parametrize('cls', map(lambda x: getattr(types, x), types.__all__))
def test_create_signature(cls):
    # Create the signature
    result = create_signature(cls)
    # Ensure result is a Signature
    assert type(result) == inspect.Signature
    # Create names to assert against
    parameter_names = [name for name in result.parameters.keys()]
    # Ensure all signature arguments are lowercase
    assert all(map(lambda x: x.islower(), parameter_names))

    # Create a dict of all the default arguments
    default_parameters = dict([(cls.instance_attributes[key], value.default)
                               for key, value in cls._schema.items()
                               if not value.default == inspect._empty])
    # Create a dict of all the required arguments. Use the default value if there is one
    required_parameters = dict([(cls.instance_attributes[key], 'TEST_PARAMETER')
                                for key, value in cls._schema.items()
                                if value.required])

    # Ensure error occurs when required parameters are missing
    if required_parameters:
        with pytest.raises(TypeError):
            bound = result.bind()

    kwargs = required_parameters
    kwargs.update(default_parameters)
    bound = result.bind(*(None,),**kwargs)
    bound.apply_defaults()
    # Ensure that the default parameters are assigned correctly
    assert all(map(lambda x: bound.arguments[x[0]] == x[1], default_parameters.items()))
    # Ensure that the required parameters
    assert all(map(lambda x: bound.arguments[x[0]] == x[1], required_parameters.items()))


@pytest.mark.parametrize('cls', map(lambda x: getattr(types, x), types.__all__))
def test_assign_descriptors(cls):
    descriptors = dict([(cls.instance_attributes[attr], schema_value.typ)
                   for attr, schema_value
                   in cls._schema.items()
                   if issubclass(schema_value.typ, Descriptor)])
    cls = assign_descriptors(cls)

    assert all(map(lambda x: hasattr(cls, x), descriptors.keys()))
    assert all(map(lambda x: type(getattr(cls, x[0])) == x[1], descriptors.items()))
