import json

from ..endpoints.annotations import LastTransactionID
from ..endpoints.other_responses import other_responses


def create_objects(schema, key, obj):
    typ = schema.get(key)
    try:
        obj = typ(**obj)
    except TypeError:
        obj = typ(obj)

    return key, obj


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

    async def create(json_data, schema):
        return dict([create_objects(schema, json_object, object_field)
                     for json_object, object_field in json_data.items()])

    return await create(json_body, schema)


async def _stream_parser(response, endpoint):
    print('STREAMING')
    async with response as resp:
        response_schema = endpoint.responses[resp.status]
        async for line in resp.content:
            body = json.loads(line)
            key = body.pop('type')
            yield dict([create_objects(response_schema, key, body)])


async def parse_response(self, response, endpoint):
    if endpoint.host == 'REST':
        result = await _rest_response(self, response, endpoint)
    else:
        result = _stream_parser(response, endpoint)
    return result
