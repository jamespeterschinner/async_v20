from ..definitions.types import *
from .metaclass import *
from .annotations import *


class GETInstrumentsCandles(object):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/instruments/', Instrument, '/candles')

    # description of endpoint
    description = 'Fetch candlestick data for an instrument.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'instrument', 'located': 'path', 'type': InstrumentName, 'description': 'InstrumentName'},
        {'name': 'price', 'located': 'query', 'type': Price, 'description': 'str'},
        {'name': 'granularity', 'located': 'query', 'type': CandlestickGranularity,
         'description': 'CandlestickGranularity'},
        {'name': 'count', 'located': 'query', 'type': Count, 'description': 'int'},
        {'name': 'from', 'located': 'query', 'type': FromDateTime, 'description': 'DateTime'},
        {'name': 'to', 'located': 'query', 'type': ToDateTime, 'description': 'DateTime'},
        {'name': 'smooth', 'located': 'query', 'type': Smooth, 'description': 'boolean'},
        {'name': 'incluclassirst', 'located': 'query', 'type': Incluclassirst, 'description': 'boolean'},
        {'name': 'dailyAlignment', 'located': 'query', 'type': DailyAlignment, 'description': 'int'},
        {'name': 'alignmentTimezone', 'located': 'query', 'type': AlignmentTimezone, 'description': 'str'},
        {'name': 'weeklyAlignment', 'located': 'query', 'type': WeeklyAlignment,
         'description': 'WeeklyAlignment'},
    ] # TODO ASK OANDA if incluc.. is a typo

    # valid responses
    responses = {
        200: {'instrument': InstrumentName, 'granularity': CandlestickGranularity, 'candles': Array[Candlestick]}}

    # error msgs'
    error = (400, 401, 404, 405)


class GETInstrumentOrderBook(object):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/instruments/', Instrument, '/orderBook')

    # description of endpoint
    description = 'Fetch a gzip compressed order book for an instrument.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'instrument', 'located': 'path', 'type': InstrumentName, 'description': 'InstrumentName'},
        {'name': 'time', 'located': 'query', 'type': DateTime, 'description': 'DateTime'},
    ]

    # valid responses
    responses = {200: {'orderBook': OrderBook}}

    # error msgs'
    error = (400, 401, 404, 405)


class GETInstrumentsPositionBook(object):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/instruments/', Instrument, '/positionBook')

    # description of endpoint
    description = 'Fetch a gzip compressed position book for an instrument.'

    # parameters required to send to endpoint
    parameters = [
        {'name': 'Authorization', 'located': 'header', 'type': Authorization, 'description': 'str'},
        {'name': 'Accept-Datetime-Format', 'located': 'header', 'type': AcceptDatetimeFormat,
         'description': 'AcceptDatetimeFormat'},
        {'name': 'instrument', 'located': 'path', 'type': InstrumentName, 'description': 'InstrumentName'},
        {'name': 'time', 'located': 'query', 'type': DateTime, 'description': 'DateTime'},
    ]

    # valid responses
    responses = {200: {'positionBook': PositionBook}}

    # error msgs'
    error = (400, 401, 404, 405)