from functools import wraps
from itertools import chain, starmap
import inspect

async def _flatten_dict(dictionary):
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
                yield (key, value)

    # Put each key into a tuple to initiate building a tuple of subkeys
    dictionary = {key: value async for key, value in dictionary.items()}

    # Keep unpacking the dictionary until all value's are not dictionary's
    dictionary = dict(chain.from_iterable(starmap(unpack, dictionary.items())))
    return dictionary

def return_kwargs(func):
    """Cause the wrapped function to return a dict of keyword arguments
    """
    @wraps(func)
    async def wrap(*args, **kwargs):
        bound_arguments = inspect.signature(func).bind(*args, **kwargs)
        bound_arguments.apply_defaults()
        return  await _flatten_dict(dict(bound_arguments.arguments))
    return wrap