import ujson as json
from functools import wraps
from inspect import signature
from operator import itemgetter

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

    def wrap(self, *args, **kwargs):
        def format():
            for name, value in kwargs.items():
                try:
                    yield instance_attributes[name], value
                except KeyError:
                    continue

        return new(self, *args, **dict(format()))

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

        # This dictionary is used to create pandas.Series objects. The template ensures that all
        # like objects have same length Series allowing for them to be passed into a dataframe
        class_obj.template = dict.fromkeys(sig.parameters)

        for index, attr in enumerate(class_obj.template):
            setattr(class_obj, attr, property(itemgetter(index)))

        return class_obj


class Model(tuple, metaclass=ORM):
    _schema = {}
    _fields = []
    _delimiter = '_'
    _derived = None

    # Format string used when generating a summary for this object
    _summary_format = ''

    # Format string used when generating a name for this object
    _name_format = ''

    def __init__(self, *args, **kwargs):
        super().__init__()

    def __new__(self, *args, **kwargs):
        sig = self.__new__.__signature__
        self._fields = []  # Would normally place this is the class. Didn't segment instance attrs though

        # This dict allow for camelCase and snake_case to be passed without error
        kwargs = {self.__class__.instance_attributes[key]: value for key, value in kwargs.items()}
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        # When assigning attrs to the instance. The passed value is then passed to the argument's annotation
        # Which is basically type checking. In order to do this, we need a list of tuples with:
        # name :- name of attribute
        # annotation :- signature annotation
        # value :- passed value
        annotations = {attr: sig.parameters[attr].annotation for attr in self.template}
        arguments = [(attr, annotations[attr], value) for attr, value in bound.arguments.items()]

        # Instantiate annotations with value and assign to instance
        data = []
        for name, annotation, value in arguments:
            self._fields.append(name)
            attribute_value = create_attribute(annotation, value) if value else value
            data.append(attribute_value)
        data = tuple(data)
        result = tuple.__new__(self, data)
        return result

    # def __repr__(self):
    #     return self.__class__.__name__

    # Recursion might be an issue
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
    if isinstance(data, Model):
        result = data
    elif isinstance(data, dict):
        result = typ(**data)
    elif isinstance(data, tuple):
        result = typ(*data)
    else:
        result = typ(data)
    return result
