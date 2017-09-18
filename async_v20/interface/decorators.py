from inspect import signature
from .helpers import _make_args_optional
from .helpers import _create_annotation_lookup
from .helpers import _create_body
from .helpers import _create_request_params
from .helpers import _create_url
from .parser import _parse_response
from functools import wraps

def endpoint(endpoint):

    def wrapper(method):
        sig = _make_args_optional(signature(method))

        @wraps(method)
        async def wrap(self, *args, **kwargs):

            arguments = sig.bind(*args, **kwargs).arguments
            arguments = await _create_annotation_lookup(sig, arguments)


            # json_body = await _create_body(self, endpoint.request_schema, arguments)
            headers = await _create_request_params(self, endpoint, arguments, 'header')
            url = await _create_url(self, endpoint, arguments)
            parameters = await _create_request_params(self, endpoint, arguments, 'query')

            print(url)
            print(headers)
            # TODO add json data to request?
            response = self.session.request(method=endpoint.method,
                                            url=url,
                                            headers=headers,
                                            params=parameters)

            return await _parse_response(self, response, endpoint)

        return wrap

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
