from async_v20.helpers import sleep
from yarl import URL
from inspect import Signature, _empty

def _make_args_optional(signature):
    sig = Signature([param.replace(default=None)
                     if param.default == _empty
                     else param
                     for param in signature.parameters.values()][1:])  # Slice drops off 'self'
    return sig

async def _create_annotation_lookup(signature, bound_arguments):
    async def wait(x):
        await sleep()
        return x

    annotations_lookup = {param.name: param.annotation for param in signature.parameters.values()}
    return {annotations_lookup[name]: await wait(value)  for name, value in bound_arguments.items()}


async def _create_body(self, request_schema, arguments):
    # We first create a look up table with the class as the key.
    # This allows for the convenience function to have descriptive args
    lookup = {type(value): value for value in arguments.values()}

    async def dumps(obj):
        await sleep()
        obj = lookup.get(obj, None)

    return {key: await dumps(obj) for key, obj in request_schema.items()}


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
            except KeyError:
                print(f"WARNING: missing {typ.__name__} in {param_location}")
                pass  # TODO: This Should raise a warning that not all header parameters were created
        return result

    parameters = ((name, await lookup(typ)) for name, typ in possible_arguments)
    return {name: value async for name, value in parameters if value}


async def _create_url(self, path, arguments):
    return URL.build(scheme='https', host=self.host, path=await path(arguments))


async def _create_params(self, query_args, arguments):
    async def _resolver(arg):
        await sleep()
        value = arguments.pop('arg', None)
        return arg, value

    params = [await _resolver(arg) for arg in query_args]
    return dict([param for param in params if all(param)])


async def _parse_response(self, response, endpoint):
    async with response as resp:
        status = resp.status
        headers = resp.raw_headers
        body = await resp.json()

    # Update client headers. Such as lastTransactionID and the like
    for key, value in headers:
        self.default_parameters['key'] = value
    print(status)
    print(type(status))
    response_schema = endpoint.responses[status]  # look up the template to process the data

    async def create(key, objs):
        await sleep()
        typ = response_schema.get(key)
        async def build(obj):
            await sleep()
            try:
                obj = typ(**obj)
            except AttributeError:
                pass
            finally:
                return obj

        if isinstance(objs, list):
            objs = [await build(obj) for obj in objs]

        return key, objs  # change here to typ in you'd like the class def as the key

    return dict([await create(key, objs) for key, objs in body.items()])
