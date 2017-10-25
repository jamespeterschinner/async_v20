from ..definitions.types import ClientExtensions
from ..definitions.types import DateTime
from ..definitions.types import TransactionID


class Authorization(str):
    pass


class Instruments(str):
    pass


class Alias(str):
    pass


class Count(int):
    pass


class Smooth(object):
    pass  # bool


class includeFirst(object):
    pass  # bool


class DailyAlignment(int):
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

class IncludeUnitsAvailable(object):
    pass  # bool


class Snapshot(object):
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
    pass


class LongClientExtensions(ClientExtensions):
    pass


class ShortClientExtensions(ClientExtensions):
    pass


class Units(str):
    pass


class LastTransactionID(TransactionID):
    pass

class FromTransactionID(TransactionID):
    pass

class ToTransactionID(TransactionID):
    pass