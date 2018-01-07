import logging
from inspect import _empty
from itertools import starmap, chain

from .attributes import instance_attributes
from ..exceptions import InvalidValue
from ..exceptions import UnknownValue
from ..exceptions import IncompatibleValue

logger = logging.getLogger(__name__)

def check_conflicting_arguments(self, kwargs, preset_values):
    for argument, preset_value in preset_values.items():
        value = kwargs.pop(argument, None)
        if value is not None and value != preset_value:
            msg = f'CLASS {self.__class__.__name__}.{argument}' \
                  f' MUST == {preset_value} NOT {value}'
            logger.error(msg)
            raise IncompatibleValue(msg)

def json_to_instance_attributes(self, kwargs, template):
    for name, value in kwargs.items():
        try:
            yield instance_attributes[name], value
        except KeyError:
            possible_arguments = ', '.join(attr for attr in template)
            msg = f'`{name}` is not a valid keyword argument. ' \
                  f'Possible arguments for class {self.__class__.__name__} ' \
                  f'include: {possible_arguments}'
            logger.error(msg)
            raise UnknownValue(msg)


def create_indexed_lookup(array, one_to_many):
    id_index = {}
    instrument_index = {}

    def construct_indexes():
        for index, obj in enumerate(array):

            key = str(getattr(obj, 'id', getattr(obj, 'trade_id', None)))
            if key is not None:
                id_index.update({key: index})

            key = getattr(obj, 'instrument', getattr(obj, 'name', None))
            if key is not None:
                if one_to_many:
                    instrument_index.setdefault(key, []).append(index)
                    continue
                instrument_index.update({key: index})

    def get_id(id_, default=None):
        if not id_index:
            construct_indexes()
        try:
            return array[id_index[str(id_)]]
        except KeyError:
            return default

    def get_instruments(instrument, default=None):
        # ArrayPosition can only have a One to One relationship between an instrument
        # and a Position. Though ArrayTrades and others can have a Many to One relationship
        if not instrument_index:
            construct_indexes()
        try:
            return type(array)(*(array[index] for index in instrument_index[instrument]))
        except KeyError:
            return default

    def get_instrument(instrument, default=None):
        if not instrument_index:
            construct_indexes()
        try:
            return array[instrument_index[instrument]]
        except KeyError:
            return default

    array.get_id = get_id
    if one_to_many:
        array.get_instruments = get_instruments
    else:
        array.get_instrument = get_instrument
    return array


def domain_check(value, example=None, possible_values=None):
    if example:
        if not len(str(example)) == len(str(value)):
            msg = f'{value} does not match length of example {example}'
            logger.error(msg)
            raise InvalidValue(msg)

    if possible_values:
        if not value in possible_values:
            possible_values = ', '.join(possible_values)
            msg = f'{value} must be in {possible_values}. Possible values are {possible_values}'
            logger.error(msg)
            raise InvalidValue(msg)

    return True


def flatten_dict(dictionary, delimiter='_'):
    """Flatten a nested dictionary structure"""

    def unpack(parent_key, parent_value):
        """Unpack one level of nesting in a dictionary"""
        try:
            items = parent_value.items()
        except AttributeError:
            # parent_value was not a dict, no need to flatten
            yield (parent_key, parent_value)
        else:
            for key, value in items:
                yield (parent_key + delimiter + key, value)

    while True:
        # Keep unpacking the dictionary until all value's are not dictionary's
        dictionary = dict(chain.from_iterable(starmap(unpack, dictionary.items())))
        if not any(isinstance(value, dict) for value in dictionary.values()):
            break

    return dictionary


def create_doc_signature(obj, sig):
    names = list(sig.parameters.keys())
    annotations = list(
        map(lambda x: '' if x.annotation == _empty else ': ' + x.annotation.__name__, sig.parameters.values()))
    defaults = list(map(lambda x: '' if x.default == _empty else '=' + str(x.default), sig.parameters.values()))
    arguments = ', '.join(''.join(argument) for argument in zip(names, annotations, defaults))
    return f'{obj.__name__}({arguments})\n{obj.__doc__}'
