from ..definitions.types import *
from .metaclass import *


class GETPositions(object):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/positions'

    # description of endpoint
    description = 'List all Positions for an Account. The Positions returned are for every ' \
                  'instrument that has had a position during the lifetime of an the Account.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': str, 'description': 'str'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
    ]

    # valid responses
    responses = {200: {'positions': Array[Position], 'lastTransactionID': TransactionID}}

    # error msgs'
    error = [401, 404, 405]


class GETOpenPositions(object):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/openPositions'

    # description of endpoint
    description = 'List all open Positions for an Account. An open Position is a ' \
                  'Position in an Account that currently has a Trade opened for it.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': str, 'description': 'str'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
    ]

    # valid responses
    responses = {200: {'positions': Array[Position], 'lastTransactionID': TransactionID}}

    # error msgs'
    error = [401, 404, 405]


class GETPositionsInstrument(object):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/positions/{instrument}'

    # description of endpoint
    description = 'Get the details of a single Instrument’s Position in an Account. The Position may by open or not.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': str, 'description': 'str'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'instrument', 'located': 'path', 'type': InstrumentName, 'description': 'InstrumentName'},
    ]

    # valid responses
    responses = {200: {'position': Position, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = [401, 404, 405]


class PUTPositionsInstrumentClose(object):
    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = '/v3/accounts/{accountID}/positions/{instrument}/close'

    # description of endpoint
    description = 'Closeout the open Position for a specific instrument in an Account.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': str, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'instrument', 'located': 'path', 'type': InstrumentName, 'description': 'InstrumentName'},
    ]

    # valid responses
    responses = {
        200: {'longOrderCreateTransaction': MarketOrderTransaction, 'longOrderFillTransaction': OrderFillTransaction,
              'longOrderCancelTransaction': OrderCancelTransaction,
              'shortOrderCreateTransaction': MarketOrderTransaction, 'shortOrderFillTransaction': OrderFillTransaction,
              'shortOrderCancelTransaction': OrderCancelTransaction, 'relatedTransactionIDs': Array[TransactionID],
              'lastTransactionID': TransactionID},
        400: {'longOrderRejectTransaction': MarketOrderRejectTransaction,
              'shortOrderRejectTransaction': MarketOrderRejectTransaction,
              'relatedTransactionIDs': Array[TransactionID], 'lastTransactionID': TransactionID, 'errorCode': str,
              'errorMessage': str},
        404: {'longOrderRejectTransaction': MarketOrderRejectTransaction,
              'shortOrderRejectTransaction': MarketOrderRejectTransaction,
              'relatedTransactionIDs': Array[TransactionID], 'lastTransactionID': TransactionID, 'errorCode': str,
              'errorMessage': str}}

    # error msgs'
    error = [401, 405]

    # TODO longunits and short units need to default to 'ALL'
    # json schema representation
    request_schema = {'longUnits': str, 'longClientExtensions': ClientExtensions, 'shortUnits': str,
                      'shortClientExtensions': ClientExtensions}
