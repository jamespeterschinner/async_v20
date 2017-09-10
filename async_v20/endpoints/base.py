from typing import List
from inspect import signature
import json
import re


class EndPoint(object):
    """Base object representation of an endpoint"""

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
        return [parameter['name'] for parameter
                in cls.parameters if parameter['located'] == 'header']

    @classmethod
    def query_args(cls):
        return [parameter['name'] for parameter
                in cls.parameters if parameter['located'] == 'query']

    @classmethod
    def path_args(cls):
        return [parameter['name'] for parameter
                in cls.parameters if parameter['located'] == 'path']