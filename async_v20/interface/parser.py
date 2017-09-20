import json

from ..endpoints.annotations import LastTransactionID
from ..endpoints.other_responses import other_responses
from ..helpers import sleep


class UnableToBuildObject(Exception):
    pass


async def create_objects(schema, key, objs):
    await sleep()
    typ = schema.get(key)

    async def build(obj):
        await sleep()
        try:
            obj = typ(**obj)
        except AttributeError:
            raise UnableToBuildObject(typ.__name__)
        finally:
            return obj

    if isinstance(objs, list):
        objs = [await build(obj) for obj in objs]

    if isinstance(objs, dict):
        objs = await build(objs)

    return key, objs  # change here to typ in you'd like the class def as the key


async def _rest_response(self, response, endpoint):
    async with response as resp:
        status = resp.status
        headers = resp.raw_headers
        json_body = await resp.json()

    print(f'RESPONSE STATUS: {status}')

    # Update client headers. Such as lastTransactionID and the like
    for key, value in headers:
        self.default_parameters['key'] = value

    last_transaction_id = json_body.get('lastTransactionID', None)
    if last_transaction_id:
        self.default_parameters.update({LastTransactionID: last_transaction_id})

    try:
        schema = endpoint.responses[status]  # look up the template to process the data
    except KeyError:
        schema = other_responses[status]  # See if a response status is an error code

    async def create(json_data, schema):
        return dict([await create_objects(schema, json_object, object_field)
                for json_object, object_field in json_data.items()])

    return await create(json_body, schema)


async def _stream_parser(self, response, endpoint):
    print('STREAMING')
    async with response as resp:
        response_schema = endpoint.responses[resp.status]
        async for data in resp.content.iter_chunked(self.stream_chunk_size):
            lines = data.split()
            for line in lines:
                body = json.loads(line)
                key = body.pop('type')
                yield dict(await create_objects(response_schema, key, body))


async def parse_response(self, response, endpoint):
    if endpoint.host == 'REST':
        result = await _rest_response(self, response, endpoint)
    else:
        result = _stream_parser(self, response, endpoint)
    return result
