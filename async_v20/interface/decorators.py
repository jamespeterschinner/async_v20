"""Module that defines the behaviour of the exposed client method calls by using decorators"""

from functools import wraps
from inspect import signature

from .helpers import make_args_optional
from .helpers import request
from .helpers import serial_request_async_generator


def endpoint(endpoint, serial=False):
    """Define a method call to be exposed to the user"""

    if serial:
        serial_request = serial_request_async_generator()
        endpoint.initialized = False

    def wrapper(method):
        """Take the wrapped method and return a coroutine"""

        method.endpoint = True

        sig = make_args_optional(signature(method))

        @wraps(method)
        async def serial_wrap(self, *args, **kwargs):
            if not endpoint.initialized:
                await serial_request.asend(None)
                endpoint.initialized = True

            return await serial_request.asend((self, endpoint, sig, args, kwargs))

        @wraps(method)
        async def parallel_wrap(self, *args, **kwargs):
            return await request(self, endpoint, sig, *args, **kwargs)

        return {True: serial_wrap, False: parallel_wrap}[serial]

    return wrapper


def add_signature(class_obj):
    sig = signature(class_obj.__init__)

    def wrapper(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            return func(*args, **kwargs)

        wrap.__signature__ = sig
        return wrap

    return wrapper
