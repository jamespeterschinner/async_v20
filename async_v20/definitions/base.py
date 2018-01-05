import logging
import ujson as json
from collections import OrderedDict
from functools import wraps, partial
from inspect import signature, Signature

import pandas as pd

from .attributes import instance_attributes
from .attributes import json_attributes
from .helpers import create_doc_signature
from .helpers import create_indexed_lookup
from .helpers import flatten_dict
from .helpers import get_attribute
from .helpers import lazy_evaluate
from .helpers import null_attribute
from .primitives import Primitive, Specifier
from ..exceptions import IncompatibleValue, UnknownValue, InstantiationFailure

logger = logging.getLogger(__name__)


def arg_parse(new: classmethod, signature=Signature) -> classmethod:
    """Wrapper to convert camelCase arguments to snake_case """

    @wraps(new)
    def wrap(cls, *args, args_have_been_formatted=False, **kwargs):

        # This argument is set when data is returned from
        # the __new__ method of a class derived from Model
        if args_have_been_formatted:
            # locals() returns __class__ so we remove it.
            kwargs.pop('__class__', None)
            return new(cls, **kwargs)

        # Remove preset arguments this class defines from kwargs
        # Also make sure that if the argument was supplied it
        # is the same as the preset value
        for argument, preset_value in cls._preset_arguments.items():
            value = kwargs.pop(argument, None)
            if value is not None:
                if not value == preset_value:
                    msg = f'CLASS {cls.__name__}.{argument}' \
                          f' MUST == {preset_value} NOT {value}'
                    logger.error(msg)
                    raise IncompatibleValue(msg)

        def format():
            for name, value in kwargs.items():
                try:
                    yield instance_attributes[name], value
                except KeyError:
                    possible_arguments = ', '.join(param.name for param in signature.parameters.values()
                                                   if param.name != 'cls')
                    msg = f'`{name}` is not a valid keyword argument. ' \
                          f'Possible arguments for class {cls.__name__} ' \
                          f'include: {possible_arguments}'
                    logger.error(msg)
                    raise UnknownValue(msg)

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
    def __init__(cls, *args, **kwargs):
        super().__init__(cls)

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

            # Setting this argument to true prevents the argument parser
            # from converting camelCase to snake_case multiple times when
            # super().__new__ is called
            class_obj._preset_arguments.update(args_have_been_formatted=True)

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
                setattr(class_obj, attr, property(partial(get_attribute, index)))

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
    _preset_arguments = {}

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

    def __init__(self, *args, **kwargs):
        super().__init__()

    def __new__(cls, *args, **kwargs):

        # contains all the attributes the class instance contains
        fields = []

        arguments = ((attr, cls.__annotations__[attr], kwargs[attr]) for attr in cls.template)

        def construct_object_data(arguments):

            for name, annotation, value in arguments:
                # Sometimes OANDA JSON responses contain null values.
                # Ellipsis (...) is used as the default parameter
                # to determine the difference between None and null
                # This is important because it allows converting objects
                # back into the EXACT JSON they were created from.
                # Without dropping the null values

                if value is ...:
                    yield null_attribute
                elif value is None:
                    fields.append(name)
                    yield null_attribute
                else:
                    fields.append(name)
                    yield lazy_evaluate(partial(create_attribute, annotation, value))

        instance = super().__new__(cls, tuple(construct_object_data(arguments)))
        instance._fields = tuple(fields)
        return instance

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
        def create_data():
            for key, value in self.data(json=json, datetime_format=datetime_format).items():
                if isinstance(value, str):
                    try:
                        value = int(value)
                    except ValueError:
                        pass
                yield key, value

        return pd.Series(dict(create_data()))


class Array(tuple):
    """Mixin to denote objects that are sent from OANDA in an array.
    Also used to correctly serialize objects.
    """

    def __init_subclass__(cls, contains, one_to_many=True, **kwargs):
        # Denotes the type the Array contains
        cls._contains = contains
        cls._one_to_may = one_to_many

    def __new__(cls, *items):
        instance = super().__new__(cls, tuple(create_attribute(cls._contains, item) for item in items))
        return create_indexed_lookup(instance, cls._one_to_may)

    def dataframe(self, json=False, datetime_format=None):
        """Create a pandas.Dataframe"""
        return pd.DataFrame(obj.series(json=json, datetime_format=datetime_format) for obj in self)


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
