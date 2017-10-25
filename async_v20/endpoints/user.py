from .annotations import *
from .base import EndPoint, Path
from ..definitions.types import *
from .annotations import UserSpecifier, Authorization

__all__ = ['GETUserSpecifier', 'GETExternalInfo']


class GETUserSpecifier(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = Path('/v3/users/', UserSpecifier)

    # description of endpoint
    description = 'Fetch the user information for the specified user.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'string'},
        {'name': 'userSpecifier', 'located': 'query', 'type': UserSpecifier, 'description': 'The User Specifier'},
    ]

    # valid responses
    responses = {200: {'userInfo': UserInfo}}

    # error msgs'
    error = [401, 403, 405]


class GETExternalInfo(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = Path('/v3/users/', UserSpecifier, '/externalInfo')

    # description of endpoint
    description = 'Fetch the externally-available user information for the specified user.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'string'},
        {'name': 'userSpecifier', 'located': 'query', 'type': UserSpecifier, 'description': 'The User Specifier'},
    ]

    # valid responses
    responses = {200: {'userInfo': UserInfoExternal}}

    # error msgs'
    error = (401, 403, 405)
