from .helpers import domain_check

__all__ = ['AcceptDatetimeFormat', 'AccountUnits', 'Currency', 'DateTime', 'DecimalNumber',
           'Unit', 'Direction',
           'InstrumentName', 'InstrumentType']


class AcceptDatetimeFormat(str):
    """DateTime header
    """

    # Valid values
    values = {
        'UNIX': 'If “UNIX” is specified DateTime fields will be specified or '
                'returned in the “12345678.000000123” format.',
        'RFC3339': 'If “RFC3339” is specified DateTime will be specified or '
                   'returned in “YYYY-MM-DDTHH:MM:SS.nnnnnnnnnZ” format.'
    }
    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class AccountUnits(float):
    """The string representation of a quantity of an Account’s home currency.
    """

    # Type checking
    # TODO keep an eye on this. OANDA specifies this as a str.
    # Though it makes more sense for it to be a float
    # floats automatically get converted to to strings anyway
    # when serialized into JSON

    # Correct syntax of value
    format_syntax = 'A decimal number encoded as a string. The amount of precision ' \
                    'provided depends on the Account’s home currency.'
    def __new__(cls, value):
        return super().__new__(cls, value)


class Currency(str):
    """Currency name identifier. Used by clients to refer to currencies.
    """

    # Correct syntax of value
    format_syntax = 'A string containing an ISO 4217 currency'

    def __new__(cls, value):
        return super().__new__(cls, value)


class DateTime(str):
    """A date and time value using either RFC3339 or UNIX time representation.
    """

    # Correct syntax of value
    format_syntax = 'The RFC 3339 representation is a string conforming to'

    def __new__(cls, value):
        return super().__new__(cls, value)


class DecimalNumber(float):
    """The string representation of a decimal number.
    """

    # Correct syntax of value
    format_syntax = 'A decimal number encoded as a string. The amount of precision ' \
                    'provided depends on what the number represents.'

    def __new__(cls, value):
        return super().__new__(cls, round(float(value),5))


class Unit(float):
    """A unit is a standard allotment of a currency
    """

    # Correct syntax of value
    format_syntax = 'A decimal number encoded as a string. The amount of precision ' \
                    'provided depends on what the number represents.'

    def __new__(cls, value):
        return super().__new__(cls, round(float(value),0))


class Direction(str):
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


class InstrumentName(str):
    """Instrument name identifier. Used by clients to refer to an Instrument.
    """

    # Correct syntax of value
    format_syntax = 'A string containing the base currency and quote currency delimited by a “_”.'

    def __new__(cls, value):
        return super().__new__(cls, value)


class InstrumentType(str):
    """The type of an Instrument.
    """

    # Type checking
    typ = str

    # Valid values
    values = {
        'CURRENCY': 'Currency',
        'CFD': 'Contract For Difference',
        'METAL': 'Metal'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)