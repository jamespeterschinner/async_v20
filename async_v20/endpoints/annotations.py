from ..definitions.types import DateTime
from ..definitions.types import ClientExtensions


class Authorization(str): pass

class Instruments(str): pass

class Alias(str): pass

class Count(int): pass

class Smooth(bool): pass

# TODO figure out what this is about
class Incluclassirst(bool): pass

class DailyAlignment(int): pass

class AlignmentTimezone(str): pass

class Ids(str): pass

class LongUnits(str): pass
 # this needs to default to 'ALL'

class ShortUnits(str): pass
 #  this also needs to default to 'ALL'

class IncludeUnitsAvailable(bool): pass

class Snapshot(bool): pass

class PageSize(int): pass

class Type(str): pass

class UserSpecifier(str): pass

class FromDateTime(DateTime): pass

class ToDateTime(DateTime): pass

class TradeClientExtensions(ClientExtensions): pass

class LongClientExtensions(ClientExtensions): pass

class ShortClientExtensions(ClientExtensions): pass

class Units(str): pass