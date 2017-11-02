from ..definitions.base import Model
from ..definitions.types import ClientExtensions, ClientID, ClientComment, ClientTag
from ..definitions.types import DateTime
from ..definitions.types import TransactionID

__all__ = ['Alias', 'AlignmentTimezone', 'Authorization', 'Count', 'DailyAlignment', 'FromTime',
           'FromTransactionID', 'Ids', 'IncludeFirstQuery', 'IncludeUnitsAvailable', 'Instruments', 'LastTransactionID',
           'LongClientExtensions', 'LongUnits', 'PageSize', 'ShortClientExtensions', 'ShortUnits', 'Smooth', 'Snapshot',
           'ToTime', 'ToTransactionID', 'TradeClientExtensions', 'Type', 'Units', 'UserSpecifier']


class Bool(object):
    def __new__(cls, arg):
        return str(bool(arg))


class Authorization(str):
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
            raise ValueError(f'Count value {value} is NOT within range(1,5001)')
        return super().__new__(cls, value)


class Smooth(Bool):
    pass


class IncludeFirstQuery(Bool):
    """A flag that controls whether the candlestick that is covered by the
    from time should be included in the results. This flag enables clients
    to use the timestamp of the last completed candlestick received to poll
    for future candlesticks but avoid receiving the previous candlestick
    repeatedly. [default=True]"""

    def __new__(cls, value=True):
        return super().__new__(cls, value)


class DailyAlignment(str):
    # valid values
    # TODO: Identify all annotations that don't return string
    # and get placed in  the http query
    pass


class AlignmentTimezone(str):
    pass


class Ids(str):
    pass


class LongUnits(str):
    pass


# this needs to default to 'ALL'

class ShortUnits(str):
    pass


# this also needs to default to 'ALL'

class IncludeUnitsAvailable(Bool):
    pass  # bool


class Snapshot(Bool):
    pass  # bool


class PageSize(int):
    pass


class Type(str):
    pass


class UserSpecifier(str):
    pass


class FromTime(DateTime):
    pass


class ToTime(DateTime):
    pass


class TradeClientExtensions(ClientExtensions):
    def __new__(cls, id: ClientID = None, tag: ClientTag = None, comment: ClientComment = None):
        return Model.__new__(**locals())


class LongClientExtensions(ClientExtensions):
    def __new__(cls, id: ClientID = None, tag: ClientTag = None, comment: ClientComment = None):
        return Model.__new__(**locals())


class ShortClientExtensions(ClientExtensions):
    def __new__(cls, id: ClientID = None, tag: ClientTag = None, comment: ClientComment = None):
        return Model.__new__(**locals())


class Units(str):
    pass


class LastTransactionID(TransactionID):
    pass


class FromTransactionID(TransactionID):
    pass


class ToTransactionID(TransactionID):
    pass
