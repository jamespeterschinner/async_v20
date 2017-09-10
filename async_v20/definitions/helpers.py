from itertools import chain, starmap

from async_v20.helpers import sleep


async def flatten_dict(dictionary):
    """Flatten a nested dictionary structure"""

    async def unpack(parent_key, parent_value):
        """Unpack one level of nesting in a dictionary"""
        await sleep()
        if isinstance(parent_value, (dict, list)):
            try:
                items = parent_value.items()
            except AttributeError:
                try:
                    items = chain(parent_value)
                except TypeError:
                    # parent value was not iterable or a dict
                    return (parent_key, parent_value)
                else:
                    for index, value in enumerate(items):
                        # yield (parent_key + '_' + str(index), value)
                        return (parent_key , value)
            else:
                for key, value in items:
                    return (parent_key + '_' + key, value)
        else:
            return (parent_key, parent_value)

    # Put each key into a tuple to initiate building a tuple of subkeys
    dictionary = {key: value for key, value in dictionary.items()}

    while True:
        # Keep unpacking the dictionary until all value's are not dictionary's
        dictionary = dict(chain.from_iterable(await starmap(unpack, dictionary.items())))
        if not any(isinstance(value, dict) for value in dictionary.values()):
            break

    return dictionary