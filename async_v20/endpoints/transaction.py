from .annotations import *
from .base import EndPoint, Path
from ..definitions.descriptors import *
from ..definitions.metaclass import Array
from ..definitions.types import *

__all__ = ['GETTransactions', 'GETTransactionID', 'GETIDrange', 'GETSinceID', 'GETTransactionsStream']


class GETTransactions(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = Path('/v3/accounts/', AccountID, '/transactions')

    # description of endpoint
    description = 'Get a list of Transactions pages that satisfy a time-based Transaction query.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'from', 'located': 'query', 'type': FromTime, 'description': 'DateTime'},
        {'name': 'to', 'located': 'query', 'type': ToTime, 'description': 'DateTime'},
        {'name': 'pageSize', 'located': 'query', 'type': PageSize, 'description': 'int'},
        {'name': 'type', 'located': 'query', 'type': Type,
         'description': 'List of TransactionFilter (csv)'},
    ]

    # valid responses
    responses = {
        200: {'from': DateTime, 'to': DateTime, 'pageSize': int, 'type': Array(TransactionFilter), 'count': int,
              'pages': Array(str), 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (400, 401, 403, 404, 405, 416)


class GETTransactionID(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = Path('/v3/accounts/', AccountID, '/transactions/', TransactionID)

    # description of endpoint
    description = 'Get the details of a single Account Transaction.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'transactionID', 'located': 'path', 'type': TransactionID, 'description': 'TransactionID'},
    ]

    # valid responses
    responses = {200: {'transaction': Transaction, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405)


class GETIDrange(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = Path('/v3/accounts/', AccountID, '/transactions/idrange')

    # description of endpoint
    description = 'Get a range of Transactions for an Account based on the Transaction IDs.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'from', 'located': 'query', 'type': TransactionID, 'description': 'TransactionID'},
        {'name': 'to', 'located': 'query', 'type': TransactionID, 'description': 'TransactionID'},
        {'name': 'type', 'located': 'query', 'type': Type,
         'description': 'List of TransactionFilter (csv)'},
    ]

    # valid responses
    responses = {200: {'transactions': Array(Transaction), 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (400, 401, 404, 405, 416)


class GETSinceID(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = Path('/v3/accounts/', AccountID, '/transactions/sinceid')

    # description of endpoint
    description = 'Get a range of Transactions for an Account starting at ' \
                  '(but not including) a provided Transaction ID.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'id', 'located': 'query', 'type': TransactionID, 'description': 'TransactionID'},
    ]

    # valid responses
    responses = {200: {'transactions': Array(Transaction), 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (400, 401, 404, 405, 416)


class GETTransactionsStream(EndPoint):
    # host to use for this endpoint
    host = 'STREAM'

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = Path('/v3/accounts/', AccountID, '/transactions/stream')

    # description of endpoint
    description = 'Get a stream of Transactions for an Account starting from when the request is made.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
    ]

    # valid responses
    responses = {200: {'transaction': Transaction, 'transactionHeartbeat': TransactionHeartbeat}}

    # error msgs'
    error = (400, 401, 404, 405)
