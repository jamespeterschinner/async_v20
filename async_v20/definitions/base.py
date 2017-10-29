import ujson as json

import pandas as pd

from .helpers import flatten_dict
from .metaclass import *


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
                        continue
                    yield key, value
        return pd.Series(dict(self.template, **dict(create_data())))
