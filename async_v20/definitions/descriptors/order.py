from .base import Descriptor

__all__ = ['CancellableOrderType', 'OrderID', 'OrderPositionFill', 'OrderSpecifier', 'OrderState', 'OrderStateFilter',
           'OrderTriggerCondition', 'OrderType', 'TimeInForce']


class CancellableOrderType(Descriptor):
    """The type of the Order.
    """

    # Type checking
    typ = str

    # Valid values
    values = {
        'LIMIT': 'A Limit Order',
        'STOP': 'A Stop Order',
        'MARKET_IF_TOUCHED': 'A Market-if-touched Order',
        'TAKE_PROFIT': 'A Take Profit Order',
        'STOP_LOSS': 'A Stop Loss Order',
        'TRAILING_STOP_LOSS': 'A Trailing Stop Loss Order'
    }


class OrderID(Descriptor):
    """The Order’s identifier, unique within the Order’s Account.
    """

    # Type checking
    typ = str

    # Correct syntax of value
    format_syntax = 'The string representation of the OANDA-assigned OrderID. ' \
                    'OANDA-assigned OrderIDs are positive integers, and are derived from the ' \
                    'TransactionID of the Transaction that created the Order.'
    # Example of correct format
    example = '1523'


class OrderPositionFill(Descriptor):
    """Specification of how Positions in the Account
    are modified when the Order is filled.
    """

    # Type checking
    typ = str

    # Valid values
    values = {
        'OPEN_ONLY': 'When the Order is filled, only allow Positions to be opened or extended.',
        'REDUCE_FIRST': 'When the Order is filled, always fully reduce an existing Position '
                        'before opening a new Position.',
        'REDUCE_ONLY': 'When the Order is filled, only reduce an existing Position.',
        'DEFAULT': 'When the Order is filled, use REDUCE_FIRST behaviour for non-client hedging Accounts, '
                   'and OPEN_ONLY behaviour for client hedging Accounts.'
    }


class OrderSpecifier(Descriptor):
    """The specification of an Order as referred to by clients
    """

    # Type checking
    typ = str

    # Correct syntax of value
    format_syntax = 'Either the Order’s OANDA-assigned OrderID or the Order’s client-provided ' \
                    'ClientID prefixed by the “@” symbol'
    # Example of correct format
    example = '1523'


class OrderState(Descriptor):
    """The current state of the Order.
    """

    # Type checking
    typ = str

    # Valid values
    values = {
        'PENDING': 'The Order is currently pending execution',
        'FILLED': 'The Order has been filled',
        'TRIGGERED': 'The Order has been triggered',
        'CANCELLED': 'The Order has been cancelled'
    }


class OrderStateFilter(Descriptor):
    """The state to filter the requested Orders by.
    """

    # Type checking
    typ = str

    # Valid values
    values = {
        'PENDING': 'The Orders that are currently pending execution',
        'FILLED': 'The Orders that have been filled',
        'TRIGGERED': 'The Orders that have been triggered',
        'CANCELLED': 'The Orders that have been cancelled',
        'ALL': 'The Orders that are in any of the possible states listed above'
    }


class OrderTriggerCondition(Descriptor):
    """Specification of which price component should be used when determining if an
    Order should be triggered and filled. This allows Orders to be triggered based
    on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (
    ask for sell, bid for buy) price depending on the desired behaviour. Orders are
    always filled using their default price component. This feature is only provided
    through the REST API. Clients who choose to specify a non-default trigger condition
    will not see it reflected in any of OANDA’s proprietary or partner trading platforms,
    their transaction history or their account statements. OANDA platforms always assume
    that an Order’s trigger condition is set to the default value when indicating the distance
    from an Order’s trigger price, and will always provide the default trigger condition
    when creating or modifying an Order.
    """

    # Type checking
    typ = str

    # Valid values
    values = {
        'DEFAULT': 'Trigger an Order the “natural” way: '
                   'compare its price to the ask for long Orders and bid for short Orders.',
        'INVERSE': 'Trigger an Order the opposite of the “natural” way: '
                   'compare its price the bid for long Orders and ask for short Orders.',
        'BID': 'Trigger an Order by comparing its price to the bid regardless of whether it is long or short.',
        'ASK': 'Trigger an Order by comparing its price to the ask regardless of whether it is long or short.',
        'MID': 'Trigger an Order by comparing its price to the midpoint regardless of whether it is long or short.'
    }


class OrderType(Descriptor):
    """The type of the Order.
    """

    # Type checking
    typ = str

    # Valid values
    values = {
        'MARKET': 'A Market Order',
        'LIMIT': 'A Limit Order',
        'STOP': 'A Stop Order',
        'MARKET_IF_TOUCHED': 'A Market-if-touched Order',
        'TAKE_PROFIT': 'A Take Profit Order',
        'STOP_LOSS': 'A Stop Loss Order',
        'TRAILING_STOP_LOSS': 'A Trailing Stop Loss Order'
    }


class TimeInForce(Descriptor):
    """The time-in-force of an Order. TimeInForce describes how long an Order
    should remain pending before being automatically cancelled by the execution system.
    """

    # Type checking
    typ = str

    # Valid values
    values = {
        'GTC': 'The Order is “Good unTil Cancelled”',
        'GTD': 'The Order is “Good unTil Date” and will be cancelled at the provided time',
        'GFD': 'The Order is “Good For Day” and will be cancelled at 5pm New York time',
        'FOK': 'The Order must be immediately “Filled Or Killed”',
        'IOC': 'The Order must be “Immediatedly paritally filled Or Cancelled”'
    }
