from .base import Descriptor


class AccountFinancingMode(Descriptor):
    """The financing mode of an Account
    """

    # Type checking
    typ = str

    # Valid values
    values = {
        'NO_FINANCING': 'No financing is paid/charged for open Trades in the Account',
        'SECOND_BY_SECOND': 'Second-by-second financing is paid/charged for open Trades in the Account, '
                            'both daily and when the the Trade is closed',
        'DAILY': 'A full day’s worth of financing is paid/charged for open Trades in the Account '
                 'daily at 5pm New York time'
    }


class AccountID(Descriptor):
    """The string representation of an Account Identifier.
    """

    # Type checking
    typ = str

    # Correct syntax of value
    format_syntax = '“-“-delimited string with format “{siteID}-{divisionID}-{userID}-{accountNumber}”'
    # Example of correct format
    example = '001-011-5838423-001'


class PositionAggregationMode(Descriptor):
    """The way that position values for an Account are calculated and aggregated.
    """

    # Type checking
    typ = str

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
