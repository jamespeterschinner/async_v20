import logging

import pandas as pd

from .helpers import domain_check
from ..exceptions import InvalidValue, InvalidFormatArguments

logger = logging.getLogger(__name__)

__all__ = ['AcceptDatetimeFormat', 'AccountFinancingMode', 'AccountID', 'AccountUnits', 'CancellableOrderType',
           'CandlestickGranularity', 'ClientComment', 'ClientID', 'ClientTag', 'Currency', 'DateTime', 'DecimalNumber',
           'Direction', 'FundingReason', 'InstrumentName', 'InstrumentType', 'LimitOrderReason',
           'MarketIfTouchedOrderReason', 'MarketOrderMarginCloseoutReason', 'MarketOrderReason', 'OrderCancelReason',
           'OrderFillReason', 'OrderID', 'OrderPositionFill', 'OrderSpecifier', 'OrderState', 'OrderStateFilter',
           'OrderTriggerCondition', 'OrderType', 'PositionAggregationMode', 'PriceComponent', 'PriceStatus',
           'PriceValue', 'Reason', 'RequestID', 'StopLossOrderReason', 'StopOrderReason',
           'TakeProfitOrderReason', 'TimeInForce', 'TradeID', 'TradePL', 'TradeSpecifier', 'TradeState',
           'TradeStateFilter', 'TrailingStopLossOrderReason', 'TransactionFilter', 'TransactionID',
           'TransactionRejectReason', 'TransactionType', 'WeeklyAlignment', 'GuaranteedStopLossOrderMode']


class Primitive(object):
    """Mixin class to denote primitive type"""
    pass


class Specifier(object):
    """Mixin class to denote primitive type can be used for
    specifying an Order/Trade/Position"""
    # This is necessary due to different types using a mixture
    # of int and str which prevents inheritance due to 'Lay-out error'
    pass



class DateTime(Primitive):
    """A date and time value using either RFC3339 or UNIX time representation.
    """

    def __new__(cls, value, **kwargs):
        if not isinstance(value, (int, float, str)):
            pass
        else:
            value = str(value)
            if 'Z' not in value:
                seconds, decimal, fraction = value.partition('.')

                if not fraction and len(seconds) > 10:
                    seconds, fraction = value[:10], value[10:]
                # value has decimal number
                if fraction:
                    fraction = fraction + '000000000'[:-len(fraction)]
                else:
                    fraction = '000000000'

                value = int(seconds + fraction)
                kwargs.update(tz='UTC')

        return pd.Timestamp(value, **kwargs)


def _datetime_to_json(self, datetime_format):
    if datetime_format == 'RFC3339':
        nanoseconds = str(self.nanosecond)
        nanoseconds = nanoseconds + '000'[:-len(nanoseconds)]
        result = self.strftime(f'%Y-%m-%dT%H:%M:%S.%f{nanoseconds}Z')
    elif datetime_format == 'UNIX':
        result = str(self.value)
        result = f'{result[:-9]}.{result[-9:]}'
    else:
        msg = f'datetime_format {datetime_format} is not a valid value. It must be either "RFC3339" or "UNIX"'
        logger.error(msg)
        raise InvalidValue(msg)

    return result


pd.Timestamp.json = _datetime_to_json


