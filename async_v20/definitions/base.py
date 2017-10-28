import ujson as json
from .helpers import flatten_dict
import pandas as pd

from .metaclass import *


class Model(metaclass=ORM):
    _schema = {}
    _fields = []
    _delimiter = '_'
    _derived = None

    # Format string used when generating a summary for this object
    _summary_format = ''

    # Format string used when generating a name for this object
    _name_format = ''


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
                    try:
                        attr = [obj.json_dict(float_to_string) for obj in attr]
                    except AttributeError:
                        attr = [str(obj)
                                if float_to_string and isinstance(obj, float)
                                else obj
                                for obj in attr]
            elif float_to_string and isinstance(attr, float):
                attr = str(attr)
            return attr

        return {self.__class__.json_attributes[attr]: get_object_fields(attr)
                for attr in self._fields}

    def json_data(self):
        return json.dumps(self.json_dict(float_to_string=True))

    def data(self, float_to_string=False):
        return flatten_dict(self.json_dict(float_to_string), self._delimiter)

    def series(self):

        def str_to_int(value):
            try:
                value = int(value)
            except ValueError:
                pass
            return value

        data = {key: str_to_int(value) if isinstance(value, str) else value
                for key, value in self.data(float_to_string=False).items()}
        return pd.Series(dict(self.template, **data))
