"""Module that defines the behaviour of the exposed client method calls by using decorators"""

from functools import wraps
from inspect import signature

from .helpers import create_request_kwargs
from .helpers import make_args_optional
from .parser import parse_response


async def serial_request_async_generator():
    self, endpoint, sig, args, kwargs = yield
    while True:
        request_kwargs = await create_request_kwargs(self, endpoint, sig, *args, **kwargs)
        print(request_kwargs)
        response = self.session.request(**request_kwargs)
        self, endpoint, sig, args, kwargs = yield await parse_response(self, response, endpoint)


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
            await self.initialize()
            if not endpoint.initialized:
                await serial_request.asend(None)
                endpoint.initialized = True

            return await serial_request.asend((self, endpoint, sig, args, kwargs))

        @wraps(method)
        async def parallel_wrap(self, *args, **kwargs):
            await self.initialize()
            request_kwargs = await create_request_kwargs(self, endpoint, sig, *args, **kwargs)

            response = self.session.request(**request_kwargs)

            return await parse_response(self, response, endpoint)

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
