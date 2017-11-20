from inspect import _empty
from itertools import starmap, chain
from pandas import Timestamp, Timedelta


def domain_check(value, example=None, possible_values=None):
    if example:
        try:
            assert len(example) == len(value)
        except (AssertionError, TypeError):
            msg = f'{value} does not match length of example {example}'
            raise ValueError(msg)

    if possible_values:
        try:
            assert value in possible_values
        except AssertionError:
            possible_values = ', '.join(possible_values)
            msg = f'{value} must be in {possible_values}. Possible values are {possible_values}'
            raise ValueError(msg)

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

def time_to_time_stamp(time):
    """Convert a RFC3339 or UNIX timestamp to pandas Timestamp"""
    try:
        # This will work with RFC3339
        time_stamp = Timestamp(time)
    except ValueError:
        # This will work with UNIX
        nanoseconds = lambda: {'nanoseconds': int(time[-3:])}
        time_stamp =  (Timestamp.utcfromtimestamp(float(time)) +
                       Timedelta(**nanoseconds())).tz_localize('UTC')

    return time_stamp

def create_doc_signature(obj, sig):
    names = list(sig.parameters.keys())
    annotations = list(
        map(lambda x: '' if x.annotation == _empty else ': ' + x.annotation.__name__, sig.parameters.values()))
    defaults = list(map(lambda x: '' if x.default == _empty else '=' + str(x.default), sig.parameters.values()))
    arguments = ', '.join(''.join(argument) for argument in zip(names, annotations, defaults))
    return f'{obj.__name__}({arguments})\n{obj.__doc__}'
