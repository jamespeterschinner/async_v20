from itertools import chain, starmap
from async_v20.helpers import sleep
from inspect import Signature, Parameter, _empty
from .descriptors.base import DescriptorProtocol


async def _flatten_dict(dictionary):
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
                yield (parent_key + '_' + key, value)

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


class IndexDict(dict):
    def __getitem__(self, item):
        result = None
        try:
            result = super().__getitem__(item)
        except KeyError:
            try:
                result = list(self.values())[item]
            except IndexError:
                pass
        return result

    def reverse_lookup(self, index):
        return list(self.keys())[index]


def _create_signature(cls):
    def create_parameter(key, schema_value):
        name = key.lower()
        annotation = schema_value.typ
        default = schema_value.default
        if default == _empty and schema_value.required == False:
            default = None
        return Parameter(name=name, annotation=annotation, default=default, kind=Parameter.POSITIONAL_OR_KEYWORD)

    def sort_key(param):
        default = False
        if param.default != _empty:
            default = True
        return default

    return Signature(sorted([create_parameter(key, value) for key, value in cls._schema.items()], key=sort_key))


def _assign_descriptors(cls):
    for attr, schema_value in cls._schema.items():
        typ = schema_value.typ
        if issubclass(typ, DescriptorProtocol):
            if callable(typ):  # This is to keep IDE happy. Descriptor class is callable!
                setattr(cls, attr, typ())
    return cls


def _create_arg_lookup(cls):
    cls._arg_lookup = IndexDict([(attr.lower(), schema_value.typ)
                                 for attr, schema_value in cls._schema.items()])
    return cls
