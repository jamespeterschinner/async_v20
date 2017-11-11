"""Module that defines the behaviour of the exposed client method calls by using decorators
"""
from functools import wraps
from inspect import signature

from .helpers import create_request_kwargs
from .parser import parse_response
from ..definitions.helpers import create_doc_signature


async def _serial_request_async_generator():
    self, request_args, endpoint, predicate = yield
    while True:
        request = await self.request.asend(None)
        response = request(**request_args)
        self, request_args, endpoint, predicate = yield await parse_response(self, response, endpoint, predicate)


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

            predicate = kwargs.pop('predicate', lambda x: x)

            request_args = create_request_kwargs(self, endpoint, sig, *args, **kwargs)

            return await serial_request.asend((self, request_args, endpoint, predicate))

        @wraps(method)
        async def parallel_wrap(self, *args, **kwargs):

            # Unlike serial wrap,
            # This can never be called during initialisation.
            # Because initialisation only uses endpoints
            # that require serial behaviour.
            await self.initialize()

            predicate = kwargs.pop('predicate', lambda x: x)

            request_args = create_request_kwargs(self, endpoint, sig, *args, **kwargs)

            request = await self.request.asend(None)

            response = request(**request_args)

            return await parse_response(self, response, endpoint, predicate)

        serial_wrap.__signature__ = sig

        parallel_wrap.__signature__ = sig

        return {True: serial_wrap, False: parallel_wrap}[serial]

    return wrapper


def add_signature(obj):
    sig = signature(obj.__new__)

    def wrapper(func):
        @wraps(func)
        def wrap(self, *args, **kwargs):
            return func(self, *args, **kwargs)

        wrap.shortcut = True
        wrap.__signature__ = sig
        wrap.__doc__ = create_doc_signature(wrap, sig)
        return wrap

    return wrapper
