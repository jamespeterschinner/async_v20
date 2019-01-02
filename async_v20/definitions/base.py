import logging
import ujson as json
from functools import wraps, partial
from inspect import signature

import pandas as pd

from .attributes import json_attributes
from .helpers import check_conflicting_arguments
from .helpers import create_doc_signature
from .helpers import flatten_dict
from .helpers import json_to_instance_attributes
from .helpers import sentinel
from .primitives import Primitive, Specifier, InstrumentName
from ..exceptions import IncompatibleValue, UnknownKeywordArgument, InstantiationFailure

logger = logging.getLogger(__name__)


def arg_parse(__init__, template: tuple, preset_values: dict) -> classmethod:
    """Wrapper to convert camelCase arguments to snake_case"""

    @wraps(__init__)
    def wrap(self, *args, **kwargs):
        check_conflicting_arguments(self, kwargs, preset_values)
        kwargs = dict(json_to_instance_attributes(self, kwargs, template))
        return __init__(self, *args, **kwargs)

    wrap.__annotations__ = __init__.__annotations__
    return wrap


class Metaclass(type):
    """Metaclass for all types in async_v20.

    This class:
        - Configures how the subclasses instantiate their attributes
        - Adds __slots__ to improve memory management
        - Wraps the subclass' __init__ to handle CamelCase kwargs
        - Creates a nicer documentation signature for readthedocs.io
        - Allows subclass' to pre-define attributes by passing arguments. eg.

        class Foo(Model, foo=Bar)
            pass

        would have the attribute foo_instance.foo == Bar
        """

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

        # jit == True object attribute instantiation is deferred
        class_obj._instantiate = {
            True: lambda self, name, typ, data:
            object.__setattr__(self, '_' + name, partial(create_attribute, typ, data)),
            False: lambda self, name, typ, data:
            object.__setattr__(self, name, create_attribute(typ, data))}[jit]

        class_obj._preset_values = kwargs

        if not class_obj.__name__ == 'Model':
            # Only add the argument parser to objects that derive from Model
            class_obj.__init__ = arg_parse(class_obj.__init__, bound_signature.parameters, kwargs)
            class_obj.__init__.__signature__ = unbound_signature

        # Create a pretty signature for documentation
        class_obj.__doc__ = create_doc_signature(class_obj, bound_signature)

        class_obj.__annotations__ = class_obj.__init__.__annotations__

        return class_obj


class Model(object, metaclass=Metaclass):
    # Make attribute assignment impossible
    __slots__ = ('_fields', '_str')

    _delimiter = '_'

    def __setattr__(self, key, value):
        raise NotImplementedError

    def __delattr__(self, item):
        raise NotImplementedError

    def __str__(self):
        return self._str

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
        return result

    def __hash__(self):
        return hash(self._str)

    def __eq__(self, other):
        try:
            if self._str == other._str:
                return True
        except AttributeError:
            pass
        return False

    def __init__(self, **kwargs):

        # contains all the attributes the class instance contains
        fields = []
        for name, attr in self._preset_values.items():
            fields.append(name)
            object.__setattr__(self, name, attr)

        for name, value in kwargs.items():
            annotation = self.__annotations__[name]
            if value is sentinel:
                pass
            elif value is None:
                fields.append(name)
                object.__setattr__(self, name, None)
            else:
                fields.append(name)
                self._instantiate(name, annotation, value)
        object.__setattr__(self, '_str', f'{self.__class__.__name__}(**{kwargs})')
        object.__setattr__(self, '_fields', tuple(fields))

    def get(self, name, default=None):
        return getattr(self, name, default)

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
                        attr = attr.json(datetime_format=datetime_format)
                    elif datetime_format == 'UNIX':
                        attr = attr.value

                yield field, attr

        return {json_attributes[field] if json else field: attr for field, attr in fields()}

    def json(self, datetime_format='UNIX'):
        """Return the JSON representation of the object

        Args:
            datetime_format: either `UNIX` or `RFC3339` controls the representation
              of :class:`~async_v20.definitions.primitives.DataTime` objects"""
        return json.dumps(self.dict(json=True, datetime_format=datetime_format))

    def data(self, json=False, datetime_format=None, delimiter=None):
        """Return the a flattened dictionary representation of the object

        Args:
            json: True, dict will contain OANDA's JSON representation of objects (camelCase),
              False, dict will contain async_v20 representation of objects (snake_case).
            datetime_format: either `UNIX` or `RFC3339` will serialize the date times into the
              corresponding format
            delimiter: Value to use when flattening the the data structure. Defaults to `_`
        """
        if delimiter is None:
            delimiter = self._delimiter
        return flatten_dict(self.dict(json=json, datetime_format=datetime_format), delimiter)

    def series(self, json=False, datetime_format=None, delimiter=None):
        """Return a :class:`pandas.Series` representation of the object

        Args:
            json: True, dict will contain OANDA's JSON representation of objects (camelCase),
              False, dict will contain async_v20 representation of objects (snake_case).
            datetime_format: either `UNIX` or `RFC3339` will serialize the date times into the
              corresponding format
            delimiter: Value to use when flattening the the data structure. Defaults to `_`
        """
        return pd.Series(self.data(json=json, datetime_format=datetime_format, delimiter=delimiter))


