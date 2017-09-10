from async_v20.helpers import sleep

async def _create_body(self, request_schema, kwargs):
    # We first create a look up table with the class as the key.
    # This allows for the convenience function to have descriptive args
    lookup = {type(value): value for value in kwargs.values()}
    async def dumps(obj):
        await sleep()
        obj =  lookup.get(obj, None)
    return {key: await dumps(obj) for key, obj in request_schema.items()}

async def _create_headers(self, header_args, kwargs):
    async def _resolver(arg):
        await sleep()
        value = kwargs.pop('arg', None)
        if not value:
            value = self.default_parameters.get(arg, None)  # TODO find out if this default value will cause an issue
        return arg, value

    return dict([await _resolver(arg) for arg in header_args])


async def _create_path(self, endpoint, path_args, kwargs):
    async def _resolver(arg):
        await sleep()
        value = kwargs.pop(arg, None)
        # look for default value in client session
        if not value:
            value = getattr(self, arg, None)
        return arg, value
    args = [await _resolver(arg) for arg in path_args]
    return endpoint.path(**dict([arg for arg in args if all(arg)]))


async def _create_params(self, query_args, kwargs):
    async def _resolver(arg):
        await sleep()
        value = kwargs.pop('arg', None)
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
    response_schema = endpoint.responses[status] # look up the template to process the data

    async def create(key, objs):
        await sleep()
        typ = response_schema.get(key)

        async def build(obj):
            await sleep()
            try:
                obj = await typ.from_dict(obj)
            except AttributeError:
                pass
            finally:
                return obj

        if isinstance(objs, list):
            objs = [await build(obj) for obj in objs]

        return key, objs  # change here to typ in you'd like the class def as the key

    return dict([await create(key, objs) for key, objs in body.items()])


