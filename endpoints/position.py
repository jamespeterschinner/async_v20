class GETPositions(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/positions'

    # description of endpoint
    description = 'List all Positions for an Account. The Positions returned are for every instrument that has had a position during the lifetime of an the Account.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The Account’s Positions are provided.'},
    ]

    # error msgs'
    error = ['401', '404', '405']

    # json schema representation
    schema = """
        {
            # 
            # The list of Account Positions.
            # 
            positions : (Array[Position]),

            # 
            # The ID of the most recent Transaction created for the Account
            # 
            lastTransactionID : (TransactionID)
        }
        """


class GETOpenPositions(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/openPositions'

    # description of endpoint
    description = 'List all open Positions for an Account. An open Position is a Position in an Account that currently has a Trade opened for it.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The Account’s open Positions are provided.'},
    ]

    # error msgs'
    error = ['401', '404', '405']

    # json schema representation
    schema = """
        {
            # 
            # The list of open Positions in the Account.
            # 
            positions : (Array[Position]),

            # 
            # The ID of the most recent Transaction created for the Account
            # 
            lastTransactionID : (TransactionID)
        }
        """


class GETPositionsInstrument(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/accounts/{accountID}/positions/{instrument}'

    # description of endpoint
    description = 'Get the details of a single Instrument’s Position in an Account. The Position may by open or not.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'instrument', 'located': 'path', 'type': 'InstrumentName', 'description': 'InstrumentName'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The Position is provided.'},
    ]

    # error msgs'
    error = ['401', '404', '405']

    # json schema representation
    schema = """
        {
            # 
            # The requested Position.
            # 
            position : (Position),

            # 
            # The ID of the most recent Transaction created for the Account
            # 
            lastTransactionID : (TransactionID)
        }
        """


class PUTPositionsInstrumentClose(object):

    # the HTTP verb to use for this endpoint
    method = 'PUT'

    # path to endpoint
    path = '/v3/accounts/{accountID}/positions/{instrument}/close'

    # description of endpoint
    description = 'Closeout the open Position for a specific instrument in an Account.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': 'AccountID', 'description': 'AccountID'},
        {'name': 'instrument', 'located': 'path', 'type': 'InstrumentName', 'description': 'InstrumentName'},
    ]

    # valid responses
    responses = [
        {'response': '200', 'description': '– The Position closeout request has been successfully processed.'},
        {'response': '400',
         'description': '– The Parameters provided that describe the Position closeout are invalid.'},
        {'response': '404',
         'description': '– The Account or one or more of the Positions specified does not exist.'},
    ]

    # error msgs'
    error = ['401', '405']

    # json schema representation
    schema = """
        {
            # 
            # Indication of how much of the long Position to closeout. Either the
            # string “ALL”, the string “NONE”, or a DecimalNumber representing how many
            # units of the long position to close using a PositionCloseout MarketOrder.
            # The units specified must always be positive.
            # 
            longUnits : (string, default=ALL),

            # 
            # The client extensions to add to the MarketOrder used to close the long
            # position.
            # 
            longClientExtensions : (ClientExtensions),

            # 
            # Indication of how much of the short Position to closeout. Either the
            # string “ALL”, the string “NONE”, or a DecimalNumber representing how many
            # units of the short position to close using a PositionCloseout
            # MarketOrder. The units specified must always be positive.
            # 
            shortUnits : (string, default=ALL),

            # 
            # The client extensions to add to the MarketOrder used to close the short
            # position.
            # 
            shortClientExtensions : (ClientExtensions)
        }
        """