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
        # When creating a new class we need to update the _dispatch attribute.
        # The _dispatch attribute allows an OANDA JSON response (converted to a dict)
        # to be passed to base class specified in OANDA's docs

        # Only class' that have a deeper inheritance structure than Model->Subclass
        # require the dispatch parameter. These include:
        # - specialisation of Transaction
        # - specialisation of Orders
        parent = next(iter(cls.__bases__))

        # Must use name of class to avoid cyclic imports
        if parent is not Model:
            # This value is used to determine what subclass to return from the parent
            dispatch_key = cls._schema.get('type')
            # The streaming objects are unique, in that they specify a 'type'
            # with no base class. This checks for that
            if dispatch_key:
                cls.specialized = True
                cls._dispatch.update({dispatch_key.default: cls})
        else:
            cls._derived = cls


    def __new__(cls, *args, **kwargs):
        if cls._dispatch:
            args, kwargs, typ = parse_args_for_typ(cls, args, kwargs)

            if typ and cls._dispatch:
                cls = cls._dispatch[typ]
            else:
                msg = f"{cls.__name__}.__new__() missing required keyword argument: 'type'. \n" \
                      f"Possible values are: {', '.join(cls._dispatch)}"
                raise TypeError(msg)

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
