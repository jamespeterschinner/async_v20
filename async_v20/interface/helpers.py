from functools import partial
from inspect import Signature, _empty

from async_v20.helpers import sleep


def make_args_optional(signature):
    sig = Signature([param.replace(default=None)
                     if param.default == _empty
                     else param
                     for param in signature.parameters.values()][1:])  # Slice drops off 'self'
    return sig


async def create_annotation_lookup(signature, bound_arguments):
    async def wait(x):
        await sleep()
        return x

    annotations_lookup = {param.name: param.annotation for param in signature.parameters.values()}
    return {annotations_lookup[name]: await wait(value) for name, value in bound_arguments.items()}


async def _create_request_params(self, endpoint, arguments: dict, param_location: str):
    possible_arguments = ((parameter['name'], parameter['type']) for parameter in endpoint.parameters if
                          parameter['located'] == param_location)

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


async def create_url(self, endpoint, arguments, stream=False):
    endpoint_path = await endpoint.path(arguments, default=self.default_parameters)
    host = self.hosts[endpoint.host]
    return host(path=endpoint_path)


header_params = partial(_create_request_params, param_location='header')

query_params = partial(_create_request_params, param_location='query')


async def create_body(request_schema, arguments):
    # Reverse the request schema to allow for lookups
    lookup = {value: key for key, value in request_schema.items()}

    async def dumps(arguments):
        """Iterate over the arguments returning json_dicts of matching objects"""
        for argument in arguments.values():
            await sleep()
            try:
                key = lookup.get(argument._derived, None)
            except AttributeError:
                continue
            else:
                if key:
                    yield (key, await argument.json_dict())


    return dict([json_data async for json_data in dumps(arguments)])
