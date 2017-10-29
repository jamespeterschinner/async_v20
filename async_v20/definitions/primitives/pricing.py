from .helpers import domain_check

__all__ = ['PriceStatus', 'PriceValue']


class PriceStatus(str):
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


class PriceValue(float):
    """The string representation of a Price for an Instrument.
    """

    # Correct syntax of value
    format_syntax = 'A decimal number encodes as a string. The amount of precision ' \
                    'provided depends on the Price’s Instrument.'

    def __new__(cls, value):
        return super().__new__(cls, round(float(value), 5))