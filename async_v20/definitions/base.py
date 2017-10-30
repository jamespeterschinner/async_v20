import ujson as json
from functools import wraps
from inspect import signature
from operator import itemgetter
from collections import OrderedDict
import pandas as pd

from .attributes import instance_attributes
from .attributes import json_attributes
from .helpers import create_doc_signature
from .helpers import flatten_dict


class JSONArray(object):
    typ = None

    def __new__(cls, data):
        try:
            return tuple(create_attribute(cls.typ, obj) for obj in data)
        except TypeError:
            msg = f'FAILED TO CREATE OBJECT: {cls.typ} FROM DATA: {data} DATA TYPE: {type(data)}'
            raise Exception(msg)


class Array(type):
    """Used to denote objects that are sent from OANDA in an array.
    Also used to correctly serialize objects.
    """

    def __new__(mcs, typ):
        return super().__new__(mcs, f'Array_{typ.__name__}', (JSONArray,), {'typ': typ})


def format_args(new):
    wraps(new)

    def wrap(cls, *args, **kwargs):
        def format():
            for name, value in kwargs.items():
                try:
                    yield instance_attributes[name], value
                except KeyError:
                    continue

        return new(cls, *args, **dict(format()))

    wrap.__annotations__ = new.__annotations__
    return wrap


class ORM(type):
    instance_attributes = {}
    json_attributes = {}

    def __init__(self, *args, **kwargs):
        super().__init__(self)
        pass

    def __new__(mcs, *args, **kwargs):
        class_obj = super().__new__(mcs, *args, **kwargs)
        mcs.instance_attributes = instance_attributes
        mcs.json_attributes = json_attributes

        # Create class signature
        sig = signature(class_obj)

        class_obj.__new__ = format_args(class_obj.__new__)

        # Update
        class_obj.__new__.__signature__ = sig

        # Create a pretty signature for documentation
        class_obj.__doc__ = create_doc_signature(class_obj, sig)

        # This is the overall template of the object.
        # Because Model objects are tuples the order of attributes
        # is important. As can been seen the order of attributes is
        # defined by the order of arguments in the signature
        class_obj.template = OrderedDict.fromkeys(sig.parameters)

        # Create getters for each attribute
        for index, attr in enumerate(class_obj.template):
            setattr(class_obj, attr, property(itemgetter(index)))

        return class_obj


class Model(tuple, metaclass=ORM):

    # The delimiter to use when flattening dictionaries
    _delimiter = '_'

    # Format string used when generating a summary for this object
    _summary_format = ''

    # Format string used when generating a name for this object
    _name_format = ''

    def __new__(cls, *args, **kwargs):

        # contains all the attributes the class contains
        cls._fields = []

        arguments = ((attr, cls.__new__.__annotations__[attr], kwargs[attr]) for attr in cls.template)

        def construct_object_data():
            for name, annotation, value in arguments:
                cls._fields.append(name)
                yield create_attribute(annotation, value) if value else value

        result = tuple.__new__(cls, tuple(construct_object_data()))
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

        return {self.__class__.json_attributes[field]: attr for field, attr in fields()}

    def json_data(self):
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
    if typ is None:
        return
    elif isinstance(data, Model):
        result = data
    elif isinstance(data, dict):
        result = typ(**data)
    elif isinstance(data, tuple):
        result = typ(*data)
    else:
        result = typ(data)
    return result
