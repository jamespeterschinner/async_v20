class GETTransactions(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/transactions'

    # description of endpoint
    description = 'Get a list of Transactions pages that satisfy a time-based Transaction query.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'from', 'located': 'query', 'type': 'DateTime', 'description': 'DateTime'},
        {'name': 'to', 'located': 'query', 'type': 'DateTime', 'description': 'DateTime'},
        {'name': 'pageSize', 'located': 'query', 'type': 'integer', 'description': 'integer'},
        {'name': 'type', 'located': 'query', 'type': 'List of TransactionFilter (csv)',
         'description': 'List of TransactionFilter (csv)'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The requested time range of Transaction pages are provided.'},
    ]

    # error msgs'
    error = ['400', '401', '403', '404', '405', '416']

    # json schema representation
    schema = """
        {
            # 
            # The starting time provided in the request.
            # 
            from : (DateTime),

            # 
            # The ending time provided in the request.
            # 
            to : (DateTime),

            # 
            # The pageSize provided in the request
            # 
            pageSize : (integer),

            # 
            # The Transaction-type filter provided in the request
            # 
            type : (Array[TransactionFilter]),

            # 
            # The number of Transactions that are contained in the pages returned
            # 
            count : (integer),

            # 
            # The list of URLs that represent idrange queries providing the data for
            # each page in the query results
            # 
            pages : (Array[string]),

            # 
            # The ID of the most recent Transaction created for the Account
            # 
            lastTransactionID : (TransactionID)
        }
        """


class GETTransactionID(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/transactions/{transactionID}'

    # description of endpoint
    description = 'Get the details of a single Account Transaction.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'transactionID', 'located': 'path', 'type': 'TransactionID', 'description': 'TransactionID'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The details of the requested Transaction are provided.'},
    ]

    # error msgs'
    error = ['401', '404', '405']

    # json schema representation
    schema = """
        {
            # 
            # The details of the Transaction requested
            # 
            transaction : (Transaction),

            # 
            # The ID of the most recent Transaction created for the Account
            # 
            lastTransactionID : (TransactionID)
        }
        """


class GETIDrange(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/transactions/idrange'

    # description of endpoint
    description = 'Get a range of Transactions for an Account based on the Transaction IDs.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'from', 'located': 'query', 'type': 'TransactionID', 'description': 'TransactionID'},
        {'name': 'to', 'located': 'query', 'type': 'TransactionID', 'description': 'TransactionID'},
        {'name': 'type', 'located': 'query', 'type': 'List of TransactionFilter (csv)',
         'description': 'List of TransactionFilter (csv)'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The requested time range of Transactions are provided.'},
    ]

    # error msgs'
    error = ['400', '401', '404', '405', '416']

    # json schema representation
    schema = """
        {
            # 
            # The list of Transactions that satisfy the request.
            # 
            transactions : (Array[Transaction]),

            # 
            # The ID of the most recent Transaction created for the Account
            # 
            lastTransactionID : (TransactionID)
        }
        """


class GETSinceID(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/transactions/sinceid'

    # description of endpoint
    description = 'Get a range of Transactions for an Account starting at (but not including) a provided Transaction ID.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'id', 'located': 'query', 'type': 'TransactionID', 'description': 'TransactionID'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The requested time range of Transactions are provided.'},
    ]

    # error msgs'
    error = ['400', '401', '404', '405', '416']

    # json schema representation
    schema = """
        {
            # 
            # The list of Transactions that satisfy the request.
            # 
            transactions : (Array[Transaction]),

            # 
            # The ID of the most recent Transaction created for the Account
            # 
            lastTransactionID : (TransactionID)
        }
        """


class GETTransactionsStream(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/transactions/stream'

    # description of endpoint
    description = 'Get a stream of Transactions for an Account starting from when the request is made.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– Connecting to the Transaction Stream was successful.'},
    ]

    # error msgs'
    error = ['400', '401', '404', '405']

    # json schema representation
    schema = ''
