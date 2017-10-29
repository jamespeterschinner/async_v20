from .annotations import *
from .base import EndPoint, Path
from ..definitions.primitives import *
from ..definitions.base import Array
from ..definitions.types import *

__all__ = ['POSTOrders', 'GETOrders', 'GETPendingOrders', 'GETOrderSpecifier', 'PUTOrderSpecifier',
           'PUTOrderSpecifierCancel', 'PUTClientExtensions']


class POSTOrders(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'POST'

    # path to endpoint
    path = Path('/v3/accounts/', AccountID, '/orders')

    # description of endpoint
    description = 'Create an Order for an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
    ]

    # valid responses
    responses = {201: {'orderCreateTransaction': Transaction, 'orderFillTransaction': OrderFillTransaction,
                       'orderCancelTransaction': OrderCancelTransaction, 'orderReissueTransaction': Transaction,
                       'orderReissueRejectTransaction': Transaction, 'relatedTransactionIDs': Array(TransactionID),
                       'lastTransactionID': TransactionID},
                 400: {'orderRejectTransaction': Transaction, 'relatedTransactionIDs': Array(TransactionID),
                       'lastTransactionID': TransactionID, 'errorCode': str, 'errorMessage': str},
                 404: {'orderRejectTransaction': Transaction, 'relatedTransactionIDs': Array(TransactionID),
                       'lastTransactionID': TransactionID, 'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 403, 405)

    # json schema representation
    request_schema = {OrderRequest: 'order'}


class GETOrders(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = Path('/v3/accounts/', AccountID, '/orders')

    # description of endpoint
    description = 'Get a list of Orders for an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'ids', 'located': 'query', 'type': Ids,
         'description': 'List of OrderID (csv)'},
        {'name': 'state', 'located': 'query', 'type': OrderStateFilter, 'description': 'OrderStateFilter'},
        {'name': 'instrument', 'located': 'query', 'type': InstrumentName, 'description': 'InstrumentName'},
        {'name': 'count', 'located': 'query', 'type': Count, 'description': 'int'},
        {'name': 'beforeID', 'located': 'query', 'type': OrderID, 'description': 'OrderID'},
    ]

    # valid responses
    responses = {200: {'orders': Array(Order), 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (400, 404, 405)


class GETPendingOrders(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = Path('/v3/accounts/', AccountID, '/pendingOrders')

    # description of endpoint
    description = 'List all pending Orders in an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
    ]

    # valid responses
    responses = {200: {'orders': Array(Order), 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class GETOrderSpecifier(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = Path('/v3/accounts/', AccountID, '/orders/', OrderSpecifier)

    # description of endpoint
    description = 'Get details for a single Order in an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'orderSpecifier', 'located': 'path', 'type': OrderSpecifier, 'description': 'OrderSpecifier'},
    ]

    # valid responses
    responses = {200: {'order': Order, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class PUTOrderSpecifier(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = Path('/v3/accounts/', AccountID, '/orders/', OrderSpecifier)

    # description of endpoint
    description = 'Replace an Order in an Account by simultaneously cancelling it and creating a replacement Order'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'orderSpecifier', 'located': 'path', 'type': OrderSpecifier, 'description': 'OrderSpecifier'},
    ]

    # valid responses
    responses = {201: {'orderCancelTransaction': OrderCancelTransaction, 'orderCreateTransaction': Transaction,
                       'orderFillTransaction': OrderFillTransaction, 'orderReissueTransaction': Transaction,
                       'orderReissueRejectTransaction': Transaction,
                       'replacingOrderCancelTransaction': OrderCancelTransaction,
                       'relatedTransactionIDs': Array(TransactionID), 'lastTransactionID': TransactionID},
                 400: {'orderRejectTransaction': Transaction, 'relatedTransactionIDs': Array(TransactionID),
                       'lastTransactionID': TransactionID, 'errorCode': str, 'errorMessage': str},
                 404: {'orderCancelRejectTransaction': Transaction, 'relatedTransactionIDs': Array(TransactionID),
                       'lastTransactionID': TransactionID, 'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 405)

    # json schema representation
    request_schema = {OrderRequest: 'order'}


class PUTOrderSpecifierCancel(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = Path('/v3/accounts/', AccountID, '/orders/', OrderSpecifier, '/cancel')

    # description of endpoint
    description = 'Cancel a pending Order in an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'orderSpecifier', 'located': 'path', 'type': OrderSpecifier, 'description': 'OrderSpecifier'},
    ]

    # valid responses
    responses = {200: {'orderCancelTransaction': OrderCancelTransaction, 'relatedTransactionIDs': Array(TransactionID),
                       'lastTransactionID': TransactionID},
                 400: {'orderCancelRejectTransaction': OrderCancelRejectTransaction,
                       'relatedTransactionIDs': Array(TransactionID), 'lastTransactionID': TransactionID,
                       'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 405)


class PUTClientExtensions(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = Path('/v3/accounts/', AccountID, '/orders/', OrderSpecifier, '/clientExtensions')

    # description of endpoint
    description = 'Update the Client Extensions for an Order in an Account. Do not set, ' \
                  'modify, or delete clientExtensions if your account is associated with MT4.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'orderSpecifier', 'located': 'path', 'type': OrderSpecifier, 'description': 'OrderSpecifier'},
    ]

    # valid responses
    responses = {200: {'orderClientExtensionsModifyTransaction': OrderClientExtensionsModifyTransaction,
                       'lastTransactionID': TransactionID, 'relatedTransactionIDs': Array(TransactionID)},
                 400: {'orderClientExtensionsModifyRejectTransaction': OrderClientExtensionsModifyRejectTransaction,
                       'lastTransactionID': TransactionID, 'relatedTransactionIDs': Array(TransactionID),
                       'errorCode': str, 'errorMessage': str},
                 404: {'orderClientExtensionsModifyRejectTransaction': OrderClientExtensionsModifyRejectTransaction,
                       'lastTransactionID': TransactionID, 'relatedTransactionIDs': Array(TransactionID),
                       'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 405)

    # json schema representation
    request_schema = {'clientExtensions': ClientExtensions, 'tradeClientExtensions': TradeClientExtensions}
