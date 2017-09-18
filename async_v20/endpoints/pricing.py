from .annotations import *
from .base import EndPoint, Path
from .metaclass import *
from ..definitions.descriptors import *
from ..definitions.types import *

__all__ = ['GETPricing', 'GETPricingStream']


class GETPricing(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = Path('/v3/accounts/', AccountID, '/pricing')

    # description of endpoint
    description = 'Get pricing information for a specified list of Instruments within an Account.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'instruments', 'located': 'query', 'type': Instruments,
         'description': 'List of InstrumentName (csv)'},
        {'name': 'since', 'located': 'query', 'type': DateTime, 'description': 'DateTime'},
        {'name': 'includeUnitsAvailable', 'located': 'query', 'type': IncludeUnitsAvailable, 'description': 'boolean'}
    ]

    # valid responses
    responses = {200: {'prices': Array[Price], 'time': DateTime}}

    # error msgs'
    error = (400, 401, 404, 405)


class GETPricingStream(EndPoint):
    # host to use for this endpoint
    host = 'STREAM'

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = Path('/v3/accounts/', AccountID, '/pricing/stream')

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
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'accountID', 'located': 'path', 'type': AccountID, 'description': 'AccountID'},
        {'name': 'instruments', 'located': 'query', 'type': Instruments,
         'description': 'List of InstrumentName (csv)'},
        {'name': 'snapshot', 'located': 'query', 'type': Snapshot, 'description': 'boolean'},
    ]

    # valid responses
    responses = {200: {'PRICE': Price, 'HEARTBEAT': PricingHeartbeat}}

    # error msgs'
    error = (400, 401, 404, 405)
