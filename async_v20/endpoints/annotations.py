from ..definitions.types import ClientExtensions, ClientID, ClientComment, ClientTag
from ..definitions.types import DateTime
from ..definitions.types import TransactionID
from ..definitions.base import Model

class Bool(object):
    def __new__(cls, arg):
        return bool(arg)

class Authorization(str):
    pass


class Instruments(str):
    pass


class Alias(str):
    pass


class Count(int):
    pass


class Smooth(Bool):
    pass


class includeFirst(Bool):
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
    def __new__(self, id: ClientID = None, tag: ClientTag = None, comment: ClientComment = None):
        return Model.__new__(**locals())


class LongClientExtensions(ClientExtensions):
    def __new__(self, id: ClientID = None, tag: ClientTag = None, comment: ClientComment = None):
        return Model.__new__(**locals())


class ShortClientExtensions(ClientExtensions):
    def __new__(self, id: ClientID = None, tag: ClientTag = None, comment: ClientComment = None):
        return Model.__new__(**locals())


class Units(str):
    pass


class LastTransactionID(TransactionID):
    pass

class FromTransactionID(TransactionID):
    pass

class ToTransactionID(TransactionID):
    pass