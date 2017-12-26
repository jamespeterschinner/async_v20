from .annotations import *
from .base import EndPoint, HEADER, PATH, QUERY
from ..definitions.primitives import *
from ..definitions.types import *

__all__ = ['POSTOrders', 'GETOrders', 'GETPendingOrders', 'GETOrderSpecifier', 'PUTOrderSpecifier',
           'PUTOrderSpecifierCancel', 'PUTClientExtensions']


class POSTOrders(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'POST'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/orders')

    # description of endpoint
    description = 'Create an Order for an Account'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID')}

    # valid responses
    responses = {201: {'orderCreateTransaction': Transaction, 'orderFillTransaction': OrderFillTransaction,
                       'orderCancelTransaction': OrderCancelTransaction, 'orderReissueTransaction': Transaction,
                       'orderReissueRejectTransaction': Transaction, 'relatedTransactionIDs': ArrayTransactionID,
                       'lastTransactionID': TransactionID},
                 400: {'orderRejectTransaction': Transaction, 'relatedTransactionIDs': ArrayTransactionID,
                       'lastTransactionID': TransactionID, 'errorCode': str, 'errorMessage': str},
                 404: {'orderRejectTransaction': Transaction, 'relatedTransactionIDs': ArrayTransactionID,
                       'lastTransactionID': TransactionID, 'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 403, 405)

    # json schema representation
    request_schema = {OrderRequest: 'order'}


class GETOrders(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/orders')

    # description of endpoint
    description = 'Get a list of Orders for an Account'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), Ids: (QUERY, 'ids'), OrderStateFilter: (QUERY, 'state'),
                  InstrumentName: (QUERY, 'instrument'), Count: (QUERY, 'count'), OrderID: (QUERY, 'beforeID')}

    # valid responses
    responses = {200: {'orders': ArrayOrder, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (400, 404, 405)


class GETPendingOrders(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/pendingOrders')

    # description of endpoint
    description = 'List all pending Orders in an Account'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID')}

    # valid responses
    responses = {200: {'orders': ArrayOrder, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class GETOrderSpecifier(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/orders/', OrderSpecifier)

    # description of endpoint
    description = 'Get details for a single Order in an Account'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), OrderSpecifier: (PATH, 'orderSpecifier')}

    # valid responses
    responses = {200: {'order': Order, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class PUTOrderSpecifier(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/orders/', OrderSpecifier)

    # description of endpoint
    description = 'Replace an Order in an Account by simultaneously cancelling it and creating a replacement Order'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), OrderSpecifier: (PATH, 'orderSpecifier')}

    # valid responses
    responses = {201: {'orderCancelTransaction': OrderCancelTransaction, 'orderCreateTransaction': Transaction,
                       'orderFillTransaction': OrderFillTransaction, 'orderReissueTransaction': Transaction,
                       'orderReissueRejectTransaction': Transaction,
                       'replacingOrderCancelTransaction': OrderCancelTransaction,
                       'relatedTransactionIDs': ArrayTransactionID, 'lastTransactionID': TransactionID},
                 400: {'orderRejectTransaction': Transaction, 'relatedTransactionIDs': ArrayTransactionID,
                       'lastTransactionID': TransactionID, 'errorCode': str, 'errorMessage': str},
                 404: {'orderCancelRejectTransaction': Transaction, 'relatedTransactionIDs': ArrayTransactionID,
                       'lastTransactionID': TransactionID, 'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 405)

    # json schema representation
    request_schema = {OrderRequest: 'order'}


class PUTOrderSpecifierCancel(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/orders/', OrderSpecifier, '/cancel')

    # description of endpoint
    description = 'Cancel a pending Order in an Account'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), OrderSpecifier: (PATH, 'orderSpecifier')}

    # valid responses
    responses = {200: {'orderCancelTransaction': OrderCancelTransaction, 'relatedTransactionIDs': ArrayTransactionID,
                       'lastTransactionID': TransactionID},
                 400: {'orderCancelRejectTransaction': OrderCancelRejectTransaction,
                       'relatedTransactionIDs': ArrayTransactionID, 'lastTransactionID': TransactionID,
                       'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 405)


class PUTClientExtensions(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/orders/', OrderSpecifier, '/clientExtensions')

    # description of endpoint
    description = 'Update the Client Extensions for an Order in an Account. Do not set, ' \
                  'modify, or delete clientExtensions if your account is associated with MT4.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), OrderSpecifier: (PATH, 'orderSpecifier')}

    # valid responses
    responses = {200: {'orderClientExtensionsModifyTransaction': OrderClientExtensionsModifyTransaction,
                       'lastTransactionID': TransactionID, 'relatedTransactionIDs': ArrayTransactionID},
                 400: {'orderClientExtensionsModifyRejectTransaction': OrderClientExtensionsModifyRejectTransaction,
                       'lastTransactionID': TransactionID, 'relatedTransactionIDs': ArrayTransactionID,
                       'errorCode': str, 'errorMessage': str},
                 404: {'orderClientExtensionsModifyRejectTransaction': OrderClientExtensionsModifyRejectTransaction,
                       'lastTransactionID': TransactionID, 'relatedTransactionIDs': ArrayTransactionID,
                       'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 405)

    # json schema representation
    request_schema = {'clientExtensions': ClientExtensions, 'tradeClientExtensions': TradeClientExtensions}
