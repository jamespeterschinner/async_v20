from inspect import signature, Signature, _empty
from .helpers import _create_body
from .helpers import _parse_response
from .helpers import _create_params
from .helpers import _create_headers
from .helpers import _create_path
from functools import wraps
from ..definitions.helpers import IndexDict

def endpoint(endpoint):
    header_args = endpoint.header_args()
    query_args = endpoint.query_args()
    path_args = endpoint.path_args()

    def wrapper(method):
        sig = signature(method)
        # TODO remove self from sig
        sig = Signature([param.replace(default=None)
                         if param.default == _empty
                         else param
                         for param in sig.parameters.values()])

        @wraps(method)
        async def wrap(self, *args, **kwargs):
            bound = sig.bind(*args, **kwargs)
            arguments = bound.arguments
            json_body = await _create_body(self, endpoint.request_schema, arguments)
            headers = await _create_headers(self, header_args, arguments)
            path = await _create_path(self, endpoint.path, path_args, arguments)
            parameters = await _create_params(self, query_args, arguments)

            # TODO add json data to request do iu need to await this?
            response = self.session.request(method=endpoint.method,
                                            path=path,
                                            headers=headers,
                                            parameters=parameters)

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
