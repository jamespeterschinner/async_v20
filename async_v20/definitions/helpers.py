from inspect import Signature, Parameter, _empty
from itertools import starmap, chain
# from inflection import underscore

from .descriptors.base import Descriptor


def flatten_dict(dictionary, delimiter='_'):
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


def _sig_sort_key(param):
    default = False
    if param.default != _empty:
        default = True
    return default


def _create_signature_from_parameters(parameters):
    return Signature(sorted(parameters, key=_sig_sort_key))


def create_signature(cls):
    schema = cls._schema

    def create_parameter(key, schema_value):
        name = cls.instance_attributes[key]
        annotation = schema_value.typ
        default = schema_value.default
        if default == _empty and schema_value.required is False:
            default = None
        return Parameter(name=name, annotation=annotation, default=default, kind=Parameter.POSITIONAL_OR_KEYWORD)

    def parameters(schema):
        yield Parameter(name='self', kind=Parameter.POSITIONAL_ONLY)
        for key, value in schema.items():
            yield create_parameter(key, value)

    return _create_signature_from_parameters(parameters(schema))


def create_doc_signature(cls, sig):
    names = list(sig.parameters.keys())
    annotations = list(map(lambda x: '' if x.annotation == _empty else ': ' + x.annotation.__name__
                           , sig.parameters.values()))

    defaults = list(map(lambda x: '' if x.default == _empty else '=' + str(x.default), sig.parameters.values()))
    arguments = ', '.join(''.join(argument) for argument in zip(names, annotations, defaults))
    return f'{cls.__name__}({arguments})\n{cls.__doc__}'



def assign_descriptors(cls):
    for attr, schema_value in cls._schema.items():
        typ = schema_value.typ
        if issubclass(typ, Descriptor):
            attr = cls.instance_attributes[attr]
            setattr(cls, attr, typ(name='_' + attr))
    return cls


def create_attribute(typ, data):
    if isinstance(data, dict):
        result = typ(**data)
    elif isinstance(data, tuple):
        result = typ(*data)
    else:
        result = typ(data)
    return result

