from typing import List
from ..helpers import sleep

class Path(object):
    """capture the construction of a path"""

    def __init__(self, *path):
        self.path = path

    async def __call__(self, arguments: dict):
        async def lookup(segment):
            await sleep()
            return arguments[segment]

        return ''.join([segment if isinstance(segment, str)
                       else await lookup(segment)
                       for segment in self.path])


class EndPoint(object):
    """Base object representation of an endpoint"""

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



    @classmethod
    def header_args(cls):
        return

    @classmethod
    def query_args(cls):
        return [parameter['typ'] for parameter
                in cls.parameters if parameter['located'] == 'query']
