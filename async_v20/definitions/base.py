import ujson as json

import pandas as pd

from .metaclass import *


class Model(metaclass=ORM):
    _schema = {}
    _fields = []
    _delimiter = '_'
    _derived = None

    # More info about this code be found in PEP 487 https://www.python.org/dev/peps/pep-0487/
    def __init_subclass__(cls, **kwargs):
        dispatch_key = cls._schema.get('type', None)
        if dispatch_key:
            cls._dispatch.update({dispatch_key.default: cls})
        else:
            cls._derived = cls

    def __new__(cls, *args, **kwargs):
        if cls._dispatch:
            typ = kwargs.get('type', None)
            if typ:
                return cls._dispatch[typ](*args, **kwargs)
        else:
            return super().__new__(cls)

    def __repr__(self):
        return self.__class__.__name__

    # Recursion might be an issue
    def json_dict(self, float_to_string=True):
        def get_object_fields(attr):
            attr = getattr(self, attr)
            if not isinstance(attr, (int, float, str)):
                try:
                    attr = attr.json_dict(float_to_string)
                except AttributeError:
                    attr = [obj.json_dict(float_to_string) for obj in attr]
            elif float_to_string and isinstance(attr, float):
                attr = str(attr)
            return attr

        return {self.__class__.json_attributes[attr]: get_object_fields(attr)
                for attr in self._fields}


    def json_data(self):
        return json.dumps({self.json_dict()})

    def data(self, float_to_string=True):
        return flatten_dict(self.json_dict(float_to_string), self._delimiter)

    def series(self):
        return pd.Series(dict(self.template, **self.data(float_to_string=False)))