class AccountFinancingMode(str, Primitive):
    """The financing mode of an Account
    """

    # Valid values
    values = {
        'NO_FINANCING': 'No financing is paid/charged for open Trades in the Account',
        'SECOND_BY_SECOND': 'Second-by-second financing is paid/charged for open Trades in the Account, '
                            'both daily and when the the Trade is closed',
        'DAILY': 'A full day’s worth of financing is paid/charged for open Trades in the Account '
                 'daily at 5pm New York time'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class AccountID(str, Primitive):
    """The string representation of an Account Identifier.
    """

    # Correct syntax of value
    format_syntax = '"-"-delimited string with format "{siteID}-{divisionID}-{userID}-{accountNumber}"'
    # Example of correct format
    example = '001-011-5838423-001'

    def __new__(cls, value):
        assert domain_check(value, example=cls.example)
        return super().__new__(cls, value)


class PositionAggregationMode(str, Primitive):
    """The way that position values for an Account are calculated and aggregated.
    """

    # Valid values
    values = {
        'ABSOLUTE_SUM': 'The Position value or margin for each side (long and short) of '
                        'the Position are computed independently and added together.',
        'MAXIMAL_SIDE': 'The Position value or margin for each side (long and short) '
                        'of the Position are computed independently. The Position value or '
                        'margin chosen is the maximal absolute value of the two.',
        'NET_SUM': 'The units for each side (long and short) of the Position are netted '
                   'together and the resulting value (long or short) is used to compute '
                   'the Position value or margin.'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class CandlestickGranularity(str, Primitive):
    """The granularity of a candlestick
    """

    # Valid values
    values = {
        'S5': '5 second candlesticks, minute alignment',
        'S10': '10 second candlesticks, minute alignment',
        'S15': '15 second candlesticks, minute alignment',
        'S30': '30 second candlesticks, minute alignment',
        'M1': '1 minute candlesticks, minute alignment',
        'M2': '2 minute candlesticks, hour alignment',
        'M4': '4 minute candlesticks, hour alignment',
        'M5': '5 minute candlesticks, hour alignment',
        'M10': '10 minute candlesticks, hour alignment',
        'M15': '15 minute candlesticks, hour alignment',
        'M30': '30 minute candlesticks, hour alignment',
        'H1': '1 hour candlesticks, hour alignment',
        'H2': '2 hour candlesticks, day alignment',
        'H3': '3 hour candlesticks, day alignment',
        'H4': '4 hour candlesticks, day alignment',
        'H6': '6 hour candlesticks, day alignment',
        'H8': '8 hour candlesticks, day alignment',
        'H12': '12 hour candlesticks, day alignment',
        'D': '1 day candlesticks, day alignment',
        'W': '1 week candlesticks, aligned to start of week',
        'M': '1 month candlesticks, aligned to first day of the month'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class WeeklyAlignment(str, Primitive):
    """The day of the week to use for candlestick granularities with weekly alignment.
    """

    # Valid values
    values = {
        'Monday': 'Monday',
        'Tuesday': 'Tuesday',
        'Wednesday': 'Wednesday',
        'Thursday': 'Thursday',
        'Friday': 'Friday',
        'Saturday': 'Saturday',
        'Sunday': 'Sunday'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class PriceComponent(str, Primitive):
    # Valid values
    values = {'M': 'midpoint candles',
              'B': 'bid candles',
              'A': 'ask candles'}

    # Pre-constructed permutations to speed up domain checking
    value_permutations = {'AB', 'B', 'BAM', 'AM', 'M',
                          'BM', 'AMB', 'MBA', 'MA', 'A',
                          'MB', 'ABM', 'BMA', 'MAB', 'BA'}

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.value_permutations)
        return super().__new__(cls, value)


class CancellableOrderType(str, Primitive):
    """The type of the Order.
    """

    # Valid values
    values = {
        'LIMIT': 'A Limit Order',
        'STOP': 'A Stop Order',
        'MARKET_IF_TOUCHED': 'A Market-if-touched Order',
        'TAKE_PROFIT': 'A Take Profit Order',
        'STOP_LOSS': 'A Stop Loss Order',
        'TRAILING_STOP_LOSS': 'A Trailing Stop Loss Order'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class OrderID(int, Primitive, Specifier):
    """The Order’s identifier, unique within the Order’s Account.
    """

    # Correct syntax of value
    format_syntax = 'The string representation of the OANDA-assigned OrderID. ' \
                    'OANDA-assigned OrderIDs are positive integers, and are derived from the ' \
                    'TransactionID of the Transaction that created the Order.'

    # Example of correct format
    example = '1523'

    def __new__(cls, value):
        return super().__new__(cls, value)


class OrderPositionFill(str, Primitive):
    """Specification of how Positions in the Account
    are modified when the Order is filled.
    """

    # Valid values
    values = {
        'OPEN_ONLY': 'When the Order is filled, only allow Positions to be opened or extended.',
        'REDUCE_FIRST': 'When the Order is filled, always fully reduce an existing Position '
                        'before opening a new Position.',
        'REDUCE_ONLY': 'When the Order is filled, only reduce an existing Position.',
        'DEFAULT': 'When the Order is filled, use REDUCE_FIRST behaviour for non-client hedging Accounts, '
                   'and OPEN_ONLY behaviour for client hedging Accounts.'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class OrderSpecifier(str, Primitive, Specifier):
    """The specification of an Order as referred to by clients
    """

    # Correct syntax of value
    format_syntax = 'Either the Order’s OANDA-assigned OrderID or the Order’s client-provided ' \
                    'ClientID prefixed by the "@" symbol'
    # Example of correct format
    example = '1523'

    def __new__(cls, value):
        return super().__new__(cls, value)


class OrderState(str, Primitive):
    """The current state of the Order.
    """

    # Valid values
    values = {
        'PENDING': 'The Order is currently pending execution',
        'FILLED': 'The Order has been filled',
        'TRIGGERED': 'The Order has been triggered',
        'CANCELLED': 'The Order has been cancelled'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class OrderStateFilter(str, Primitive):
    """The state to filter the requested Orders by.
    """

    # Valid values
    values = {
        'PENDING': 'The Orders that are currently pending execution',
        'FILLED': 'The Orders that have been filled',
        'TRIGGERED': 'The Orders that have been triggered',
        'CANCELLED': 'The Orders that have been cancelled',
        'ALL': 'The Orders that are in any of the possible states listed above'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class OrderTriggerCondition(str, Primitive):
    """Specification of which price component should be used when determining if an
    Order should be triggered and filled. This allows Orders to be triggered based
    on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (
    ask for sell, bid for buy) price depending on the desired behaviour. Orders are
    always filled using their default price component. This feature is only provided
    through the REST API. Clients who choose to specify a non-default trigger condition
    will not see it reflected in any of OANDA’s proprietary or partner trading platforms,
    their transaction history or their account statements. OANDA platforms always assume
    that an Order’s trigger condition is set to the default value when indicating the distance
    from an Order’s trigger price, and will always provide the default trigger condition
    when creating or modifying an Order.
    """

    # Valid values
    values = {
        'DEFAULT': 'Trigger an Order the "natural" way: '
                   'compare its price to the ask for long Orders and bid for short Orders.',
        'INVERSE': 'Trigger an Order the opposite of the "natural" way: '
                   'compare its price the bid for long Orders and ask for short Orders.',
        'BID': 'Trigger an Order by comparing its price to the bid regardless of whether it is long or short.',
        'ASK': 'Trigger an Order by comparing its price to the ask regardless of whether it is long or short.',
        'MID': 'Trigger an Order by comparing its price to the midpoint regardless of whether it is long or short.'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class OrderType(str, Primitive):
    """The type of the Order.
    """

    # Valid values
    values = {
        'MARKET': 'A Market Order',
        'LIMIT': 'A Limit Order',
        'STOP': 'A Stop Order',
        'MARKET_IF_TOUCHED': 'A Market-if-touched Order',
        'TAKE_PROFIT': 'A Take Profit Order',
        'STOP_LOSS': 'A Stop Loss Order',
        'TRAILING_STOP_LOSS': 'A Trailing Stop Loss Order'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class TimeInForce(str, Primitive):
    """The time-in-force of an Order. TimeInForce describes how long an Order
    should remain pending before being automatically cancelled by the execution system.
    """

    # Valid values
    values = {
        'GTC': 'The Order is "Good unTil Cancelled"',
        'GTD': 'The Order is "Good unTil Date" and will be cancelled at the provided time',
        'GFD': 'The Order is "Good For Day" and will be cancelled at 5pm New York time',
        'FOK': 'The Order must be immediately "Filled Or Killed"',
        'IOC': 'The Order must be "Immediatedly paritally filled Or Cancelled"'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class PriceStatus(str, Primitive):
    """The status of the Price.
    """

    # Valid values
    values = {
        'tradeable': 'The Instrument’s price is tradeable.',
        'non-tradeable': 'The Instrument’s price is not tradeable.',
        'invalid': 'The Instrument of the price is invalid or there is no valid Price for the Instrument.'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class PriceValue(float, Primitive):
    """The string representation of a Price for an Instrument.
    """

    # Correct syntax of value
    format_syntax = 'A decimal number encodes as a string. The amount of precision ' \
                    'provided depends on the Price’s Instrument. Must be positive'

    def __new__(cls, value):
        try:
            assert float(value) >= 0
        except AssertionError:
            msg = f'Cannot create PriceValue from {value}. PriceValues must be positive'
            logger.error(msg)
            raise InvalidValue(msg)
        return super().__new__(cls, value)

    def format(self, precision, min_=None, max_=None):
        # Ignore the sign. `self` should be positive
        if not precision >= 0:
            msg = f'Cannot format PriceValue. precision {precision} must be >= 0'
            logger.error(msg)
            raise InvalidFormatArguments(msg)
        if min_ and max_:
            if not min_ <= max_:
                msg = f'Cannot format PriceValue. min_ {min_} is not <= max_ {max_}'
                logger.error(msg)
                raise InvalidFormatArguments(msg)

        value = self
        if min_:
            value = (value, min_)[value < min_]
        if max_:
            value = (value, max_)[value > max_]

        return super().__new__(self.__class__, round(value, precision))


class AcceptDatetimeFormat(str, Primitive):
    """DateTime header
    """

    # Valid values
    values = {
        'UNIX': 'If "UNIX" is specified DateTime fields will be specified or '
                'returned in the "12345678.000000123" format.',
        'RFC3339': 'If "RFC3339" is specified DateTime will be specified or '
                   'returned in "YYYY-MM-DDTHH:MM:SS.nnnnnnnnnZ" format.'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class AccountUnits(float, Primitive):
    """The string representation of a quantity of an Account’s home currency.
    """

    # TODO keep an eye on this. OANDA specifies this as a str.
    # Though it makes more sense for it to be a float
    # floats automatically get converted to to strings anyway
    # when serialized into JSON

    # Correct syntax of value
    format_syntax = 'A decimal number encoded as a string. The amount of precision ' \
                    'provided depends on the Account’s home currency.'

    def __new__(cls, value):
        return super().__new__(cls, value)


class Currency(str, Primitive):
    """Currency name identifier. Used by clients to refer to currencies.
    """

    # Correct syntax of value
    format_syntax = 'A string containing an ISO 4217 currency'

    def __new__(cls, value):
        return super().__new__(cls, value)


class DecimalNumber(float, Primitive):
    """The string representation of a decimal number.
    """

    # Correct syntax of value
    format_syntax = 'A decimal number encoded as a string. The amount of precision ' \
                    'provided depends on what the number represents.'

    def __new__(cls, value):
        return super().__new__(cls, value)

    def format(self, precision, min_=None, max_=None):
        # A DecimalNumber can se + / -
        if not precision >= 0:
            msg = f'Cannot format PriceValue. precision {precision} must be >= 0'
            logger.error(msg)
            raise InvalidFormatArguments(msg)

        if min_ and max_:
            if not min_ <= max_:
                msg = f'Cannot format PriceValue. min_ {min_} is not <= max_ {max_}'
                logger.error(msg)
                raise InvalidFormatArguments(msg)

        value = abs(self)
        if min_:
            value = (value, min_)[value < min_]
        if max_:
            value = (value, max_)[value > max_]
        value = value * (1, -1)[self < 0]

        return super().__new__(self.__class__, round(value, precision))


class Direction(str, Primitive):
    """In the context of an Order or a
    Trade, defines whether the units are positive or negative.
    """

    # Valid values
    values = {
        'LONG': 'A long Order is used to to buy units of an Instrument. '
                'A Trade is long when it has bought units of an Instrument.',
        'SHORT': 'A short Order is used to to sell units of an Instrument.'
                 'A Trade is short when it has sold units of an Instrument.'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class InstrumentName(str, Primitive):
    """Instrument name identifier. Used by clients to refer to an Instrument.
    """

    # Correct syntax of value
    format_syntax = 'A string containing the base currency and quote currency delimited by a "_".'

    def __new__(cls, value):
        return super().__new__(cls, value)


class InstrumentType(str, Primitive):
    """The type of an Instrument.
    """

    # Valid values
    values = {
        'CURRENCY': 'Currency',
        'CFD': 'Contract For Difference',
        'METAL': 'Metal'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class TradeSpecifier(str, Primitive, Specifier):
    """The identification of a Trade as referred to by clients
    """

    # Correct syntax of value
    format_syntax = 'Either the Trade’s OANDA-assigned TradeID or the Trade’s client-provided ' \
                    'ClientID prefixed by the "@" symbol'
    # Example of correct format
    example = '@my_trade_id'

    def __new__(cls, value):
        return super().__new__(cls, value)


class TradeID(int, Primitive, Specifier):
    """The Trade’s identifier, unique within the Trade’s Account.
    """

    # Correct syntax of value
    format_syntax = 'The string representation of the OANDA-assigned TradeID. ' \
                    'OANDA-assigned https://github.com/jamespeterschinner/async_v20/issues/12s are positive integers, and are ' \
                    'derived from the TransactionID of the Transaction that opened the Trade.'
    # Example of correct format
    example = '1523'

    def __new__(cls, value):
        return super().__new__(cls, value)


class TradePL(str, Primitive):
    """The classification of TradePLs.
    """

    # Valid values
    values = {
        'POSITIVE': 'An open Trade currently has a positive (profitable) unrealized P/L, '
                    'or a closed Trade realized a positive amount of P/L.',
        'NEGATIVE': 'An open Trade currently has a negative (losing) unrealized P/L, '
                    'or a closed Trade realized a negative amount of P/L.',
        'ZERO': 'An open Trade currently has unrealized P/L of zero (neither profitable nor losing),'
                ' or a closed Trade realized a P/L amount of zero.'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class TradeState(str, Primitive):
    """The current state of the Trade.
    """

    # Valid values
    values = {
        'OPEN': 'The Trade is currently open',
        'CLOSED': 'The Trade has been fully closed',
        'CLOSE_WHEN_TRADEABLE': 'The Trade will be closed as soon as the trade’s instrument becomes tradeable'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class TradeStateFilter(str, Primitive):
    """The state to filter the Trades by
    """

    # Type checking
    typ = str

    # Valid values
    values = {
        'OPEN': 'The Trades that are currently open',
        'CLOSED': 'The Trades that have been fully closed',
        'CLOSE_WHEN_TRADEABLE': 'The Trades  that will be closed as soon as the trades’ instrument becomes tradeable',
        'ALL': 'The Trades that are in any of the possible states listed above.'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class ClientComment(str, Primitive):
    """A client-provided comment that can contain any data and may be assigned to their Orders or
    Trades. Comments are typically used to provide extra context or meaning to an Order or Trade.
    """

    # Example of correct format
    example = 'This is a client comment'

    def __new__(cls, value):
        return super().__new__(cls, value)


class ClientID(str, Primitive, Specifier):
    """A client-provided identifier, used by clients to refer to their
    Orders or Trades with an identifier that they have provided.
    """

    # Example of correct format
    example = 'my_order_id'

    def __new__(cls, value):
        return super().__new__(cls, value)


class ClientTag(str, Primitive):
    """A client-provided tag that can contain any data and may be assigned to their
    Orders or Trades. Tags are typically used to associate groups of Trades and/or Orders together.
    """

    # Example of correct format
    example = 'client_tag_1'

    def __new__(cls, value):
        return super().__new__(cls, value)


class Reason(Primitive, str):
    """Generic reason for any transaction that may occur"""
    values = {}

    def __init_subclass__(cls, **kwargs):
        Reason.values.update(cls.values)

    def __new__(cls, value, possible_values=None):
        if possible_values:
            assert domain_check(value, possible_values=possible_values)
        else:
            assert domain_check(value, possible_values=Reason.values)
        return str.__new__(cls, value)


class FundingReason(Reason):
    """The reason that an Account is being funded.
    """

    # Valid values
    values = {
        'CLIENT_FUNDING': 'The client has initiated a funds transfer',
        'ACCOUNT_TRANSFER': 'Funds are being transfered between two Accounts.',
        'DIVISION_MIGRATION': 'Funds are being transfered as part of a Division migration',
        'SITE_MIGRATION': 'Funds are being transfered as part of a Site migration',
        'ADJUSTMENT': 'Funds are being transfered as part of an Account adjustment'
    }

    def __new__(cls, value):
        return super().__new__(cls, value, possible_values=cls.values)


class LimitOrderReason(Reason):
    """The reason that the Limit Order was initiated
    """

    # Valid values
    values = {
        'CLIENT_ORDER': 'The Limit Order was initiated at the request of a client',
        'REPLACEMENT': 'The Limit Order was initiated as a replacement for an existing Order',
    }

    def __new__(cls, value):
        return super().__new__(cls, value, possible_values=cls.values)


class MarketIfTouchedOrderReason(Reason):
    """The reason that the Market-if-touched Order was initiated
    """

    # Valid values
    values = {
        'CLIENT_ORDER': 'The Market-if-touched Order was initiated at the request of a client',
        'REPLACEMENT': 'The Market-if-touched Order was initiated as a replacement for an existing Order',
    }

    def __new__(cls, value):
        return super().__new__(cls, value, possible_values=cls.values)


class MarketOrderMarginCloseoutReason(Reason):
    """The reason that the Market Order was created to perform a margin closeout
    """

    # Valid values
    values = {
        'MARGIN_CHECK_VIOLATION': 'Trade closures resulted from violating OANDA’s margin policy',
        'REGULATORY_MARGIN_CALL_VIOLATION': 'Trade closures came from a margin closeout event resulting from '
                                            'regulatory conditions placed on the Account’s margin call'
    }

    def __new__(cls, value):
        return super().__new__(cls, value, possible_values=cls.values)


class MarketOrderReason(Reason):
    """The reason that the Market Order was created
    """

    # Valid values
    values = {
        'CLIENT_ORDER': 'The Market Order was created at the request of a client',
        'TRADE_CLOSE': 'The Market Order was created to close a Trade at the request of a client',
        'POSITION_CLOSEOUT': 'The Market Order was created to close a Position at the request of a client',
        'MARGIN_CLOSEOUT': 'The Market Order was created as part of a Margin Closeout',
        'DELAYED_TRADE_CLOSE': 'The Market Order was created to close a trade marked for delayed closure'
    }

    def __new__(cls, value):
        return super().__new__(cls, value, possible_values=cls.values)


class OrderCancelReason(Reason):
    """The reason that an Order was cancelled.
    """

    # Valid values
    values = {
        'INTERNAL_SERVER_ERROR': 'The Order was cancelled because at the time of filling, '
                                 'an unexpected internal server error occurred.',
        'ACCOUNT_LOCKED': 'The Order was cancelled because at the time of filling the account was locked.',
        'ACCOUNT_NEW_POSITIONS_LOCKED': 'The order was to be filled, however the account is configured to not allow new'
                                        'positions to be created.',
        'ACCOUNT_ORDER_CREATION_LOCKED': 'Filling the Order wasn’t possible because it required the creation of a '
                                         'dependent Order and the Account is locked for Order creation.',
        'ACCOUNT_ORDER_FILL_LOCKED': 'Filling the Order was not possible because the Account is locked for filling '
                                     'Orders.',
        'CLIENT_REQUEST': 'The Order was cancelled explicitly at the request of the client.',
        'MIGRATION': 'The Order cancelled because it is being migrated to another account.',
        'MARKET_HALTED': 'Filling the Order wasn’t possible because the Order’s instrument was halted.',
        'LINKED_TRADE_CLOSED': 'The Order is linked to an open Trade that was closed.',
        'TIME_IN_FORCE_EXPIRED': 'The time in force specified for this order has passed.',
        'INSUFFICIENT_MARGIN': 'Filling the Order wasn’t possible because the Account had insufficient margin.',
        'FIFO_VIOLATION': 'Filling the Order would have resulted in a a FIFO violation.',
        'BOUNDS_VIOLATION': 'Filling the Order would have violated the Order’s price bound.',
        'CLIENT_REQUEST_REPLACED': 'The Order was cancelled for replacement at the request of the client.',
        'INSUFFICIENT_LIQUIDITY': 'Filling the Order wasn’t possible because enough liquidity available.',
        'TAKE_PROFIT_ON_FILL_GTD_TIMESTAMP_IN_PAST': 'Filling the Order would have resulted in the creation of a '
                                                     'Take Profit Order with a GTD time in the past.',
        'TAKE_PROFIT_ON_FILL_LOSS': 'Filling the Order would result in the creation of a Take Profit Order that '
                                    'would have been filled immediately, closing the new Trade at a loss.',
        'LOSING_TAKE_PROFIT': 'Filling the Order would result in the creation of a Take Profit Loss Order that would '
                              'close the new Trade at a loss when filled.',
        'STOP_LOSS_ON_FILL_GTD_TIMESTAMP_IN_PAST': 'Filling the Order would have resulted in the creation of a Stop '
                                                   'Loss Order with a GTD time in the past.',
        'STOP_LOSS_ON_FILL_LOSS': 'Filling the Order would result in the creation of a Stop Loss Order that would have '
                                  'been filled immediately, closing the new Trade at a loss.',
        'TRAILING_STOP_LOSS_ON_FILL_GTD_TIMESTAMP_IN_PAST': 'Filling the Order would have resulted in the creation of '
                                                            'a Trailing Stop Loss Order with a GTD time in the past.',
        'CLIENT_TRADE_ID_ALREADY_EXISTS': 'Filling the Order would result in the creation of a new Open Trade with a '
                                          'client Trade ID already in use.',
        'POSITION_CLOSEOUT_FAILED': 'Closing out a position wasn’t fully possible.',
        'OPEN_TRADES_ALLOWED_EXCEEDED': 'Filling the Order would cause the maximum open trades allowed for the Account '
                                        'to be exceeded.',
        'PENDING_ORDERS_ALLOWED_EXCEEDED': 'Filling the Order would have resulted in exceeding the number of pending '
                                           'Orders allowed for the Account.',
        'TAKE_PROFIT_ON_FILL_CLIENT_ORDER_ID_ALREADY_EXISTS': 'Filling the Order would have resulted in the creation '
                                                              'of a Take Profit Order with a client Order ID that is '
                                                              'already in use.',
        'STOP_LOSS_ON_FILL_CLIENT_ORDER_ID_ALREADY_EXISTS': 'Filling the Order would have resulted in the creation of '
                                                            'a Stop Loss Order with a client Order ID that is already '
                                                            'in use.',
        'TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_ID_ALREADY_EXISTS': 'Filling the Order would have resulted in the '
                                                                     'creation of a Trailing Stop Loss Order with a '
                                                                     'client Order ID that is already in use.',
        'POSITION_SIZE_EXCEEDED': 'Filling the Order would have resulted in the Account’s maximum position size limit '
                                  'being exceeded for the Order’s instrument.'
    }

    def __new__(cls, value):
        return super().__new__(cls, value, possible_values=cls.values)


class OrderFillReason(Reason):
    """The reason that an Order was filled
    """

    # Valid values
    values = {
        'LIMIT_ORDER': 'The Order filled was a Limit Order',
        'STOP_ORDER': 'The Order filled was a Stop Order',
        'MARKET_IF_TOUCHED_ORDER': 'The Order filled was a Market-if-touched Order',
        'TAKE_PROFIT_ORDER': 'The Order filled was a Take Profit Order',
        'STOP_LOSS_ORDER': 'The Order filled was a Stop Loss Order',
        'TRAILING_STOP_LOSS_ORDER': 'The Order filled was a Trailing Stop Loss Order',
        'MARKET_ORDER': 'The Order filled was a Market Order',
        'MARKET_ORDER_TRADE_CLOSE': 'The Order filled was a Market Order used to explicitly close a Trade',
        'MARKET_ORDER_POSITION_CLOSEOUT': 'The Order filled was a Market Order used to explicitly close a Position',
        'MARKET_ORDER_MARGIN_CLOSEOUT': 'The Order filled was a Market Order used for a Margin Closeout',
        'MARKET_ORDER_DELAYED_TRADE_CLOSE': 'The Order filled was a Market Order used for a delayed Trade close'
    }

    def __new__(cls, value):
        return super().__new__(cls, value, possible_values=cls.values)


class RequestID(str, Primitive):
    """The request identifier.
    """

    # Is this necessary, NO! I guess it's about consistency
    def __new__(cls, value):
        return super().__new__(cls, value)


class StopLossOrderReason(Reason):
    """The reason that the Stop Loss Order was initiated
    """

    # Valid values
    values = {
        'CLIENT_ORDER': 'The Stop Loss Order was initiated at the request of a client',
        'REPLACEMENT': 'The Stop Loss Order was initiated as a replacement for an existing Order',
        'ON_FILL': 'The Stop Loss Order was initiated automatically when an Order was filled that opened a new Trade '
                   'requiring a Stop Loss Order.'
    }

    def __new__(cls, value):
        return super().__new__(cls, value, possible_values=cls.values)


class StopOrderReason(Reason):
    """The reason that the Stop Order was initiated
    """

    # Valid values
    values = {
        'CLIENT_ORDER': 'The Stop Order was initiated at the request of a client',
        'REPLACEMENT': 'The Stop Order was initiated as a replacement for an existing Order',
    }

    def __new__(cls, value):
        return super().__new__(cls, value, possible_values=cls.values)


class TakeProfitOrderReason(Reason):
    """The reason that the Take Profit Order was initiated
    """

    # Valid values
    values = {
        'CLIENT_ORDER': 'The Take Profit Order was initiated at the request of a client',
        'REPLACEMENT': 'The Take Profit Order was initiated as a replacement for an existing Order',
        'ON_FILL': 'The Take Profit Order was initiated automatically when an Order was filled that opened a new Trade '
                   'requiring a Take Profit Order.'
    }

    def __new__(cls, value):
        return super().__new__(cls, value, possible_values=cls.values)


class TrailingStopLossOrderReason(Reason):
    """The reason that the Trailing Stop Loss Order was initiated
    """

    # Valid values
    values = {
        'CLIENT_ORDER': 'The Trailing Stop Loss Order was initiated at the request of a client',
        'REPLACEMENT': 'The Trailing Stop Loss Order was initiated as a replacement for an existing Order',
        'ON_FILL': 'The Trailing Stop Loss Order was initiated automatically when an Order was filled that opened a '
                   'new Trade requiring a Trailing Stop Loss Order.'}

    def __new__(cls, value):
        return super().__new__(cls, value, possible_values=cls.values)


class TransactionFilter(str, Primitive):
    """A filter that can be used when fetching Transactions
    """

    # Valid values
    values = {
        'ORDER': 'Order-related Transactions. These are the Transactions that create, cancel, fill or trigger Orders',
        'FUNDING': 'Funding-related Transactions',
        'ADMIN': 'Administrative Transactions',
        'CREATE': 'Account Create Transaction',
        'CLOSE': 'Account Close Transaction',
        'REOPEN': 'Account Reopen Transaction',
        'CLIENT_CONFIGURE': 'Client Configuration Transaction',
        'CLIENT_CONFIGURE_REJECT': 'Client Configuration Reject Transaction',
        'TRANSFER_FUNDS': 'Transfer Funds Transaction',
        'TRANSFER_FUNDS_REJECT': 'Transfer Funds Reject Transaction',
        'MARKET_ORDER': 'Market Order Transaction',
        'MARKET_ORDER_REJECT': 'Market Order Reject Transaction',
        'LIMIT_ORDER': 'Limit Order Transaction',
        'LIMIT_ORDER_REJECT': 'Limit Order Reject Transaction',
        'STOP_ORDER': 'Stop Order Transaction',
        'STOP_ORDER_REJECT': 'Stop Order Reject Transaction',
        'MARKET_IF_TOUCHED_ORDER': 'Market if Touched Order Transaction',
        'MARKET_IF_TOUCHED_ORDER_REJECT': 'Market if Touched Order Reject Transaction',
        'TAKE_PROFIT_ORDER': 'Take Profit Order Transaction',
        'TAKE_PROFIT_ORDER_REJECT': 'Take Profit Order Reject Transaction',
        'STOP_LOSS_ORDER': 'Stop Loss Order Transaction',
        'STOP_LOSS_ORDER_REJECT': 'Stop Loss Order Reject Transaction',
        'TRAILING_STOP_LOSS_ORDER': 'Trailing Stop Loss Order Transaction',
        'TRAILING_STOP_LOSS_ORDER_REJECT': 'Trailing Stop Loss Order Reject Transaction',
        'ONE_CANCELS_ALL_ORDER': 'One Cancels All Order Transaction',
        'ONE_CANCELS_ALL_ORDER_REJECT': 'One Cancels All Order Reject Transaction',
        'ONE_CANCELS_ALL_ORDER_TRIGGERED': 'One Cancels All Order Trigger Transaction',
        'ORDER_FILL': 'Order Fill Transaction',
        'ORDER_CANCEL': 'Order Cancel Transaction',
        'ORDER_CANCEL_REJECT': 'Order Cancel Reject Transaction',
        'ORDER_CLIENT_EXTENSIONS_MODIFY': 'Order Client Extensions Modify Transaction',
        'ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT': 'Order Client Extensions Modify Reject Transaction',
        'TRADE_CLIENT_EXTENSIONS_MODIFY': 'Trade Client Extensions Modify Transaction',
        'TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT': 'Trade Client Extensions Modify Reject Transaction',
        'MARGIN_CALL_ENTER': 'Margin Call Enter Transaction',
        'MARGIN_CALL_EXTEND': 'Margin Call Extend Transaction',
        'MARGIN_CALL_EXIT': 'Margin Call Exit Transaction',
        'DELAYED_TRADE_CLOSURE': 'Delayed Trade Closure Transaction',
        'DAILY_FINANCING': 'Daily Financing Transaction',
        'RESET_RESETTABLE_PL': 'Reset Resettable PL Transaction'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class TransactionID(int, Primitive, Specifier):
    """The unique Transaction identifier within each Account.
    """

    # Correct syntax of value
    format_syntax = 'String representation of the numerical OANDA-assigned TransactionID'
    # Example of correct format
    example = '1523'

    def __new__(cls, value):
        return super().__new__(cls, value)


class TransactionRejectReason(Reason):
    """The reason that a Transaction was rejected.
    """

    # Valid values
    values = {
        'INTERNAL_SERVER_ERROR': 'An unexpected internal server error has occurred',
        'INSTRUMENT_PRICE_UNKNOWN': 'The system was unable to determine the current price for the Order’s instrument',
        'ACCOUNT_NOT_ACTIVE': 'The Account is not active',
        'ACCOUNT_LOCKED': 'The Account is locked',
        'ACCOUNT_ORDER_CREATION_LOCKED': 'The Account is locked for Order creation',
        'ACCOUNT_CONFIGURATION_LOCKED': 'The Account is locked for configuration',
        'ACCOUNT_DEPOSIT_LOCKED': 'The Account is locked for deposits',
        'ACCOUNT_WITHDRAWAL_LOCKED': 'The Account is locked for withdrawals',
        'ACCOUNT_ORDER_CANCEL_LOCKED': 'The Account is locked for Order cancellation',
        'INSTRUMENT_NOT_TRADEABLE': 'The instrument specified is not tradeable by the Account',
        'PENDING_ORDERS_ALLOWED_EXCEEDED': 'Creating the Order would result in the maximum number of allowed pending '
                                           'Orders being exceeded',
        'ORDER_ID_UNSPECIFIED': 'Neither the Order ID nor client Order ID are specified',
        'ORDER_DOESNT_EXIST': 'The Order specified does not exist',
        'ORDER_IDENTIFIER_INCONSISTENCY': 'The Order ID and client Order ID specified do not identify the same Order',
        'TRADE_ID_UNSPECIFIED': 'Neither the Trade ID nor client Trade ID are specified',
        'TRADE_DOESNT_EXIST': 'The Trade specified does not exist',
        'TRADE_IDENTIFIER_INCONSISTENCY': 'The Trade ID and client Trade ID specified do not identify the same Trade',
        'INSTRUMENT_MISSING': 'Order instrument has not been specified',
        'INSTRUMENT_UNKNOWN': 'The instrument specified is unknown',
        'UNITS_MISSING': 'Order units have not been not specified',
        'UNITS_INVALID': 'Order units specified are invalid',
        'UNITS_PRECISION_EXCEEDED': 'The units specified contain more precision than is allowed for the Order’s '
                                    'instrument',
        'UNITS_LIMIT_EXCEEDED': 'The units specified exceeds the maximum number of units allowed',
        'UNITS_MIMIMUM_NOT_MET': 'The units specified is less than the minimum number of units required',
        'PRICE_MISSING': 'The price has not been specified',
        'PRICE_INVALID': 'The price specifed is invalid',
        'PRICE_PRECISION_EXCEEDED': 'The price specified contains more precision than is allowed for the instrument',
        'PRICE_DISTANCE_MISSING': 'The price distance has not been specified',
        'PRICE_DISTANCE_INVALID': 'The price distance specifed is invalid',
        'PRICE_DISTANCE_PRECISION_EXCEEDED': 'The price distance specified contains more precision than is allowed for '
                                             'the instrument',
        'PRICE_DISTANCE_MAXIMUM_EXCEEDED': 'The price distance exceeds that maximum allowed amount',
        'PRICE_DISTANCE_MINIMUM_NOT_MET': 'The price distance does not meet the minimum allowed amount',
        'TIME_IN_FORCE_MISSING': 'The TimeInForce field has not been specified',
        'TIME_IN_FORCE_INVALID': 'The TimeInForce specified is invalid',
        'TIME_IN_FORCE_GTD_TIMESTAMP_MISSING': 'The TimeInForce is GTD but no GTD timestamp is provided',
        'TIME_IN_FORCE_GTD_TIMESTAMP_IN_PAST': 'The TimeInForce is GTD but the GTD timestamp is in the past',
        'PRICE_BOUND_INVALID': 'The price bound specified is invalid',
        'PRICE_BOUND_PRECISION_EXCEEDED': 'The price bound specified contains more precision than is allowed for the '
                                          'Order’s instrument',
        'ORDERS_ON_FILL_DUPLICATE_CLIENT_ORDER_IDS': 'Multiple Orders on fill share the same client Order ID',
        'TRADE_ON_FILL_CLIENT_EXTENSIONS_NOT_SUPPORTED': 'The Order does not support Trade on fill client extensions '
                                                         'because it cannot create a new Trade',
        'CLIENT_ORDER_ID_INVALID': 'The client Order ID specified is invalid',
        'CLIENT_ORDER_ID_ALREADY_EXISTS': 'The client Order ID specified is already assigned to another pending Order',
        'CLIENT_ORDER_TAG_INVALID': 'The client Order tag specified is invalid',
        'CLIENT_ORDER_COMMENT_INVALID': 'The client Order comment specified is invalid',
        'CLIENT_TRADE_ID_INVALID': 'The client Trade ID specified is invalid',
        'CLIENT_TRADE_ID_ALREADY_EXISTS': 'The client Trade ID specifed is already assigned to another open Trade',
        'CLIENT_TRADE_TAG_INVALID': 'The client Trade tag specified is invalid',
        'CLIENT_TRADE_COMMENT_INVALID': 'The client Trade comment is invalid',
        'ORDER_FILL_POSITION_ACTION_MISSING': 'The OrderFillPositionAction field has not been specified',
        'ORDER_FILL_POSITION_ACTION_INVALID': 'The OrderFillPositionAction specified is invalid',
        'TRIGGER_CONDITION_MISSING': 'The TriggerCondition field has not been specified',
        'TRIGGER_CONDITION_INVALID': 'The TriggerCondition specified is invalid',
        'ORDER_PARTIAL_FILL_OPTION_MISSING': 'The OrderFillPositionAction field has not been specified',
        'ORDER_PARTIAL_FILL_OPTION_INVALID': 'The OrderFillPositionAction specified is invalid.',
        'INVALID_REISSUE_IMMEDIATE_PARTIAL_FILL': 'When attempting to reissue an order (currently only a '
                                                  'MarketIfTouched) that was immediately partially filled, it is not '
                                                  'possible to create a correct pending Order.',
        'TAKE_PROFIT_ORDER_ALREADY_EXISTS': 'A Take Profit Order for the specified Trade already exists',
        'TAKE_PROFIT_ON_FILL_PRICE_MISSING': 'The Take Profit on fill specified does not provide a price',
        'TAKE_PROFIT_ON_FILL_PRICE_INVALID': 'The Take Profit on fill specified contains an invalid price',
        'TAKE_PROFIT_ON_FILL_PRICE_PRECISION_EXCEEDED': 'The Take Profit on fill specified contains a price with more '
                                                        'precision than is allowed by the Order’s instrument',
        'TAKE_PROFIT_ON_FILL_TIME_IN_FORCE_MISSING': 'The Take Profit on fill specified does not provide a TimeInForce',
        'TAKE_PROFIT_ON_FILL_TIME_IN_FORCE_INVALID': 'The Take Profit on fill specifies an invalid TimeInForce',
        'TAKE_PROFIT_ON_FILL_GTD_TIMESTAMP_MISSING': 'The Take Profit on fill specifies a GTD TimeInForce but does not '
                                                     'provide a GTD timestamp',
        'TAKE_PROFIT_ON_FILL_GTD_TIMESTAMP_IN_PAST': 'The Take Profit on fill specifies a GTD timestamp that is in the '
                                                     'past',
        'TAKE_PROFIT_ON_FILL_CLIENT_ORDER_ID_INVALID': 'The Take Profit on fill client Order ID specified is invalid',
        'TAKE_PROFIT_ON_FILL_CLIENT_ORDER_TAG_INVALID': 'The Take Profit on fill client Order tag specified is invalid',
        'TAKE_PROFIT_ON_FILL_CLIENT_ORDER_COMMENT_INVALID': 'The Take Profit on fill client Order comment specified is'
                                                            ' invalid',
        'TAKE_PROFIT_ON_FILL_TRIGGER_CONDITION_MISSING': 'The Take Profit on fill specified does not provide a '
                                                         'TriggerCondition',
        'TAKE_PROFIT_ON_FILL_TRIGGER_CONDITION_INVALID': 'The Take Profit on fill specifies an invalid '
                                                         'TriggerCondition',
        'STOP_LOSS_ORDER_ALREADY_EXISTS': 'A Stop Loss Order for the specified Trade already exists',
        'STOP_LOSS_ON_FILL_PRICE_MISSING': 'The Stop Loss on fill specified does not provide a price',
        'STOP_LOSS_ON_FILL_PRICE_INVALID': 'The Stop Loss on fill specifies an invalid price',
        'STOP_LOSS_ON_FILL_PRICE_PRECISION_EXCEEDED': 'The Stop Loss on fill specifies a price with more precision '
                                                      'than is allowed by the Order’s instrument',
        'STOP_LOSS_ON_FILL_TIME_IN_FORCE_MISSING': 'The Stop Loss on fill specified does not provide a TimeInForce',
        'STOP_LOSS_ON_FILL_TIME_IN_FORCE_INVALID': 'The Stop Loss on fill specifies an invalid TimeInForce',
        'STOP_LOSS_ON_FILL_GTD_TIMESTAMP_MISSING': 'The Stop Loss on fill specifies a GTD TimeInForce but does not'
                                                   ' provide a GTD timestamp',
        'STOP_LOSS_ON_FILL_GTD_TIMESTAMP_IN_PAST': 'The Stop Loss on fill specifies a GTD timestamp that is in the '
                                                   'past',
        'STOP_LOSS_ON_FILL_CLIENT_ORDER_ID_INVALID': 'The Stop Loss on fill client Order ID specified is invalid',
        'STOP_LOSS_ON_FILL_CLIENT_ORDER_TAG_INVALID': 'The Stop Loss on fill client Order tag specified is invalid',
        'STOP_LOSS_ON_FILL_CLIENT_ORDER_COMMENT_INVALID': 'The Stop Loss on fill client Order comment specified is '
                                                          'invalid',
        'STOP_LOSS_ON_FILL_TRIGGER_CONDITION_MISSING': 'The Stop Loss on fill specified does not provide a '
                                                       'TriggerCondition',
        'STOP_LOSS_ON_FILL_TRIGGER_CONDITION_INVALID': 'The Stop Loss on fill specifies an invalid TriggerCondition',
        'TRAILING_STOP_LOSS_ORDER_ALREADY_EXISTS': 'A Trailing Stop Loss Order for the specified Trade already exists',
        'TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MISSING': 'The Trailing Stop Loss on fill specified does not '
                                                             'provide a distance',
        'TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_INVALID': 'The Trailing Stop Loss on fill distance is invalid',
        'TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_PRECISION_EXCEEDED': 'The Trailing Stop Loss on fill distance '
                                                                        'contains more precision than is allowed by '
                                                                        'the instrument',
        'TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MAXIMUM_EXCEEDED': 'The Trailing Stop Loss on fill price distance '
                                                                      'exceeds the maximum allowed amount',
        'TRAILING_STOP_LOSS_ON_FILL_PRICE_DISTANCE_MINIMUM_NOT_MET': 'The Trailing Stop Loss on fill price distance '
                                                                     'does not meet the minimum allowed amount',
        'TRAILING_STOP_LOSS_ON_FILL_TIME_IN_FORCE_MISSING': 'The Trailing Stop Loss on fill specified does not '
                                                            'provide a TimeInForce',
        'TRAILING_STOP_LOSS_ON_FILL_TIME_IN_FORCE_INVALID': 'The Trailing Stop Loss on fill specifies an invalid '
                                                            'TimeInForce',
        'TRAILING_STOP_LOSS_ON_FILL_GTD_TIMESTAMP_MISSING': 'The Trailing Stop Loss on fill TimeInForce is specified '
                                                            'as GTD but no GTD timestamp is provided',
        'TRAILING_STOP_LOSS_ON_FILL_GTD_TIMESTAMP_IN_PAST': 'The Trailing Stop Loss on fill GTD timestamp is in the '
                                                            'past',
        'TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_ID_INVALID': 'The Trailing Stop Loss on fill client Order ID '
                                                              'specified is invalid',
        'TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_TAG_INVALID': 'The Trailing Stop Loss on fill client Order tag '
                                                               'specified is invalid',
        'TRAILING_STOP_LOSS_ON_FILL_CLIENT_ORDER_COMMENT_INVALID': 'The Trailing Stop Loss on fill client Order '
                                                                   'comment specified is invalid',
        'TRAILING_STOP_LOSS_ORDERS_NOT_SUPPORTED': 'A client attempted to create either a Trailing Stop Loss order or '
                                                   'an order with a Trailing Stop Loss On Fill specified, which may '
                                                   'not yet be supported.',
        'TRAILING_STOP_LOSS_ON_FILL_TRIGGER_CONDITION_MISSING': 'The Trailing Stop Loss on fill specified does not '
                                                                'provide a TriggerCondition',
        'TRAILING_STOP_LOSS_ON_FILL_TRIGGER_CONDITION_INVALID': 'The Tailing Stop Loss on fill specifies an invalid '
                                                                'TriggerCondition',
        'CLOSE_TRADE_TYPE_MISSING': 'The request to close a Trade does not specify a full or partial close',
        'CLOSE_TRADE_PARTIAL_UNITS_MISSING': 'The request to close a Trade partially did not specify the number of '
                                             'units to close',
        'CLOSE_TRADE_UNITS_EXCEED_TRADE_SIZE': 'The request to partially close a Trade specifies a number of units '
                                               'that exceeds the current size of the given Trade',
        'CLOSEOUT_POSITION_DOESNT_EXIST': 'The Position requested to be closed out does not exist',
        'CLOSEOUT_POSITION_INCOMPLETE_SPECIFICATION': 'The request to closeout a Position was specified incompletely',
        'CLOSEOUT_POSITION_UNITS_EXCEED_POSITION_SIZE': 'A partial Position closeout request specifies a number of '
                                                        'units that exceeds the current Position',
        'CLOSEOUT_POSITION_REJECT': 'The request to closeout a Position could not be fully satisfied',
        'CLOSEOUT_POSITION_PARTIAL_UNITS_MISSING': 'The request to partially closeout a Position did not specify the '
                                                   'number of units to close.',
        'MARKUP_GROUP_ID_INVALID': 'The markup group ID provided is invalid',
        'POSITION_AGGREGATION_MODE_INVALID': 'The PositionAggregationMode provided is not supported/valid.',
        'ADMIN_CONFIGURE_DATA_MISSING': 'No configuration parameters provided',
        'MARGIN_RATE_INVALID': 'The margin rate provided is invalid',
        'MARGIN_RATE_WOULD_TRIGGER_CLOSEOUT': 'The margin rate provided would cause an immediate margin closeout',
        'ALIAS_INVALID': 'The account alias string provided is invalid',
        'CLIENT_CONFIGURE_DATA_MISSING': 'No configuration parameters provided',
        'MARGIN_RATE_WOULD_TRIGGER_MARGIN_CALL': 'The margin rate provided would cause the Account to enter a margin '
                                                 'call state.',
        'AMOUNT_INVALID': 'Funding is not possible because the requested transfer amount is invalid',
        'INSUFFICIENT_FUNDS': 'The Account does not have sufficient balance to complete the funding request',
        'AMOUNT_MISSING': 'Funding amount has not been specified',
        'FUNDING_REASON_MISSING': 'Funding reason has not been specified',
        'CLIENT_EXTENSIONS_DATA_MISSING': 'Neither Order nor Trade on Fill client extensions were provided for'
                                          ' modification',
        'REPLACING_ORDER_INVALID': 'The Order to be replaced has a different type than the replacing Order.',
        'REPLACING_TRADE_ID_INVALID': 'The replacing Order refers to a different Trade than the Order that is being '
                                      'replaced.'
    }

    def __new__(cls, value):
        return super().__new__(cls, value, possible_values=cls.values)


class TransactionType(str, Primitive):
    """The possible types of a Transaction
    """

    # Valid values
    values = {
        'CREATE': 'Account Create Transaction',
        'CLOSE': 'Account Close Transaction',
        'REOPEN': 'Account Reopen Transaction',
        'CLIENT_CONFIGURE': 'Client Configuration Transaction',
        'CLIENT_CONFIGURE_REJECT': 'Client Configuration Reject Transaction',
        'TRANSFER_FUNDS': 'Transfer Funds Transaction',
        'TRANSFER_FUNDS_REJECT': 'Transfer Funds Reject Transaction',
        'MARKET_ORDER': 'Market Order Transaction',
        'MARKET_ORDER_REJECT': 'Market Order Reject Transaction',
        'LIMIT_ORDER': 'Limit Order Transaction',
        'LIMIT_ORDER_REJECT': 'Limit Order Reject Transaction',
        'STOP_ORDER': 'Stop Order Transaction',
        'STOP_ORDER_REJECT': 'Stop Order Reject Transaction',
        'MARKET_IF_TOUCHED_ORDER': 'Market if Touched Order Transaction',
        'MARKET_IF_TOUCHED_ORDER_REJECT': 'Market if Touched Order Reject Transaction',
        'TAKE_PROFIT_ORDER': 'Take Profit Order Transaction',
        'TAKE_PROFIT_ORDER_REJECT': 'Take Profit Order Reject Transaction',
        'STOP_LOSS_ORDER': 'Stop Loss Order Transaction',
        'STOP_LOSS_ORDER_REJECT': 'Stop Loss Order Reject Transaction',
        'TRAILING_STOP_LOSS_ORDER': 'Trailing Stop Loss Order Transaction',
        'TRAILING_STOP_LOSS_ORDER_REJECT': 'Trailing Stop Loss Order Reject Transaction',
        'ORDER_FILL': 'Order Fill Transaction',
        'ORDER_CANCEL': 'Order Cancel Transaction',
        'ORDER_CANCEL_REJECT': 'Order Cancel Reject Transaction',
        'ORDER_CLIENT_EXTENSIONS_MODIFY': 'Order Client Extensions Modify Transaction',
        'ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT': 'Order Client Extensions Modify Reject Transaction',
        'TRADE_CLIENT_EXTENSIONS_MODIFY': 'Trade Client Extensions Modify Transaction',
        'TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT': 'Trade Client Extensions Modify Reject Transaction',
        'MARGIN_CALL_ENTER': 'Margin Call Enter Transaction',
        'MARGIN_CALL_EXTEND': 'Margin Call Extend Transaction',
        'MARGIN_CALL_EXIT': 'Margin Call Exit Transaction',
        'DELAYED_TRADE_CLOSURE': 'Delayed Trade Closure Transaction',
        'DAILY_FINANCING': 'Daily Financing Transaction',
        'RESET_RESETTABLE_PL': 'Reset Resettable PL Transaction'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)

class GuaranteedStopLossOrderMode(str, Primitive):
    """The overall behaviour of the Account regarding guaranteed Stop Loss Orders
    """

    # Valid values
    values = { 'DISABLED' : 'The Account is not permitted to create guaranteed Stop Loss Orders.',
               'ALLOWED' : 'The Account is able, but not required to have guaranteed Stop Loss Orders for open Trades.',
               'REQUIRED' : 'The Account is required to have guaranteed Stop Loss Orders for all open Trades.'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)