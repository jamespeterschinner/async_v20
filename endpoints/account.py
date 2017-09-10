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
    responses = [
        {'response': '200', 'description': '– The list of authorized Accounts has been provided.'},
    ]

    # error msgs'
    error = ['401', '405']

    # json schema representation
    schema = """
        {
            # 
            # The list of Accounts the client is authorized to access and their
            # associated properties.
            # 
            accounts : (Array[AccountProperties])
        }
        """


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
    responses = [
        {'response': '200', 'description': 'The full Account details are provided'},
    ]

    # error msgs'
    error = ['400', '401', '405']

    # json schema representation
    schema = """
        {
            # 
            # The full details of the requested Account.
            # 
            account : (Account),

            # 
            # The ID of the most recent Transaction created for the Account.
            # 
            lastTransactionID : (TransactionID)
        }
        """


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
    responses = [
        {'response': '200', 'description': '– The Account summary  are provided'},
    ]

    # error msgs'
    error = ['400', '401', '405']

    # json schema representation
    schema = """
        {
            # 
            # The summary of the requested Account.
            # 
            account : (AccountSummary),

            # 
            # The ID of the most recent Transaction created for the Account.
            # 
            lastTransactionID : (TransactionID)
        }
        """


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
    responses = [
        {'response': '200',
         'description': '– The list of tradeable instruments for the Account has been provided.'},
    ]

    # error msgs'
    error = ['400', '401', '405']

    # json schema representation
    schema = """
        {
            # 
            # The requested list of instruments.
            # 
            instruments : (Array[Instrument]),

            # 
            # The ID of the most recent Transaction created for the Account.
            # 
            lastTransactionID : (TransactionID)
        }
        """


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
    responses = [
        {'response': '200', 'description': '– The Account was configured successfully.'},
        {'response': '400', 'description': '– The configuration specification was invalid.'},
        {'response': '403', 'description': '– The configuration operation was forbidden on the Account.'},
    ]

    # error msgs'
    error = ['401', '404', '405']

    # json schema representation
    schema = """
        {
            # 
            # Client-classined alias (name) for the Account
            # 
            alias : (string),

            # 
            # The string representation of a decimal number.
            # 
            marginRate : (DecimalNumber)
        }
        """


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
    responses = [
        {'response': '200', 'description': '– The Account state and changes are provided.'},
    ]

    # error msgs'
    error = ['401', '404', '405', '416']

    # json schema representation
    schema = """
        {
            # 
            # The changes to the Account’s Orders, Trades and Positions since the
            # specified Transaction ID. Only provided if the sinceTransactionID is
            # supplied to the poll request.
            # 
            changes : (AccountChanges),
    
            # 
            # The Account’s current price-dependent state.
            # 
            state : (AccountChangesState),
    
            # 
            # The ID of the last Transaction created for the Account.  This Transaction
            # ID should be used for future poll requests, as the client has already
            # observed all changes up to and including it.
            # 
            lastTransactionID : (TransactionID)
        }
        """
