from ..definitions.types import *
from .metaclass import *

class GETTrades(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/trades'

    # description of endpoint
    description = 'Get a list of Trades for an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'ids', 'located': 'query', 'type': 'List of TradeID (csv)',
         'description': 'List of TradeID (csv)'},
        {'name': 'state', 'located': 'query', 'type': 'TradeStateFilter', 'description': 'TradeStateFilter'},
        {'name': 'instrument', 'located': 'query', 'type': 'InstrumentName', 'description': 'InstrumentName'},
        {'name': 'count', 'located': 'query', 'type': 'int', 'description': 'int'},
        {'name': 'beforeID', 'located': 'query', 'type': 'TradeID', 'description': 'TradeID'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The list of Trades requested'},
    ]

    # error msgs'
    error = ['401', '404', '405']

    # json schema representation
    schema = """
        {
            # 
            # The list of Trade detail objects
            # 
            trades : (Array[Trade]),

            # 
            # The ID of the most recent Transaction created for the Account
            # 
            lastTransactionID : (TransactionID)
        }
        """


class GETOpenTrades(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/openTrades'

    # description of endpoint
    description = 'Get the list of open Trades for an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The Account’s list of open Trades is provided'},
    ]

    # error msgs'
    error = ['401', '404', '405']

    # json schema representation
    schema = """
        {
            # 
            # The Account’s list of open Trades
            # 
            trades : (Array[Trade]),

            # 
            # The ID of the most recent Transaction created for the Account
            # 
            lastTransactionID : (TransactionID)
        }
        """


class GETTradeSpecifier(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/trades/{tradeSpecifier}'

    # description of endpoint
    description = 'Get the details of a specific Trade in an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'tradeSpecifier', 'located': 'path', 'type': 'TradeSpecifier', 'description': 'TradeSpecifier'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The details for the requested Trade is provided'},
    ]

    # error msgs'
    error = ['401', '404', '405']

    # json schema representation
    schema = """
        {
            # 
            # The Account’s list of open Trades
            # 
            trade : (Trade),

            # 
            # The ID of the most recent Transaction created for the Account
            # 
            lastTransactionID : (TransactionID)
        }
        """


class PUTTradeSpecifierClose(object):

    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = '/v3/accounts/{accountID}/trades/{tradeSpecifier}/close'

    # description of endpoint
    description = 'Close (partially or fully) a specific open Trade in an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'tradeSpecifier', 'located': 'path', 'type': 'TradeSpecifier', 'description': 'TradeSpecifier'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The Trade has been closed as requested'},
        {'response': '400', 'description': '– The Trade cannot be closed as requested.'},
        {'response': '404', 'description': '– The Account or Trade specified does not exist.'},
    ]

    # error msgs'
    error = ['401', '405']

    # json schema representation
    schema = """
        {
            # 
            # Indication of how much of the Trade to close. Either the string “ALL”
            # (indicating that all of the Trade should be closed), or a DecimalNumber
            # representing the number of units of the open Trade to Close using a
            # TradeClose MarketOrder. The units specified must always be positive, and
            # the magnitude of the value cannot exceed the magnitude of the Trade’s
            # open units.
            # 
            units : (string, default=ALL)
        }
        """


class PUTTradeSpecifierClientExtensions(object):

    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = '/v3/accounts/{accountID}/trades/{tradeSpecifier}/clientExtensions'

    # description of endpoint
    description = 'Update the Client Extensions for a Trade. Do not add, update, or ' \
                  'delete the Client Extensions if your account is associated with MT4.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'tradeSpecifier', 'located': 'path', 'type': 'TradeSpecifier', 'description': 'TradeSpecifier'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The Trade’s Client Extensions have been updated as requested.'},
        {'response': '400', 'description': '– The Trade’s Client Extensions cannot be modified as requested.'},
        {'response': '404', 'description': '– The Account or Trade specified does not exist.'},
    ]

    # error msgs'
    error = ['401', '405']

    # json schema representation
    schema = """
        {
            # 
            # The Client Extensions to update the Trade with. Do not add, update, or
            # delete the Client Extensions if your account is associated with MT4.
            # 
            clientExtensions : (ClientExtensions)
        }
        """


class PUTTradesSpecifierOrders(object):

    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = '/v3/accounts/{accountID}/trades/{tradeSpecifier}/orders'

    # description of endpoint
    description = 'Create, replace and cancel a Trade’s dependent Orders (Take Profit, Stop Loss and Trailing Stop Loss) through the Trade itself'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'tradeSpecifier', 'located': 'path', 'type': 'TradeSpecifier', 'description': 'TradeSpecifier'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The Trade’s dependent Orders have been modified as requested.'},
        {'response': '400', 'description': '– The Trade’s dependent Orders cannot be modified as requested.'},
    ]

    # error msgs'
    error = ['401', '404', '405']

    # json schema representation
    schema = """
        {
            # 
            # The specification of the Take Profit to create/modify/cancel. If
            # takeProfit is set to null, the Take Profit Order will be cancelled if it
            # exists. If takeProfit is not provided, the exisiting Take Profit Order
            # will not be modified. If a sub-field of takeProfit is not specified, that
            # field will be set to a default value on create, and be inherited by the
            # replacing order on modify.
            # 
            takeProfit : (TakeProfitDetails),

            # 
            # The specification of the Stop Loss to create/modify/cancel. If stopLoss
            # is set to null, the Stop Loss Order will be cancelled if it exists. If
            # stopLoss is not provided, the exisiting Stop Loss Order will not be
            # modified. If a sub-field of stopLoss is not specified, that field will be
            # set to a default value on create, and be inherited by the replacing order
            # on modify.
            # 
            stopLoss : (StopLossDetails),

            # 
            # The specification of the Trailing Stop Loss to create/modify/cancel. If
            # trailingStopLoss is set to null, the Trailing Stop Loss Order will be
            # cancelled if it exists. If trailingStopLoss is not provided, the
            # exisiting Trailing Stop Loss Order will not be modified. If a sub-field
            # of trailngStopLoss is not specified, that field will be set to a default
            # value on create, and be inherited by the replacing order on modify.
            # 
            trailingStopLoss : (TrailingStopLossDetails)
        }
        """
