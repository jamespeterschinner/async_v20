from inspect import Signature, Parameter, _empty
from itertools import chain, starmap

from .descriptors.base import Descriptor

delimiter = '.'

async def async_flatten_dict(dictionary, delimiter=delimiter):
    """Flatten a nested dictionary structure"""

    async def unpack(parent_key, parent_value):
        """Unpack one level of nesting in a dictionary"""
        try:
            items = parent_value.items()
        except AttributeError:
            # parent_value was not a dict, no need to flatten
            yield (parent_key, parent_value)
        else:
            for key, value in items:
                yield (parent_key + delimiter + key, value)

    async def run(gen):
        return [pair async for pair in gen]

    while True:
        # Keep unpacking the dictionary until all value's are not dictionary's
        agens = (unpack(k, v) for k, v in dictionary.items())
        pairs = [await run(gen) for gen in agens]
        dictionary = dict(chain.from_iterable(pairs))
        if not any(isinstance(value, dict) for value in dictionary.values()):
            break

    return dictionary

def flatten_dict(dictionary, delimiter=delimiter):
    """Flatten a nested dictionary structure"""

    def unpack(parent_key, parent_value):
        """Unpack one level of nesting in a dictionary"""
        try:
            items = parent_value.items()
        except AttributeError:
            # parent_value was not a dict, no need to flatten
            yield (parent_key, parent_value)
        else:
            for key, value in items:
                yield (parent_key + delimiter + key, value)

    while True:
        # Keep unpacking the dictionary until all value's are not dictionary's
        dictionary = dict(chain.from_iterable(starmap(unpack, dictionary.items())))
        if not any(isinstance(value, dict) for value in dictionary.values()):
            break

    return dictionary

def create_signature(schema):
    def create_parameter(key, schema_value):
        name = key.lower()
        annotation = schema_value.typ
        default = schema_value.default
        if default == _empty and schema_value.required is False:
            default = None
        return Parameter(name=name, annotation=annotation, default=default, kind=Parameter.POSITIONAL_OR_KEYWORD)

    def sort_key(param):
        default = False
        if param.default != _empty:
            default = True
        return default

    return Signature(sorted([create_parameter(key, value) for key, value in schema.items()], key=sort_key))


def assign_descriptors(cls):
    for attr, schema_value in cls._schema.items():
        typ = schema_value.typ
        if issubclass(typ, Descriptor):
            if callable(typ):  # This is to keep IDE happy. Descriptor class is callable!
                attr = attr.lower()
                setattr(cls, attr, typ())
    return cls

def create_attribute(typ, data):
    if isinstance(data, dict):
        return typ(**data)
    else:
        return typ(data)
