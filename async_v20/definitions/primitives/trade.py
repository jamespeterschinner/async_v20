from .helpers import domain_check

__all__ = ['TradeID', 'TradePL', 'TradeSpecifier', 'TradeState', 'TradeStateFilter']


class TradeID(int):
    """The Trade’s identifier, unique within the Trade’s Account.
    """

    # Correct syntax of value
    format_syntax = 'The string representation of the OANDA-assigned TradeID. ' \
                    'OANDA-assigned TradeIDs are positive integers, and are ' \
                    'derived from the TransactionID of the Transaction that opened the Trade.'
    # Example of correct format
    example = '1523'

    # TODO replace with super() call when possible
    def __new__(cls, value):
        return int(value)

class TradePL(str):
    """The classification of TradePLs.
    """

    # Valid values
    values = {
        'POSITIVE': 'An open Trade currently has a positive (profitable) unrealized P/L, '
                    'or a closed Trade realized a positive amount of P/L.',
        'NEGATIVE': 'An open Trade currently has a negative (losing) unrealized P/L, '
                    'or a closed Trade realized a negative amount of P/L.',
        'ZERO': 'An open Trade currently has unrealized P/L of zero (neither profitable nor losing),'
                ' or a closed Trade realized a P/L amount of zero.'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class TradeSpecifier(str):
    """The identification of a Trade as referred to by clients
    """

    # Correct syntax of value
    format_syntax = 'Either the Trade’s OANDA-assigned TradeID or the Trade’s client-provided ' \
                    'ClientID prefixed by the “@” symbol'
    # Example of correct format
    example = '@my_trade_id'

    def __new__(cls, value):
        assert domain_check(value, example=cls.example)
        return super().__new__(cls, value)


class TradeState(str):
    """The current state of the Trade.
    """

    # Valid values
    values = {
        'OPEN': 'The Trade is currently open',
        'CLOSED': 'The Trade has been fully closed',
        'CLOSE_WHEN_TRADEABLE': 'The Trade will be closed as soon as the trade’s instrument becomes tradeable'
    }

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)


class TradeStateFilter(str):
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

    def __new__(cls, value):
        assert domain_check(value, possible_values=cls.values)
        return super().__new__(cls, value)

