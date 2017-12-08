from typing import List


class EndPoint(object):
    """Base object representation of an endpoint"""

    # Default host to use unless otherwise specified by a derived class
    host = 'REST'

    # Path needs to be a Path object
    path = ()

    # the HTTP verb to use for this endpoint
    method = str

    # description of endpoint
    description = str

    # parameters required to send to endpoint
    parameters = List[dict]

    # valid responses
    responses = List[dict]

    # error msgs'
    error = List[str]

    # json format the data body as per the response_schema below
    request_schema = dict()
