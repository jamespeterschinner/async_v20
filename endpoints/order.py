class POSTOrders(object):

    # the HTTP verb to use for this endpoint
    method = 'POST'

    # path to endpoint
    path = '/v3/accounts/{accountID}/orders'

    # description of endpoint
    description = 'Create an Order for an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
    ]

    # valid responses
    responses = [
        {'response': '201', 'description': '– The Order was created as specified'},
        {'response': '400', 'description': '– The Order specification was invalid'},
        {'response': '404', 'description': '– The Order or Account specified does not exist.'},
    ]

    # error msgs'
    error = ['401', '403', '405']

    # json schema representation
    schema = """
        {
            # 
            # Specification of the Order to create
            # 
            order : (OrderRequest)
        }
        """


class GETOrders(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/orders'

    # description of endpoint
    description = 'Get a list of Orders for an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'ids', 'located': 'query', 'type': 'List of OrderID (csv)',
         'description': 'List of OrderID (csv)'},
        {'name': 'state', 'located': 'query', 'type': 'OrderStateFilter', 'description': 'OrderStateFilter'},
        {'name': 'instrument', 'located': 'query', 'type': 'InstrumentName', 'description': 'InstrumentName'},
        {'name': 'count', 'located': 'query', 'type': 'integer', 'description': 'integer'},
        {'name': 'beforeID', 'located': 'query', 'type': 'OrderID', 'description': 'OrderID'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The list of Orders requested'},
    ]

    # error msgs'
    error = ['400', '404', '405']

    # json schema representation
    schema = """
        {
            # 
            # The list of Order detail objects
            # 
            orders : (Array[Order]),

            # 
            # The ID of the most recent Transaction created for the Account
            # 
            lastTransactionID : (TransactionID)
        }
        """


class GETPendingOrders(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/pendingOrders'

    # description of endpoint
    description = 'List all pending Orders in an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– List of pending Orders for the Account'},
    ]

    # error msgs'
    error = ['401', '404', '405']

    # json schema representation
    schema = """
        {
            # 
            # The list of pending Order details
            # 
            orders : (Array[Order]),

            # 
            # The ID of the most recent Transaction created for the Account
            # 
            lastTransactionID : (TransactionID)
        }
        """


class GETOrderSpecifier(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/orders/{orderSpecifier}'

    # description of endpoint
    description = 'Get details for a single Order in an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'orderSpecifier', 'located': 'path', 'type': 'OrderSpecifier', 'description': 'OrderSpecifier'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The details of the Order requested'},
    ]

    # error msgs'
    error = ['401', '404', '405']

    # json schema representation
    schema = """
        {
            # 
            # The details of the Order requested
            # 
            order : (Order),

            # 
            # The ID of the most recent Transaction created for the Account
            # 
            lastTransactionID : (TransactionID)
        }
        """


class PUTOrderSpecifier(object):

    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = '/v3/accounts/{accountID}/orders/{orderSpecifier}'

    # description of endpoint
    description = 'Replace an Order in an Account by simultaneously cancelling it and creating a replacement Order'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'orderSpecifier', 'located': 'path', 'type': 'OrderSpecifier', 'description': 'OrderSpecifier'},
    ]

    # valid responses
    responses = [
        {'response': '201', 'description': '– The Order was successfully cancelled and replaced'},
        {'response': '400', 'description': '– The Order specification was invalid'},
        {'response': '404', 'description': '– The Account or Order specified does not exist.'},
    ]

    # error msgs'
    error = ['401', '405']

    # json schema representation
    schema = """
        {
            # 
            # Specification of the replacing Order
            # 
            order : (OrderRequest)
        }
        """


class PUTOrderSpecifierCancel(object):

    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = '/v3/accounts/{accountID}/orders/{orderSpecifier}/cancel'

    # description of endpoint
    description = 'Cancel a pending Order in an Account'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'orderSpecifier', 'located': 'path', 'type': 'OrderSpecifier', 'description': 'OrderSpecifier'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The Order was cancelled as specified'},
        {'response': '404', 'description': '– The Account or Order specified does not exist.'},
    ]

    # error msgs'
    error = ['401', '405']

    # json schema representation
    schema = """
        {
            # 
            # The Transaction that cancelled the Order
            # 
            orderCancelTransaction : (OrderCancelTransaction),

            # 
            # The IDs of all Transactions that were created while satisfying the
            # request.
            # 
            relatedTransactionIDs : (Array[TransactionID]),

            # 
            # The ID of the most recent Transaction created for the Account
            # 
            lastTransactionID : (TransactionID)
        }
        """


class PUTClientExtensions(object):

    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = '/v3/accounts/{accountID}/orders/{orderSpecifier}/clientExtensions'

    # description of endpoint
    description = 'Update the Client Extensions for an Order in an Account. Do not set, modify, or delete clientExtensions if your account is associated with MT4.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'orderSpecifier', 'located': 'path', 'type': 'OrderSpecifier', 'description': 'OrderSpecifier'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The Order’s Client Extensions were successfully modified'},
        {'response': '400', 'description': '– The Order Client Extensions specification was invalid'},
        {'response': '404', 'description': '– The Account or Order specified does not exist.'},
    ]

    # error msgs'
    error = ['401', '405']

    # json schema representation
    schema = """
        {
            # 
            # The Client Extensions to update for the Order. Do not set, modify, or
            # delete clientExtensions if your account is associated with MT4.
            # 
            clientExtensions : (ClientExtensions),

            # 
            # The Client Extensions to update for the Trade created when the Order is
            # filled. Do not set, modify, or delete clientExtensions if your account is
            # associated with MT4.
            # 
            tradeClientExtensions : (ClientExtensions)
        }
        """
