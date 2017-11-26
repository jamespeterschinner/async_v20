"""Module that defines the behaviour of the exposed client method calls by using decorators
"""
from concurrent.futures._base import TimeoutError as ConcurrentTimeoutError
from functools import wraps
from inspect import signature

from .helpers import create_request_kwargs
from .parser import parse_response
from ..definitions.helpers import create_doc_signature


def endpoint(endpoint, initialization_step=False):
    """Define a method call to be exposed to the user"""

    def wrapper(method):
        """Take the wrapped method and return a coroutine"""

        method.endpoint = endpoint

        sig = signature(method)

        method.__doc__ = create_doc_signature(method, sig)


        @wraps(method)
        async def wrap(self, *args, **kwargs):
            await self.initialize(initialization_step)

            request_args = create_request_kwargs(self, endpoint, sig, *args, **kwargs)

            await self._request_limiter()
            print('SENDING REQUEST WITH THESE ARGUMENTS:\n', request_args)
            response = self.session.request(**request_args)

            try:
                return await parse_response(self, response, endpoint)
            except ConcurrentTimeoutError:
                raise TimeoutError(f'{method.__name__} to longer than {self.rest_timeout} seconds')

        wrap.__signature__ = sig

        return wrap

    return wrapper


def shortcut(func):
    sig = signature(func)

    @wraps(func)
    def wrap(self, *args, **kwargs):
        return func(self, *args, **kwargs)

    wrap.shortcut = True
    wrap.__signature__ = sig
    wrap.__doc__ = create_doc_signature(wrap, sig)
    return wrap
