from async_v20.definitions.attributes import *

def test_keys_in_json_attributes_are_lowercase():
    assert all(str.islower(i) for i in json_attributes)

def test_values_in_instance_attributes_are_lowercase():
    assert all(str.islower(i) for i in instance_attributes.values())

def test_every_value_in_instance_attributes_is_a_key_in_json_attributes():
    assert all(i in json_attributes for i in instance_attributes.values())