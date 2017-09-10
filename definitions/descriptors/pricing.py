from .base import Descriptor

class PriceStatus(Descriptor):
    """The status of the Price.
    """

    # Type checking
    typ = str

    # Valid values
    values = {
        'tradeable': 'The Instrument’s price is tradeable.',
        'non-tradeable': 'The Instrument’s price is not tradeable.',
        'invalid': 'The Instrument of the price is invalid or there is no valid Price for the Instrument.'
    }


class PriceValue(Descriptor):
    """The string representation of a Price for an Instrument.
    """

    # Type checking
    typ = (str, float)

    # Correct syntax of value
    format_syntax = 'A decimal number encodes as a string. The amount of precision provided depends on the Price’s Instrument.'


