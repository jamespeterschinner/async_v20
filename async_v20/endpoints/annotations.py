from ..definitions.types import ClientExtensions
from ..definitions.primitives import InstrumentName
from ..definitions.types import TransactionID
from ..definitions.types import DateTime

__all__ = ['Alias', 'AlignmentTimezone', 'Authorization', 'Count', 'DailyAlignment', 'FromTime',
           'FromTransactionID', 'Ids', 'IncludeFirstQuery', 'Instruments', 'LastTransactionID',
           'LongClientExtensions', 'LongUnits', 'PageSize', 'ShortClientExtensions', 'ShortUnits',
           'Smooth', 'Snapshot', 'SinceTransactionID',
           'ToTime', 'ToTransactionID', 'TradeClientExtensions', 'Type', 'Units', 'UserSpecifier']


class Bool(object):
    def __new__(cls, arg):
        return bool(arg)


class Authorization(str):
    """Contains OANDA's v20 API authorization token"""
    pass


class Instruments(str):
    pass


class Alias(str):
    pass


class Count(int):
    """The number of candlesticks to return in the reponse.
    Count should not be specified if both the start and end
    parameters are provided, as the time range combined
    with the graularity will determine the number of
    candlesticks to return. [default=500, maximum=5000]"""

    def __new__(cls, value=500):
        if not 0 < value <= 5000:
            raise ValueError(f'Count: MUST be within range(1,5001). Supplied {value}')
        return super().__new__(cls, value)


class Smooth(Bool):
    """A flag that controls whether the candlestick is
    'smoothed' or not. A smoothed candlestick uses the
    previous candle’s close price as its open price,
    while an unsmoothed candlestick uses the first price
    from its time range as its open price. [default=False]"""

    def __new__(cls, value=False):
        return super().__new__(cls, value)


class IncludeFirstQuery(Bool):
    """A flag that controls whether the candlestick that is covered by the
    from time should be included in the results. This flag enables clients
    to use the timestamp of the last completed candlestick received to poll
    for future candlesticks but avoid receiving the previous candlestick
    repeatedly. [default=True]"""

    def __new__(cls, value=True):
        return super().__new__(cls, value)


class DailyAlignment(int):
    """The hour of the day (in the specified timezone)
    to use for granularities that have daily alignments.
    [default=17, minimum=0, maximum=23]"""

    def __new__(cls, value=17):
        if not 0 <= value <= 23:
            raise ValueError(f'DailyAlignment: Must be within range(24). Supplied: {value}')
        return super().__new__(cls, value)


class AlignmentTimezone(str):
    """The timezone to use for the dailyAlignment parameter.
    Candlesticks with daily alignment will be aligned to the
    dailyAlignment hour within the alignmentTimezone.
    [default=America/New_York]"""

    # TODO find out what are the valid time zones

    def __new__(cls, value='America/New_York'):
        return super().__new__(cls, value)


class Ids(str):
    pass


class LongUnits(str):
    """Indication of how much of the long Position to closeout. Either the
    string "ALL", the string "NONE", or a DecimalNumber representing how many
    units of the long position to close using a PositionCloseout MarketOrder.
    The units specified must always be positive.
    """

    def __new__(cls, value='ALL'):
        return super().__new__(cls, value)


class ShortUnits(str):
    """ Indication of how much of the short Position to closeout. Either the
    string "ALL", the string "NONE", or a DecimalNumber representing how many
    units of the short position to close using a PositionCloseout
    MarketOrder. The units specified must always be positive.
    """

    def __new__(cls, value='ALL'):
        return super().__new__(cls, value)


class Snapshot(Bool):
    """Flag that enables/disables the sending of a pricing snapshot
    when initially connecting to the stream. [default=True]"""

    def __new__(cls, value=True):
        return super().__new__(cls, value)


class PageSize(int):
    """The number of Transactions to include in each page
    of the results. [default=100, maximum=1000]"""

    def __new__(cls, value=100):
        if not 0 < value <= 1000:
            raise ValueError(f'PageSize: Must be within range(). Supplied: {value}')
        return super().__new__(cls, value)


class Type(str):
    pass


class UserSpecifier(str):
    pass


class FromTime(DateTime):
    """A DateTime to be used as the starting period of a query"""
    pass


class ToTime(DateTime):
    """A DateTime to be used as the ending period of a query"""
    pass


class TradeClientExtensions(ClientExtensions):
    pass


class LongClientExtensions(ClientExtensions):
    """The client extensions to add to the MarketOrder used to close the long
    position
    """
    pass


class ShortClientExtensions(ClientExtensions):
    """The client extensions to add to the MarketOrder used to close the short
    position"""
    pass


class Units(str):
    """Indication of how much of the Trade to close. Either the string "ALL"
    (indicating that all of the Trade should be closed), or a DecimalNumber
    representing the number of units of the open Trade to Close using a
    TradeClose MarketOrder. The units specified must always be positive, and
    the magnitude of the value cannot exceed the magnitude of the Trade’s
    open units
    """

    def __new__(cls, value='ALL'):
        return super().__new__(cls, value)


class LastTransactionID(TransactionID):
    """Contains the most recent TransactionID"""
    pass

class SinceTransactionID(TransactionID):
    """The account changes to get Since LastTransactionID for account_changes() method"""
    pass


class FromTransactionID(TransactionID):
    """A TransactionID to be used as the starting period of a query"""
    pass


class ToTransactionID(TransactionID):
    """A TransactionID to be used as the ending period of a query"""
    pass

class ServiceID(str):
    """The specifier of the service to get"""
    pass

class ServiceListID(str):
    """Identification string of service list to get"""
    pass

class Start(str):
    """Only show events which started after this date, inclusive.
    Suggested format  RFC 2822 or RFC 1123"""
    pass

class End(str):
    """Only show events which started before this date, inclusive.
    Suggested format  RFC 2822 or RFC 1123"""
    pass

class EventSid(str):
    """The SID of the event to get"""
    pass

class StatusID(str):
    """The ID of the status to get"""
    pass

