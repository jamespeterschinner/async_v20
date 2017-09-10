from ..definitions.types import *
from .metaclass import *
from .annotations import *

class GETUserSpecifier(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/users/', UserSpecifier)

    # description of endpoint
    description = 'Fetch the user information for the specified user.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'userSpecifier', 'located': 'query', 'type': 'string', 'description': 'The User Specifier'},
    ]

    # valid responses
    responses = {200: {'userInfo': UserInfo}}

    # error msgs'
    error = [401, 403, 405]


class GETExternalInfo(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/users/', UserSpecifier, '/externalInfo')

    # description of endpoint
    description = 'Fetch the externally-available user information for the specified user.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'userSpecifier', 'located': 'query', 'type': 'string', 'description': 'The User Specifier'},
    ]

    # valid responses
    responses = {200: {'userInfo': UserInfoExternal}}

    # error msgs'
    error = (401, 403, 405)




