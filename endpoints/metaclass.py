"""Metaclass used in this package"""


# Small metaclass that simply returns
# any value passed to it though the slice syntax
# This is done purely as documentation.
class JSONArray(type):
    def __getitem__(cls, value):
        return value


# This array class indicates to the reader of code that
# this particular JSON value is expected to be an Array
class Array(metaclass=JSONArray):
    pass
