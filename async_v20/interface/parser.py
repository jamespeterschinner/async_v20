import ujson as json

from .response import Response
from ..definitions.base import create_attribute
from ..endpoints.annotations import LastTransactionID
from ..endpoints.other_responses import other_responses


def _lookup_schema(endpoint, status):
    try:
        schema = endpoint.responses[status]  # look up the template to process the data
    except KeyError:
        schema = other_responses[status]  # See if a response status is an error code
    else:
        # Returns true if the status was a valid response
        return schema, status, True
    # Returns False if the status wasn't in the endpoints expected response
    return schema, status, False


async def _create_response(json_body, endpoint, status):
    # Placed this in create response to minimize all the arguments being passed around
    schema, status, boolean = _lookup_schema(endpoint, status)

    # Here we iterate through all the json objects returned in the response
    # and construct the corresponding async_v20 type as determined by the endpoints
    # Schema
    print("JSON_BODY", json_body)
    def create_data():
        for json_object, json_field in json_body.items():
            yield json_object, create_attribute(schema.get(json_object), json_field)

    return Response(tuple(create_data()), status, boolean)


async def _rest_response(self, response, endpoint):
    async with response as resp:
        status = resp.status
        headers = resp.raw_headers
        json_body = await resp.json()

    # Update client headers. Such as lastTransactionID and the like
    self.default_parameters.update(headers)
    last_transaction_id = json_body.get('lastTransactionID', None)
    if last_transaction_id:
        self.default_parameters.update({LastTransactionID: last_transaction_id})

    return await _create_response(json_body, endpoint, status)


async def _stream_parser(response, endpoint):
    async with response as resp:
        async for line in resp.content:
            body = json.loads(line)  # Turn bytes into json
            key = body.get('type')  # We must determine what type of object as been sent. So we
            json_body = {key: body}  # can construct a phony json body similar to a rest response
            yield await _create_response(json_body, endpoint, resp.status)


async def parse_response(self, response, endpoint):
    if endpoint.host == 'REST':
        result = await _rest_response(self, response, endpoint)
    else:
        result = _stream_parser(response, endpoint)
    return result
