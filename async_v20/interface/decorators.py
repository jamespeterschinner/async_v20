"""Module that defines the behaviour of the exposed client method calls by using decorators
"""
from functools import wraps
from inspect import signature

from .helpers import create_request_kwargs
from .parser import parse_response
from ..definitions.helpers import create_doc_signature

async def _serial_request_async_generator():
    self, request_args, endpoint = yield
    while True:
        request = await self.request.asend(None)
        response = request(**request_args)
        self, request_args, endpoint = yield await parse_response(self, response, endpoint)


def endpoint(endpoint, serial=False):
    """Define a method call to be exposed to the user"""

    if serial:
        serial_request = _serial_request_async_generator()
        endpoint.initialized = False

    def wrapper(method):
        """Take the wrapped method and return a coroutine"""

        method.endpoint = endpoint

        sig = signature(method)

        method.__doc__ = create_doc_signature(method, sig)

        @wraps(method)
        async def serial_wrap(self, *args, **kwargs):
            try:
                await self.initialize()
            except ValueError:
                pass

            if not endpoint.initialized:
                await serial_request.asend(None)
                endpoint.initialized = True

            request_args = create_request_kwargs(self, endpoint, sig, *args, **kwargs)

            return await serial_request.asend((self, request_args, endpoint))

        @wraps(method)
        async def parallel_wrap(self, *args, **kwargs):
            try:
                await self.initialize()
            except ValueError:
                pass

            request_args = create_request_kwargs(self, endpoint, sig, *args, **kwargs)

            request = await self.request.asend(None)

            response = request(**request_args)

            return await parse_response(self, response, endpoint)

        serial_wrap.__signature__ = sig

        parallel_wrap.__signature__ = sig

        return {True: serial_wrap, False: parallel_wrap}[serial]

    return wrapper


def add_signature(class_obj):
    sig = signature(class_obj.__new__)

    def wrapper(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            return func(*args, **kwargs)

        wrap.__signature__ = sig
        wrap.__doc__ = create_doc_signature(func, sig)
        return wrap

    return wrapper
