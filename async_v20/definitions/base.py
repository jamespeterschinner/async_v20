import ujson as json
from collections import OrderedDict
from functools import wraps
from inspect import signature, Signature
from operator import itemgetter

import pandas as pd

from .attributes import instance_attributes
from .attributes import json_attributes
from .helpers import create_doc_signature
from .helpers import flatten_dict


class Primitive(object):
    """Mixin class to denote primitive type"""
    pass


class Array(tuple):
    """Mixin to denote objects that are sent from OANDA in an array.
    Also used to correctly serialize objects.
    """

    # Denotes the type the Array contains
    _contains = None

    def __new__(cls, *data):
        try:
            return super().__new__(cls, (create_attribute(cls._contains, obj) for obj in data))
        except (TypeError, ValueError):
            msg = f'FAILED TO CREATE OBJECT: {cls.__name__} FROM DATA: {data} DATA TYPE: {type(data)}'
            raise ValueError(msg)


def arg_parse(new: classmethod, signature=Signature) -> classmethod:
    """Wrapper to convert camelCase arguments to snake_case """

    @wraps(new)
    def wrap(cls, *args, args_have_been_formatted=False, **kwargs):
        # Don't format arguments twice
        if args_have_been_formatted:
            # locals() returns __class__
            # If it exists remove it.
            kwargs.pop('__class__', None)
            return new(cls, **kwargs)

        # Remove preset arguments this class defines from kwargs
        for argument in cls._preset_arguments:
            kwargs.pop(argument, None)

        def format():
            for name, value in kwargs.items():
                try:
                    yield instance_attributes[name], value
                except KeyError:
                    continue

        return new(cls, *args, **dict(format()))

    wrap.__signature__ = signature
    wrap.__annotations__ = new.__annotations__
    return wrap


def tool_tip(init, signature):
    @wraps(init)
    def wrap(*args, **kwargs):
        return init(*args, **kwargs)

    wrap.__signature__ = signature
    return wrap


class ORM(type):
    def __init__(self, *args, **kwargs):
        super().__init__(self)

    def __new__(mcs, *args, **kwargs):

        class_obj = super().__new__(mcs, *args, **kwargs)

        # This signature defines the data structure of the objects
        # (providing the object is derived directly from Model)
        # This signature has no 'self' parameter
        template_signature = signature(class_obj)

        # This signature does have a 'self' parameter
        pretty_signature = signature(class_obj.__new__)

        # This is for tool tips in IDE's (only tested in PyCharm)
        class_obj.__init__ = tool_tip(class_obj.__init__, pretty_signature)

        if not class_obj == 'Model':
            # Only add the argument parser to objects that derive from Model
            # Model should never be instantiated on it's own so arguments
            # should already be parsed by models subclasses
            class_obj.__new__ = arg_parse(class_obj.__new__, pretty_signature)

        # Create a pretty signature for documentation
        class_obj.__doc__ = create_doc_signature(class_obj, pretty_signature)

        if class_obj.__bases__[0].__name__ == 'Model':

            # This is the overall template of the object.
            # Because Model objects are tuples the order of attributes
            # is important. This order is
            # defined by the order of arguments in the signature.
            # Only objects that derive directly from model get a template.
            # This means class' derived further down the inheritance tree
            # have the same data structure.
            # Which is nice because object attributes can then use the same itemgetter
            # And
            # All objects derived from the same type will have a the columns aligning
            # when the .series method is called.
            class_obj.template = OrderedDict.fromkeys(template_signature.parameters)

            # Create getters for each attribute
            for index, attr in enumerate(class_obj.template):
                setattr(class_obj, attr, property(itemgetter(index)))

            # Model.__new__ uses this class attribute to
            class_obj.__annotations__ = class_obj.__new__.__annotations__

        return class_obj


class Model(tuple, metaclass=ORM):
    # Make attribute assignment impossible
    __slots__ = ()

    # The delimiter to use when flattening dictionaries
    _delimiter = '_'

    # Representation string used when generating a summary for this object
    _repr_format = ''

    # Arguments the base class defines
    # But the derived class require they are fixed.
    # Any arguments passed, that match names in `_preset_arguments`
    # will be removed. Prior to calling new.
    _preset_arguments = ()

    def __repr__(self):
        def information():

            # These attributes seem to be the most important to users
            for attribute in ('amount', 'financing', 'id', 'instrument',
                              'pl', 'price', 'reason', 'time', 'units'):
                try:
                    value = getattr(self, attribute)
                except (IndexError, AttributeError):
                    continue
                if value is not None:
                    yield f'{attribute}={value}'

        return f'<{self.__class__.__name__}: {", ".join(information())}>'

    def __init__(self, *args, **kwargs):
        super().__init__()

    def __new__(cls, *args, **kwargs):

        # contains all the attributes the class contains
        cls._fields = []

        arguments = ((attr, cls.__annotations__[attr], kwargs[attr]) for attr in cls.template)

        def construct_object_data():
            for name, annotation, value in arguments:
                cls._fields.append(name)
                yield create_attribute(annotation, value) if value else value

        result = super().__new__(cls, tuple(construct_object_data()))
        return result

    def json_dict(self, float_to_string=True):
        def fields():
            for field in self._fields:
                attr = getattr(self, field)
                if attr is None:
                    continue
                if not isinstance(attr, (int, float, str)):
                    try:
                        attr = attr.json_dict(float_to_string)
                    except AttributeError:
                        try:
                            attr = [obj.json_dict(float_to_string) for obj in attr]
                        except AttributeError:
                            attr = [str(obj)
                                    if float_to_string and isinstance(obj, float)
                                    else obj
                                    for obj in attr]


                elif float_to_string and isinstance(attr, float):
                    attr = str(attr)
                yield field, attr

        return {json_attributes[field]: attr for field, attr in fields()}

    def json(self):
        return json.dumps(self.json_dict(float_to_string=True))

    def data(self, float_to_string=False):
        return flatten_dict(self.json_dict(float_to_string), self._delimiter)

    def series(self):
        def create_data():
            for key, value in self.data(float_to_string=False).items():
                if isinstance(value, str):
                    try:
                        value = int(value)
                    except ValueError:
                        pass
                yield key, value

        return pd.Series(dict(self.template, **dict(create_data())))


def create_attribute(typ, data):
    try:
        if isinstance(data, (Model, Array, Primitive)):
            if not issubclass(type(data), typ):
                raise TypeError(f'{data} must be of type {typ}')
            result = data
        elif isinstance(data, dict):
            result = typ(**data)
        elif isinstance(data, (tuple, list)):
            result = typ(*data)
        else:
            result = typ(data)
    except TypeError as e:
        # This error handling is required when there is no
        # schema available to parse the data. Typically
        # when an error code has been returned
        # A none value should be returned if this is the case
        if typ is not None:
            raise TypeError(e)
    else:
        return result
