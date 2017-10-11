from functools import partial
from inspect import Signature, _empty

from ..helpers import sleep


def make_args_optional(signature):
    sig = Signature([param.replace(default=None)
                     if param.default == _empty
                     else param
                     for param in signature.parameters.values()][1:])  # Slice drops off 'self'
    return sig


def create_annotation_lookup(signature, bound_arguments):
    """Combine the signatures annotations with bound arguments to create a lookup dict
    for subsequent functions to identify arguments they need to use"""
    annotations_lookup = {param.name: param.annotation for param in signature.parameters.values()}
    return {annotations_lookup[name]: value for name, value in bound_arguments.items()}


def _arguments(endpoint, param_location):
    return ((parameter['name'], parameter['type']) for parameter in endpoint.parameters if
            parameter['located'] == param_location)


async def _create_request_params(self, endpoint, arguments: dict, param_location: str):
    possible_arguments = _arguments(endpoint, param_location)

    async def lookup(typ):
        await sleep()
        result = None
        try:
            result = arguments[typ]
        except KeyError:
            try:
                result = self.default_parameters[typ]
            except TypeError:
                # TODO create exception module
                raise Exception('No default parameters provided')
            except KeyError:
                print(f"WARNING: missing {typ.__name__} in {param_location}")
                pass  # TODO: This Should raise a warning that not all header parameters were created
        return result

    parameters = ((name, await lookup(typ)) for name, typ in possible_arguments)
    return {name: value async for name, value in parameters if value}


async def create_url(self, endpoint, arguments):
    endpoint_path = await endpoint.path(arguments, default=self.default_parameters)
    host = self.hosts[endpoint.host]
    return host(path=endpoint_path)


def create_body(request_schema, arguments):
    # Reverse the request schema to allow for lookups
    lookup = {value: key for key, value in request_schema.items()}

    def dumps():
        """Iterate over the arguments returning json_dicts of matching objects"""
        for argument in arguments.values():
            try:
                key = lookup.get(argument._derived, None)
            except AttributeError:
                continue
            else:
                if key:
                    yield (key, argument.json_dict())

    return dict([json_data for json_data in dumps()])


header_params = partial(_create_request_params, param_location='header')

query_params = partial(_create_request_params, param_location='query')


async def create_request_kwargs(self, endpoint, sig, *args, **kwargs):
    """Create a coroutine to construct and parse a request"""
    arguments = sig.bind(*args, **kwargs).arguments
    arguments = create_annotation_lookup(sig, arguments)

    json = create_body(endpoint.request_schema, arguments)

    headers = await header_params(self, endpoint, arguments)
    url = await create_url(self, endpoint, arguments)
    parameters = await query_params(self, endpoint, arguments)

    request_kwargs = {
        'method': endpoint.method,
        'url': url,
        'headers': headers,
        'params': parameters,
        'json': json,
    }

    if endpoint.host == 'STREAM':
        request_kwargs.update({'timeout': 0})

    return request_kwargs
