import ujson as json
from asyncio import TimeoutError as AsyncTimeOutError
from async_timeout import timeout
import logging
from .response import Response
from .rest import update_account
from ..definitions.base import create_attribute
from ..endpoints.account import GETAccountID
from ..endpoints.annotations import LastTransactionID
from ..endpoints.annotations import SinceTransactionID
from ..endpoints.other_responses import other_responses
from ..endpoints.pricing import GETPricingStream
from ..endpoints.transaction import GETTransactionsStream
from ..exceptions import ResponseTimeout, UnexpectedStatus

from time import time

TRANSACTION = 'transaction'
HEARTBEAT = 'heartbeat'
PRICE = 'price'

logger = logging.getLogger(__name__)

def _lookup_schema(endpoint, status):
    try:
        schema = endpoint.responses[status]  # look up the template to process the data
    except KeyError:
        try:
            schema = other_responses[status]  # See if a response status is an error code
        except KeyError:
            msg = str(status)
            logger.error(msg)
            raise UnexpectedStatus(msg)
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


async def _rest_response(self, response, endpoint, enable_rest, method_name):
    try:
        async with timeout(self.rest_timeout):
            async with response as resp:
                schema, status, boolean = _lookup_schema(endpoint, resp.status)
                # Update client headers.
                self.default_parameters.update(resp.raw_headers)
                json_body = await resp.json()

    except AsyncTimeOutError:
        msg = f'{method_name} took longer than {self.rest_timeout} seconds'
        logger.error(msg)
        raise ResponseTimeout(msg)
    else:
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
            self.default_parameters.update({SinceTransactionID: last_transaction_id})
            self._account = response.account

    return response


def _construct_json_body_and_schema(line, schema, endpoint):
    """This helper function standardises the streaming responses"""
    try:
        typ = line['type']
        obj = schema[typ]
        key = None
        if HEARTBEAT in typ.lower():
            key = HEARTBEAT
        elif endpoint == GETPricingStream:
            key = PRICE
        elif endpoint == GETTransactionsStream:
            key = TRANSACTION
    except KeyError:
        json_body, json_schema = line, schema
    else:
        json_body, json_schema = {key: line}, {key: obj}
    return json_body, json_schema


async def _stream_parser(self, response, endpoint, method_name):
    async with response as resp:
        schema, status, boolean = _lookup_schema(endpoint, resp.status)
        while not resp.content.at_eof():
            try:
                async with timeout(self.stream_timeout):
                    line = json.loads(await resp.content.readline())
            except AsyncTimeOutError:
                msg = f'{method_name} took longer than {self.stream_timeout} seconds'
                logger.error(msg)
                raise ResponseTimeout(msg)

            json_body, json_schema = _construct_json_body_and_schema(line, schema, endpoint)

            yield await _create_response(json_body, endpoint, json_schema, status, boolean, self.datetime_format)


async def parse_response(self, response, endpoint, enable_rest, method_name):
    if endpoint.host in 'REST HEALTH':
        result = await _rest_response(self, response, endpoint, enable_rest, method_name)
    else:
        result = _stream_parser(self, response, endpoint, method_name)
    return result
