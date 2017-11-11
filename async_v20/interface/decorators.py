"""Module that defines the behaviour of the exposed client method calls by using decorators
"""
from functools import wraps
from inspect import signature

from .helpers import create_request_kwargs
from .parser import parse_response
from ..definitions.helpers import create_doc_signature

def endpoint(endpoint):
    """Define a method call to be exposed to the user"""

    def wrapper(method):
        """Take the wrapped method and return a coroutine"""

        method.endpoint = endpoint

        sig = signature(method)

        method.__doc__ = create_doc_signature(method, sig)

        @wraps(method)
        async def wrap(self, *args, **kwargs):
            try:
                await self.initialize()
            except ValueError:
                pass

            predicate = kwargs.pop('predicate', lambda x: x)

            request_args = create_request_kwargs(self, endpoint, sig, *args, **kwargs)

            await self.request_limiter()

            response = self.session.request(**request_args)

            return await parse_response(self, response, endpoint, predicate)

        wrap.__signature__ = sig

        return wrap

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
