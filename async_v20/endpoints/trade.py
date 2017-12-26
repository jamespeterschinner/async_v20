from .annotations import *
from .base import EndPoint, HEADER, PATH, QUERY
from ..definitions.primitives import *
from ..definitions.types import *

__all__ = ['GETTrades', 'GETOpenTrades', 'GETTradeSpecifier', 'PUTTradeSpecifierClose',
           'PUTTradeSpecifierClientExtensions', 'PUTTradesSpecifierOrders']


class GETTrades(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/trades')

    # description of endpoint
    description = 'Get a list of Trades for an Account'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), Ids: (QUERY, 'ids'), TradeStateFilter: (QUERY, 'state'),
                  InstrumentName: (QUERY, 'instrument'), Count: (QUERY, 'count'), TradeID: (QUERY, 'beforeID')}

    # valid responses
    responses = {200: {'trades': ArrayTrade, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class GETOpenTrades(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/openTrades')

    # description of endpoint
    description = 'Get the list of open Trades for an Account'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID')}

    # valid responses
    responses = {200: {'trades': ArrayTrade, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class GETTradeSpecifier(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/trades/', TradeSpecifier)

    # description of endpoint
    description = 'Get the details of a specific Trade in an Account'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), TradeSpecifier: (PATH, 'tradeSpecifier')}

    # valid responses
    responses = {200: {'trade': Trade, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class PUTTradeSpecifierClose(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/trades/', TradeSpecifier, '/close')

    # description of endpoint
    description = 'Close (partially or fully) a specific open Trade in an Account'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), TradeSpecifier: (PATH, 'tradeSpecifier')}

    # valid responses
    responses = {200: {'orderCreateTransaction': MarketOrderTransaction, 'orderFillTransaction': OrderFillTransaction,
                       'orderCancelTransaction': OrderCancelTransaction, 'relatedTransactionIDs': ArrayTransactionID,
                       'lastTransactionID': TransactionID},
                 400: {'orderRejectTransaction': MarketOrderRejectTransaction, 'errorCode': str,
                       'errorMessage': str},
                 404: {'orderRejectTransaction': MarketOrderRejectTransaction, 'lastTransactionID': TransactionID,
                       'relatedTransactionIDs': ArrayTransactionID, 'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 405)

    # json schema representation
    request_schema = {Units: 'units'}


class PUTTradeSpecifierClientExtensions(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/trades/', TradeSpecifier, '/clientExtensions')

    # description of endpoint
    description = 'Update the Client Extensions for a Trade. Do not add, update, or ' \
                  'delete the Client Extensions if your account is associated with MT4.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), TradeSpecifier: (PATH, 'tradeSpecifier')}

    # valid responses
    responses = {200: {'tradeClientExtensionsModifyTransaction': TradeClientExtensionsModifyTransaction,
                       'relatedTransactionIDs': ArrayTransactionID, 'lastTransactionID': TransactionID},
                 400: {'tradeClientExtensionsModifyRejectTransaction': TradeClientExtensionsModifyRejectTransaction,
                       'lastTransactionID': TransactionID, 'relatedTransactionIDs': ArrayTransactionID,
                       'errorCode': str, 'errorMessage': str},
                 404: {'tradeClientExtensionsModifyRejectTransaction': TradeClientExtensionsModifyRejectTransaction,
                       'lastTransactionID': TransactionID, 'relatedTransactionIDs': ArrayTransactionID,
                       'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 405)

    # json schema representation
    request_schema = {ClientExtensions: 'clientExtensions'}


class PUTTradesSpecifierOrders(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/trades/', TradeSpecifier, '/orders')

    # description of endpoint
    description = 'Create, replace and cancel a Trade’s dependent Orders ' \
                  '(Take Profit, Stop Loss and Trailing Stop Loss) through the Trade itself'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), TradeSpecifier: (PATH, 'tradeSpecifier')}

    # valid responses
    responses = {200: {'takeProfitOrderCancelTransaction': OrderCancelTransaction,
                       'takeProfitOrderTransaction': TakeProfitOrderTransaction,
                       'takeProfitOrderFillTransaction': OrderFillTransaction,
                       'takeProfitOrderCreatedCancelTransaction': OrderCancelTransaction,
                       'stopLossOrderCancelTransaction': OrderCancelTransaction,
                       'stopLossOrderTransaction': StopLossOrderTransaction,
                       'stopLossOrderFillTransaction': OrderFillTransaction,
                       'stopLossOrderCreatedCancelTransaction': OrderCancelTransaction,
                       'trailingStopLossOrderCancelTransaction': OrderCancelTransaction,
                       'trailingStopLossOrderTransaction': TrailingStopLossOrderTransaction,
                       'relatedTransactionIDs': ArrayTransactionID, 'lastTransactionID': TransactionID},
                 400: {'takeProfitOrderCancelRejectTransaction': OrderCancelRejectTransaction,
                       'takeProfitOrderRejectTransaction': TakeProfitOrderRejectTransaction,
                       'stopLossOrderCancelRejectTransaction': OrderCancelRejectTransaction,
                       'stopLossOrderRejectTransaction': StopLossOrderRejectTransaction,
                       'trailingStopLossOrderCancelRejectTransaction': OrderCancelRejectTransaction,
                       'trailingStopLossOrderRejectTransaction': TrailingStopLossOrderRejectTransaction,
                       'lastTransactionID': TransactionID, 'relatedTransactionIDs': ArrayTransactionID,
                       'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 404, 405)

    # json schema representation
    request_schema = {TakeProfitDetails: 'takeProfit', StopLossDetails: 'stopLoss',
                      TrailingStopLossDetails: 'trailingStopLoss'}
