"""Module that defines the behaviour of the exposed client method calls by using decorators
"""
import logging
from functools import wraps
from inspect import signature

from .helpers import create_request_kwargs, construct_arguments
from .parser import parse_response
from ..definitions.helpers import create_doc_signature
from ..endpoints.annotations import SinceTransactionID
from ..exceptions import ResponseTimeout
from asyncio import TimeoutError as AsyncTimeOutError
logger = logging.getLogger(__name__)


def endpoint(endpoint, rest=False, initialize_required=True):
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
                await self.initialize(method.__name__)
            elif not self.session:
                await self.initialize_session()

            logger.info('%s(args=%s, kwargs=%s)', method.__name__, args, kwargs)
            arguments = construct_arguments(self, sig, *args, **kwargs)

            enable_rest = False
            if rest and arguments[SinceTransactionID] == self.default_parameters[SinceTransactionID]:
                enable_rest = True

            request_kwargs = create_request_kwargs(self, endpoint, arguments)

            await self._request_limiter()

            if self.debug:
                logger.debug('client.session.request(kwargs=%s)', request_kwargs)
            response = self.session.request(**request_kwargs)

            return await parse_response(self, response, endpoint, enable_rest, method.__name__)


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
