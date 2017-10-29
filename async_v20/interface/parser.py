import ujson as json

from .response import Response
from ..definitions.base import create_attribute
from ..endpoints.annotations import LastTransactionID
from ..endpoints.other_responses import other_responses


def _create_objects(schema, key, data):
    typ = schema.get(key)
    return key, create_attribute(typ, data)

async def _create_response(json_body, schema):
    return Response([_create_objects(schema, json_object, object_field)
                 for json_object, object_field in json_body.items()])

async def _rest_response(self, response, endpoint):
    async with response as resp:
        status = resp.status
        headers = resp.raw_headers
        json_body = await resp.json()

    print(f'RESPONSE STATUS: {status}')

    # Update client headers. Such as lastTransactionID and the like
    self.default_parameters.update(headers)
    last_transaction_id = json_body.get('lastTransactionID', None)
    if last_transaction_id:
        self.default_parameters.update({LastTransactionID: last_transaction_id})

    try:
        schema = endpoint.responses[status]  # look up the template to process the data
    except KeyError:
        schema = other_responses[status]  # See if a response status is an error code

    result = await _create_response(json_body, schema)
    result.raw_body = json_body
    return result


async def _stream_parser(response, endpoint):
    async with response as resp:
        schema = endpoint.responses[resp.status]
        async for line in resp.content:
            body = json.loads(line)
            key = body.get('type')
            json_body = {key: body}
            yield await _create_response(json_body, schema)


async def parse_response(self, response, endpoint):
    if endpoint.host == 'REST':
        result = await _rest_response(self, response, endpoint)
    else:
        result = _stream_parser(response, endpoint)
    return result
