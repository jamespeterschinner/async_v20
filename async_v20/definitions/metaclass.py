from inspect import signature
from .attributes import instance_attributes
from .attributes import json_attributes
from .helpers import create_attribute
from .helpers import create_doc_signature
from operator import itemgetter
from functools import wraps

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
