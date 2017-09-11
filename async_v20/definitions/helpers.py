from itertools import chain, starmap
from async_v20.helpers import sleep
from inspect import Signature, Parameter
from .descriptors.base import Descriptor


async def flatten_dict(dictionary):
    """Flatten a nested dictionary structure"""

    async def unpack(parent_key, parent_value):
        """Unpack one level of nesting in a dictionary"""
        await sleep()
        if isinstance(parent_value, (dict, list)):
            try:
                items = parent_value.items()
            except AttributeError:
                try:
                    items = chain(parent_value)
                except TypeError:
                    # parent value was not iterable or a dict
                    return parent_key, parent_value
                else:
                    for index, value in enumerate(items):
                        # yield (parent_key + '_' + str(index), value)
                        return parent_key, value
            else:
                for key, value in items:
                    return (parent_key + '_' + key, value)
        else:
            return parent_key, parent_value

    # Put each key into a tuple to initiate building a tuple of subkeys
    dictionary = {key: value for key, value in dictionary.items()}

    while True:
        # Keep unpacking the dictionary until all value's are not dictionary's
        dictionary = dict(chain.from_iterable(await starmap(unpack, dictionary.items())))
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

    def reverse_lookup(self, index):
        return list(self.keys())[index]

def _create_signature(cls):
    def create_parameter(key, schema_value):
        name = key.lowercase()
        annotation = schema_value.typ
        default = schema_value.default
        return Parameter(name=name, annotation=annotation, default=default, kind=Parameter.POSITIONAL_OR_KEYWORD)
    return Signature([create_parameter(key, value) for key, value in cls.schema.items()])


def _assign_descriptors(cls):
    for attr, schema_value in cls.schema.items():
        typ = schema_value.typ
        if isinstance(typ, Descriptor):
            if callable(typ):  # This is to keep IDE happy. Descriptor class is callable!
                setattr(cls, attr, typ())
    return cls

def _create_arg_lookup(cls):
    cls._arg_lookup = IndexDict([(attr.lowercase(), schema_value.typ)
                                 for attr, schema_value in cls.schema.items()])
    return cls

async def _set_kwargs(self, kwargs):
    for attr, value in kwargs.items():
        await sleep()
        obj = self.__class__.arg_lookup[attr]
        setattr(self, attr, obj(**value))
    return self

async def _set_args(self, args):
    for index, value in enumerate(args):
        await sleep()
        obj = self.__class__.arg_lookup[index]
        attr = self.__class__.arg_lookup.reverse_lookup(index)
        setattr(self, attr, obj(**value))
    return self
