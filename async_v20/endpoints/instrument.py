from .annotations import *
from .base import EndPoint, HEADER, PATH, QUERY
from ..definitions.primitives import *
from ..definitions.types import *

__all__ = ['GETInstrumentsCandles', 'GETInstrumentOrderBook', 'GETInstrumentsPositionBook']


class GETInstrumentsCandles(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/instruments/', InstrumentName, '/candles')

    # description of endpoint
    description = 'Fetch candlestick data for an instrument.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  InstrumentName: (PATH, 'instrument'), PriceComponent: (QUERY, 'price'),
                  CandlestickGranularity: (QUERY, 'granularity'), Count: (QUERY, 'count'), FromTime: (QUERY, 'from'),
                  ToTime: (QUERY, 'to'), Smooth: (QUERY, 'smooth'), IncludeFirstQuery: (QUERY, 'includeFirst'),
                  DailyAlignment: (QUERY, 'dailyAlignment'), AlignmentTimezone: (QUERY, 'alignmentTimezone'),
                  WeeklyAlignment: (QUERY, 'weeklyAlignment')}

    # valid responses
    responses = {
        200: {'instrument': InstrumentName, 'granularity': CandlestickGranularity, 'candles': ArrayCandlestick}}

    # error msgs'
    error = (400, 401, 404, 405)


class GETInstrumentOrderBook(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/instruments/', InstrumentName, '/orderBook')

    # description of endpoint
    description = 'Fetch a gzip compressed order book for an instrument.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  InstrumentName: (PATH, 'instrument'), DateTime: (QUERY, 'time')}

    # valid responses
    responses = {200: {'orderBook': OrderBook}}

    # error msgs'
    error = (400, 401, 404, 405)


class GETInstrumentsPositionBook(EndPoint):
    # the HTTP verb to use for this endpoint
    method = 'GET'

    # path to endpoint
    path = ('/v3/instruments/', InstrumentName, '/positionBook')

    # description of endpoint
    description = 'Fetch a gzip compressed position book for an instrument.'

    # parameters required to send to endpoint
    parameters = {Authorization: (HEADER, 'Authorization'), AcceptDatetimeFormat: (HEADER, 'Accept-Datetime-Format'),
                  InstrumentName: (PATH, 'instrument'), DateTime: (QUERY, 'time')}

    # valid responses
    responses = {200: {'positionBook': PositionBook}}

    # error msgs'
    error = (400, 401, 404, 405)