class Array(object):
    """Mixin to denote objects that are sent from OANDA in an array.
    Also used to correctly serialize objects.
    """

    def __contains__(self, item):
        """Return True if item in this array or item matches an
        objects id or instrument attribute, False otherwise.

        Note: this traverses all or part of the array, instantiating the
        objects. Using `x in array` may, therefore, have a serious impact on
        performance.

        """
        if str(item) in self._id_index or item in self._instrument_index:
            return True
        for value in self:
            if value == item:
                return True

    def __init__(self, *items):
        """Initialize a new array.

        The *items passed in are assumed to be JSON data. If an item is
        accessed, it is passed to `create_attribute` with the appropriate
        class type.

        Initially, objects are stored in self._items. When accessed, the
        objects are reified and stored in self.items. This is transparently
        handled by self.__getitem__(self, key).

        """
        object.__setattr__(self, '_items', items)
        object.__setattr__(self, 'items', [])

    def __init_subclass__(cls, **kwargs):
        """Record the type *contained in* the subclass-array.

        A subclass like:

            class array_holding_foo(Array, contains=Foo):
                pass

        will have all its inner objects instantiated using class Foo.

        """
        cls._contains = kwargs.pop('contains')

    def __repr__(self):
        return f'<{self._contains.__name__} x {len(self)}>'

    def __hash__(self):
        return hash(str(self._items))

    def __eq__(self, other):
        try:
            if str(self._items) == str(other._items):
                return True
        except AttributeError:
            pass
        return False

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        """Iterate over items in array. Use integer indexing so that
        __getitem__ can handle reifying all the objects.

        """
        for index in range(len(self)):
            yield self[index]

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.__class__(*[self._items[index]
                                    for index in range(len(self._items))[key]])

        length = len(self._items)
        if key < 0:
            key += length

        if not (0 <= key < length):
            raise IndexError('Array index out of range')

        if key >= len(self.items):
            self.items.__iadd__([None] * (key - len(self.items) + 1))

        if self.items[key] is None:
            json = self._items[key]
            self.items[key] = create_attribute(self._contains, json)

        return self.items[key]

    def __getattr__(self, item):
        try:
            indexes = self._construct_indexes()
            for key, value in indexes.items():
                object.__setattr__(self, key, value)
            return indexes[item]
        except KeyError as e:
            raise AttributeError(e)

    def __add__(self, other):
        return self.__class__(*self, *other)

    __radd__ = __add__

    def __delattr__(self, item):
        raise NotImplementedError

    def __setattr__(self, key, value):
        raise NotImplementedError

    def _construct_indexes(self):
        id_index = {}
        trade_id_index = {}
        instrument_index = {}
        for index, json_model in enumerate(self._items):
            # json_model is either a json_dict. Or a Model object
            # constructed from the json_dict
            try:
                key = json_model.get('id', None)
                if key is not None:
                    id_index.update({str(key): index})


                key = json_model.get('trade_id', json_model.get('tradeID'))
                if key is not None:
                    trade_id_index.setdefault(str(key), []).append(index)

                key = json_model.get('instrument', json_model.get('name', None))
                if key is not None:
                    instrument_index.setdefault(key, []).append(index)
            except AttributeError:
                break

        return dict(
            _id_index=id_index,
            _trade_id_index=trade_id_index,
            _instrument_index=instrument_index
        )

    def get_id(self, id_, default=None):
        """Return the objects in the array where the
        `object.id` attribute matches the passed id
        else return the default"""
        try:
            return self[self._id_index[str(id_)]]
        except KeyError:
            pass
        return default

    def get_trade_id(self, id_, default=None, *, type=None):
        """Return the first object in the array where the
        `object.trade_id` attribute matches the passed id
        else return the default

        Args:
            id_: The trade_id to get.
            default: The default value to return if the id_ cannot be found
            type: The returned objects OANDA type. eg. 'STOP_LOSS'
                not to be confused the `type(instance)`
        """
        try:
            if type is not None:
                for obj in (self[idx] for idx in self._trade_id_index[str(id_)]):
                    if getattr(obj, 'type', None) == type:
                        return obj
                return default

            return self[self._trade_id_index[str(id_)][0]]
        except KeyError:
            pass
        return default

    def get_trade_ids(self, id_, default=None):
        """Return the objects in the array where the
        `object.trade_id` attribute matches the passed id
        else return the default"""
        try:
            return self.__class__(*[self[idx] for idx in self._trade_id_index[str(id_)]])
        except KeyError:
            pass
        return default


    def get_instrument(self, instrument, default=None):
        """Return the first object in the array where
        where the `object.instrument` matches the passed instrument
        else return default"""
        try:
            return self[self._instrument_index[instrument][0]]
        except KeyError:
            pass
        return default

    def get_instruments(self, instrument, default=None):
        """Return all the objects in the array where the
        `object.instrument` attribute matches the passed instrument
        else return the default"""
        try:
            return self.__class__(*[self[idx] for idx in self._instrument_index[instrument]])
        except KeyError:
            pass
        return default

    def dataframe(self, json=False, datetime_format=None):
        """Create a pandas.Dataframe

        Args:
            json: True, DataFrame columns will have the JSON representation,
                False, DataFrame columns will have the object attribute representation

            datetime_format: 'UNIX' or 'RFC3339'
        """
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
        elif isinstance(data, InstrumentName):
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
    except (TypeError, ValueError, UnknownKeywordArgument):
        # This error handling is required when there is no
        # schema available to parse the data. Typically
        # when an error code has been returned
        # A none value should be returned if this is the case
        if typ is not None:
            msg = f'Could not create {typ}. DATA: {data}, TYPE: {type(data)}'
            logger.error(msg)
            raise InstantiationFailure(msg)
    else:
        return result
