from .annotations import *
from .base import EndPoint, HEADER, PATH
from ..definitions.primitives import *
from ..definitions.types import *

__all__ = ['GETPositions', 'GETOpenPositions', 'GETPositionsInstrument', 'PUTPositionsInstrumentClose']


class GETPositions(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/positions')

    # description of endpoint
    description = 'List all Positions for an Account. The Positions returned are for every ' \
                  'instrument that has had a position during the lifetime of an the Account.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AccountID: (PATH, 'accountID')}

    # valid responses
    responses = {200: {'positions': ArrayPosition, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class GETOpenPositions(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/openPositions')

    # description of endpoint
    description = 'List all open Positions for an Account. An open Position is a ' \
                  'Position in an Account that currently has a Trade opened for it.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AccountID: (PATH, 'accountID')}

    # valid responses
    responses = {200: {'positions': ArrayPosition, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class GETPositionsInstrument(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/positions/', InstrumentName)

    # description of endpoint
    description = 'Get the details of a single Instrument’s Position in an Account. The Position may by open or not.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AccountID: (PATH, 'accountID'),
                  InstrumentName: (PATH, 'instrument')}

    # valid responses
    responses = {200: {'position': Position, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class PUTPositionsInstrumentClose(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/positions/', InstrumentName, '/close')

    # description of endpoint
    description = 'Closeout the open Position for a specific instrument in an Account.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), InstrumentName: (PATH, 'instrument')}

    # valid responses
    responses = {
        200: {'longOrderCreateTransaction': MarketOrderTransaction, 'longOrderFillTransaction': OrderFillTransaction,
              'longOrderCancelTransaction': OrderCancelTransaction,
              'shortOrderCreateTransaction': MarketOrderTransaction, 'shortOrderFillTransaction': OrderFillTransaction,
              'shortOrderCancelTransaction': OrderCancelTransaction, 'relatedTransactionIDs': ArrayTransactionID,
              'lastTransactionID': TransactionID},
        400: {'longOrderRejectTransaction': MarketOrderRejectTransaction,
              'shortOrderRejectTransaction': MarketOrderRejectTransaction,
              'relatedTransactionIDs': ArrayTransactionID, 'lastTransactionID': TransactionID, 'errorCode': str,
              'errorMessage': str},
        404: {'longOrderRejectTransaction': MarketOrderRejectTransaction,
              'shortOrderRejectTransaction': MarketOrderRejectTransaction,
              'relatedTransactionIDs': ArrayTransactionID, 'lastTransactionID': TransactionID, 'errorCode': str,
              'errorMessage': str}}

    # error msgs'
    error = (401, 405)

    # json schema representation
    request_schema = {LongUnits: 'longUnits', LongClientExtensions: 'longClientExtensions', ShortUnits: 'shortUnits',
                      ShortClientExtensions: 'shortClientExtensions'}
