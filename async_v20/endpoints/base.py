from typing import List


class Path(object):
    """capture the construction of a path"""

    def __init__(self, *path):
        self.path = path

    def __call__(self, arguments: dict, default: dict):
        def lookup(segment):
            try:
                result = arguments[segment]
            except KeyError:
                result = default[segment]
            return result

        return ''.join([segment if isinstance(segment, str)
                        else lookup(segment)
                        for segment in self.path])


class EndPoint(object):
    """Base object representation of an endpoint"""

    # Default host to use unless otherwise specified by a derived class
    host = 'REST'

    # Path needs to be a Path object
    path = Path

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
