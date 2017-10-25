from functools import wraps
import inspect

from async_v20.definitions.helpers import flatten_dict

def order_dict(obj):
    if isinstance(obj, dict):
        return sorted((k, order_dict(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(order_dict(x) for x in obj)
    else:
        return obj
