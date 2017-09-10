from .base import Descriptor

class TradeID(Descriptor):
    """The Trade’s identifier, unique within the Trade’s Account.
    """

    # Type checking
    typ = str

    # Correct syntax of value
    format_syntax = 'The string representation of the OANDA-assigned TradeID. OANDA-assigned TradeIDs are positive integers, and are derived from the TransactionID of the Transaction that opened the Trade.'
    # Example of correct format
    example = '1523'


class TradePL(Descriptor):
    """The classification of TradePLs.
    """

    # Type checking
    typ = str

    # Valid values
    values = {
        'POSITIVE': 'An open Trade currently has a positive (profitable) unrealized P/L, or a closed Trade realized a positive amount of P/L.',
        'NEGATIVE': 'An open Trade currently has a negative (losing) unrealized P/L, or a closed Trade realized a negative amount of P/L.',
        'ZERO': 'An open Trade currently has unrealized P/L of zero (neither profitable nor losing), or a closed Trade realized a P/L amount of zero.'
    }


class TradeSpecifier(Descriptor):
    """The identification of a Trade as referred to by clients
    """

    # Type checking
    typ = str

    # Correct syntax of value
    format_syntax = 'Either the Trade’s OANDA-assigned TradeID or the Trade’s client-provided ClientID prefixed by the “@” symbol'
    # Example of correct format
    example = '@my_trade_id'


class TradeState(Descriptor):
    """The current state of the Trade.
    """

    # Type checking
    typ = str

    # Valid values
    values = {
        'OPEN': 'The Trade is currently open',
        'CLOSED': 'The Trade has been fully closed',
        'CLOSE_WHEN_TRADEABLE': 'The Trade will be closed as soon as the trade’s instrument becomes tradeable'
    }


class TradeStateFilter(Descriptor):
    """The state to filter the Trades by
    """

    # Type checking
    typ = str

    # Valid values
    values = {
        'OPEN': 'The Trades that are currently open',
        'CLOSED': 'The Trades that have been fully closed',
        'CLOSE_WHEN_TRADEABLE': 'The Trades  that will be closed as soon as the trades’ instrument becomes tradeable',
        'ALL': 'The Trades that are in any of the possible states listed above.'
    }



