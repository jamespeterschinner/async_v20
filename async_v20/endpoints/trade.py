from ..definitions.types import *
from .metaclass import *


class GETTrades(object):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/trades')

    # description of endpoint
    description = 'Get a list of Trades for an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': str, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'ids', 'located': 'query', 'type': str,
         'description': 'List of TradeID (csv)'},
        {'name': 'state', 'located': 'query', 'type': TradeStateFilter, 'description': 'TradeStateFilter'},
        {'name': 'instrument', 'located': 'query', 'type': InstrumentName, 'description': 'InstrumentName'},
        {'name': 'count', 'located': 'query', 'type': int, 'description': 'int'},
        {'name': 'beforeID', 'located': 'query', 'type': TradeID, 'description': 'TradeID'},
    ]

    # valid responses
    responses = {200: {'trades': Array[Trade], 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class GETOpenTrades(object):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/openTrades')

    # description of endpoint
    description = 'Get the list of open Trades for an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': str, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
    ]

    # valid responses
    responses = {200: {'trades': Array[Trade], 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class GETTradeSpecifier(object):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/trades/', TradeSpecifier)

    # description of endpoint
    description = 'Get the details of a specific Trade in an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': str, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'tradeSpecifier', 'located': 'path', 'type': TradeSpecifier, 'description': 'TradeSpecifier'},
    ]

    # valid responses
    responses = {200: {'trade': Trade, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class PUTTradeSpecifierClose(object):
    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/trades/', TradeSpecifier, '/close')

    # description of endpoint
    description = 'Close (partially or fully) a specific open Trade in an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': str, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'tradeSpecifier', 'located': 'path', 'type': TradeSpecifier, 'description': 'TradeSpecifier'},
    ]

    # valid responses
    responses = {200: {'orderCreateTransaction': MarketOrderTransaction, 'orderFillTransaction': OrderFillTransaction,
                       'orderCancelTransaction': OrderCancelTransaction, 'relatedTransactionIDs': Array[TransactionID],
                       'lastTransactionID': TransactionID},
                 400: {'orderRejectTransaction': MarketOrderRejectTransaction, 'errorCode': str,
                       'errorMessage': str},
                 404: {'orderRejectTransaction': MarketOrderRejectTransaction, 'lastTransactionID': TransactionID,
                       'relatedTransactionIDs': Array[TransactionID], 'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 405)

    # TODO needs to default to 'ALL'
    # json schema representation
    request_schema = {'units': str}


class PUTTradeSpecifierClientExtensions(object):
    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/trades/', TradeSpecifier, '/clientExtensions')

    # description of endpoint
    description = 'Update the Client Extensions for a Trade. Do not add, update, or ' \
                  'delete the Client Extensions if your account is associated with MT4.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': str, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'tradeSpecifier', 'located': 'path', 'type': TradeSpecifier, 'description': 'TradeSpecifier'},
    ]

    # valid responses
    responses = {200: {'tradeClientExtensionsModifyTransaction': TradeClientExtensionsModifyTransaction,
                       'relatedTransactionIDs': Array[TransactionID], 'lastTransactionID': TransactionID},
                 400: {'tradeClientExtensionsModifyRejectTransaction': TradeClientExtensionsModifyRejectTransaction,
                       'lastTransactionID': TransactionID, 'relatedTransactionIDs': Array[TransactionID],
                       'errorCode': str, 'errorMessage': str},
                 404: {'tradeClientExtensionsModifyRejectTransaction': TradeClientExtensionsModifyRejectTransaction,
                       'lastTransactionID': TransactionID, 'relatedTransactionIDs': Array[TransactionID],
                       'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 405)

    # json schema representation
    request_schema = {'clientExtensions': ClientExtensions}


class PUTTradesSpecifierOrders(object):
    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/trades/', TradeSpecifier, '/orders')

    # description of endpoint
    description = 'Create, replace and cancel a Trade’s dependent Orders ' \
                  '(Take Profit, Stop Loss and Trailing Stop Loss) through the Trade itself'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': str, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'tradeSpecifier', 'located': 'path', 'type': TradeSpecifier, 'description': 'TradeSpecifier'},
    ]

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
                       'relatedTransactionIDs': Array[TransactionID], 'lastTransactionID': TransactionID},
                 400: {'takeProfitOrderCancelRejectTransaction': OrderCancelRejectTransaction,
                       'takeProfitOrderRejectTransaction': TakeProfitOrderRejectTransaction,
                       'stopLossOrderCancelRejectTransaction': OrderCancelRejectTransaction,
                       'stopLossOrderRejectTransaction': StopLossOrderRejectTransaction,
                       'trailingStopLossOrderCancelRejectTransaction': OrderCancelRejectTransaction,
                       'trailingStopLossOrderRejectTransaction': TrailingStopLossOrderRejectTransaction,
                       'lastTransactionID': TransactionID, 'relatedTransactionIDs': Array[TransactionID],
                       'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 404, 405)

    # json schema representation
    request_schema = {'takeProfit': TakeProfitDetails, 'stopLoss': StopLossDetails,
                      'trailingStopLoss': TrailingStopLossDetails}
