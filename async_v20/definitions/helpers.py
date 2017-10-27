from inspect import Signature, Parameter, _empty
from itertools import chain, starmap

from inflection import underscore

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


def create_signature(cls):
    schema = cls._schema

    def create_parameter(key, schema_value):
        name = cls.instance_attributes[key]
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

    def parameters(schema):
        yield Parameter(name='self', kind=Parameter.POSITIONAL_ONLY)
        for key, value in schema.items():
            yield create_parameter(key, value)

    return Signature(sorted(parameters(schema), key=sort_key))

def create_doc_signature(cls, sig):
    names = list(sig.parameters.keys())
    annotations = list(map(lambda x: '' if x.annotation == _empty else ': '+ x.annotation.__name__
                           , sig.parameters.values()))

    defaults = list(map(lambda x: '' if x.default == _empty else '=' + str(x.default), sig.parameters.values()))
    arguments = ', '.join(''.join(argument) for argument in zip(names, annotations, defaults))
    return f'{cls.__name__}({arguments})\n{cls.__doc__}'

def create_instance_attributes(cls):
    instance_attributes = {key: underscore(key) for key in cls._schema}
    instance_attributes.update({value: value for value in instance_attributes.values()})
    return instance_attributes


def create_json_attributes(cls):
    return {underscore(key): key for key in cls._schema}


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


def parse_args_for_typ(cls, args, kwargs):
    """See if a type was given in the arguments"""
    none = {None}  # default type argument

    def search_args(args):
        typ = sorted(none.union(set(args)).intersection(none.union(cls._dispatch)),
                     key=lambda x: False if x else True)[0]
        if typ is not None:
            args = tuple(arg for arg in args if arg != typ)
        return args, typ

    args, typ = search_args(args)
    typ = kwargs.pop('type', typ)
    print('Called')
    print('PARSER', args, kwargs, typ)
    return args, kwargs, typ