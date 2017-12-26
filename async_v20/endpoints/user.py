from .annotations import UserSpecifier, Authorization
from .base import EndPoint, HEADER, QUERY
from ..definitions.types import *

__all__ = ['GETUserSpecifier', 'GETExternalInfo']


class GETUserSpecifier(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/users/', UserSpecifier)

    # description of endpoint
    description = 'Fetch the user information for the specified user.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), UserSpecifier: (QUERY, 'userSpecifier')}

    # valid responses
    responses = {200: {'userInfo': UserInfo}}

    # error msgs'
    error = [401, 403, 405]


class GETExternalInfo(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/users/', UserSpecifier, '/externalInfo')

    # description of endpoint
    description = 'Fetch the externally-available user information for the specified user.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), UserSpecifier: (QUERY, 'userSpecifier')}

    # valid responses
    responses = {200: {'userInfo': UserInfoExternal}}

    # error msgs'
    error = (401, 403, 405)
