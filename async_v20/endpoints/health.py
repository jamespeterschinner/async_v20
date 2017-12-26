from .health_annotations import *
from ..definitions.health_types import *
from ..endpoints.base import EndPoint, PATH, QUERY, HEALTH


class GETServices(EndPoint):
    host = HEALTH

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/services',)

    # valid responses
    responses = {200: {'services': ArrayService}}


class GETService(EndPoint):
    host = HEALTH

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/services/', ServiceID)

    parameters = {ServiceID: (PATH, 'service-id')}

    # valid responses
    responses = {200: Service}


class GETServiceLists(EndPoint):
    host = HEALTH

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/service-lists',)

    # valid responses
    responses = {200: {'lists': ArrayServiceList}}


class GETServiceList(EndPoint):
    host = HEALTH

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/service-lists/', ServiceListID)

    parameters = {ServiceListID: (PATH, 'service_list_id')}

    # valid responses
    responses = {200: {'lists': ServiceList}}


class GETEvents(EndPoint):
    host = HEALTH

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/services/', ServiceID, '/events')

    # parameters required to send to endpoint
    parameters = {ServiceID: (PATH, 'service-id'), Start: (QUERY, 'start'), End: (QUERY, 'end')}

    # valid responses
    responses = {200: {'events': ArrayEvent}}


class GETCurrentEvent(EndPoint):
    host = HEALTH

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/services/', ServiceID, '/events/current')

    # parameters required to send to endpoint
    parameters = {ServiceID: (PATH, 'service-id')}

    # valid responses
    responses = {200: {'events': Event}}


class GETEvent(EndPoint):
    host = HEALTH

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/services/', ServiceID, '/events/', EventSid)

    # parameters required to send to endpoint
    parameters = {ServiceID: (PATH, 'service-id'),
                  EventSid: (PATH, 'event-sid')}

    # valid responses
    responses = {200: {'events': Event}}


class GETStatuses(EndPoint):
    host = HEALTH

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/statuses',)

    # valid responses
    responses = {200: {'statuses': ArrayStatus}}


class GETStatus(EndPoint):
    host = HEALTH

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/statuses/', StatusID)

    # parameters required to send to endpoint
    parameters = {StatusID: (PATH, 'status-id')}

    # valid responses
    responses = {200: Status}


class GETImages(EndPoint):
    host = HEALTH

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/api/v1/status-images',)

    # valid responses
    responses = {200: {'images': ArrayImage}}
