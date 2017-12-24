from .annotations import *
from .types import *
from ..endpoints.base import EndPoint


class GETServices(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/services',)

    # valid responses
    responses = {200: {'services': ArrayService}}


class GETService(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/services', ServiceID)

    # valid responses
    responses = {200:  Service}


class GETServiceLists(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/service-lists',)

    # valid responses
    responses = {200: {'lists': ArrayServiceList}}


class GETServiceList(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/service-lists', ServiceListId)

    # valid responses
    responses = {200: {'lists': ServiceList}}


class GETEvents(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/services/', ServiceID, '/events')

    # parameters required to send to endpoint
    parameters = [
        {'name': 'start', 'located': 'query', 'type': Start, 'description': 'DateTime'},
        {'name': 'end', 'located': 'query', 'type': End, 'description': 'DateTime'}
    ]

    # valid responses
    responses = {200: {'events': ArrayEvent}}


class GETCurrentEvent(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/services/', ServiceID, '/events/current')

    # valid responses
    responses = {200: {'events': Event}}


class GETEvent(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/services/', ServiceID, '/events/', EventSid)

    # valid responses
    responses = {200: {'events': Event}}

class GETStatus(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/statuses',)

    # valid responses
    responses = {200: {'status': ArrayStatus}}

class GETStatu(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/statuses', StatusId)

    # valid responses
    responses = {200: Status}