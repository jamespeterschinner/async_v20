from .annotations import *
from .base import EndPoint, HEADER, PATH, QUERY
from ..definitions.primitives import *
from ..definitions.types import *

__all__ = ['GETPricing', 'GETPricingStream']


class GETPricing(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/pricing')

    # description of endpoint
    description = 'Get pricing information for a specified list of Instruments within an Account.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), Instruments: (QUERY, 'instruments'), DateTime: (QUERY, 'since')}

    # valid responses
    responses = {200: {'prices': ArrayPrice, 'time': DateTime}}

    # error msgs'
    error = (400, 401, 404, 405)


class GETPricingStream(EndPoint):
    # host to use for this endpoint
    host = 'STREAM'

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/accounts/', AccountID, '/pricing/stream')

    # description of endpoint
    description = '''Get a stream of Account Prices starting from when the request is made.
    This pricing stream does not include every single price created for the Account, 
    but instead will provide at most 4 prices per second (every 250 milliseconds) 
    for each instrument being requested. If more than one price is created for an instrument 
    during the 250 millisecond window, only the price in effect at the end of the window is sent.
    This means that during periods of rapid price movement, subscribers to this stream will 
    not be sent every price. Pricing windows for different connections to the price stream 
    are not all aligned in the same way (i.e.they are not all aligned to the top of the second).
    This means that during periods of rapid price movement, different subscribers may observe 
    different prices depending on their alignment.'''

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  AccountID: (PATH, 'accountID'), Instruments: (QUERY, 'instruments'), Snapshot: (QUERY, 'snapshot')}

    # valid responses
    responses = {200: {'PRICE': Price, 'HEARTBEAT': PricingHeartbeat}}

    # error msgs'
    error = (400, 401, 404, 405)
