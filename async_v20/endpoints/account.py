from .annotations import Alias
from .annotations import Authorization
from .annotations import Instruments
from .annotations import SinceTransactionID
from .base import EndPoint, HEADER, PATH, QUERY
from ..definitions.primitives import *
from ..definitions.types import *

__all__ = ['GETAccounts', 'GETAccountID', 'GETAccountIDSummary', 'GETAccountIDInstruments',
           'PATCHAccountIDConfiguration', 'GETAccountIDChanges']


class GETAccounts(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts',)

    # description of endpoint
    description = 'Get a list of all Accounts authorized for the provided token.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization')}

    # valid responses
    responses = {200: {'accounts': ArrayAccountProperties}}

    # error msgs'
    error = (401, 405)


class GETAccountID(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID)

    # description of endpoint
    description = 'Get the full details for a single Account that a client has access to. ' \
                  'Full pending Order, open Trade and open Position representations are provided.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID')}
    # valid responses
    responses = {200: {'account': Account, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (400, 401, 405)


class GETAccountIDSummary(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/summary')

    # description of endpoint
    description = 'Get a summary for a single Account that a client has access to.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID')}

    # valid responses
    responses = {200: {'account': AccountSummary, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (400, 401, 405)


class GETAccountIDInstruments(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/instruments')

    # description of endpoint
    description = 'Get the list of tradeable instruments for the given Account.' \
                  'The list of tradeable instruments is dependent on the regulatory ' \
                  'division that the Account is located in, thus should be the same for all ' \
                  'Accounts owned by a single user.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AccountID: (PATH, 'accountID'),
                  Instruments: (QUERY, 'instruments')}

    # valid responses
    responses = {200: {'instruments': ArrayInstrument, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (400, 401, 405)


class PATCHAccountIDConfiguration(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'PATCH'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/configuration')

    # description of endpoint
    description = 'Set the client-configurable portions of an Account.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID')}

    # valid responses
    responses = {200: {'clientConfigureTransaction': ClientConfigureTransaction, 'lastTransactionID': TransactionID},
                 400: {'clientConfigureRejectTransaction': ClientConfigureRejectTransaction,
                       'lastTransactionID': TransactionID, 'errorCode': str, 'errorMessage': str},
                 403: {'clientConfigureRejectTransaction': ClientConfigureRejectTransaction,
                       'lastTransactionID': TransactionID, 'errorCode': str, 'errorMessage': str}}

    # error msgs'
    error = (401, 404, 405)

    # json schema representation
    request_schema = {Alias: 'alias', DecimalNumber: 'marginRate'}


class GETAccountIDChanges(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/changes')
    # description of endpoint
    description = 'Endpoint used to poll an Account for its current state and changes since a specified TransactionID.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), SinceTransactionID: (QUERY, 'sinceTransactionID')}

    # valid responses
    responses = {200: {'changes': AccountChanges, 'state': AccountChangesState, 'lastTransactionID': TransactionID}}

    # error msgs'
    error = (401, 404, 405, 416)
