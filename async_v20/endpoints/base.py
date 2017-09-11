from typing import List
from inspect import Signature, Parameter, isclass
import inspect

class Path(object):
    """capture the construction of a path"""

    def __init__(self, *args):
        self.path = args
        self.sig = Signature([Parameter(name=cls.__name__.lower(), kind=Parameter.POSITIONAL_OR_KEYWORD,
                                        annotation=cls) for cls in args if isclass(cls)])
        self.__call__.__signature__ = self.sig

    def __call__(self, *args, **kwargs):
        bound = self.sig.bind(*args, **kwargs)
        annotations = (param.annotation for param in self.sig.parameters.values())
        values = (value for value in bound.arguments.values())
        lookup = {annotation: value for annotation, value in zip(annotations, values)}
        return ''.join(segment if isinstance(segment, str)
                       else lookup[segment]
                       for segment in self.path)


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