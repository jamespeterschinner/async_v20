import logging
import ujson as json
from functools import wraps, partial
from inspect import signature

import pandas as pd

from .attributes import json_attributes
from .helpers import check_conflicting_arguments
from .helpers import create_doc_signature
from .helpers import create_indexed_lookup
from .helpers import flatten_dict
from .helpers import json_to_instance_attributes
from .primitives import Primitive, Specifier
from ..exceptions import IncompatibleValue, UnknownValue, InstantiationFailure

logger = logging.getLogger(__name__)


def arg_parse(__init__, template: tuple, preset_values: dict) -> classmethod:
    """Wrapper to convert camelCase arguments to snake_case """

    @wraps(__init__)
    def wrap(self, *args, **kwargs):
        check_conflicting_arguments(self, kwargs, preset_values)
        kwargs = dict(json_to_instance_attributes(self, kwargs, template))
        try:
            return __init__(self, *args, **kwargs)
        except TypeError as e:
            msg = f'Could note create {self.__class__}. ARGUMENTS: {args, kwargs}. {e}'
            logger.error(msg)
            raise InstantiationFailure(msg)

    wrap.__annotations__ = __init__.__annotations__
    return wrap


class ORM(type):

    def __new__(mcs, name, bases, namespace, **kwargs):
        jit = kwargs.pop('jit', True)

        try:
            arg_names = tuple(signature(namespace.get('__init__')).parameters)
        except TypeError:
            arg_names = ()

        slots = arg_names + tuple(kwargs) + tuple(namespace.get('__slots__', ()))
        if jit:
            slots = slots + tuple(map(lambda x: '_' + x, arg_names))

        namespace['__slots__'] = slots

        class_obj = super().__new__(mcs, name, bases, namespace)

        bound_signature = signature(class_obj)  # Does not have `self`

        unbound_signature = signature(class_obj.__init__)  # Does have `self`

        template = tuple(bound_signature.parameters)

        class_obj._jit = jit

        class_obj._preset_values = kwargs

        if not class_obj.__name__ == 'Model':
            # Only add the argument parser to objects that derive from Model
            class_obj.__init__ = arg_parse(class_obj.__init__, template, kwargs)
            class_obj.__init__.__signature__ = unbound_signature

            class_obj._template = template

        # Create a pretty signature for documentation
        class_obj.__doc__ = create_doc_signature(class_obj, bound_signature)

        class_obj.__annotations__ = class_obj.__init__.__annotations__

        return class_obj


