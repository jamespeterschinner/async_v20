"""Module that defines the behaviour of the exposed client method calls by using decorators
"""
from concurrent.futures._base import TimeoutError as ConcurrentTimeoutError
from functools import wraps
from inspect import signature

from .helpers import create_request_kwargs, construct_arguments
from .parser import parse_response
from ..definitions.helpers import create_doc_signature

from ..endpoints.annotations import SinceTransactionID


def endpoint(endpoint, rest=False, initialization_step=False, initialize_required=True):
    """Define a method call to be exposed to the user"""


    def wrapper(method):
        """Take the wrapped method and return a coroutine"""

        method.endpoint = endpoint

        method.initialize_required = initialize_required

        sig = signature(method)

        method.__doc__ = create_doc_signature(method, sig)

        @wraps(method)
        async def wrap(self, *args, **kwargs):
            if initialize_required:
                await self.initialize(initialization_step)
            elif not self.session:
                await self.initialize_session()

            arguments = construct_arguments(self, sig, *args, **kwargs)

            enable_rest = False
            if rest and arguments[SinceTransactionID] == self.default_parameters[SinceTransactionID]:
                enable_rest = True


            request_args = create_request_kwargs(self, endpoint, arguments)

            await self._request_limiter()

            response = self.session.request(**request_args)

            try:
                return await parse_response(self, response, endpoint, enable_rest)
            except ConcurrentTimeoutError:
                raise TimeoutError(f'{method.__name__} took longer than {self.rest_timeout} seconds')

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
