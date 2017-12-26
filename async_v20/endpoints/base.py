HEADER = 'header'
PATH = 'path'
QUERY = 'query'
HEALTH = 'HEALTH'

class EndPoint(object):
    """Base object representation of an endpoint"""

    # Default host to use unless otherwise specified by a derived class
    host = 'REST'

    # Path needs to be a Path object
    path = ()

    # the HTTP verb to use for this endpoint
    method = ''

    # description of endpoint
    description = ''

    # parameters required to send to endpoint
    parameters = {}

    # valid responses
    responses = {}

    # error msgs'
    error = ()

    # json format the data body as per the response_schema below
    request_schema = {}
