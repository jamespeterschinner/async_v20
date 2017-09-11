from ..types import *
from ...endpoints.metaclass import Array

default = lambda x: x
required = True
boolean = bool
integer = int
string = str


class Instrument:
    """Full specification of an Instrument.
    """
    # JSON representation of object
    schema = {
        # The name of the Instrument
        'name': InstrumentName,
        # The type of the Instrument
        'type': InstrumentType,
        # The display name of the Instrument
        'displayName': string,
        # The location of the “pip” for this instrument. The decimal position of
        # the pip in this Instrument’s price can be found at 10 ^ pipLocation (e.g.
        # -4 pipLocation results in a decimal pip position of 10 ^ -4 = 0.0001).
        'pipLocation': integer,
        # The number of decimal places that should be used to display prices for
        # this instrument. (e.g. a displayPrecision of 5 would result in a price of
        # “1” being displayed as “1.00000”)
        'displayPrecision': integer,
        # The amount of decimal places that may be provided when specifying the
        # number of units traded for this instrument.
        'tradeUnitsPrecision': integer,
        # The smallest number of units allowed to be traded for this instrument.
        'minimumTradeSize': DecimalNumber,
        # The maximum trailing stop distance allowed for a trailing stop loss
        # created for this instrument. Specified in price units.
        'maximumTrailingStopDistance': DecimalNumber,
        # The minimum trailing stop distance allowed for a trailing stop loss
        # created for this instrument. Specified in price units.
        'minimumTrailingStopDistance': DecimalNumber,
        # The maximum position size allowed for this instrument. Specified in
        # units.
        'maximumPositionSize': DecimalNumber,
        # The maximum units allowed for an Order placed for this instrument.
        # Specified in units.
        'maximumOrderUnits': DecimalNumber,
        # The margin rate for this instrument.
        'marginRate': DecimalNumber,
        # The commission structure for this instrument.
        'commission': InstrumentCommission}


class InstrumentCommission:
    """An InstrumentCommission represents an instrument-specific commission
    """
    # JSON representation of object
    schema = {
        # The name of the instrument
        'instrument': InstrumentName,
        # The commission amount (in the Account’s home currency) charged per
        # unitsTraded of the instrument
        'commission': DecimalNumber,
        # The number of units traded that the commission amount is based on.
        'unitsTraded': DecimalNumber,
        # The minimum commission amount (in the Account’s home currency) that is
        # charged when an Order is filled for this instrument.
        'minimumCommission': DecimalNumber}
