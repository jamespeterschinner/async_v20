import json

from ..endpoints.annotations import LastTransactionID
from ..endpoints.other_responses import other_responses
from ..helpers import sleep


async def create_objects(schema, key, objs):
    await sleep()
    typ = schema.get(key)
    print(f'TYPE: {typ}')

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

    if isinstance(objs, dict):
        objs = await build(objs)

    return key, objs  # change here to typ in you'd like the class def as the key


async def _rest_response(self, response, endpoint):
    async with response as resp:
        status = resp.status
        headers = resp.raw_headers
        body = await resp.json()

    print(f'RESPONSE STATUS: {status}')

    # Update client headers. Such as lastTransactionID and the like
    for key, value in headers:
        self.default_parameters['key'] = value

    try:
        response_schema = endpoint.responses[status]  # look up the template to process the data
    except KeyError:
        response_schema = other_responses[status]  # See if a response status is an error code

    class Response(object):
        """Object to assign attributes to"""

        @classmethod
        async def create(cls, json_data):
            class_instance = cls()
            for json_key, json_data in json_data.items():
                attr, response_value = await create_objects(response_schema, json_key, json_data)
                setattr(class_instance, attr, response_value)
                if attr == 'lastTransactionID':  # Keep track of the last transaction id
                    self.default_parameters.update({LastTransactionID: response_value})
            return class_instance

    return await Response.create(body)


async def _stream_parser(self, response, endpoint):
    print('STREAMING')
    async with response as resp:
        response_schema = endpoint.responses[resp.status]
        async for data in resp.content.iter_chunked(self.stream_chunk_size):
            lines = data.split()
            for line in lines:
                body = json.loads(line)
                key = body.pop('type')
                print(await create_objects(response_schema, key, body))


async def _parse_response(self, response, endpoint):
    if endpoint.host == 'REST':
        result = await _rest_response(self, response, endpoint)
    else:
        result = await _stream_parser(self, response, endpoint)
    return result
