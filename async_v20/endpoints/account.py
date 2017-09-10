from ..definitions.types import *
from .metaclass import *


class GETAccounts(object):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts'

    # description of endpoint
    description = 'Get a list of all Accounts authorized for the provided token.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
    ]

    # valid responses
    responses = {'200', {'accounts': Array[AccountProperties]}}

    # error msgs'
    error = ['401', '405']



class GETAccountID(object):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}'

    # description of endpoint
    description = 'Get the full details for a single Account that a client has access to. ' \
                  'Full pending Order, open Trade and open Position representations are provided.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
    ]

    # valid responses
    responses = {'200': {'account': Account, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = ['400', '401', '405']


class GETAccountIDSummary(object):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/summary'

    # description of endpoint
    description = 'Get a summary for a single Account that a client has access to.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
    ]

    # valid responses
    responses = {'200': {'account': AccountSummary, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = ['400', '401', '405']


class GETAccountIDInstruments(object):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/instruments'

    # description of endpoint
    description = 'Get the list of tradeable instruments for the given Account. The list of tradeable instruments is dependent on the regulatory division that the Account is located in, thus should be the same for all Accounts owned by a single user.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'instruments', 'located': 'query', 'type': 'List of InstrumentName (csv)',
         'description': 'List of InstrumentName (csv)'},
    ]

    # valid responses
    responses = {'200': {'instruments': Array[Instrument], 'lastTransactionID': TransactionID}}

    # error msgs'
    error = ['400', '401', '405']


class PATCHAccountIDConfiguration(object):
    # the HTTP verb to use for this endpoint
    method = 'PATCH'

    # path to endpoint
    path = '/v3/accounts/{accountID}/configuration'

    # description of endpoint
    description = 'Set the client-configurable portions of an Account.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
    ]

    # valid responses
    responses = {200: {'clientConfigureTransaction': ClientConfigureTransaction, 'lastTransactionID': TransactionID},
                 400: {'clientConfigureRejectTransaction': ClientConfigureRejectTransaction,
                       'lastTransactionID': TransactionID, 'errorCode': string, 'errorMessage': string},
                 403: {'clientConfigureRejectTransaction': ClientConfigureRejectTransaction,
                       'lastTransactionID': TransactionID, 'errorCode': string, 'errorMessage': string}}

    # error msgs'
    error = ['401', '404', '405']

    # json schema representation
    request_schema = {'alias': string, 'marginRate': DecimalNumber}


class GETAccountIDChanges(object):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/changes'

    # description of endpoint
    description = 'Endpoint used to poll an Account for its current state and changes since a specified TransactionID.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'sinceTransactionID', 'located': 'query', 'type': 'TransactionID', 'description': 'TransactionID'},
    ]

    # valid responses
    responses = {'200', {'changes': AccountChanges, 'state': AccountChangesState, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = ['401', '404', '405', '416']
