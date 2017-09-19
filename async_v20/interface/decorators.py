"""Module that defines the behaviour of the exposed client method calls by using decorators"""

from functools import wraps
from inspect import signature

from .helpers import create_annotation_lookup
from .helpers import create_body
from .helpers import create_request_params
from .helpers import create_url
from .helpers import make_args_optional
from .parser import parse_response


async def request(self, endpoint, sig, *args, **kwargs):
    """Create a coroutine to construct and parse a request"""
    arguments = sig.bind(*args, **kwargs).arguments
    arguments = await create_annotation_lookup(sig, arguments)

    json = await create_body(endpoint.request_schema, arguments)
    headers = await create_request_params(self, endpoint, arguments, 'header')
    url = await create_url(self, endpoint, arguments)
    parameters = await create_request_params(self, endpoint, arguments, 'query')

    print(url)
    print(headers)
    # TODO test json data being sent correctly
    response = self.session.request(method=endpoint.method,
                                    url=url,
                                    headers=headers,
                                    params=parameters,
                                    json=json)

    return await parse_response(self, response, endpoint)


async def serial_request_async_generator():
    self, endpoint, sig, args, kwargs = yield
    while True:
        self, endpoint, sig, args, kwargs = yield await request(self, endpoint, sig, *args, **kwargs)


def endpoint(endpoint, serial=False):
    """Define a method call to be exposed to the user"""

    if serial:
        serial_request = serial_request_async_generator()
        endpoint.initialized = False

    def wrapper(method):
        """Take the wrapped method and return a coroutine"""
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