class Model(object, metaclass=ORM):
    # Make attribute assignment impossible
    __slots__ = ('_fields',)

    _delimiter = '_'

    def __setattr__(self, key, value):
        raise NotImplementedError

    def __delattr__(self, item):
        raise NotImplementedError

    def __repr__(self):
        def information():

            # These attributes seem to be the most important to users
            for attribute in ('id', 'instrument', 'amount', 'units',
                              'current_units', 'realized_pl',
                              'unrealized_pl', 'price', 'reason', 'time'):
                try:
                    value = getattr(self, attribute)
                except (IndexError, AttributeError):
                    continue
                if value is not None:
                    yield f'{attribute}={value}'

        # Attempt to get important attributes otherwise provide everything
        attributes = ', '.join(information())
        if not attributes:
            attributes = ', '.join(self._fields)

        return f'<{self.__class__.__name__}: {attributes}>'

    def __getattr__(self, item):
        result = self.__getattribute__('_' + item)()
        object.__setattr__(self, item, result)
        object.__delattr__(self, '_' + item)
        return result

    def __init__(self, **kwargs):

        # contains all the attributes the class instance contains
        fields = []
        instantiate = {
            True: lambda name, typ, data:
                object.__setattr__(self, '_' + name, partial(create_attribute, typ, data)),
            False: lambda name, typ, data:
                object.__setattr__(self, name, create_attribute(typ, data))}[self._jit]

        for name, attr in self._preset_values.items():
            fields.append(name)
            object.__setattr__(self, name, attr)

        for name in self._template:
            value = kwargs[name]
            annotation = self.__annotations__[name]
            if value is ...:
                pass
            elif value is None:
                fields.append(name)
                object.__setattr__(self, name, None)
            else:
                fields.append(name)
                instantiate(name, annotation, value)

        object.__setattr__(self, '_fields', tuple(fields))

    def replace(self, **kwargs):
        return self.__class__(**dict(self.dict(), **kwargs))

    def dict(self, json=False, datetime_format=None):
        """Convert object into a dictionary representation

        Args:
            json: - bool. True converts dict keys into JSON format
            datetime_format: - str. convert pd.Timestamps to desired format
        """

        def fields():

            for field in self._fields:

                attr = getattr(self, field)

                if not isinstance(attr, (int, float, str, pd.Timestamp)):
                    # Means attr is either a Model object, tuple, list, None
                    try:
                        attr = attr.dict(json=json, datetime_format=datetime_format)
                    except AttributeError:
                        try:
                            attr = [obj.dict(json=json, datetime_format=datetime_format) for obj in attr]
                        except AttributeError:
                            attr = [str(obj)
                                    if json and isinstance(obj, float)
                                    else obj
                                    for obj in attr]
                        except TypeError:
                            # Attr is None. account_changes endpoint
                            # returns items with null
                            attr = attr
                elif json and isinstance(attr, (float, Specifier)):
                    # Technically OANDA's spec declares all specifiers as strings
                    # though TradeID and OrderID in async_v20 are integers. As this
                    # seems to be most useful type. We will make sure to cast them back
                    # to strings when sending JSON data to OANDA
                    attr = str(attr)
                elif isinstance(attr, pd.Timestamp):
                    if json or datetime_format == 'RFC3339':
                        attr = attr.json(datetime_format)
                    elif datetime_format == 'UNIX':
                        attr = attr.value

                yield field, attr

        return {json_attributes[field] if json else field: attr for field, attr in fields()}

    def json(self, datetime_format='UNIX'):
        return json.dumps(self.dict(json=True, datetime_format=datetime_format))

    def data(self, json=False, datetime_format=None):
        return flatten_dict(self.dict(json=json, datetime_format=datetime_format), self._delimiter)

    def series(self, json=False, datetime_format=None):
        return pd.Series(self.data(json=json, datetime_format=datetime_format))


class Array(tuple):
    """Mixin to denote objects that are sent from OANDA in an array.
    Also used to correctly serialize objects.
    """

    def __init_subclass__(cls, **kwargs):
        # Denotes the type the Array contains
        cls._contains = kwargs.pop('contains')
        cls._one_to_many = kwargs.pop('one_to_many', True)

    def __new__(cls, *items):
        instance = super().__new__(cls, tuple(create_attribute(cls._contains, item) for item in items))
        return create_indexed_lookup(instance, cls._one_to_many)

    def dataframe(self, json=False, datetime_format=None):
        """Create a pandas.Dataframe"""
        return pd.DataFrame(obj.data(json=json, datetime_format=datetime_format) for obj in self)


def create_attribute(typ, data):
    """Correctly instantiate object based upon type of argument passed"""
    try:
        if isinstance(data, dict):
            result = typ(**data)
        elif isinstance(data, Specifier):
            if not issubclass(typ, Specifier):
                msg = f'{data} must be a {Specifier} is {type(data)}'
                logger.error(msg)
                raise IncompatibleValue(msg)
            result = typ(data)
        elif isinstance(data, (Model, Array, Primitive)):
            if not issubclass(type(data), typ):
                msg = f'{data} must be of type {typ} is {type(data)}'
                logger.error(msg)
                raise IncompatibleValue(msg)
            result = data
        elif isinstance(data, (tuple, list)):
            result = typ(*data)
        else:
            result = typ(data)
    except (TypeError, ValueError, UnknownValue):
        # This error handling is required when there is no
        # schema available to parse the data. Typically
        # when an error code has been returned
        # A none value should be returned if this is the case
        if typ is not None:
            msg = f'Could note create {typ}. DATA: {data}, TYPE: {type(data)}'
            logger.error(msg)
            raise InstantiationFailure(msg)
    else:
        return result
