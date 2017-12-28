import ujson as json
import async_timeout
from asyncio import TimeoutError as AsyncTimeOutError
from .response import Response
from .rest import update_account
from ..definitions.base import create_attribute
from ..endpoints.account import GETAccountID
from ..endpoints.annotations import LastTransactionID
from ..endpoints.annotations import SinceTransactionID
from ..endpoints.other_responses import other_responses



def _lookup_schema(endpoint, status):
    try:
        schema = endpoint.responses[status]  # look up the template to process the data
    except KeyError:
        try:
            schema = other_responses[status]  # See if a response status is an error code
        except KeyError:
            raise ConnectionError(f'Unexpected response status {status}')
        else:
            # Returns False if the status wasn't in the endpoints expected response
            return schema, status, False
    else:
        # Returns true if the status was a valid response
        return schema, status, True


async def _create_response(json_body, endpoint, schema, status, boolean, datetime_format):
    # Here we iterate through all the json objects returned in the response
    # and construct the corresponding async_v20 type as determined by the endpoints
    # Schema
    if isinstance(schema, dict):
        data = []
        for json_object, json_field in json_body.items():
            data.append((json_object, create_attribute(schema.get(json_object), json_field)))
    else:
        obj = schema(**json_body)
        data = [(obj.__class__.__name__, obj)]
    return Response(data, status, boolean, datetime_format)


async def _rest_response(self, response, endpoint, enable_rest):
    async with response as resp:
        schema, status, boolean = _lookup_schema(endpoint, resp.status)

        # Update client headers.
        self.default_parameters.update(resp.raw_headers)
        json_body = await resp.json()

    response = await _create_response(json_body, endpoint, schema, status, boolean, self.datetime_format)

    if response:
        last_transaction_id = getattr(response, 'lastTransactionID', None)
        if last_transaction_id:
            self.default_parameters.update({LastTransactionID: last_transaction_id})

            # This code is to implement the RESTful nature of the v20 API
            # - Keep track of the last transaction id used to update
            # - Add / Remove / Replace changes to account
            if enable_rest:
                self.default_parameters.update({SinceTransactionID: last_transaction_id})
                update_account(self, response.changes, response.state)

        if endpoint == GETAccountID:
            # Means account_details was requested. So we catch the account state on the way through.
            # This occurs during initialization of OandaClient.
            self._account = response.account

    return response



async def _stream_parser(self, response, endpoint):
    async with response as resp:
        schema, status, boolean = _lookup_schema(endpoint, resp.status)
        while not resp.content.at_eof():
            try:
                async with async_timeout.timeout(self.stream_timeout):
                    body = json.loads(await resp.content.readline())
                    json_body = {body.get('type'): body}  # mimic a rest response
                    yield await _create_response(json_body, endpoint, schema, status, boolean, self.datetime_format)
            except AsyncTimeOutError as e:
                raise TimeoutError(e)


async def parse_response(self, response, endpoint, enable_rest):
    if endpoint.host in 'REST HEALTH':
        result = await _rest_response(self, response, endpoint, enable_rest)
    else:
        result = _stream_parser(self, response, endpoint)
    return result
