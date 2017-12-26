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
    responses = {200: {'transaction': Transaction, 'transactionHeartbeat': TransactionHeartbeat}}

    # error msgs'
    error = (400, 401, 404, 405)
