from ..definitions.types import *
from .metaclass import *


class GETInstrumentsCandles(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/instruments/{instrument}/candles'

    # description of endpoint
    description = 'Fetch candlestick data for an instrument.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'instrument', 'located': 'path', 'type': 'InstrumentName', 'description': 'InstrumentName'},
        {'name': 'price', 'located': 'query', 'type': 'string', 'description': 'string'},
        {'name': 'granularity', 'located': 'query', 'type': 'CandlestickGranularity',
         'description': 'CandlestickGranularity'},
        {'name': 'count', 'located': 'query', 'type': 'int', 'description': 'int'},
        {'name': 'from', 'located': 'query', 'type': 'DateTime', 'description': 'DateTime'},
        {'name': 'to', 'located': 'query', 'type': 'DateTime', 'description': 'DateTime'},
        {'name': 'smooth', 'located': 'query', 'type': 'boolean', 'description': 'boolean'},
        {'name': 'incluclassirst', 'located': 'query', 'type': 'boolean', 'description': 'boolean'},
        {'name': 'dailyAlignment', 'located': 'query', 'type': 'int', 'description': 'int'},
        {'name': 'alignmentTimezone', 'located': 'query', 'type': 'string', 'description': 'string'},
        {'name': 'weeklyAlignment', 'located': 'query', 'type': 'WeeklyAlignment',
         'description': 'WeeklyAlignment'},
    ]

    # valid responses
    responses = {'200': {'instrument': InstrumentName, 'granularity': CandlestickGranularity, 'candles': Array[Candlestick]}}

    # error msgs'
    error = ['400', '401', '404', '405']



class GETInstrumentOrderBook(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/instruments/{instrument}/orderBook'

    # description of endpoint
    description = 'Fetch a gzip compressed order book for an instrument.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'instrument', 'located': 'path', 'type': 'InstrumentName', 'description': 'InstrumentName'},
        {'name': 'time', 'located': 'query', 'type': 'DateTime', 'description': 'DateTime'},
    ]

    # valid responses
    responses = {'200': {'orderBook': OrderBook}}

    # error msgs'
    error = ['400', '401', '404', '405']


class GETInstrumentsPositionBook(object):

    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = '/v3/instruments/{instrument}/positionBook'

    # description of endpoint
    description = 'Fetch a gzip compressed position book for an instrument.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': 'string', 'description': 'string'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': 'AcceptDatetimeFormat',
         'description': 'AcceptDatetimeFormat'},
        {'name': 'instrument', 'located': 'path', 'type': 'InstrumentName', 'description': 'InstrumentName'},
        {'name': 'time', 'located': 'query', 'type': 'DateTime', 'description': 'DateTime'},
    ]

    # valid responses
    responses = {'200': {'positionBook': PositionBook}}

    # error msgs'
    error = ['400', '401', '404', '405']

