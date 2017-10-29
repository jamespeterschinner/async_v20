from async_v20.definitions.helpers import flatten_dict

nested_dict = {'a': {'b': 2, 'c': {'d': 4}}}
flattened_dict = {'a_b': 2, 'a_c_d': 4}


def test_flatten_dict():
    result = flatten_dict(nested_dict, delimiter='_')
    assert result == flattened_dict
