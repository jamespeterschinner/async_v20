from .annotations import *
from .base import EndPoint, HEADER, PATH, QUERY
from ..definitions.primitives import *
from ..definitions.types import *

__all__ = ['GETTransactions', 'GETTransactionID', 'GETIDrange', 'GETSinceID', 'GETTransactionsStream']


class GETTransactions(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/transactions')

    # description of endpoint
    description = 'Get a list of Transactions pages that satisfy a time-based Transaction query.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), FromTime: (QUERY, 'from'), ToTime: (QUERY, 'to'),
                  PageSize: (QUERY, 'pageSize'), Type: (QUERY, 'type')}

    # valid responses
    responses = {
        200: {'from': DateTime, 'to': DateTime, 'pageSize': int, 'type': ArrayTransactionFilter, 'count': int,
              'pages': ArrayStr, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (400, 401, 403, 404, 405, 416)


class GETTransactionID(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/transactions/', TransactionID)

    # description of endpoint
    description = 'Get the details of a single Account Transaction.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), TransactionID: (PATH, 'transactionID')}

    # valid responses
    responses = {200: {'transaction': Transaction, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class GETIDrange(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/transactions/idrange')

    # description of endpoint
    description = 'Get a range of Transactions for an Account based on the Transaction IDs.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), FromTransactionID: (QUERY, 'from'), ToTransactionID: (QUERY, 'to'),
                  Type: (QUERY, 'type')}

    # valid responses
    responses = {200: {'transactions': ArrayTransaction, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (400, 401, 404, 405, 416)


class GETSinceID(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/transactions/sinceid')

    # description of endpoint
    description = 'Get a range of Transactions for an Account starting at ' \
                  '(but not including) a provided Transaction ID.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), TransactionID: (QUERY, 'id')}

    # valid responses
    responses = {200: {'transactions': ArrayTransaction, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (400, 401, 404, 405, 416)


class GETTransactionsStream(EndPoint):
    # host to use for this endpoint
    host = 'STREAM'

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/transactions/stream')

    # description of endpoint
    description = 'Get a stream of Transactions for an Account starting from when the request is made.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AccountID: (PATH, 'accountID')}

    # valid responses
    responses = {200: {'HEARTBEAT': TransactionHeartbeat,
                       'CREATE': CreateTransaction,
                       'CLOSE': CloseTransaction,
                       'REOPEN': ReopenTransaction,
                       'CLIENT_CONFIGURE': ClientConfigureTransaction,
                       'CLIENT_CONFIGURE_REJECT': ClientConfigureRejectTransaction,
                       'TRANSFER_FUNDS': TransferFundsTransaction,
                       'TRANSFER_FUNDS_REJECT': TransferFundsRejectTransaction,
                       'MARKET_ORDER': MarketOrderTransaction,
                       'MARKET_ORDER_REJECT': MarketOrderRejectTransaction,
                       'LIMIT_ORDER': LimitOrderTransaction,
                       'LIMIT_ORDER_REJECT': LimitOrderRejectTransaction,
                       'STOP_ORDER': StopOrderTransaction,
                       'STOP_ORDER_REJECT': StopOrderRejectTransaction,
                       'MARKET_IF_TOUCHED_ORDER': MarketIfTouchedOrderTransaction,
                       'MARKET_IF_TOUCHED_ORDER_REJECT': MarketIfTouchedOrderRejectTransaction,
                       'TAKE_PROFIT_ORDER': TakeProfitOrderTransaction,
                       'TAKE_PROFIT_ORDER_REJECT': TakeProfitOrderRejectTransaction,
                       'STOP_LOSS_ORDER': StopLossOrderTransaction,
                       'STOP_LOSS_ORDER_REJECT': StopOrderRejectTransaction,
                       'TRAILING_STOP_LOSS_ORDER': TrailingStopLossOrderTransaction,
                       'TRAILING_STOP_LOSS_ORDER_REJECT': TrailingStopLossOrderRejectTransaction,
                       'ORDER_FILL': OrderFillTransaction,
                       'ORDER_CANCEL': OrderCancelTransaction,
                       'ORDER_CANCEL_REJECT': OrderCancelRejectTransaction,
                       'ORDER_CLIENT_EXTENSIONS_MODIFY': OrderClientExtensionsModifyTransaction,
                       'ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT': OrderClientExtensionsModifyRejectTransaction,
                       'TRADE_CLIENT_EXTENSIONS_MODIFY': TradeClientExtensionsModifyTransaction,
                       'TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT': TradeClientExtensionsModifyRejectTransaction,
                       'MARGIN_CALL_ENTER': MarginCallEnterTransaction,
                       'MARGIN_CALL_EXTEND': MarginCallExtendTransaction,
                       'MARGIN_CALL_EXIT': MarginCallExitTransaction,
                       'DELAYED_TRADE_CLOSURE': DelayedTradeClosureTransaction,
                       'DAILY_FINANCING': DailyFinancingTransaction,
                       'RESET_RESETTABLE_PL': ResetResettablePLTransaction}
                 }

    # error msgs'
    error = (400, 401, 404, 405)
