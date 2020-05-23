from .base import *
from .primitives import *

__all__ = ['Account', 'AccountChanges', 'AccountChangesState', 'AccountProperties', 'AccountSummary',
           'ArrayAccountProperties', 'ArrayCalculatedPositionState', 'ArrayCalculatedTradeState', 'ArrayCandlestick',
           'ArrayDynamicOrderState', 'ArrayInstrument', 'ArrayLiquidityRegenerationScheduleStep',
           'ArrayOpenTradeFinancing', 'ArrayOrder', 'ArrayOrderBookBucket', 'ArrayPosition', 'ArrayPositionBookBucket',
           'ArrayPositionFinancing', 'ArrayPrice', 'ArrayPriceBucket', 'ArrayStr', 'ArrayTrade', 'ArrayTradeID',
           'ArrayTradeReduce', 'ArrayTradeSummary', 'ArrayTransaction', 'ArrayTransactionFilter', 'ArrayTransactionID',
           'CalculatedPositionState', 'CalculatedTradeState', 'Candlestick', 'CandlestickData',
           'ClientConfigureRejectTransaction', 'ClientConfigureTransaction', 'ClientExtensions', 'ClientPrice',
           'CloseTransaction', 'CreateTransaction', 'DailyFinancingTransaction', 'DelayedTradeClosureTransaction',
           'DynamicOrderState', 'Instrument', 'InstrumentCommission', 'LimitOrder', 'LimitOrderRejectTransaction',
           'LimitOrderRequest', 'LimitOrderTransaction', 'LiquidityRegenerationSchedule',
           'LiquidityRegenerationScheduleStep', 'MarginCallEnterTransaction', 'MarginCallExitTransaction',
           'MarginCallExtendTransaction', 'MarketIfTouchedOrder', 'MarketIfTouchedOrderRejectTransaction',
           'MarketIfTouchedOrderRequest', 'MarketIfTouchedOrderTransaction', 'MarketOrder',
           'MarketOrderDelayedTradeClose', 'MarketOrderMarginCloseout', 'MarketOrderPositionCloseout',
           'MarketOrderRejectTransaction', 'MarketOrderRequest', 'MarketOrderTradeClose', 'MarketOrderTransaction',
           'OpenTradeFinancing', 'Order', 'OrderBook', 'OrderBookBucket', 'OrderCancelRejectTransaction',
           'OrderCancelTransaction', 'OrderClientExtensionsModifyRejectTransaction',
           'OrderClientExtensionsModifyTransaction', 'OrderFillTransaction', 'OrderIdentifier', 'OrderRequest',
           'Position', 'PositionBook', 'PositionBookBucket', 'PositionFinancing', 'PositionSide', 'Price',
           'PriceBucket', 'PricingHeartbeat', 'QuoteHomeConversionFactors', 'ReopenTransaction',
           'ResetResettablePLTransaction', 'StopLossDetails', 'StopLossOrder', 'StopLossOrderRejectTransaction',
           'StopLossOrderRequest', 'StopLossOrderTransaction', 'StopOrder', 'StopOrderRejectTransaction',
           'StopOrderRequest', 'StopOrderTransaction', 'TakeProfitDetails', 'TakeProfitOrder',
           'TakeProfitOrderRejectTransaction', 'TakeProfitOrderRequest', 'TakeProfitOrderTransaction', 'Trade',
           'TradeClientExtensionsModifyRejectTransaction', 'TradeClientExtensionsModifyTransaction', 'TradeOpen',
           'TradeReduce', 'TradeSummary', 'TrailingStopLossDetails', 'TrailingStopLossOrder',
           'TrailingStopLossOrderRejectTransaction', 'TrailingStopLossOrderRequest', 'TrailingStopLossOrderTransaction',
           'Transaction', 'TransactionHeartbeat', 'TransferFundsRejectTransaction', 'TransferFundsTransaction',
           'UnitsAvailable', 'UnitsAvailableDetails', 'UserInfo', 'UserInfoExternal', 'VWAPReceipt']


class ArrayStr(Array, contains=str):
    pass


class ArrayTradeID(Array, contains=TradeID):
    pass


class ArrayTransactionFilter(Array, contains=TransactionFilter):
    pass


class ArrayTransactionID(Array, contains=TransactionID):
    pass


class ArrayDict(Array, contains=dict):
    # TODO: Update this class when OANDA updates documentation for Instrument class.
    # This class is used for the 'tags' attribute of the Instrument class
    pass


class ClientExtensions(Model):
    """A ClientExtensions object allows a client to attach a clientID, tag and
    comment to Orders and Trades in their Account.  Do not set, modify, or
    delete this field if your account is associated with MT4.

    Attributes:
        id: :class:`~async_v20.ClientID`
            The Client ID of the Order/Trade
        tag: :class:`~async_v20.ClientTag`
            A tag associated with the Order/Trade
        comment: :class:`~async_v20.ClientComment`
            A comment associated with the Order/Trade

    """

    def __init__(self, id: ClientID = sentinel, tag: ClientTag = sentinel, comment: ClientComment = sentinel):
        Model.__init__(**locals())


class TakeProfitDetails(Model):
    """TakeProfitDetails specifies the details of a Take Profit Order to be
    created on behalf of a client. This may happen when an Order is filled that
    opens a Trade requiring a Take Profit, or when a Trade's dependent Take
    Profit Order is modified directly through the Trade.

    Attributes:
        price: :class:`~async_v20.PriceValue`
            The price that the Take Profit Order will be triggered at.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time in force for the created Take Profit
            Order. This may only be GTC, GTD or GFD.
        gtd_time: :class:`~async_v20.DateTime`
            The date when the Take Profit Order will be cancelled on if timeInForce is GTD.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The Client Extensions to add to the Take Profit Order when created.

    """

    def __init__(self, price: PriceValue = sentinel, time_in_force: TimeInForce = sentinel,
                 gtd_time: DateTime = sentinel,
                 client_extensions: ClientExtensions = sentinel):
        Model.__init__(**locals())


class StopLossDetails(Model):
    """StopLossDetails specifies the details of a Stop Loss Order to be created on
    behalf of a client. This may happen when an Order is filled that opens a
    Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is
    modified directly through the Trade.

    Attributes:
        price: :class:`~async_v20.PriceValue`
            The price that the Stop Loss Order will be triggered at.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time in force for the created Stop Loss
            Order. This may only be GTC, GTD or GFD.
        gtd_time: :class:`~async_v20.DateTime`
            The date when the Stop Loss Order will be cancelled on if timeInForce is GTD.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The Client Extensions to add to the Stop Loss Order when created.

    """

    def __init__(self, price: PriceValue = sentinel, time_in_force: TimeInForce = sentinel,
                 gtd_time: DateTime = sentinel,
                 client_extensions: ClientExtensions = sentinel):
        Model.__init__(**locals())


class TrailingStopLossDetails(Model):
    """TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order
    to be created on behalf of a client. This may happen when an Order is
    filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's
    dependent Trailing Stop Loss Order is modified directly through the Trade.

    Attributes:
        distance: :class:`~async_v20.PriceValue`
            The distance (in price units) from the Trade's fill price
            that the Trailing Stop Loss Order will be triggered at.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time in force for the created Trailing Stop
            Loss Order. This may only be GTC, GTD or GFD.
        gtd_time: :class:`~async_v20.DateTime`
            The date when the Trailing Stop Loss Order
            will be cancelled on if timeInForce is GTD.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The Client Extensions to add to the Trailing Stop Loss Order when created.

    """

    def __init__(self, distance: PriceValue = sentinel, time_in_force: TimeInForce = sentinel,
                 gtd_time: DateTime = sentinel,
                 client_extensions: ClientExtensions = sentinel):
        Model.__init__(**locals())


class OrderRequest(Model, jit=False):
    """The base Order specification. Contains all attributes an OrderRequest
    may contain.

    Attributes:

        instrument: :class:`~async_v20.InstrumentName`
        trade_id: :class:`~async_v20.TradeID`
        price: :class:`~async_v20.PriceValue`
        type: :class:`~async_v20.OrderType`
        client_trade_id: :class:`~async_v20.ClientID`
        time_in_force: :class:`~async_v20.TimeInForce`
        gtd_time: :class:`~async_v20.DateTime`
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
        client_extensions: :class:`~async_v20.ClientExtensions`
        distance: :class:`~async_v20.PriceValue`
        instrument: :class:`~async_v20.InstrumentName`
        units: :class:`~async_v20.DecimalNumber`
        price_bound: :class:`~async_v20.PriceValue`
        position_fill: :class:`~async_v20.OrderPositionFill`
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
    """

    def __init__(self, instrument: InstrumentName, trade_id: TradeID = sentinel, price: PriceValue = sentinel,
                 type: OrderType = sentinel,
                 client_trade_id: ClientID = sentinel, time_in_force: TimeInForce = sentinel,
                 gtd_time: DateTime = sentinel,
                 trigger_condition: OrderTriggerCondition = sentinel, client_extensions: ClientExtensions = sentinel,
                 distance: PriceValue = sentinel, units: DecimalNumber = sentinel,
                 price_bound: PriceValue = sentinel, position_fill: OrderPositionFill = sentinel,
                 take_profit_on_fill: TakeProfitDetails = sentinel, stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel):
        Model.__init__(**locals())


class UnitsAvailableDetails(Model):
    """Representation of how many units of an Instrument are available to be traded
    for both long and short Orders.

    Attributes:
        long: :class:`~async_v20.DecimalNumber`
            The units available for long Orders.
        short: :class:`~async_v20.DecimalNumber`
            The units available for short Orders.

    """

    def __init__(self, long: DecimalNumber = sentinel, short: DecimalNumber = sentinel):
        Model.__init__(**locals())


class UnitsAvailable(Model):
    """Representation of how many units of an Instrument are available to be
    traded by an Order depending on its position Fill option.

    Attributes:

        default: :class:`~async_v20.UnitsAvailableDetails`
            The number of units that are available to be traded using an Order with a positionFill option of
            "DEFAULT". For an Account with hedging enabled,
            this value will be the same as the "OPEN_ONLY" value. For an Account without hedging enabled,
            this value will be the same as the "REDUCE_FIRST" value.
        reduce_first: :class:`~async_v20.UnitsAvailableDetails`
            The number of units that may are available to be
            traded with an Order with a positionFill option of "REDUCE_FIRST".
        reduce_only: :class:`~async_v20.UnitsAvailableDetails`
            The number of units that may are available to be
            traded with an Order with a positionFill option of "REDUCE_ONLY".
        open_only: :class:`~async_v20.UnitsAvailableDetails`
            The number of units that may are available to be
            traded with an Order with a positionFill option of "OPEN_ONLY".

    """

    def __init__(self, default: UnitsAvailableDetails = sentinel, reduce_first: UnitsAvailableDetails = sentinel,
                 reduce_only: UnitsAvailableDetails = sentinel, open_only: UnitsAvailableDetails = sentinel):
        Model.__init__(**locals())


class LiquidityRegenerationScheduleStep(Model):
    """A liquidity regeneration schedule Step indicates the amount of bid and ask
    liquidity that is used by the Account at a certain time. These amounts will
    only change at the timestamp of the following step.

    Attributes:
        timestamp: :class:`~async_v20.DateTime`
            The timestamp of the schedule step.
        bid_liquidity_used: :class:`~async_v20.DecimalNumber`
            The amount of bid liquidity used at this step in the schedule.
        ask_liquidity_used: :class:`~async_v20.DecimalNumber`
            The amount of ask liquidity used at this step in the schedule.

    """

    def __init__(self, timestamp: DateTime = sentinel, bid_liquidity_used: DecimalNumber = sentinel,
                 ask_liquidity_used: DecimalNumber = sentinel):
        Model.__init__(**locals())


class ArrayLiquidityRegenerationScheduleStep(Array, contains=LiquidityRegenerationScheduleStep):
    pass


class LiquidityRegenerationSchedule(Model):
    """A LiquidityRegenerationSchedule indicates how liquidity that is used when
    filling an Order for an instrument is regenerated following the fill.  A
    liquidity regeneration schedule will be in effect until the timestamp of
    its final step, but may be replaced by a schedule created for an Order of
    the same instrument that is filled while it is still in effect.

    Attributes:
        steps: ( :class:`~async_v20.LiquidityRegenerationScheduleStep`, ...)
            The steps in the Liquidity Regeneration Schedule

    """

    def __init__(self, steps: ArrayLiquidityRegenerationScheduleStep = sentinel):
        Model.__init__(**locals())


class CandlestickData(Model):
    """The price data (open, high, low, close) for the Candlestick representation.

    Attributes:
        o: :class:`~async_v20.PriceValue`
            The first (open) price in the time-range represented by the candlestick.
        h: :class:`~async_v20.PriceValue`
            The highest price in the time-range represented by the candlestick.
        l: :class:`~async_v20.PriceValue`
            The lowest price in the time-range represented by the candlestick.
        c: :class:`~async_v20.PriceValue`
            The last (closing) price in the time-range represented by the candlestick.

    """

    def __init__(self, o: PriceValue = sentinel, h: PriceValue = sentinel, l: PriceValue = sentinel,
                 c: PriceValue = sentinel):
        Model.__init__(**locals())


class OrderIdentifier(Model):
    """An OrderIdentifier is used to refer to an Order, and contains both the
    OrderID and the ClientOrderID.

    Attributes:
        order_id: :class:`~async_v20.OrderID`
            The OANDA-assigned Order ID
        client_order_id: :class:`~async_v20.OrderID`
            The client-provided client Order ID

    """

    def __init__(self, order_id: OrderID = sentinel, client_order_id: ClientID = sentinel):
        Model.__init__(**locals())


class QuoteHomeConversionFactors(Model):
    """QuoteHomeConversionFactors represents the factors that can be used used to
    convert quantities of a Price's Instrument's quote currency into the
    Account's home currency.

    Attributes:
        positive_units: :class:`~async_v20.DecimalNumber`
            The factor used to convert a positive amount of the
            Price's Instrument's quote currency into a positive
            amount of the Account's home currency. Conversion is performed by multiplying
            the quote units by the conversion factor.
        negative_units: :class:`~async_v20.DecimalNumber`
            The factor used to convert a negative amount of the Price's Instrument's
            quote currency into a negative amount of the Account's home currency. Conversion is performed by
            multiplying the quote units by the conversion factor.

    """

    def __init__(self, positive_units: DecimalNumber = sentinel, negative_units: DecimalNumber = sentinel):
        Model.__init__(**locals())


class MarketOrderMarginCloseout(Model):
    """Details for the Market Order extensions specific to a Market Order placed
    that is part of a Market Order Margin Closeout in a client's account

    Attributes:
        reason: :class:`~async_v20.MarketOrderMarginCloseoutReason`
            The reason the Market Order was created to perform a margin closeout

    """

    def __init__(self, reason: MarketOrderMarginCloseoutReason = sentinel):
        Model.__init__(**locals())


class InstrumentCommission(Model):
    """An InstrumentCommission represents an instrument-specific commission

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The name of the instrument
        commission: :class:`~async_v20.DecimalNumber`
            The commission amount (in the Account's home
            currency) charged per unitsTraded of the instrument
        units_traded: :class:`~async_v20.DecimalNumber`
            The number of units traded that the commission amount is based on.
        minimum_commission: :class:`~async_v20.DecimalNumber`
            The minimum commission amount (in the Account's home currency) that
            is charged when an Order is filled for this instrument.

    """

    def __init__(self, instrument: InstrumentName = sentinel, commission: DecimalNumber = sentinel,
                 units_traded: DecimalNumber = sentinel,
                 minimum_commission: DecimalNumber = sentinel):
        Model.__init__(**locals())


class OrderBookBucket(Model):
    """The order book data for a partition of the instrument's prices.

    Attributes:
        price: :class:`~async_v20.PriceValue`
            The lowest price (inclusive) covered by the bucket. The bucket covers the
            price range from the price to price + the order book's bucketWidth.
        long_count_percent: :class:`~async_v20.DecimalNumber`
            The percentage of the total number of orders
            represented by the long orders found in this bucket.
        short_count_percent: :class:`~async_v20.DecimalNumber`
            The percentage of the total number of orders
            represented by the short orders found in this bucket.

    """

    def __init__(self, price: PriceValue = sentinel, long_count_percent: DecimalNumber = sentinel,
                 short_count_percent: DecimalNumber = sentinel):
        Model.__init__(**locals())


class ArrayOrderBookBucket(Array, contains=OrderBookBucket):
    pass


class PositionBookBucket(Model):
    """The position book data for a partition of the instrument's prices.

    Attributes:
        price: :class:`~async_v20.PriceValue`
            The lowest price (inclusive) covered by the bucket. The bucket covers the
            price range from the price to price + the position book's bucketWidth.
        long_count_percent: :class:`~async_v20.DecimalNumber`
            The percentage of the total number of positions
            represented by the long positions found in this bucket.
        short_count_percent: :class:`~async_v20.DecimalNumber`
            The percentage of the total number of positions
            represented by the short positions found in this bucket.

    """

    def __init__(self, price: PriceValue = sentinel, long_count_percent: DecimalNumber = sentinel,
                 short_count_percent: DecimalNumber = sentinel):
        Model.__init__(**locals())


class ArrayPositionBookBucket(Array, contains=PositionBookBucket):
    pass


class DynamicOrderState(Model):
    """The dynamic state of an Order. This is only relevant to TrailingStopLoss
    Orders, as no other Order type has dynamic state.

    Attributes:
        id: :class:`~async_v20.OrderID`
            The Order's ID.
        trailing_stop_value: :class:`~async_v20.PriceValue`
            The Order's calculated trailing stop value.
        trigger_distance: :class:`~async_v20.PriceValue`
            The distance between the Trailing Stop Loss Order's trailingStopValue and the current
            Market Price. This represents the distance (in price
            units) of the Order from a triggering price. If the distance could not be determined,
            this value will not be set.
        is_trigger_distance_exact: :class:`bool`
            True if an exact trigger distance could be calculated. If false,
            it means the provided trigger distance
            is a best estimate. If the distance could not be determined, this value will not be set.

    """

    def __init__(self, id: OrderID = sentinel, trailing_stop_value: PriceValue = sentinel,
                 trigger_distance: PriceValue = sentinel,
                 is_trigger_distance_exact: bool = sentinel):
        Model.__init__(**locals())


class ArrayDynamicOrderState(Array, contains=DynamicOrderState):
    pass


class CalculatedPositionState(Model):
    """The dynamic (calculated) state of a Position

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The Position's Instrument.
        net_unrealized_pl: :class:`~async_v20.AccountUnits`
            The Position's net unrealized profit/loss
        long_unrealized_pl: :class:`~async_v20.AccountUnits`
            The unrealized profit/loss of the Position's long open Trades
        short_unrealized_pl: :class:`~async_v20.AccountUnits`
            The unrealized profit/loss of the Position's short open Trades
        Margin_used:
            Margin currently used by the Position

    """

    def __init__(self, instrument: InstrumentName = sentinel, net_unrealized_pl: AccountUnits = sentinel,
                 long_unrealized_pl: AccountUnits = sentinel, short_unrealized_pl: AccountUnits = sentinel,
                 margin_used: AccountUnits = sentinel):
        Model.__init__(**locals())


class ArrayCalculatedPositionState(Array, contains=CalculatedPositionState, one_to_many=False):
    pass


class PositionSide(Model):
    """The representation of a Position for a single direction (long or short).

    Attributes:
        units: :class:`~async_v20.DecimalNumber`
            Number of units in the position (negative
            value indicates short position, positive indicates long position).
        average_price: :class:`~async_v20.PriceValue`
            Volume-weighted average of the underlying Trade open prices for the Position.
        trade_ids: ( :class:`~async_v20.TradeID`, ...),
            List of the open Trade IDs which contribute to the open Position.
        pl: :class:`~async_v20.AccountUnits`
            Profit/loss realized by the PositionSide over the lifetime of the Account.
        unrealized_pl: :class:`~async_v20.AccountUnits`
            The unrealized profit/loss of all open
            Trades that contribute to this PositionSide.
        resettable_pl: :class:`~async_v20.AccountUnits`
            Profit/loss realized by the PositionSide since the
            Account's resettablePL was last reset by the client.

    """

    def __init__(self, units: DecimalNumber = sentinel, average_price: PriceValue = sentinel,
                 trade_ids: ArrayTradeID = sentinel,
                 pl: AccountUnits = sentinel, unrealized_pl: AccountUnits = sentinel,
                 resettable_pl: AccountUnits = sentinel,
                 financing: DecimalNumber = sentinel,
                 guaranteed_execution_fees: AccountUnits = sentinel):
        Model.__init__(**locals())


class Position(Model):
    """The specification of a Position within an Account.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The Position's Instrument.
        pl: :class:`~async_v20.AccountUnits`
            Profit/loss realized by the Position over the lifetime of the Account.
        unrealized_pl: :class:`~async_v20.AccountUnits`
            The unrealized profit/loss of all open Trades that contribute to this Position.
        resettable_pl: :class:`~async_v20.AccountUnits`
            Profit/loss realized by the Position since the
            Account's resettablePL was last reset by the client.
        commission: :class:`~async_v20.AccountUnits`
            The total amount of commission paid for this instrument over
            the lifetime of the Account. Represented in the Account's home currency.
        long: :class:`~async_v20.PositionSide`
            The details of the long side of the Position.
        short: :class:`~async_v20.PositionSide`
            The details of the short side of the Position.

    """

    def __init__(self, instrument: InstrumentName = sentinel, pl: AccountUnits = sentinel,
                 unrealized_pl: AccountUnits = sentinel,
                 resettable_pl: AccountUnits = sentinel, commission: AccountUnits = sentinel,
                 long: PositionSide = sentinel,
                 short: PositionSide = sentinel, financing: DecimalNumber = sentinel,
                 margin_used: AccountUnits = sentinel,
                 guaranteed_execution_fees: AccountUnits = sentinel):
        Model.__init__(**locals())


class ArrayPosition(Array, contains=Position, one_to_many=False):
    pass


class PriceBucket(Model):
    """A Price Bucket represents a price available for an amount of liquidity

    Attributes:
        price: :class:`~async_v20.PriceValue`
            The Price offered by the PriceBucket
        liquidity: :class:`int`
            The amount of liquidity offered by the PriceBucket

    """

    def __init__(self, price: PriceValue = sentinel, liquidity: int = sentinel):
        Model.__init__(**locals())


class ArrayPriceBucket(Array, contains=PriceBucket):
    pass


class ClientPrice(Model):
    """Client price for an Account.

    Attributes:
        bids: ( :class:`~async_v20.PriceBucket`, ...),
            The list of prices and liquidity available on the Instrument's bid side.
            It is possible for this list to be empty if there is no
            bid liquidity currently available for the Instrument in the Account.
        asks: ( :class:`~async_v20.PriceBucket`, ...),
            The list of prices and liquidity available on the Instrument's ask side.
            It is possible for this list to be empty if there is no
            ask liquidity currently available for the Instrument in the Account.
        closeout_bid: :class:`~async_v20.PriceValue`
            The closeout bid Price. This Price is used when a bid is required to closeout a Position
            (margin closeout
            or manual) yet there is no bid liquidity. The closeout bid is never used to open a new position.
        closeout_ask: :class:`~async_v20.PriceValue`
            The closeout ask Price. This Price is used when a ask is required to closeout a Position
            (margin closeout or manual) yet there is no ask liquidity.
            The closeout ask is never used to open a new position.
        timestamp: :class:`~async_v20.DateTime`
            The date/time when the Price was created.

    """

    def __init__(self, bids: ArrayPriceBucket = sentinel, asks: ArrayPriceBucket = sentinel,
                 closeout_bid: PriceValue = sentinel, closeout_ask: PriceValue = sentinel,
                 timestamp: DateTime = sentinel):
        Model.__init__(**locals())


class PricingHeartbeat(Model):
    """A PricingHeartbeat object is injected into the Pricing stream to ensure
    that the HTTP connection remains active.

    Attributes:
        type: :class:`str`
            The string "HEARTBEAT"
        time: :class:`~async_v20.DateTime`
            The date/time when the Heartbeat was created.

    """

    def __init__(self, type: str = sentinel, time: DateTime = sentinel):
        Model.__init__(**locals())


class CalculatedTradeState(Model):
    """The dynamic (calculated) state of an open Trade

    Attributes:
        id: :class:`~async_v20.TradeID`
            The Trade's ID.
        unrealized_pl: :class:`~async_v20.AccountUnits`
            The Trade's unrealized profit/loss.

    """

    def __init__(self, id: TradeID = sentinel, unrealized_pl: AccountUnits = sentinel,
                 margin_used: AccountUnits = sentinel):
        Model.__init__(**locals())


class ArrayCalculatedTradeState(Array, contains=CalculatedTradeState):
    pass


class MarketOrderDelayedTradeClose(Model):
    """Details for the Market Order extensions specific to a Market Order placed
    with the intent of fully closing a specific open trade that should have
    already been closed but wasn't due to halted market conditions

    Attributes:
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade being closed
        client_trade_id: :class:`~async_v20.TradeID`
            The Client ID of the Trade being closed
        source_transaction_id: :class:`~async_v20.TransactionID`
            The Transaction ID of the DelayedTradeClosure transaction
            to which this Delayed Trade Close belongs to

    """

    def __init__(self, trade_id: TradeID = sentinel, client_trade_id: TradeID = sentinel,
                 source_transaction_id: TransactionID = sentinel):
        Model.__init__(**locals())


class MarketOrderPositionCloseout(Model):
    """A MarketOrderPositionCloseout specifies the extensions to a Market Order
    when it has been created to closeout a specific Position.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The instrument of the Position being closed out.
        units: :class:`str`
            Indication of how much of the Position to close. Either "ALL", or a DecimalNumber reflection a
            partial close of the Trade. The DecimalNumber must always be positive,
            and represent a number that doesn't exceed the absolute size of the Position.

    """

    def __init__(self, instrument: InstrumentName = sentinel, units: str = sentinel):
        Model.__init__(**locals())


class MarketOrderTradeClose(Model):
    """A MarketOrderTradeClose specifies the extensions to a Market Order that has
    been created specifically to close a Trade.

    Attributes:
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade requested to be closed
        client_trade_id: :class:`str` :class:`~async_v20.TradeID`
            The client ID of the Trade requested to be closed
        units: :class:`str`
            Indication of how much of the Trade to close. Either
            "ALL", or a DecimalNumber reflection a partial close of the Trade.

    """

    def __init__(self, trade_id: TradeID = sentinel, client_trade_id: str = sentinel, units: str = sentinel):
        Model.__init__(**locals())


class OpenTradeFinancing(Model):
    """OpenTradeFinancing is used to pay/collect daily financing charge for an
    open Trade within an Account

    Attributes:
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade that financing is being paid/collected for.
        financing: :class:`~async_v20.AccountUnits`
            The amount of financing paid/collected for the Trade.

    """

    def __init__(self, trade_id: TradeID = sentinel, financing: AccountUnits = sentinel):
        Model.__init__(**locals())


class ArrayOpenTradeFinancing(Array, contains=OpenTradeFinancing):
    pass


class PositionFinancing(Model):
    """OpenTradeFinancing is used to pay/collect daily financing charge for a
    Position within an Account

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The instrument of the Position that financing is being paid/collected for.
        financing: :class:`~async_v20.AccountUnits`
            The amount of financing paid/collected for the Position.
        open_trade_financings: ( :class:`~async_v20.OpenTradeFinancing`, ...)
            The financing paid/collecte for each open Trade within the Position.

    """

    def __init__(self, instrument: InstrumentName = sentinel, financing: AccountUnits = sentinel,
                 open_trade_financings: ArrayOpenTradeFinancing = sentinel):
        Model.__init__(**locals())


class ArrayPositionFinancing(Array, contains=PositionFinancing):
    pass


class TradeOpen(Model):
    """A TradeOpen object represents a Trade for an instrument that was opened in
    an Account. It is found embedded in Transactions that affect the position
    of an instrument in the Account, specifically the OrderFill Transaction.

    Attributes:
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade that was opened
        units: :class:`~async_v20.DecimalNumber`
            The number of units opened by the Trade
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions for the newly opened Trade
        initial_margin_required: :class:`~async_v20.AccountUnits`
            The margin required at the time the Trade was created. Note, this is the
            ‘pure’ margin required, it is not the ‘effective’ margin used that
            factors in the trade risk if a GSLO is attached to the trade.

    """

    def __init__(self, price: DecimalNumber = sentinel, trade_id: TradeID = sentinel, units: DecimalNumber = sentinel,
                 client_extensions: ClientExtensions = sentinel,
                 guaranteed_execution_fee: AccountUnits = sentinel,
                 half_spread_cost: AccountUnits = sentinel,
                 initial_margin_required: AccountUnits = sentinel):
        Model.__init__(**locals())


class VWAPReceipt(Model):
    """A VWAP Receipt provides a record of how the price for an Order fill is
    constructed. If the Order is filled with multiple buckets in a depth of
    market, each bucket will be represented with a VWAP Receipt.

    Attributes:
        units: :class:`~async_v20.DecimalNumber`
            The number of units filled
        price: :class:`~async_v20.PriceValue`
            The price at which the units were filled

    """

    def __init__(self, units: DecimalNumber = sentinel, price: PriceValue = sentinel):
        Model.__init__(**locals())


class UserInfo(Model):
    """A representation of user information, as provided to the user themself.

    Attributes:
        username: :class:`str`
            The user-provided username.
        user_id: :class:`str`
            The user's OANDA-assigned user ID.
        country: :class:`str`
            The country that the user is based in.
        email_address: :class:`str`
            The user's email address.

    """

    def __init__(self, username: str = sentinel, user_id: str = sentinel, country: str = sentinel,
                 email_address: str = sentinel):
        Model.__init__(**locals())


class AccountProperties(Model):
    """Properties related to an Account.

    Attributes:
        id: :class:`~async_v20.AccountID`
            The Account's identifier
        mt4account_id: :class:`~async_v20.AccountID`
            The Account's associated MT4 Account ID. This field will not
            be present if the Account is not an MT4 account.
        tags: ( :class:`str`, ...)
            The Account's tags

    """

    def __init__(self, id: AccountID = sentinel, mt4_account_id: int = sentinel, tags: ArrayStr = sentinel):
        Model.__init__(**locals())


class ArrayAccountProperties(Array, contains=AccountProperties):
    pass


class Candlestick(Model):
    """The Candlestick representation

    Attributes:
        time: :class:`~async_v20.DateTime`
            The start time of the candlestick
        bid: :class:`~async_v20.CandlestickData`
            The candlestick data based on bids.
            Only provided if bid-based candles were requested.
        ask: :class:`~async_v20.CandlestickData`
            The candlestick data based on asks.
            Only provided if ask-based candles were requested.
        mid: :class:`~async_v20.CandlestickData`
            The candlestick data based on midpoints.
            Only provided if midpoint-based candles were requested.
        volume: :class:`int`
            The number of prices created during
            the time-range represented by the candlestick.
        complete: :class:`bool`
            A flag indicating if the candlestick is complete. A complete
            candlestick is one whose ending time is not in the future.

    """

    def __init__(self, time: DateTime = sentinel, bid: CandlestickData = sentinel, ask: CandlestickData = sentinel,
                 mid: CandlestickData = sentinel, volume: int = sentinel, complete: bool = sentinel):
        Model.__init__(**locals())


class ArrayCandlestick(Array, contains=Candlestick):
    pass


class OrderBook(Model):
    """The representation of an instrument's order book at a point in time

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The order book's instrument
        time: :class:`~async_v20.DateTime`
            The time when the order book snapshot was created.
        unix_time: :class:`~async_v20.DateTime`
            The time when the order book snapshot was created in unix format.
        price: :class:`~async_v20.PriceValue`
            The price (midpoint) for the order book's instrument
            at the time of the order book snapshot
        bucket_width: :class:`~async_v20.PriceValue`
            The price width for each bucket. Each bucket covers the price
            range from the bucket's price to the bucket's price + bucketWidth.
        buckets: ( :class:`~async_v20.OrderBookBucket`, ...)
            The partitioned order book, divided into buckets using a default bucket width. These
            buckets are only provided for price ranges which actually contain order or position data.

    """

    def __init__(self, instrument: InstrumentName = sentinel, time: DateTime = sentinel, unix_time: DateTime = sentinel,
                 price: PriceValue = sentinel, bucket_width: PriceValue = sentinel,
                 buckets: ArrayOrderBookBucket = sentinel):
        Model.__init__(**locals())


class PositionBook(Model):
    """The representation of an instrument's position book at a point in time

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The position book's instrument
        time: :class:`~async_v20.DateTime`
            The time when the position book snapshot was created
        price: :class:`~async_v20.PriceValue`
            The price (midpoint) for the position book's instrument
            at the time of the position book snapshot
        bucket_width: :class:`~async_v20.PriceValue`
            The price width for each bucket. Each bucket covers the price
            range from the bucket's price to the bucket's price + bucketWidth.
        buckets: ( :class:`~async_v20.PositionBookBucket`, ...)
            The partitioned position book, divided into buckets using a default bucket width. These
            buckets are only provided for price ranges which actually contain order or position data.

    """

    def __init__(self, instrument: InstrumentName = sentinel, time: DateTime = sentinel, unix_time: DateTime = sentinel,
                 price: PriceValue = sentinel,
                 bucket_width: PriceValue = sentinel, buckets: ArrayPositionBookBucket = sentinel):
        Model.__init__(**locals())


class Order(Model):
    """The base Order definition. Contains all possible attributes an Order
    may contain

    Attributes:
        id: :class:`~async_v20.OrderID`
            The Order's identifier, unique within the Order's Account.
        create_time: :class:`~async_v20.DateTime`
            The time when the Order was created.
        state: :class:`~async_v20.OrderState`
            The current state of the Order.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        trade_id: :class:`~async_v20.TradeID`
        price: :class:`~async_v20.PriceValue`
        type: :class:`~async_v20.OrderType`
        client_trade_id: :class:`~async_v20.ClientID`
        time_in_force: :class:`~async_v20.TimeInForce`
        gtd_time: :class:`~async_v20.DateTime`
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
        filling_transaction_id: :class:`~async_v20.TransactionID`
        filled_time: :class:`~async_v20.DateTime`
        trade_opened_id: :class:`~async_v20.TradeID`
        trade_reduced_id: :class:`~async_v20.TradeID`
        trade_closed_ids: ( :class:`~async_v20.TradeID`, ...),
        cancelling_transaction_id: :class:`~async_v20.TransactionID`
        cancelled_time: :class:`~async_v20.DateTime`
        replaces_order_id: :class:`~async_v20.OrderID`
        replaced_by_order_id: :class:`~async_v20.OrderID`
        distance: :class:`~async_v20.PriceValue`
        trailing_stop_value: :class:`~async_v20.PriceValue`
        instrument: :class:`~async_v20.InstrumentName`
        units: :class:`~async_v20.DecimalNumber`
        partial_fill: :class:`str`
        position_fill: :class:`~async_v20.OrderPositionFill`
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
        price_bound: :class:`~async_v20.PriceValue`
        initial_market_price: :class:`~async_v20.PriceValue`
        trade_close: :class:`~async_v20.MarketOrderTradeClose`
        long_position_closeout: :class:`~async_v20.MarketOrderPositionCloseout`
        short_position_closeout: :class:`~async_v20.MarketOrderPositionCloseout`
        margin_closeout: :class:`~async_v20.MarketOrderMarginCloseout`
        delayed_trade_close: :class:`~async_v20.MarketOrderDelayedTradeClose`
        trigger_distance: :class:`~async_v20.PriceValue`
        is_trigger_distance_exact: :class:`bool`
    """

    # TODO: Update the annotation for partial_fill when OANDA responds to email, & `guaranteed`

    def __init__(self, id: OrderID = sentinel, create_time: DateTime = sentinel, state: OrderState = sentinel,
                 client_extensions: ClientExtensions = sentinel, trade_id: TradeID = sentinel,
                 price: PriceValue = sentinel,
                 type: OrderType = sentinel, client_trade_id: ClientID = sentinel,
                 time_in_force: TimeInForce = sentinel,
                 gtd_time: DateTime = sentinel, trigger_condition: OrderTriggerCondition = sentinel,
                 filling_transaction_id: TransactionID = sentinel, filled_time: DateTime = sentinel,
                 trade_opened_id: TradeID = sentinel, trade_reduced_id: TradeID = sentinel,
                 trade_closed_ids: ArrayTradeID = sentinel, cancelling_transaction_id: TransactionID = sentinel,
                 cancelled_time: DateTime = sentinel, replaces_order_id: OrderID = sentinel,
                 replaced_by_order_id: OrderID = sentinel, distance: PriceValue = sentinel,
                 trailing_stop_value: PriceValue = sentinel, instrument: InstrumentName = sentinel,
                 units: DecimalNumber = sentinel,
                 partial_fill: str = sentinel, position_fill: OrderPositionFill = sentinel,
                 take_profit_on_fill: TakeProfitDetails = sentinel,
                 stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel, price_bound: PriceValue = sentinel,
                 initial_market_price: PriceValue = sentinel, trade_close: MarketOrderTradeClose = sentinel,
                 long_position_closeout: MarketOrderPositionCloseout = sentinel,
                 short_position_closeout: MarketOrderPositionCloseout = sentinel,
                 margin_closeout: MarketOrderMarginCloseout = sentinel,
                 delayed_trade_close: MarketOrderDelayedTradeClose = sentinel,
                 trigger_distance: PriceValue = sentinel, is_trigger_distance_exact: bool = sentinel,
                 guaranteed: bool = sentinel
                 ):
        Model.__init__(**locals())


class ArrayOrder(Array, contains=Order):
    pass


class TradeReduce(Model):
    """A TradeReduce object represents a Trade for an instrument that was reduced
    (either partially or fully) in an Account. It is found embedded in
    Transactions that affect the position of an instrument in the account,
    specifically the OrderFill Transaction.

    Attributes:
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade that was reduced or closed
        units: :class:`~async_v20.DecimalNumber`
            The number of units that the Trade was reduced by
        realized_pl: :class:`~async_v20.AccountUnits`
            The PL realized when reducing the Trade
        financing: :class:`~async_v20.AccountUnits`
            The financing paid/collected when reducing the Trade
        client_trade_id: :class:`~async_v20.ClientID`
            The ID specified by the client (undocumented by Oanda)
    """

    def __init__(self, trade_id: TradeID = sentinel, units: DecimalNumber = sentinel,
                 realized_pl: AccountUnits = sentinel,
                 financing: AccountUnits = sentinel, price: DecimalNumber = sentinel,
                 guaranteed_execution_fee: AccountUnits = sentinel,
                 half_spread_cost: AccountUnits = sentinel,
                 client_trade_id: ClientID = sentinel):
        Model.__init__(**locals())


class ArrayTradeReduce(Array, contains=TradeReduce):
    pass


class TransactionHeartbeat(Model):
    """A TransactionHeartbeat object is injected into the Transaction stream to
    ensure that the HTTP connection remains active.

    Attributes:
        type: :class:`str`
            The string "HEARTBEAT"
        last_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the most recent Transaction created for the Account
        time: :class:`~async_v20.DateTime`
            The date/time when the TransactionHeartbeat was created.

    """

    def __init__(self, type: str = sentinel, last_transaction_id: TransactionID = sentinel, time: DateTime = sentinel):
        Model.__init__(**locals())


class UserInfoExternal(Model):
    """A representation of user information, as available to external (3rd party)
    clients.

    Attributes:
        user_id: :class:`str`
            The user's OANDA-assigned user ID.
        country: :class:`str`
            The country that the user is based in.
        fifo: :class:`str`
            Flag indicating if the the user's Accounts adhere to FIFO execution rules.

    """

    def __init__(self, user_id: str = sentinel, country: str = sentinel, fifo: str = sentinel):
        Model.__init__(**locals())


class TradeSummary(Model):
    """The summary of a Trade within an Account. This representation does not
    provide the full details of the Trade's dependent Orders.

    Attributes:
        id: :class:`~async_v20.TradeID`
            The Trade's identifier, unique within the Trade's Account.
        instrument: :class:`~async_v20.InstrumentName`
            The Trade's Instrument.
        price: :class:`~async_v20.PriceValue`
            The execution price of the Trade.
        open_time: :class:`~async_v20.DateTime`
            The date/time when the Trade was opened.
        state: :class:`~async_v20.TradeState`
            The current state of the Trade.
        initial_units: :class:`~async_v20.DecimalNumber`
            The initial size of the Trade. Negative values indicate
            a short Trade, and positive values indicate a long Trade.
        initial_margin_required: :class:`~async_v20.AccountUnits`
            The margin required at the time the Trade was created. Note, this is the
            ‘pure’ margin required, it is not the ‘effective’ margin used that
            factors in the trade risk if a GSLO is attached to the trade.
        current_units: :class:`~async_v20.DecimalNumber`
            The number of units currently open for the Trade. This
            value is reduced to 0.0 as the Trade is closed.
        realized_pl: :class:`~async_v20.AccountUnits`
            The total profit/loss realized on the closed portion of the Trade.
        unrealized_pl: :class:`~async_v20.AccountUnits`
            The unrealized profit/loss on the open portion of the Trade.
        average_close_price: :class:`~async_v20.PriceValue`
            The average closing price of the Trade. Only present if
            the Trade has been closed or reduced at least once.
        closing_transaction_ids: ( :class:`~async_v20.TransactionID`, ...)
            The IDs of the Transactions that have closed portions of this Trade.
        financing: :class:`~async_v20.AccountUnits`
            The financing paid/collected for this Trade.
        close_time: :class:`~async_v20.DateTime`
            The date/time when the Trade was fully closed.
            Only provided for Trades whose state is CLOSED.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions of the Trade.
        take_profit_order_id: :class:`~async_v20.OrderID`
            ID of the Trade's Take Profit Order, only provided if such an Order exists.
        stop_loss_order_id: :class:`~async_v20.OrderID`
            ID of the Trade's Stop Loss Order, only provided if such an Order exists.
        trailing_stop_loss_order_id: :class:`~async_v20.OrderID`
            ID of the Trade's Trailing Stop Loss
            Order, only provided if such an Order exists.
        margin_used:
            Margin currently used by the Trade.

    """

    def __init__(self, id: TradeID = sentinel, instrument: InstrumentName = sentinel, price: PriceValue = sentinel,
                 open_time: DateTime = sentinel, state: TradeState = sentinel, initial_units: DecimalNumber = sentinel,
                 initial_margin_required: AccountUnits = sentinel,
                 current_units: DecimalNumber = sentinel, realized_pl: AccountUnits = sentinel,
                 unrealized_pl: AccountUnits = sentinel,
                 average_close_price: PriceValue = sentinel, closing_transaction_ids: ArrayTransactionID = sentinel,
                 financing: AccountUnits = sentinel, close_time: DateTime = sentinel,
                 client_extensions: ClientExtensions = sentinel, take_profit_order_id: OrderID = sentinel,
                 stop_loss_order_id: OrderID = sentinel, trailing_stop_loss_order_id: OrderID = sentinel,
                 margin_used: AccountUnits = sentinel):
        Model.__init__(**locals())


class ArrayTradeSummary(Array, contains=TradeSummary):
    pass


class Transaction(Model):
    """The base Transaction specification. Contains all possible attributes a transaction
    may contain.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 type: TransactionType = sentinel, extension_number: int = sentinel, division_id: int = sentinel,
                 site_id: int = sentinel, account_user_id: int = sentinel, account_number: int = sentinel,
                 home_currency: Currency = sentinel, alias: str = sentinel, margin_rate: DecimalNumber = sentinel,
                 reason: Reason = sentinel, trade_ids: TradeID = sentinel, order_id: OrderID = sentinel,
                 client_order_id: ClientID = sentinel, replaced_by_order_id: OrderID = sentinel,
                 closed_trade_id: OrderID = sentinel, trade_close_transaction_id: TransactionID = sentinel,
                 client_extensions_modify: ClientExtensions = sentinel,
                 trade_client_extensions_modify: ClientExtensions = sentinel, financing: AccountUnits = sentinel,
                 account_balance: AccountUnits = sentinel, account_financing_mode: AccountFinancingMode = sentinel,
                 position_financings: ArrayPositionFinancing = sentinel, trade_id: TradeID = sentinel,
                 client_trade_id: ClientID = sentinel, price: PriceValue = sentinel,
                 time_in_force: TimeInForce = sentinel,
                 gtd_time: DateTime = sentinel, trigger_condition: OrderTriggerCondition = sentinel,
                 client_extensions: ClientExtensions = sentinel, order_fill_transaction_id: TransactionID = sentinel,
                 replaces_order_id: OrderID = sentinel, cancelling_transaction_id: TransactionID = sentinel,
                 reject_reason: TransactionRejectReason = sentinel, amount: AccountUnits = sentinel,
                 funding_reason: FundingReason = sentinel, comment: str = sentinel,
                 instrument: InstrumentName = sentinel,
                 units: DecimalNumber = sentinel, price_bound: PriceValue = sentinel,
                 position_fill: OrderPositionFill = sentinel,
                 trade_close: MarketOrderTradeClose = sentinel,
                 long_position_closeout: MarketOrderPositionCloseout = sentinel,
                 short_position_closeout: MarketOrderPositionCloseout = sentinel,
                 margin_closeout: MarketOrderMarginCloseout = sentinel,
                 delayed_trade_close: MarketOrderDelayedTradeClose = sentinel,
                 take_profit_on_fill: TakeProfitDetails = sentinel, stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel, distance: PriceValue = sentinel,
                 full_price: ClientPrice = sentinel, pl: AccountUnits = sentinel, commission: AccountUnits = sentinel,
                 trade_opened: TradeOpen = sentinel, trades_closed: ArrayTradeReduce = sentinel,
                 trade_reduced: TradeReduce = sentinel, intended_replaces_order_id: OrderID = sentinel,
                 # TODO update when OANDA ADVISES correct type. This is currently a guess.
                 gain_quote_home_conversion_factor: DecimalNumber = sentinel,
                 loss_quote_home_conversion_factor: DecimalNumber = sentinel,
                 guaranteed_execution_fee: AccountUnits = sentinel,
                 half_spread_cost: AccountUnits = sentinel,
                 partial_fill: str = sentinel,
                 guaranteed: bool = sentinel,
                 requested_units: AccountUnits = sentinel,
                 full_vwap: DecimalNumber = sentinel):
        Model.__init__(**locals())


class ArrayTransaction(Array, contains=Transaction):
    pass


class AccountChanges(Model):
    """An AccountChanges Object is used to represent the changes to an Account's
    Orders, Trades and Positions since a specified Account TransactionID in the
    past.

    Attributes:
        orders_created: ( :class:`~async_v20.Order`, ...)
            The Orders created. These Orders may have been
            filled, cancelled or triggered in the same period.
        orders_cancelled: ( :class:`~async_v20.Order`, ...)
            The Orders cancelled.
        orders_filled: ( :class:`~async_v20.Order`, ...)
            The Orders filled.
        orders_triggered: ( :class:`~async_v20.Order`, ...)
            The Orders triggered.
        trades_opened: ( :class:`~async_v20.TradeSummary`, ...)
            The Trades opened.
        trades_reduced: ( :class:`~async_v20.TradeSummary`, ...)
            The Trades reduced.
        trades_closed: ( :class:`~async_v20.TradeSummary`, ...)
            The Trades closed.
        positions: ( :class:`~async_v20.Position`, ...)
            The Positions changed.
        transactions: ( :class:`~async_v20.Transaction`, ...)
            The Transactions that have been generated.

    """

    def __init__(self, orders_created: ArrayOrder = sentinel, orders_cancelled: ArrayOrder = sentinel,
                 orders_filled: ArrayOrder = sentinel, orders_triggered: ArrayOrder = sentinel,
                 trades_opened: ArrayTradeSummary = sentinel, trades_reduced: ArrayTradeSummary = sentinel,
                 trades_closed: ArrayTradeSummary = sentinel, positions: ArrayPosition = sentinel,
                 transactions: ArrayTransaction = sentinel):
        Model.__init__(**locals())


class GuaranteedStopLossOrderLevelRestriction(Model):
    """A GuaranteedStopLossOrderLevelRestriction represents the total position size
    that can exist within a given price window for Trades with guaranteed Stop Loss
    Orders attached for a specific Instrument.

    Attributes:
        volume: :class: `~async_v20.DecimalNumber`
            Applies to Trades with a guaranteed Stop Loss Order attached for the
            specified Instrument. This is the total allowed Trade volume that can
            exist within the priceRange based on the trigger prices of the guaranteed
            Stop Loss Orders.
        price_range: :class: `~async_v20.DecimalNumber`
            The price range the volume applies to. This value is in price units.

    """

    def __init__(self, volume: DecimalNumber = sentinel, price_range: DecimalNumber = sentinel):
        Model.__init__(**locals())


class Instrument(Model):
    """Full specification of an Instrument.

    Attributes:
        name: :class:`~async_v20.InstrumentName`
            The name of the Instrument
        type: :class:`~async_v20.InstrumentType`
            The type of the Instrument
        display_name: :class:`str` :class:`~async_v20.InstrumentName`
            The display name of the Instrument
        pip_location: :class:`int`
            The location of the "pip" for this instrument. The decimal position of the pip in this
            Instrument's price can be
            found at 10 ^ pipLocation (e.g. -4 pipLocation results in a decimal pip position of 10 ^ -4 = 0.0001).
        display_precision: :class:`int`
            The number of decimal places that should be used to display prices for this instrument.
            (e.g. a displayPrecision of 5 would result in a price of "1" being displayed as "1.00000")
        trade_units_precision: :class:`int`
            The amount of decimal places that may be provided
            when specifying the number of units traded for this instrument.
        minimum_trade_size: :class:`~async_v20.DecimalNumber`
            The smallest number of units allowed to be traded for this instrument.
        maximum_trailing_stop_distance: :class:`~async_v20.DecimalNumber`
            The maximum trailing stop distance allowed for a trailing
            stop loss created for this instrument. Specified in price units.
        minimum_trailing_stop_distance: :class:`~async_v20.DecimalNumber`
            The minimum trailing stop distance allowed for a trailing
            stop loss created for this instrument. Specified in price units.
        maximum_position_size: :class:`~async_v20.DecimalNumber`
            The maximum position size allowed for this instrument. Specified in units.
        maximum_order_units: :class:`~async_v20.DecimalNumber`
            The maximum units allowed for an Order
            placed for this instrument. Specified in units.
        margin_rate: :class:`~async_v20.DecimalNumber`
            The margin rate for this instrument.
        commission: :class:`~async_v20.InstrumentCommission`
            The commission structure for this instrument.
        guaranteed_stop_loss_order_level_restriction: :class: `~async_v20.GuaranteedStopLossOrderLevelRestriction`
            The total position size that can exist within a given price window for Trades with a guaranteed Stop Loss Orders
            attached for a specific Instrument
        guaranteed_stop_loss_order_mode:
            pass
        financing: :class:`object`

    """

    def __init__(self, name: InstrumentName = sentinel, type: InstrumentType = sentinel, display_name: str = sentinel,
                 pip_location: int = sentinel, display_precision: int = sentinel, trade_units_precision: int = sentinel,
                 minimum_trade_size: DecimalNumber = sentinel, maximum_trailing_stop_distance: DecimalNumber = sentinel,
                 minimum_trailing_stop_distance: DecimalNumber = sentinel,
                 maximum_position_size: DecimalNumber = sentinel,
                 maximum_order_units: DecimalNumber = sentinel, margin_rate: DecimalNumber = sentinel,
                 commission: InstrumentCommission = sentinel,
                 guaranteed_stop_loss_order_level_restriction: GuaranteedStopLossOrderLevelRestriction = sentinel,
                 guaranteed_stop_loss_order_mode: GuaranteedStopLossOrderMode = sentinel,
                 tags: ArrayDict = sentinel, financing: object = sentinel):
        Model.__init__(**locals())


class ArrayInstrument(Array, contains=Instrument, one_to_many=False):
    pass


class AccountChangesState(Model):
    """An AccountState Object is used to represent an Account's current price-
    dependent state. Price-dependent Account state is dependent on OANDA's
    current Prices, and includes things like unrealized PL, NAV and Trailing
    Stop Loss Order state.

    Attributes:
        unrealized_pl: :class:`~async_v20.AccountUnits`
            The total unrealized profit/loss for all Trades currently open
            in the Account. Represented in the Account's home currency.
        nav: :class:`~async_v20.AccountUnits`
            The net asset value of the Account. Equal to
            Account balance + unrealizedPL. Represented in the Account's home currency.
        margin_used: :class:`~async_v20.AccountUnits`
            Margin currently used for the Account.
            Represented in the Account's home currency.
        margin_available: :class:`~async_v20.AccountUnits`
            Margin available for Account. Represented in the Account's home currency.
        position_value: :class:`~async_v20.AccountUnits`
            The value of the Account's open
            positions represented in the Account's home currency.
        margin_closeout_unrealized_pl: :class:`~async_v20.AccountUnits`
            The Account's margin closeout unrealized PL.
        margin_closeout_nav: :class:`~async_v20.AccountUnits`
            The Account's margin closeout NAV.
        margin_closeout_margin_used: :class:`~async_v20.AccountUnits`
            The Account's margin closeout margin used.
        margin_closeout_percent: :class:`~async_v20.DecimalNumber`
            The Account's margin closeout percentage. When this value is 1.0
            or above the Account is in a margin closeout situation.
        margin_closeout_position_value: :class:`~async_v20.DecimalNumber`
            The value of the Account's open positions as used
            for margin closeout calculations represented in the Account's home currency.
        withdrawal_limit: :class:`~async_v20.AccountUnits`
            The current WithdrawalLimit for the account which will be zero or
            a positive value indicating how much can be withdrawn from the account.
        margin_call_margin_used: :class:`~async_v20.AccountUnits`
            The Account's margin call margin used.
        margin_call_percent: :class:`~async_v20.DecimalNumber`
            The Account's margin call percentage. When this value is 1.0
            or above the Account is in a margin call situation.
        orders: ( :class:`~async_v20.DynamicOrderState`, ...)
            The price-dependent state of each pending Order in the Account.
        trades: ( :class:`~async_v20.CalculatedTradeState`, ...)
            The price-dependent state for each open Trade in the Account.
        positions: ( :class:`~async_v20.CalculatedPositionState`, ..)
            The price-dependent state for each open Position in the Account.

        # TODO add documentation for Pl and resettabel_pl

    """

    def __init__(self, unrealized_pl: AccountUnits = sentinel, nav: AccountUnits = sentinel,
                 margin_used: AccountUnits = sentinel,
                 margin_available: AccountUnits = sentinel, position_value: AccountUnits = sentinel,
                 margin_closeout_unrealized_pl: AccountUnits = sentinel, margin_closeout_nav: AccountUnits = sentinel,
                 margin_closeout_margin_used: AccountUnits = sentinel,
                 margin_closeout_percent: DecimalNumber = sentinel,
                 margin_closeout_position_value: DecimalNumber = sentinel, withdrawal_limit: AccountUnits = sentinel,
                 margin_call_margin_used: AccountUnits = sentinel, margin_call_percent: DecimalNumber = sentinel,
                 orders: ArrayDynamicOrderState = sentinel, trades: ArrayCalculatedTradeState = sentinel,
                 positions: ArrayCalculatedPositionState = sentinel,
                 balance: AccountUnits = sentinel,
                 # TODO check definition against OANDA docs
                 pl: AccountUnits = sentinel,
                 resettable_pl: AccountUnits = sentinel,
                 commission: AccountUnits = sentinel,
                 guaranteed_execution_fees: AccountUnits = sentinel
                 ):
        Model.__init__(**locals())


class Price(Model):
    """The specification of an Account-specific Price.

    Attributes:
        type: :class:`str`
            The string "PRICE". Used to identify the a Price object when found in a stream.
        instrument: :class:`~async_v20.InstrumentName`
            The Price's Instrument.
        time: :class:`~async_v20.DateTime`
            The date/time when the Price was created
        status: :class:`~async_v20.PriceStatus`
            The status of the Price.
        tradeable: :class:`bool`
            Flag indicating if the Price is tradeable or not
        bids: ( :class:`~async_v20.PriceBucket`, ...),
            The list of prices and liquidity available on the Instrument's bid side. It is possible for this
            list to be empty if there is no bid liquidity currently available for the Instrument in the Account.
        asks: ( :class:`~async_v20.PriceBucket`, ...),
            The list of prices and liquidity available on the Instrument's ask side. It is possible for this
            list to be empty if there is no ask liquidity currently available for the Instrument in the Account.
        closeout_bid: :class:`~async_v20.PriceValue`
            The closeout bid Price. This Price is used when a bid is required to closeout a Position
            (margin closeout
            or manual) yet there is no bid liquidity. The closeout bid is never used to open a new position.
        closeout_ask: :class:`~async_v20.PriceValue`
            The closeout ask Price. This Price is used when a ask is required to closeout a Position
            (margin closeout
            or manual) yet there is no ask liquidity. The closeout ask is never used to open a new position.
        quote_home_conversion_factors: :class:`~async_v20.QuoteHomeConversionFactors`
            The factors used to convert quantities of this price's Instrument's
            quote currency into a quantity of the Account's home currency.
        units_available: :class:`~async_v20.UnitsAvailable`
            Representation of how many units of an Instrument are available
            to be traded by an Order depending on its postionFill option.

    """

    def __init__(self, type: str = sentinel, instrument: InstrumentName = sentinel, time: DateTime = sentinel,
                 # TODO: remove status when OANDA removes attribute
                 status: PriceStatus = sentinel, tradeable: bool = sentinel, bids: ArrayPriceBucket = sentinel,
                 asks: ArrayPriceBucket = sentinel, closeout_bid: PriceValue = sentinel,
                 closeout_ask: PriceValue = sentinel,
                 # TODO: remove quote_home_conversion_factors when OANDA removes attribute
                 quote_home_conversion_factors: QuoteHomeConversionFactors = sentinel,
                 # TODO: remove units_available when OANDA removes attribute
                 units_available: UnitsAvailable = sentinel):
        Model.__init__(**locals())


class ArrayPrice(Array, contains=Price):
    pass


class CloseTransaction(Transaction, type=TransactionType('CLOSE')):
    """A CloseTransaction represents the closing of an Account.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel,
                 request_id: RequestID = sentinel):
        Model.__init__(**locals())


class MarginCallEnterTransaction(Transaction, type=TransactionType('MARGIN_CALL_ENTER')):
    """A MarginCallEnterTransaction is created when an Account enters the margin
    call state.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel,
                 request_id: RequestID = sentinel):
        Model.__init__(**locals())


class MarginCallExitTransaction(Transaction, type=TransactionType('MARGIN_CALL_EXIT')):
    """A MarginCallExitnterTransaction is created when an Account leaves the
    margin call state.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel,
                 request_id: RequestID = sentinel):
        Model.__init__(**locals())


class MarginCallExtendTransaction(Transaction, type=TransactionType('MARGIN_CALL_EXTEND')):
    """A MarginCallExtendTransaction is created when the margin call state for an
    Account has been extended.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        extension_number: :class:`int`
            The number of the extensions to the Account's current margin call that have
            been applied. This value will be set to 1 for the first MarginCallExtend Transaction

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 extension_number: int = sentinel):
        Model.__init__(**locals())


class ReopenTransaction(Transaction, type=TransactionType('REOPEN')):
    """A ReopenTransaction represents the re-opening of a closed Account.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel,
                 request_id: RequestID = sentinel):
        Model.__init__(**locals())


class ResetResettablePLTransaction(Transaction, type=TransactionType('RESET_RESETTABLE_PL')):
    """A ResetResettablePLTransaction represents the resetting of the Account's
    resettable PL counters.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel,
                 request_id: RequestID = sentinel):
        Model.__init__(**locals())


class StopLossOrderRequest(OrderRequest, type=OrderType('STOP_LOSS')):
    """A StopLossOrderRequest specifies the parameters that may be set when
    creating a Stop Loss Order.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The StopLossOrderRequest instrument.
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade to close when the price threshold is breached.
        client_trade_id: :class:`~async_v20.TradeID`
            The client ID of the Trade to be closed when the price threshold is breached.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the StopLoss Order. The associated Trade will be
            closed by a market price that is equal to or worse than this threshold.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the StopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for StopLoss Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.

    """

    def __init__(self, instrument: InstrumentName, trade_id: TradeID, price: PriceValue,
                 client_trade_id: ClientID = sentinel, time_in_force: TimeInForce = 'GTC',
                 gtd_time: DateTime = sentinel,
                 trigger_condition: OrderTriggerCondition = 'DEFAULT', client_extensions: ClientExtensions = sentinel):
        Model.__init__(**locals())


class TakeProfitOrderRequest(OrderRequest, type=OrderType('TAKE_PROFIT')):
    """A TakeProfitOrderRequest specifies the parameters that may be set when
    creating a Take Profit Order.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The TakeProfitOrderRequest instrument.
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade to close when the price threshold is breached.
        client_trade_id: :class:`~async_v20.TradeID`
            The client ID of the Trade to be closed when the price threshold is breached.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the TakeProfit Order. The associated Trade will be
            closed by a market price that is equal to or better than this threshold.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the TakeProfit Order. Restricted
            to "GTC", "GFD" and "GTD" for TakeProfit Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the TakeProfit Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.

    """

    def __init__(self, instrument: InstrumentName, trade_id: TradeID, price: PriceValue,
                 client_trade_id: ClientID = sentinel, time_in_force: TimeInForce = 'GTC',
                 gtd_time: DateTime = sentinel,
                 trigger_condition: OrderTriggerCondition = 'DEFAULT', client_extensions: ClientExtensions = sentinel):
        Model.__init__(**locals())


class TrailingStopLossOrderRequest(OrderRequest, type=OrderType('TRAILING_STOP_LOSS')):
    """A TrailingStopLossOrderRequest specifies the parameters that may be set
    when creating a Trailing Stop Loss Order.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The TrailingStopLossOrderRequest instrument
        instrument: :class:`~async_v20.InstrumentName`
            The TrailingStopLossOrderRequest instrument
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade to close when the price threshold is breached.
        client_trade_id: :class:`~async_v20.TradeID`
            The client ID of the Trade to be closed when the price threshold is breached.
        distance: :class:`~async_v20.PriceValue`
            The price distance specified for the TrailingStopLoss Order.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the TrailingStopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.

    """

    def __init__(self, instrument: InstrumentName, trade_id: TradeID, distance: PriceValue,
                 client_trade_id: ClientID = sentinel, time_in_force: TimeInForce = 'GTC',
                 gtd_time: DateTime = sentinel,
                 trigger_condition: OrderTriggerCondition = 'DEFAULT', client_extensions: ClientExtensions = sentinel):
        Model.__init__(**locals())


class CreateTransaction(Transaction, type=TransactionType('CREATE')):
    """A CreateTransaction represents the creation of an Account.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        division_id: :class:`~async_v20.TransactionID`
            The ID of the Division that the Account is in
        site_id: :class:`~async_v20.TransactionID`
            The ID of the Site that the Account was created at
        account_user_id: :class:`int`
            The ID of the user that the Account was created for
        account_number: :class:`int`
            The number of the Account within the site/division/user
        home_currency: :class:`~async_v20.Currency`
            The home currency of the Account

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 division_id: int = sentinel, site_id: int = sentinel,
                 account_user_id: int = sentinel, account_number: int = sentinel, home_currency: Currency = sentinel):
        Model.__init__(**locals())


class ClientConfigureTransaction(Transaction, type=TransactionType('CLIENT_CONFIGURE')):
    """A ClientConfigureTransaction represents the configuration of an Account by
    a client.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        alias: :class:`str`
            The client-provided alias for the Account.
        margin_rate: :class:`~async_v20.DecimalNumber`
            The margin rate override for the Account.

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 alias: str = sentinel, margin_rate: DecimalNumber = sentinel):
        Model.__init__(**locals())


class DelayedTradeClosureTransaction(Transaction, type=TransactionType('DELAYED_TRADE_CLOSURE')):
    """A DelayedTradeClosure Transaction is created administratively to indicate
    open trades that should have been closed but weren't because the open
    trades' instruments were untradeable at the time. Open trades listed in
    this transaction will be closed once their respective instruments become
    tradeable.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        reason: :class:`~async_v20.MarketOrderReason`
            The reason for the delayed trade closure
        trade_ids: :class:`~async_v20.TradeID`
            List of Trade ID's identifying the open trades that
            will be closed when their respective instruments become tradeable

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 reason: MarketOrderReason = sentinel,
                 trade_ids: TradeID = sentinel):
        Model.__init__(**locals())


class OrderCancelTransaction(Transaction, type=TransactionType('ORDER_CANCEL')):
    """An OrderCancelTransaction represents the cancellation of an Order in the
    client's Account.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        order_id: :class:`~async_v20.TransactionID`
            The ID of the Order cancelled
        client_order_id: :class:`~async_v20.ClientID`
            The reason that the Order was cancelled.
        reason: :class:`~async_v20.OrderCancelReason`
            The reason that the Order was cancelled.
        replaced_by_order_id: :class:`~async_v20.TransactionID`
            The ID of the Order that replaced this Order
            (only provided if this Order was cancelled for replacement).

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 order_id: OrderID = sentinel, client_order_id: ClientID = sentinel,
                 reason: OrderCancelReason = sentinel, replaced_by_order_id: OrderID = sentinel,
                 closed_trade_id: OrderID = sentinel, trade_close_transaction_id: TransactionID = sentinel):
        Model.__init__(**locals())


class OrderClientExtensionsModifyTransaction(Transaction, type=TransactionType('ORDER_CLIENT_EXTENSIONS_MODIFY')):
    """A OrderClientExtensionsModifyTransaction represents the modification of an
    Order's Client Extensions.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        order_id: :class:`~async_v20.OrderID`
            The ID of the Order who's client extensions are to be modified.
        client_order_id: :class:`~async_v20.OrderID`
            The original Client ID of the Order who's client extensions are to be modified.
        client_extensions_modify: :class:`~async_v20.ClientExtensions`
            The new Client Extensions for the Order.
        trade_client_extensions_modify: :class:`~async_v20.ClientExtensions`
            The new Client Extensions for the Order's Trade on fill.

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 order_id: OrderID = sentinel,
                 client_order_id: ClientID = sentinel, client_extensions_modify: ClientExtensions = sentinel,
                 trade_client_extensions_modify: ClientExtensions = sentinel):
        Model.__init__(**locals())


class DailyFinancingTransaction(Transaction, type=TransactionType('DAILY_FINANCING')):
    """A DailyFinancingTransaction represents the daily payment/collection of
    financing for an Account.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        financing: :class:`~async_v20.AccountUnits`
            The amount of financing paid/collected for the Account.
        account_balance: :class:`~async_v20.AccountUnits`
            The Account's balance after daily financing.
        account_financing_mode: :class:`~async_v20.AccountFinancingMode`
            The account financing mode at the time of the daily financing.
        position_financings: ( :class:`~async_v20.PositionFinancing`, ...)
            The financing paid/collected for each Position in the Account.

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 financing: AccountUnits = sentinel,
                 account_balance: AccountUnits = sentinel, account_financing_mode: AccountFinancingMode = sentinel,
                 position_financings: ArrayPositionFinancing = sentinel):
        Model.__init__(**locals())


class TradeClientExtensionsModifyTransaction(Transaction, type=TransactionType('TRADE_CLIENT_EXTENSIONS_MODIFY')):
    """A TradeClientExtensionsModifyTransaction represents the modification of a
    Trade's Client Extensions.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade who's client extensions are to be modified.
        client_trade_id: :class:`~async_v20.TradeID`
            The original Client ID of the Trade who's client extensions are to be modified.
        trade_client_extensions_modify: :class:`~async_v20.ClientExtensions`
            The new Client Extensions for the Trade.

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 trade_id: TradeID = sentinel,
                 client_trade_id: ClientID = sentinel, trade_client_extensions_modify: ClientExtensions = sentinel):
        Model.__init__(**locals())


class AccountSummary(Model):
    """A summary representation of a client's Account. The AccountSummary does not
    provide to full specification of pending Orders, open Trades and Positions.

    Attributes:
        id: :class:`~async_v20.AccountID`
            The Account's identifier
        alias: :class:`str`
            Client-assigned alias for the Account. Only provided
            if the Account has an alias set
        currency: :class:`~async_v20.Currency`
            The home currency of the Account
        balance: :class:`~async_v20.AccountUnits`
            The current balance of the Account. Represented in the Account's home currency.
        created_by_user_id: :class:`int`
            ID of the user that created the Account.
        created_time: :class:`~async_v20.DateTime`
            The date/time when the Account was created.
        pl: :class:`~async_v20.AccountUnits`
            The total profit/loss realized over the lifetime of
            the Account. Represented in the Account's home currency.
        resettable_pl: :class:`~async_v20.AccountUnits`
            The total realized profit/loss for the Account since it was
            last reset by the client. Represented in the Account's home currency.
        resettabled_pl_time: :class:`~async_v20.DateTime`
            The date/time that the Account's resettablePL was last reset.
        commission: :class:`~async_v20.AccountUnits`
            The total amount of commission paid over the lifetime
            of the Account. Represented in the Account's home currency.
        margin_rate: :class:`~async_v20.DecimalNumber`
            Client-provided margin rate override for the Account.
            The effective margin rate of the Account is the lesser of this
            value and the OANDA margin rate for the Account's division.
            This value is only provided if a margin rate override
            exists for the Account.
        margin_call_enter_time: :class:`~async_v20.DateTime`
            The date/time when the Account entered a margin call state.
            Only provided if the Account is in a margin call.
        margin_call_extension_count: :class:`int`
            The number of times that the Account's current margin call was extended.
        last_margin_call_extension_time: :class:`~async_v20.DateTime`
            The date/time of the Account's last margin call extension.
        open_trade_count: :class:`int`
            The number of Trades currently open in the Account.
        open_position_count: :class:`int`
            The number of Positions currently open in the Account.
        pending_order_count: :class:`int`
            The number of Orders currently pending in the Account.
        hedging_enabled: :class:`bool`
            Flag indicating that the Account has hedging enabled.
        unrealized_pl: :class:`~async_v20.AccountUnits`
            The total unrealized profit/loss for all Trades currently open
            in the Account. Represented in the Account's home currency.
        nav: :class:`~async_v20.AccountUnits`
            The net asset value of the Account. Equal to
            Account balance + unrealizedPL. Represented in the Account's home currency.
        margin_used: :class:`~async_v20.AccountUnits`
            Margin currently used for the Account.
            Represented in the Account's home currency.
        margin_available: :class:`~async_v20.AccountUnits`
            Margin available for Account. Represented in the Account's home currency.
        position_value: :class:`~async_v20.AccountUnits`
            The value of the Account's open
            positions represented in the Account's home currency.
        margin_closeout_unrealized_pl: :class:`~async_v20.AccountUnits`
            The Account's margin closeout unrealized PL.
        margin_closeout_nav: :class:`~async_v20.AccountUnits`
            The Account's margin closeout NAV.
        margin_closeout_margin_used: :class:`~async_v20.AccountUnits`
            The Account's margin closeout margin used.
        margin_closeout_percent: :class:`~async_v20.DecimalNumber`
            The Account's margin closeout percentage. When this value is 1.0
            or above the Account is in a margin closeout situation.
        margin_closeout_position_value: :class:`~async_v20.DecimalNumber`
            The value of the Account's open positions as used
            for margin closeout calculations represented in the Account's home currency.
        withdrawal_limit: :class:`~async_v20.AccountUnits`
            The current WithdrawalLimit for the account which will be zero or
            a positive value indicating how much can be withdrawn from the account.
        margin_call_margin_used: :class:`~async_v20.AccountUnits`
            The Account's margin call margin used.
        margin_call_percent: :class:`~async_v20.DecimalNumber`
            The Account's margin call percentage. When this value is 1.0
            or above the Account is in a margin call situation.
        last_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the last Transaction created for the Account.
        dividend: :class:`~async_v20.DecimalNumber`
            Dividend
        dividendAdjustment: :class:`~async_v20.AccountUnits`
            Something
    """

    def __init__(self, id: AccountID = sentinel, alias: str = sentinel, currency: Currency = sentinel,
                 balance: AccountUnits = sentinel,
                 created_by_user_id: int = sentinel, created_time: DateTime = sentinel, pl: AccountUnits = sentinel,
                 resettable_pl: AccountUnits = sentinel, resettabled_pl_time: DateTime = sentinel,
                 commission: AccountUnits = sentinel, margin_rate: DecimalNumber = sentinel,
                 margin_call_enter_time: DateTime = sentinel, margin_call_extension_count: int = sentinel,
                 last_margin_call_extension_time: DateTime = sentinel, open_trade_count: int = sentinel,
                 open_position_count: int = sentinel, pending_order_count: int = sentinel,
                 hedging_enabled: bool = sentinel,
                 unrealized_pl: AccountUnits = sentinel, nav: AccountUnits = sentinel,
                 margin_used: AccountUnits = sentinel,
                 margin_available: AccountUnits = sentinel, position_value: AccountUnits = sentinel,
                 margin_closeout_unrealized_pl: AccountUnits = sentinel, margin_closeout_nav: AccountUnits = sentinel,
                 margin_closeout_margin_used: AccountUnits = sentinel,
                 margin_closeout_percent: DecimalNumber = sentinel,
                 margin_closeout_position_value: DecimalNumber = sentinel, withdrawal_limit: AccountUnits = sentinel,
                 margin_call_margin_used: AccountUnits = sentinel, margin_call_percent: DecimalNumber = sentinel,
                 last_transaction_id: TransactionID = sentinel, trades: ArrayTradeSummary = sentinel,
                 positions: ArrayPosition = sentinel, orders: ArrayOrder = sentinel,
                 financing: DecimalNumber = sentinel,
                 guaranteed_stop_loss_order_mode: GuaranteedStopLossOrderMode = sentinel,
                 resettable_pl_time: DateTime = sentinel,
                 guaranteed_execution_fees: AccountUnits = sentinel,
                 dividend: DecimalNumber = sentinel,
                 ):
        Model.__init__(**locals())


class MarketOrderRequest(OrderRequest, type=OrderType('MARKET')):
    """A MarketOrderRequest specifies the parameters that may be set when creating
    a Market Order.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The Market Order's Instrument.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the Market Order. A positive number of units
            results in a long Order, and a negative number of units results in a short Order.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the Market Order.
            Restricted to FOK or IOC for a MarketOrder.
        price_bound: :class:`~async_v20.PriceValue`
            The worst price that the client is willing to have the Market Order filled at.
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
            a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.

    """

    def __init__(self, instrument: InstrumentName, units: DecimalNumber,
                 time_in_force: TimeInForce = 'FOK', price_bound: PriceValue = sentinel,
                 position_fill: OrderPositionFill = 'DEFAULT', client_extensions: ClientExtensions = sentinel,
                 take_profit_on_fill: TakeProfitDetails = sentinel, stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel):
        Model.__init__(**locals())


class TakeProfitOrderTransaction(Transaction, type=TransactionType('TAKE_PROFIT_ORDER')):
    """A TakeProfitOrderTransaction represents the creation of a TakeProfit Order
    in the user's Account.

    Attributes:
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade to close when the price threshold is breached.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the TakeProfit Order. The associated Trade will be
            closed by a market price that is equal to or better than this threshold.
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        client_trade_id: :class:`~async_v20.ClientID`
            The client ID of the Trade to be closed when the price threshold is breached.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the TakeProfit Order. Restricted
            to "GTC", "GFD" and "GTD" for TakeProfit Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the TakeProfit Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: :class:`~async_v20.TakeProfitOrderReason`
            The reason that the Take Profit Order was initiated
        client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        order_fill_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancelling_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    def __init__(self, trade_id: TradeID, price: PriceValue, id: TransactionID = sentinel, time: DateTime = sentinel,
                 user_id: int = sentinel, account_id: AccountID = sentinel, batch_id: TransactionID = sentinel,
                 request_id: RequestID = sentinel,
                 client_trade_id: ClientID = sentinel, time_in_force: TimeInForce = 'GTC',
                 gtd_time: DateTime = sentinel,
                 trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: TakeProfitOrderReason = sentinel,
                 client_extensions: ClientExtensions = sentinel, order_fill_transaction_id: TransactionID = sentinel,
                 replaces_order_id: OrderID = sentinel, cancelling_transaction_id: TransactionID = sentinel):
        Model.__init__(**locals())


class TakeProfitOrder(Order, type=OrderType('TAKE_PROFIT')):
    """A TakeProfitOrder is an order that is linked to an open Trade and created
    with a price threshold. The Order will be filled (closing the Trade) by the
    first price that is equal to or better than the threshold. A
    TakeProfitOrder cannot be used to open a new Position.

    Attributes:
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade to close when the price threshold is breached.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the TakeProfit Order. The associated Trade will be
            closed by a market price that is equal to or better than this threshold.
        id: :class:`~async_v20.OrderID`
            The Order's identifier, unique within the Order's Account.
        create_time: :class:`~async_v20.DateTime`
            The time when the Order was created.
        state: :class:`~async_v20.OrderState`
            The current state of the Order.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        client_trade_id: :class:`~async_v20.ClientID`
            The client ID of the Trade to be closed when the price threshold is breached.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the TakeProfit Order. Restricted
            to "GTC", "GFD" and "GTD" for TakeProfit Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the TakeProfit Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        filling_transaction_id: :class:`~async_v20.TransactionID`
            ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filled_time: :class:`~async_v20.DateTime`
            Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        trade_opened_id: :class:`~async_v20.TradeID`
            Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        trade_reduced_id: :class:`~async_v20.TradeID`
            Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        trade_closed_ids: ( :class:`~async_v20.TradeID`, ...),
            Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancelling_transaction_id: :class:`~async_v20.TransactionID`
            ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelled_time: :class:`~async_v20.DateTime`
            Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replaced_by_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

    """

    def __init__(self, trade_id: TradeID, price: PriceValue, id: OrderID = sentinel, create_time: DateTime = sentinel,
                 state: OrderState = sentinel, client_extensions: ClientExtensions = sentinel,
                 client_trade_id: ClientID = sentinel, time_in_force: TimeInForce = 'GTC',
                 gtd_time: DateTime = sentinel,
                 trigger_condition: OrderTriggerCondition = 'DEFAULT', filling_transaction_id: TransactionID = sentinel,
                 filled_time: DateTime = sentinel, trade_opened_id: TradeID = sentinel,
                 trade_reduced_id: TradeID = sentinel,
                 trade_closed_ids: ArrayTradeID = sentinel, cancelling_transaction_id: TransactionID = sentinel,
                 cancelled_time: DateTime = sentinel, replaces_order_id: OrderID = sentinel,
                 replaced_by_order_id: OrderID = sentinel):
        Model.__init__(**locals())


class StopLossOrder(Order, type=OrderType('STOP_LOSS')):
    """A StopLossOrder is an order that is linked to an open Trade and created
    with a price threshold. The Order will be filled (closing the Trade) by the
    first price that is equal to or worse than the threshold. A StopLossOrder
    cannot be used to open a new Position.

    Attributes:
        :class:`~async_v20.TradeID`
            The ID of the Trade to close when the price threshold is breached.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the StopLoss Order. The associated Trade will be
            closed by a market price that is equal to or worse than this threshold.
        id: :class:`~async_v20.OrderID`
            The Order's identifier, unique within the Order's Account.
        create_time: :class:`~async_v20.DateTime`
            The time when the Order was created.
        state: :class:`~async_v20.OrderState`
            The current state of the Order.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        client_:class:`~async_v20.TradeID`
            The client ID of the Trade to be closed when the price threshold is breached.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the StopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for StopLoss Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        guaranteed: :class: `bool`
            Flag indicating that the Stop Loss Order is guaranteed. The default value
            depends on the GuaranteedStopLossOrderMode of the account, if it is
            REQUIRED, the default will be true, for DISABLED or ENABLED the default
            is false.
        filling_transaction_id: :class:`~async_v20.TransactionID`
            ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filled_time: :class:`~async_v20.DateTime`
            Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        trade_opened_id: :class:`~async_v20.TradeID`
            Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        trade_reduced_id: :class:`~async_v20.TradeID`
            Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        trade_closed_ids: ( :class:`~async_v20.TradeID`, ...),
            Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancelling_transaction_id: :class:`~async_v20.TransactionID`
            ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelled_time: :class:`~async_v20.DateTime`
            Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replaced_by_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

        """

    def __init__(self, trade_id: TradeID, price: PriceValue, id: OrderID = sentinel, create_time: DateTime = sentinel,
                 state: OrderState = sentinel, client_extensions: ClientExtensions = sentinel,
                 client_trade_id: ClientID = sentinel, time_in_force: TimeInForce = 'GTC',
                 gtd_time: DateTime = sentinel,
                 trigger_condition: OrderTriggerCondition = 'DEFAULT', guaranteed: bool = sentinel,
                 filling_transaction_id: TransactionID = sentinel,
                 filled_time: DateTime = sentinel, trade_opened_id: TradeID = sentinel,
                 trade_reduced_id: TradeID = sentinel,
                 trade_closed_ids: ArrayTradeID = sentinel, cancelling_transaction_id: TransactionID = sentinel,
                 cancelled_time: DateTime = sentinel, replaces_order_id: OrderID = sentinel,
                 replaced_by_order_id: OrderID = sentinel):
        Model.__init__(**locals())


class TrailingStopLossOrder(Order, type=OrderType('TRAILING_STOP_LOSS')):
    """A TrailingStopLossOrder is an order that is linked to an open Trade and
    created with a price distance. The price distance is used to calculate a
    trailing stop value for the order that is in the losing direction from the
    market price at the time of the order's creation. The trailing stop value
    will follow the market price as it moves in the winning direction, and the
    order will filled (closing the Trade) by the first price that is equal to
    or worse than the trailing stop value. A TrailingStopLossOrder cannot be
    used to open a new Position.

    Attributes:
        :class:`~async_v20.TradeID`
            The ID of the Trade to close when the price threshold is breached.
        distance: :class:`~async_v20.PriceValue`
            The price distance specified for the TrailingStopLoss Order.
        id: :class:`~async_v20.OrderID`
            The Order's identifier, unique within the Order's Account.
        create_time: :class:`~async_v20.DateTime`
            The time when the Order was created.
        state: :class:`~async_v20.OrderState`
            The current state of the Order.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        client_:class:`~async_v20.TradeID`
            The client ID of the Trade to be closed when the price threshold is breached.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the TrailingStopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        trailing_stop_value: :class:`~async_v20.PriceValue`
            The trigger price for the Trailing Stop Loss Order. The trailing stop value will trail
            (follow) the market price by the TSL order's configured "distance" as the market price moves in the
            winning direction. If the market price moves to a level that is equal to or worse than the trailing stop
            value, the order will be filled and the Trade will be closed.
        filling_transaction_id: :class:`~async_v20.TransactionID`
            ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filled_time: :class:`~async_v20.DateTime`
            Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        trade_opened_id: :class:`~async_v20.TradeID`
            Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        trade_reduced_id: :class:`~async_v20.TradeID`
            Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        trade_closed_ids: ( :class:`~async_v20.TradeID`, ...),
            Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancelling_transaction_id: :class:`~async_v20.TransactionID`
            ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelled_time: :class:`~async_v20.DateTime`
            Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replaced_by_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

    """

    def __init__(self, trade_id: TradeID, distance: PriceValue, id: OrderID = sentinel,
                 create_time: DateTime = sentinel,
                 state: OrderState = sentinel, client_extensions: ClientExtensions = sentinel,
                 client_trade_id: ClientID = sentinel,
                 time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = sentinel,
                 trigger_condition: OrderTriggerCondition = 'DEFAULT', trailing_stop_value: PriceValue = sentinel,
                 filling_transaction_id: TransactionID = sentinel, filled_time: DateTime = sentinel,
                 trade_opened_id: TradeID = sentinel, trade_reduced_id: TradeID = sentinel,
                 trade_closed_ids: ArrayTradeID = sentinel, cancelling_transaction_id: TransactionID = sentinel,
                 cancelled_time: DateTime = sentinel, replaces_order_id: OrderID = sentinel,
                 replaced_by_order_id: OrderID = sentinel):
        Model.__init__(**locals())


class Trade(Model):
    """The specification of a Trade within an Account. This includes the full
    representation of the Trade's dependent Orders in addition to the IDs of
    those Orders.

    Attributes:
        id: :class:`~async_v20.TradeID`
            The Trade's identifier, unique within the Trade's Account.
        instrument: :class:`~async_v20.InstrumentName`
            The Trade's Instrument.
        price: :class:`~async_v20.PriceValue`
            The execution price of the Trade.
        open_time: :class:`~async_v20.DateTime`
            The date/time when the Trade was opened.
        state: :class:`~async_v20.TradeState`
            The current state of the Trade.
        initial_units: :class:`~async_v20.DecimalNumber`
            The initial size of the Trade. Negative values indicate
            a short Trade, and positive values indicate a long Trade.
        initial_margin_required: :class:`~async_v20.AccountUnits`
            The margin required at the time the Trade was created. Note, this is the
            ‘pure’ margin required, it is not the ‘effective’ margin used that
            factors in the trade risk if a GSLO is attached to the trade.
        current_units: :class:`~async_v20.DecimalNumber`
            The number of units currently open for the Trade. This
            value is reduced to 0.0 as the Trade is closed.
        realized_pl: :class:`~async_v20.AccountUnits`
            The total profit/loss realized on the closed portion of the Trade.
        unrealized_pl: :class:`~async_v20.AccountUnits`
            The unrealized profit/loss on the open portion of the Trade.
        average_close_price: :class:`~async_v20.PriceValue`
            The average closing price of the Trade. Only present if
            the Trade has been closed or reduced at least once.
        closing_transaction_ids: ( :class:`~async_v20.TransactionID`, ...)
            The IDs of the Transactions that have closed portions of this Trade.
        financing: :class:`~async_v20.AccountUnits`
            The financing paid/collected for this Trade.
        close_time: :class:`~async_v20.DateTime`
            The date/time when the Trade was fully closed.
            Only provided for Trades whose state is CLOSED.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions of the Trade.
        take_profit_order: :class:`~async_v20.TakeProfitOrder`
            Full representation of the Trade's Take Profit
            Order, only provided if such an Order exists.
        stop_loss_order: :class:`~async_v20.StopLossOrder`
            Full representation of the Trade's Stop Loss
            Order, only provided if such an Order exists.
        trailing_stop_loss_order: :class:`~async_v20.TrailingStopLossOrder`
            Full representation of the Trade's Trailing Stop Loss
            Order, only provided if such an Order exists.
        margin_used:
            Margin currently used by the Trade.

    """

    def __init__(self, id: TradeID = sentinel, instrument: InstrumentName = sentinel, price: PriceValue = sentinel,
                 open_time: DateTime = sentinel, state: TradeState = sentinel, initial_units: DecimalNumber = sentinel,
                 initial_margin_required: AccountUnits = sentinel,
                 current_units: DecimalNumber = sentinel, realized_pl: AccountUnits = sentinel,
                 unrealized_pl: AccountUnits = sentinel, average_close_price: PriceValue = sentinel,
                 closing_transaction_ids: ArrayTransactionID = sentinel, financing: AccountUnits = sentinel,
                 close_time: DateTime = sentinel, client_extensions: ClientExtensions = sentinel,
                 take_profit_order: TakeProfitOrder = sentinel, stop_loss_order: StopLossOrder = sentinel,
                 trailing_stop_loss_order: TrailingStopLossOrder = sentinel,
                 margin_used: AccountUnits = sentinel):
        Model.__init__(**locals())


class ArrayTrade(Array, contains=Trade):
    pass


class ClientConfigureRejectTransaction(Transaction, type=TransactionType('CLIENT_CONFIGURE_REJECT')):
    """A ClientConfigureRejectTransaction represents the reject of configuration
    of an Account by a client.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        alias: :class:`str`
            The client-provided alias for the Account.
        margin_rate: :class:`~async_v20.DecimalNumber`
            The margin rate override for the Account.
        reject_reason: :class:`~async_v20.TransactionRejectReason`
            The reason that the Reject Transaction was created

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 alias: str = sentinel,
                 margin_rate: DecimalNumber = sentinel, reject_reason: TransactionRejectReason = sentinel):
        Model.__init__(**locals())


class OrderCancelRejectTransaction(Transaction, type=TransactionType('ORDER_CANCEL_REJECT')):
    """An OrderCancelRejectTransaction represents the rejection of the
    cancellation of an Order in the client's Account.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        order_id: :class:`~async_v20.OrderID`
            The ID of the Order intended to be cancelled
        client_order_id: :class:`~async_v20.OrderID`
            The client ID of the Order intended to be cancelled
            (only provided if the Order has a client Order ID).
        reason: :class:`~async_v20.OrderCancelReason`
            The reason that the Order was to be cancelled.
        reject_reason: :class:`~async_v20.TransactionRejectReason`
            The reason that the Reject Transaction was created

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 order_id: OrderID = sentinel,
                 client_order_id: ClientID = sentinel, reason: OrderCancelReason = sentinel,
                 reject_reason: TransactionRejectReason = sentinel):
        Model.__init__(**locals())


class OrderClientExtensionsModifyRejectTransaction(Transaction,
                                                   type=TransactionType('ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT')):
    """A OrderClientExtensionsModifyRejectTransaction represents the rejection of
    the modification of an Order's Client Extensions.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        order_id: :class:`~async_v20.OrderID`
            The ID of the Order who's client extensions are to be modified.
        client_order_id: :class:`~async_v20.OrderID`
            The original Client ID of the Order who's client extensions are to be modified.
        client_extensions_modify: :class:`~async_v20.ClientExtensions`
            The new Client Extensions for the Order.
        trade_client_extensions_modify: :class:`~async_v20.ClientExtensions`
            The new Client Extensions for the Order's Trade on fill.
        reject_reason: :class:`~async_v20.TransactionRejectReason`
            The reason that the Reject Transaction was created

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 order_id: OrderID = sentinel,
                 client_order_id: ClientID = sentinel, client_extensions_modify: ClientExtensions = sentinel,
                 trade_client_extensions_modify: ClientExtensions = sentinel,
                 reject_reason: TransactionRejectReason = sentinel):
        Model.__init__(**locals())


class TradeClientExtensionsModifyRejectTransaction(Transaction,
                                                   type=TransactionType('TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT')):
    """A TradeClientExtensionsModifyRejectTransaction represents the rejection of
    the modification of a Trade's Client Extensions.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade who's client extensions are to be modified.
        client_trade_id: :class:`~async_v20.ClientID`
            The original Client ID of the Trade who's client extensions are to be modified.
        trade_client_extensions_modify: :class:`~async_v20.ClientExtensions`
            The new Client Extensions for the Trade.
        reject_reason: :class:`~async_v20.TransactionRejectReason`
            The reason that the Reject Transaction was created

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 trade_id: TradeID = sentinel,
                 client_trade_id: ClientID = sentinel, trade_client_extensions_modify: ClientExtensions = sentinel,
                 reject_reason: TransactionRejectReason = sentinel):
        Model.__init__(**locals())


class TransferFundsTransaction(Transaction, type=TransactionType('TRANSFER_FUNDS')):
    """A TransferFundsTransaction represents the transfer of funds in/out of an
    Account.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        amount: :class:`~async_v20.AccountUnits`
            The amount to deposit/withdraw from the Account in the Account's home currency.
            A positive value indicates a deposit, a negative value indicates a withdrawal.
        funding_reason: :class:`~async_v20.FundingReason`
            The reason that an Account is being funded.
        comment: :class:`str`
            An optional comment that may be attached to a fund transfer for audit purposes
        account_balance: :class:`~async_v20.AccountUnits`
            The Account's balance after funds are transferred.

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 amount: AccountUnits = sentinel,
                 funding_reason: FundingReason = sentinel, comment: str = sentinel,
                 account_balance: AccountUnits = sentinel):
        Model.__init__(**locals())


class TransferFundsRejectTransaction(Transaction, type=TransactionType('TRANSFER_FUNDS_REJECT')):
    """A TransferFundsRejectTransaction represents the rejection of the transfer
    of funds in/out of an Account.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        amount: :class:`~async_v20.AccountUnits`
            The amount to deposit/withdraw from the Account in the Account's home currency.
            A positive value indicates a deposit, a negative value indicates a withdrawal.
        funding_reason: :class:`~async_v20.FundingReason`
            The reason that an Account is being funded.
        comment: :class:`str`
            An optional comment that may be attached to a fund transfer for audit purposes
        reject_reason: :class:`~async_v20.TransactionRejectReason`
            The reason that the Reject Transaction was created

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 amount: AccountUnits = sentinel,
                 funding_reason: FundingReason = sentinel, comment: str = sentinel,
                 reject_reason: TransactionRejectReason = sentinel):
        Model.__init__(**locals())


class LimitOrderRequest(OrderRequest, type=OrderType('LIMIT')):
    """A LimitOrderRequest specifies the parameters that may be set when creating
    a Limit Order.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The Limit Order's Instrument.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the Limit Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the Limit Order. The Limit Order will only be
            filled by a market price that is equal to or better than this price.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the Limit Order.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the Limit Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
            a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.

    """

    def __init__(self, instrument: InstrumentName, units: DecimalNumber, price: PriceValue,
                 time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = sentinel,
                 position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                 client_extensions: ClientExtensions = sentinel, take_profit_on_fill: TakeProfitDetails = sentinel,
                 stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel):
        Model.__init__(**locals())


class MarketIfTouchedOrderRequest(OrderRequest, type=OrderType('MARKET_IF_TOUCHED')):
    """A MarketIfTouchedOrderRequest specifies the parameters that may be set when
    creating a Market-if-Touched Order.

    Attributes:

        instrument: :class:`~async_v20.InstrumentName`
            The MarketIfTouched Order's Instrument.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be
            filled by a market price that crosses this price from the direction of the market price
            at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's
            price and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.
        price_bound: :class:`~async_v20.PriceValue`
            The worst market price that may be used to fill this MarketIfTouched Order.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the MarketIfTouched Order. Restricted
            to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the MarketIfTouched Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
            a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.

        """

    def __init__(self, instrument: InstrumentName, units: DecimalNumber, price: PriceValue,
                 price_bound: PriceValue = sentinel,
                 time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = sentinel,
                 position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                 client_extensions: ClientExtensions = sentinel, take_profit_on_fill: TakeProfitDetails = sentinel,
                 stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel):
        Model.__init__(**locals())


class StopOrderRequest(OrderRequest, type=OrderType('STOP')):
    """A StopOrderRequest specifies the parameters that may be set when creating a
    Stop Order.

    Attributes:

        instrument: :class:`~async_v20.InstrumentName`
            The Stop Order's Instrument.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the Stop Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the Stop Order. The Stop Order will only be
            filled by a market price that is equal to or worse than this price.
        price_bound: :class:`~async_v20.PriceValue`
            The worst market price that may be used to fill this Stop Order. If the market gaps and
            crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the Stop Order.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the Stop Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
            a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.

    """

    def __init__(self, instrument: InstrumentName, units: DecimalNumber, price: PriceValue,
                 price_bound: PriceValue = sentinel, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = sentinel,
                 position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                 client_extensions: ClientExtensions = sentinel, take_profit_on_fill: TakeProfitDetails = sentinel,
                 stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel):
        Model.__init__(**locals())


class Account(AccountSummary):
    """The full details of a client's Account. This includes full open Trade, open
    Position and pending Order representation.

    Attributes:
        id: :class:`~async_v20.AccountID`
            The Account's identifier
        alias: :class:`str`
            Client-assigned alias for the Account. Only provided
            if the Account has an alias set
        currency: :class:`~async_v20.Currency`
            The home currency of the Account
        balance: :class:`~async_v20.AccountUnits`
            The current balance of the Account. Represented in the Account's home currency.
        created_by_user_id: :class:`int`
            ID of the user that created the Account.
        created_time: :class:`~async_v20.DateTime`
            The date/time when the Account was created.
        pl: :class:`~async_v20.AccountUnits`
            The total profit/loss realized over the lifetime of
            the Account. Represented in the Account's home currency.
        resettable_pl: :class:`~async_v20.AccountUnits`
            The total realized profit/loss for the Account since it was
            last reset by the client. Represented in the Account's home currency.
        resettabled_pl_time: :class:`~async_v20.DateTime`
            The date/time that the Account's resettablePL was last reset.
        commission: :class:`~async_v20.AccountUnits`
            The total amount of commission paid over the lifetime
            of the Account. Represented in the Account's home currency.
        margin_rate: :class:`~async_v20.DecimalNumber`
            Client-provided margin rate override for the Account. The effective margin rate of the Account
            is the lesser of this value and
            the OANDA margin rate for the Account's division. This value is only provided if a margin rate override
            exists for the Account.
        margin_call_enter_time: :class:`~async_v20.DateTime`
            The date/time when the Account entered a margin call state.
            Only provided if the Account is in a margin call.
        margin_call_extension_count: :class:`int`
            The number of times that the Account's current margin call was extended.
        last_margin_call_extension_time: :class:`~async_v20.DateTime`
            The date/time of the Account's last margin call extension.
        open_trade_count: :class:`int`
            The number of Trades currently open in the Account.
        open_position_count: :class:`int`
            The number of Positions currently open in the Account.
        pending_order_count: :class:`int`
            The number of Orders currently pending in the Account.
        hedging_enabled: :class:`bool`
            Flag indicating that the Account has hedging enabled.
        unrealized_pl: :class:`~async_v20.AccountUnits`
            The total unrealized profit/loss for all Trades currently open
            in the Account. Represented in the Account's home currency.
        nav: :class:`~async_v20.AccountUnits`
            The net asset value of the Account. Equal to
            Account balance + unrealizedPL. Represented in the Account's home currency.
        margin_used: :class:`~async_v20.AccountUnits`
            Margin currently used for the Account.
            Represented in the Account's home currency.
        margin_available: :class:`~async_v20.AccountUnits`
            Margin available for Account. Represented in the Account's home currency.
        position_value: :class:`~async_v20.AccountUnits`
            The value of the Account's open
            positions represented in the Account's home currency.
        margin_closeout_unrealized_pl: :class:`~async_v20.AccountUnits`
            The Account's margin closeout unrealized PL.
        margin_closeout_nav: :class:`~async_v20.AccountUnits`
            The Account's margin closeout NAV.
        margin_closeout_margin_used: :class:`~async_v20.AccountUnits`
            The Account's margin closeout margin used.
        margin_closeout_percent: :class:`~async_v20.DecimalNumber`
            The Account's margin closeout percentage. When this value is 1.0
            or above the Account is in a margin closeout situation.
        margin_closeout_position_value: :class:`~async_v20.DecimalNumber`
            The value of the Account's open positions as used
            for margin closeout calculations represented in the Account's home currency.
        withdrawal_limit: :class:`~async_v20.AccountUnits`
            The current WithdrawalLimit for the account which will be zero or
            a positive value indicating how much can be withdrawn from the account.
        margin_call_margin_used: :class:`~async_v20.AccountUnits`
            The Account's margin call margin used.
        margin_call_percent: :class:`~async_v20.DecimalNumber`
            The Account's margin call percentage. When this value is 1.0
            or above the Account is in a margin call situation.
        last_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the last Transaction created for the Account.
        trades: ( :class:`~async_v20.TradeSummary`, ...)
            The details of the Trades currently open in the Account.
        positions: ( :class:`~async_v20.Position`, ...)
            The details all Account Positions.
        orders: ( :class:`~async_v20.Order`, ...)
            The details of the Orders currently pending in the Account.
        dividend: :class:`~async_v20.DecimalNumber`
            Dividend
        dividendAdjustment: :class:`~async_v20.DecimalNumber`
            Undocumented
    """

    def __init__(self, id: AccountID = sentinel, alias: str = sentinel, currency: Currency = sentinel,
                 balance: AccountUnits = sentinel,
                 created_by_user_id: int = sentinel, created_time: DateTime = sentinel, pl: AccountUnits = sentinel,
                 resettable_pl: AccountUnits = sentinel, resettabled_pl_time: DateTime = sentinel,
                 commission: AccountUnits = sentinel, margin_rate: DecimalNumber = sentinel,
                 margin_call_enter_time: DateTime = sentinel, margin_call_extension_count: int = sentinel,
                 last_margin_call_extension_time: DateTime = sentinel, open_trade_count: int = sentinel,
                 open_position_count: int = sentinel, pending_order_count: int = sentinel,
                 hedging_enabled: bool = sentinel,
                 unrealized_pl: AccountUnits = sentinel, nav: AccountUnits = sentinel,
                 margin_used: AccountUnits = sentinel,
                 margin_available: AccountUnits = sentinel, position_value: AccountUnits = sentinel,
                 margin_closeout_unrealized_pl: AccountUnits = sentinel, margin_closeout_nav: AccountUnits = sentinel,
                 margin_closeout_margin_used: AccountUnits = sentinel,
                 margin_closeout_percent: DecimalNumber = sentinel,
                 margin_closeout_position_value: DecimalNumber = sentinel, withdrawal_limit: AccountUnits = sentinel,
                 margin_call_margin_used: AccountUnits = sentinel, margin_call_percent: DecimalNumber = sentinel,
                 last_transaction_id: TransactionID = sentinel, trades: ArrayTradeSummary = sentinel,
                 positions: ArrayPosition = sentinel, orders: ArrayOrder = sentinel,
                 financing: DecimalNumber = sentinel,
                 guaranteed_stop_loss_order_mode: GuaranteedStopLossOrderMode = sentinel,
                 resettable_pl_time: DateTime = sentinel,
                 dividend: DecimalNumber = sentinel,
                 dividend_adjustment: AccountUnits = sentinel,
                 guaranteed_execution_fees: AccountUnits = sentinel):
        Model.__init__(**locals())


class MarketOrderTransaction(Transaction, type=TransactionType('MARKET_ORDER')):
    """A MarketOrderTransaction represents the creation of a Market Order in the
    user's account. A Market Order is an Order that is filled immediately at
    the current market price. Market Orders can be specialized when they are
    created to accomplish a specific tas': 'to' close a Trade, to closeout a
    Position or to particiate in in a Margin closeout.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The Market Order's Instrument.
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the Market Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the Market Order.
            Restricted to FOK or IOC for a MarketOrder.
        price_bound: :class:`~async_v20.PriceValue`
            The worst price that the client is willing to have the Market Order filled at.
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trade_close: :class:`~async_v20.MarketOrderTradeClose`
            Details of the Trade requested to be closed, only provided when
            the Market Order is being used to explicitly close a Trade.
        long_position_closeout: :class:`~async_v20.MarketOrderPositionCloseout`
            Details of the long Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a long Position.
        short_position_closeout: :class:`~async_v20.MarketOrderPositionCloseout`
            Details of the short Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a short Position.
        margin_closeout: :class:`~async_v20.MarketOrderMarginCloseout`
            Details of the Margin Closeout that this Market Order was created for
        delayed_trade_close: :class:`~async_v20.MarketOrderDelayedTradeClose`
            Details of the delayed Trade close that this Market Order was created for
        reason: :class:`~async_v20.MarketOrderReason`
            The reason that the Market Order was created
        client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.

    """

    def __init__(self, instrument: InstrumentName, units: DecimalNumber, id: TransactionID = sentinel,
                 time: DateTime = sentinel,
                 user_id: int = sentinel, account_id: AccountID = sentinel, batch_id: TransactionID = sentinel,
                 request_id: RequestID = sentinel,
                 time_in_force: TimeInForce = 'FOK', price_bound: PriceValue = sentinel,
                 position_fill: OrderPositionFill = 'DEFAULT', trade_close: MarketOrderTradeClose = sentinel,
                 long_position_closeout: MarketOrderPositionCloseout = sentinel,
                 short_position_closeout: MarketOrderPositionCloseout = sentinel,
                 margin_closeout: MarketOrderMarginCloseout = sentinel,
                 delayed_trade_close: MarketOrderDelayedTradeClose = sentinel, reason: MarketOrderReason = sentinel,
                 client_extensions: ClientExtensions = sentinel, take_profit_on_fill: TakeProfitDetails = sentinel,
                 stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel):
        Model.__init__(**locals())


class MarketOrderRejectTransaction(Transaction, type=TransactionType('MARKET_ORDER_REJECT')):
    """A MarketOrderRejectTransaction represents the rejection of the creation of
    a Market Order.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The Market Order's Instrument.
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the Market Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the Market Order.
            Restricted to FOK or IOC for a MarketOrder.
        price_bound: :class:`~async_v20.PriceValue`
            The worst price that the client is willing to have the Market Order filled at.
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trade_close: :class:`~async_v20.MarketOrderTradeClose`
            Details of the Trade requested to be closed, only provided when
            the Market Order is being used to explicitly close a Trade.
        long_position_closeout: :class:`~async_v20.MarketOrderPositionCloseout`
            Details of the long Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a long Position.
        short_position_closeout: :class:`~async_v20.MarketOrderPositionCloseout`
            Details of the short Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a short Position.
        margin_closeout: :class:`~async_v20.MarketOrderMarginCloseout`
            Details of the Margin Closeout that this Market Order was created for
        delayed_trade_close: :class:`~async_v20.MarketOrderDelayedTradeClose`
            Details of the delayed Trade close that this Market Order was created for
        reason: :class:`~async_v20.MarketOrderReason`
            The reason that the Market Order was created
        client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        reject_reason: :class:`~async_v20.TransactionRejectReason`
            The reason that the Reject Transaction was created

    """

    def __init__(self, instrument: InstrumentName = sentinel, units: DecimalNumber = sentinel,
                 id: TransactionID = sentinel,
                 time: DateTime = sentinel,
                 user_id: int = sentinel, account_id: AccountID = sentinel, batch_id: TransactionID = sentinel,
                 request_id: RequestID = sentinel,
                 time_in_force: TimeInForce = 'FOK', price_bound: PriceValue = sentinel,
                 position_fill: OrderPositionFill = 'DEFAULT', trade_close: MarketOrderTradeClose = sentinel,
                 long_position_closeout: MarketOrderPositionCloseout = sentinel,
                 short_position_closeout: MarketOrderPositionCloseout = sentinel,
                 margin_closeout: MarketOrderMarginCloseout = sentinel,
                 delayed_trade_close: MarketOrderDelayedTradeClose = sentinel, reason: MarketOrderReason = sentinel,
                 client_extensions: ClientExtensions = sentinel, take_profit_on_fill: TakeProfitDetails = sentinel,
                 stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel,
                 reject_reason: TransactionRejectReason = sentinel):
        Model.__init__(**locals())


class StopLossOrderTransaction(Transaction, type=TransactionType('STOP_LOSS_ORDER')):
    """A StopLossOrderTransaction represents the creation of a StopLoss Order in
    the user's Account.

    Attributes:
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade to close when the price threshold is breached.
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        client_trade_id: :class:`~async_v20.TradeID`
            The client ID of the Trade to be closed when the price threshold is breached.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the StopLoss Order. The associated Trade will be
            closed by a market price that is equal to or worse than this threshold.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the StopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for StopLoss Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: :class:`~async_v20.StopLossOrderReason`
            The reason that the Stop Loss Order was initiated
        client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        order_fill_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancelling_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).
        guaranteed: :class:`bool`
            Flag indicating that the Stop Loss Order is guaranteed. The default value
            depends on the GuaranteedStopLossOrderMode of the account, if it is
            REQUIRED, the default will be true, for DISABLED or ENABLED the default
            is false.
    """

    def __init__(self, trade_id: TradeID, price: PriceValue, id: TransactionID = sentinel, time: DateTime = sentinel,
                 user_id: int = sentinel, account_id: AccountID = sentinel, batch_id: TransactionID = sentinel,
                 request_id: RequestID = sentinel,
                 client_trade_id: ClientID = sentinel, time_in_force: TimeInForce = 'GTC',
                 gtd_time: DateTime = sentinel,
                 trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: StopLossOrderReason = sentinel,
                 client_extensions: ClientExtensions = sentinel, order_fill_transaction_id: TransactionID = sentinel,
                 replaces_order_id: OrderID = sentinel, cancelling_transaction_id: TransactionID = sentinel,
                 guaranteed: bool = sentinel):
        Model.__init__(**locals())


class TrailingStopLossOrderTransaction(Transaction, type=TransactionType('TRAILING_STOP_LOSS_ORDER')):
    """A TrailingStopLossOrderTransaction represents the creation of a
    TrailingStopLoss Order in the user's Account.

    Attributes:
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade to close when the price threshold is breached.
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        client_trade_id: :class:`~async_v20.TradeID`
            The client ID of the Trade to be closed when the price threshold is breached.
        distance: :class:`~async_v20.PriceValue`
            The price distance specified for the TrailingStopLoss Order.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the TrailingStopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: :class:`~async_v20.TrailingStopLossOrderReason`
            The reason that the Trailing Stop Loss Order was initiated
        client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        order_fill_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancelling_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    def __init__(self, trade_id: TradeID, distance: PriceValue, id: TransactionID = sentinel, time: DateTime = sentinel,
                 user_id: int = sentinel, account_id: AccountID = sentinel, batch_id: TransactionID = sentinel,
                 request_id: RequestID = sentinel,
                 client_trade_id: ClientID = sentinel, time_in_force: TimeInForce = 'GTC',
                 gtd_time: DateTime = sentinel,
                 trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: TrailingStopLossOrderReason = sentinel,
                 client_extensions: ClientExtensions = sentinel, order_fill_transaction_id: TransactionID = sentinel,
                 replaces_order_id: OrderID = sentinel, cancelling_transaction_id: TransactionID = sentinel):
        Model.__init__(**locals())


class LimitOrder(Order, type=OrderType('LIMIT')):
    """A LimitOrder is an order that is created with a price threshold, and will
    only be filled by a price that is equal to or better than the threshold.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The Limit Order's Instrument.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the Limit Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the Limit Order. The Limit Order will only be
            filled by a market price that is equal to or better than this price.
        id: :class:`~async_v20.OrderID`
            The Order's identifier, unique within the Order's Account.
        create_time: :class:`~async_v20.DateTime`
            The time when the Order was created.
        state: :class:`~async_v20.OrderState`
            The current state of the Order.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the Limit Order.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the Limit Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
            a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.
        filling_transaction_id: :class:`~async_v20.TransactionID`
            ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filled_time: :class:`~async_v20.DateTime`
            Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        trade_opened_id: :class:`~async_v20.TradeID`
            Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        trade_reduced_id: :class:`~async_v20.TradeID`
            Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        trade_closed_ids: ( :class:`~async_v20.TradeID`, ...),
            Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancelling_transaction_id: :class:`~async_v20.TransactionID`
            ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelled_time: :class:`~async_v20.DateTime`
            Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replaced_by_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

        """

    def __init__(self, instrument: InstrumentName, units: DecimalNumber, price: PriceValue, id: OrderID = sentinel,
                 create_time: DateTime = sentinel, state: OrderState = sentinel,
                 client_extensions: ClientExtensions = sentinel,
                 time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = sentinel,
                 position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                 take_profit_on_fill: TakeProfitDetails = sentinel, stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel, filling_transaction_id: TransactionID = sentinel,
                 filled_time: DateTime = sentinel, trade_opened_id: TradeID = sentinel,
                 trade_reduced_id: TradeID = sentinel,
                 trade_closed_ids: ArrayTradeID = sentinel, cancelling_transaction_id: TransactionID = sentinel,
                 cancelled_time: DateTime = sentinel, replaces_order_id: OrderID = sentinel,
                 replaced_by_order_id: OrderID = sentinel):
        Model.__init__(**locals())


class MarketIfTouchedOrder(Order, type=OrderType('MARKET_IF_TOUCHED')):
    """A MarketIfTouchedOrder is an order that is created with a price threshold,
    and will only be filled by a market price that is touches or crosses the
    threshold.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The MarketIfTouched Order's Instrument.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be
            filled by a market price that crosses this price from the direction of the market price
            at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's
            price and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.
        id: :class:`~async_v20.OrderID`
            The Order's identifier, unique within the Order's Account.
        create_time: :class:`~async_v20.DateTime`
            The time when the Order was created.
        state: :class:`~async_v20.OrderState`
            The current state of the Order.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        price_bound: :class:`~async_v20.PriceValue`
            The worst market price that may be used to fill this MarketIfTouched Order.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the MarketIfTouched Order. Restricted
            to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the MarketIfTouched Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        initial_market_price: :class:`~async_v20.PriceValue`
            The Market price at the time when the MarketIfTouched Order was created.
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
            a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.
        filling_transaction_id: :class:`~async_v20.TransactionID`
            ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filled_time: :class:`~async_v20.DateTime`
            Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        trade_opened_id: :class:`~async_v20.TradeID`
            Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        trade_reduced_id: :class:`~async_v20.TradeID`
            Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        trade_closed_ids: ( :class:`~async_v20.TradeID`, ...),
            Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancelling_transaction_id: :class:`~async_v20.TransactionID`
            ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelled_time: :class:`~async_v20.DateTime`
            Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replaced_by_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

        """

    def __init__(self, instrument: InstrumentName, units: DecimalNumber, price: PriceValue, id: OrderID = sentinel,
                 create_time: DateTime = sentinel, state: OrderState = sentinel,
                 client_extensions: ClientExtensions = sentinel,
                 price_bound: PriceValue = sentinel,
                 time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = sentinel,
                 position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                 initial_market_price: PriceValue = sentinel, take_profit_on_fill: TakeProfitDetails = sentinel,
                 stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel, filling_transaction_id: TransactionID = sentinel,
                 filled_time: DateTime = sentinel, trade_opened_id: TradeID = sentinel,
                 trade_reduced_id: TradeID = sentinel,
                 trade_closed_ids: ArrayTradeID = sentinel, cancelling_transaction_id: TransactionID = sentinel,
                 cancelled_time: DateTime = sentinel, replaces_order_id: OrderID = sentinel,
                 replaced_by_order_id: OrderID = sentinel):
        Model.__init__(**locals())


class StopOrder(Order, type=OrderType('STOP')):
    """A StopOrder is an order that is created with a price threshold, and will
    only be filled by a price that is equal to or worse than the threshold.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The Stop Order's Instrument.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the Stop Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the Stop Order. The Stop Order will only be
            filled by a market price that is equal to or worse than this price.
        id: :class:`~async_v20.OrderID`
            The Order's identifier, unique within the Order's Account.
        create_time: :class:`~async_v20.DateTime`
            The time when the Order was created.
        state: :class:`~async_v20.OrderState`
            The current state of the Order.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        price_bound: :class:`~async_v20.PriceValue`
            The worst market price that may be used to fill this Stop Order. If the market gaps and
            crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the Stop Order.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the Stop Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
            a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.
        filling_transaction_id: :class:`~async_v20.TransactionID`
            ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filled_time: :class:`~async_v20.DateTime`
            Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        trade_opened_id: :class:`~async_v20.TradeID`
            Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        trade_reduced_id: :class:`~async_v20.TradeID`
            Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        trade_closed_ids: ( :class:`~async_v20.TradeID`, ...),
            Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancelling_transaction_id: :class:`~async_v20.TransactionID`
            ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelled_time: :class:`~async_v20.DateTime`
            Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replaced_by_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

    """

    def __init__(self, instrument: InstrumentName, units: DecimalNumber, price: PriceValue, id: OrderID = sentinel,
                 create_time: DateTime = sentinel, state: OrderState = sentinel,
                 client_extensions: ClientExtensions = sentinel,
                 price_bound: PriceValue = sentinel, time_in_force: TimeInForce = 'GTC',
                 gtd_time: DateTime = sentinel, position_fill: OrderPositionFill = 'DEFAULT',
                 trigger_condition: OrderTriggerCondition = 'DEFAULT',
                 take_profit_on_fill: TakeProfitDetails = sentinel,
                 stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel, filling_transaction_id: TransactionID = sentinel,
                 filled_time: DateTime = sentinel, trade_opened_id: TradeID = sentinel,
                 trade_reduced_id: TradeID = sentinel,
                 trade_closed_ids: ArrayTradeID = sentinel, cancelling_transaction_id: TransactionID = sentinel,
                 cancelled_time: DateTime = sentinel, replaces_order_id: OrderID = sentinel,
                 replaced_by_order_id: OrderID = sentinel):
        Model.__init__(**locals())


class OrderFillTransaction(Transaction, type=TransactionType('ORDER_FILL')):
    """An OrderFillTransaction represents the filling of an Order in the client's
    Account.

    Attributes:
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        order_id: :class:`~async_v20.OrderID`
            The ID of the Order filled.
        client_order_id: :class:`~async_v20.ClientID`
            The client Order ID of the Order filled
            (only provided if the client has assigned one).
        instrument: :class:`~async_v20.InstrumentName`
            The name of the filled Order's instrument.
        units: :class:`~async_v20.DecimalNumber`
            The number of units filled by the Order.
        gain_quote_home_conversion_factor:
            This is the conversion factor in effect for the Account at the time of
            the OrderFill for converting any gains realized in Instrument quote units
            into units of the Account’s home currency.
        loss_quote_home_conversion_factor:
            This is the conversion factor in effect for the Account at the time of
            the OrderFill for converting any losses realized in Instrument quote
            units into units of the Account’s home currency.
        price: :class:`~async_v20.PriceValue`
            The average market price that the Order was filled at.
        full_price: :class:`~async_v20.PriceValue`
            The price in effect for the account at the time of the Order fill.
        reason: :class:`~async_v20.OrderFillReason`
            The reason that an Order was filled
        pl: :class:`~async_v20.AccountUnits`
            The profit or loss incurred when the Order was filled.
        financing: :class:`~async_v20.AccountUnits`
            The financing paid or collected when the Order was filled.
        commission: :class:`~async_v20.AccountUnits`
            The commission charged in the Account's home currency as a result of filling the Order. The
            commission is
            always represented as a positive quantity of the Account's home currency, however it reduces the balance in
            the Account.
        guaranteed_execution_fee:
            The total guaranteed execution fees charged for all Trades opened, closed
            or reduced with guaranteed Stop Loss Orders.
        account_balance: :class:`~async_v20.AccountUnits`
            The Account's balance after the Order was filled.
        trade_opened: :class:`~async_v20.TradeOpen`
            The Trade that was opened when the Order was filled
            (only provided if filling the Order resulted in a new Trade).
        trades_closed: (:class:`~async_v20.ArrayTradeReduce`
            The Trades that were closed when the Order was filled (only
            provided if filling the Order resulted in a closing open Trades).
        trade_reduced: :class:`~async_v20.TradeReduce`
            The Trade that was reduced when the Order was filled (only
            provided if filling the Order resulted in reducing an open Trade).
        half_spread_cost:
            The half spread cost for the OrderFill, which is the sum of the
            halfSpreadCost values in the tradeOpened, tradesClosed and tradeReduced
            fields. This can be a positive or negative value and is represented in
            the home currency of the Account.

    """

    def __init__(self, id: TransactionID = sentinel, time: DateTime = sentinel, user_id: int = sentinel,
                 account_id: AccountID = sentinel, batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 order_id: OrderID = sentinel, client_order_id: ClientID = sentinel,
                 instrument: InstrumentName = sentinel, units: DecimalNumber = sentinel, price: PriceValue = sentinel,
                 full_price: ClientPrice = sentinel, reason: OrderFillReason = sentinel, pl: AccountUnits = sentinel,
                 financing: AccountUnits = sentinel, commission: AccountUnits = sentinel,
                 account_balance: AccountUnits = sentinel,
                 trade_opened: TradeOpen = sentinel, trades_closed: ArrayTradeReduce = sentinel,
                 trade_reduced: TradeReduce = sentinel,
                 gain_quote_home_conversion_factor: DecimalNumber = sentinel,
                 loss_quote_home_conversion_factor: DecimalNumber = sentinel,
                 guaranteed_execution_fee: AccountUnits = sentinel,
                 half_spread_cost: AccountUnits = sentinel,
                 requested_units: AccountUnits = sentinel,
                 full_vwap: DecimalNumber = sentinel):
        Model.__init__(**locals())


class StopLossOrderRejectTransaction(Transaction, type=TransactionType('STOP_LOSS_ORDER_REJECT')):
    """A StopLossOrderRejectTransaction represents the rejection of the creation
    of a StopLoss Order.

    Attributes:
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade to close when the price threshold is breached.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the StopLoss Order. The associated Trade will be
            closed by a market price that is equal to or worse than this threshold.
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        client_trade_id: :class:`~async_v20.TradeID`
            The client ID of the Trade to be closed when the price threshold is breached.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the StopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for StopLoss Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: :class:`~async_v20.StopLossOrderReason`
            The reason that the Stop Loss Order was initiated
        client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        order_fill_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        intended_replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        reject_reason: :class:`~async_v20.TransactionRejectReason`
            The reason that the Reject Transaction was created

    """

    def __init__(self, trade_id: TradeID = sentinel, price: PriceValue = sentinel, id: TransactionID = sentinel,
                 time: DateTime = sentinel,
                 user_id: int = sentinel, account_id: AccountID = sentinel, batch_id: TransactionID = sentinel,
                 request_id: RequestID = sentinel,
                 client_trade_id: ClientID = sentinel, time_in_force: TimeInForce = 'GTC',
                 gtd_time: DateTime = sentinel,
                 trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: StopLossOrderReason = sentinel,
                 client_extensions: ClientExtensions = sentinel, order_fill_transaction_id: TransactionID = sentinel,
                 intended_replaces_order_id: OrderID = sentinel, reject_reason: TransactionRejectReason = sentinel):
        Model.__init__(**locals())


class MarketIfTouchedOrderTransaction(Transaction, type=TransactionType('MARKET_IF_TOUCHED_ORDER')):
    """A MarketIfTouchedOrderTransaction represents the creation of a
    MarketIfTouched Order in the user's Account.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The MarketIfTouched Order's Instrument.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be
            filled by a market price that crosses this price from the direction of the market price
            at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's price
            and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        price_bound: :class:`~async_v20.PriceValue`
            The worst market price that may be used to fill this MarketIfTouched Order.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the MarketIfTouched Order. Restricted
            to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the MarketIfTouched Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: :class:`~async_v20.MarketIfTouchedOrderReason`
            The reason that the Market-if-touched Order was initiated
        client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancelling_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    def __init__(self, instrument: InstrumentName, units: DecimalNumber, price: PriceValue,
                 id: TransactionID = sentinel,
                 time: DateTime = sentinel, user_id: int = sentinel, account_id: AccountID = sentinel,
                 batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 price_bound: PriceValue = sentinel,
                 time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = sentinel,
                 position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                 reason: MarketIfTouchedOrderReason = sentinel, client_extensions: ClientExtensions = sentinel,
                 take_profit_on_fill: TakeProfitDetails = sentinel, stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel, replaces_order_id: OrderID = sentinel,
                 cancelling_transaction_id: TransactionID = sentinel):
        Model.__init__(**locals())


class LimitOrderTransaction(Transaction, type=TransactionType('LIMIT_ORDER')):
    """A LimitOrderTransaction represents the creation of a Limit Order in the
    user's Account.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The Limit Order's Instrument.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the Limit Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the Limit Order. The Limit Order will only be
            filled by a market price that is equal to or better than this price.
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the Limit Order.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the Limit Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: :class:`~async_v20.LimitOrderReason`
            The reason that the Limit Order was initiated
        client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancelling_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).
        partial_fill: = positionFill (seems to be a mismatch in Oanda documentation)

    """

    def __init__(self, instrument: InstrumentName, units: DecimalNumber, price: PriceValue,
                 id: TransactionID = sentinel,
                 time: DateTime = sentinel, user_id: int = sentinel, account_id: AccountID = sentinel,
                 batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = sentinel,
                 position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                 reason: LimitOrderReason = sentinel, client_extensions: ClientExtensions = sentinel,
                 take_profit_on_fill: TakeProfitDetails = sentinel, stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel, replaces_order_id: OrderID = sentinel,
                 cancelling_transaction_id: TransactionID = sentinel, partial_fill: OrderPositionFill = sentinel):
        Model.__init__(**locals())


class TakeProfitOrderRejectTransaction(Transaction, type=TransactionType('TAKE_PROFIT_ORDER_REJECT')):
    """A TakeProfitOrderRejectTransaction represents the rejection of the creation
    of a TakeProfit Order.

    Attributes:
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade to close when the price threshold is breached.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the TakeProfit Order. The associated Trade will be
            closed by a market price that is equal to or better than this threshold.
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        client_trade_id: :class:`~async_v20.TradeID`
            The client ID of the Trade to be closed when the price threshold is breached.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the TakeProfit Order. Restricted
            to "GTC", "GFD" and "GTD" for TakeProfit Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the TakeProfit Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: :class:`~async_v20.TakeProfitOrderReason`
            The reason that the Take Profit Order was initiated
        client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        order_fill_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        intended_replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        reject_reason: :class:`~async_v20.TransactionRejectReason`
            The reason that the Reject Transaction was created

    """

    def __init__(self, trade_id: TradeID = sentinel, price: PriceValue = sentinel, id: TransactionID = sentinel,
                 time: DateTime = sentinel,
                 user_id: int = sentinel, account_id: AccountID = sentinel, batch_id: TransactionID = sentinel,
                 request_id: RequestID = sentinel,
                 client_trade_id: ClientID = sentinel, time_in_force: TimeInForce = 'GTC',
                 gtd_time: DateTime = sentinel,
                 trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: TakeProfitOrderReason = sentinel,
                 client_extensions: ClientExtensions = sentinel, order_fill_transaction_id: TransactionID = sentinel,
                 intended_replaces_order_id: OrderID = sentinel, reject_reason: TransactionRejectReason = sentinel):
        Model.__init__(**locals())


class TrailingStopLossOrderRejectTransaction(Transaction, type=TransactionType('TRAILING_STOP_LOSS_ORDER_REJECT')):
    """A TrailingStopLossOrderRejectTransaction represents the rejection of the
    creation of a TrailingStopLoss Order.

    Attributes:
        trade_id: :class:`~async_v20.TradeID`
            The ID of the Trade to close when the price threshold is breached.
        distance: :class:`~async_v20.PriceValue`
            The price distance specified for the TrailingStopLoss Order.
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        client_trade_id: :class:`~async_v20.TradeID`
            The client ID of the Trade to be closed when the price threshold is breached.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the TrailingStopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: :class:`~async_v20.TrailingStopLossOrderReason`
            The reason that the Trailing Stop Loss Order was initiated
        client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        order_fill_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        intended_replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        reject_reason: :class:`~async_v20.TransactionRejectReason`
            The reason that the Reject Transaction was created

    """

    def __init__(self, trade_id: TradeID = sentinel, distance: PriceValue = sentinel, id: TransactionID = sentinel,
                 time: DateTime = sentinel,
                 user_id: int = sentinel, account_id: AccountID = sentinel, batch_id: TransactionID = sentinel,
                 request_id: RequestID = sentinel,
                 client_trade_id: ClientID = sentinel, time_in_force: TimeInForce = 'GTC',
                 gtd_time: DateTime = sentinel,
                 trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: TrailingStopLossOrderReason = sentinel,
                 client_extensions: ClientExtensions = sentinel, order_fill_transaction_id: TransactionID = sentinel,
                 intended_replaces_order_id: OrderID = sentinel, reject_reason: TransactionRejectReason = sentinel):
        Model.__init__(**locals())


class StopOrderTransaction(Transaction, type=TransactionType('STOP_ORDER')):
    """A StopOrderTransaction represents the creation of a Stop Order in the
    user's Account.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The Stop Order's Instrument.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the Stop Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the Stop Order. The Stop Order will only be
            filled by a market price that is equal to or worse than this price.
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        price_bound: :class:`~async_v20.PriceValue`
            The worst market price that may be used to fill this Stop Order. If the market gaps and
            crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the Stop Order.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the Stop Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: :class:`~async_v20.StopOrderReason`
            The reason that the Stop Order was initiated
        client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancelling_transaction_id: :class:`~async_v20.TransactionID`
            The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    def __init__(self, instrument: InstrumentName, units: DecimalNumber, price: PriceValue,
                 id: TransactionID = sentinel,
                 time: DateTime = sentinel, user_id: int = sentinel, account_id: AccountID = sentinel,
                 batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 partial_fill: str = sentinel,
                 price_bound: PriceValue = sentinel, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = sentinel,
                 position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                 reason: StopOrderReason = sentinel, client_extensions: ClientExtensions = sentinel,
                 take_profit_on_fill: TakeProfitDetails = sentinel, stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel, replaces_order_id: OrderID = sentinel,
                 cancelling_transaction_id: TransactionID = sentinel):
        Model.__init__(**locals())


class MarketIfTouchedOrderRejectTransaction(Transaction, type=TransactionType('MARKET_IF_TOUCHED_ORDER_REJECT')):
    """A MarketIfTouchedOrderRejectTransaction represents the rejection of the
    creation of a MarketIfTouched Order.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The MarketIfTouched Order's Instrument.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be
            filled by a market price that crosses this price from the direction of the market price
            at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's price
            and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        price_bound: :class:`~async_v20.PriceValue`
            The worst market price that may be used to fill this MarketIfTouched Order.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the MarketIfTouched Order. Restricted
            to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the MarketIfTouched Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: :class:`~async_v20.MarketIfTouchedOrderReason`
            The reason that the Market-if-touched Order was initiated
        client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        intended_replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        reject_reason: :class:`~async_v20.TransactionRejectReason`
            The reason that the Reject Transaction was created

    """

    def __init__(self, instrument: InstrumentName = sentinel, units: DecimalNumber = sentinel,
                 price: PriceValue = sentinel,
                 id: TransactionID = sentinel,
                 time: DateTime = sentinel, user_id: int = sentinel, account_id: AccountID = sentinel,
                 batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 price_bound: PriceValue = sentinel,
                 time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = sentinel,
                 position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                 reason: MarketIfTouchedOrderReason = sentinel, client_extensions: ClientExtensions = sentinel,
                 take_profit_on_fill: TakeProfitDetails = sentinel, stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel, intended_replaces_order_id: OrderID = sentinel,
                 reject_reason: TransactionRejectReason = sentinel):
        Model.__init__(**locals())


class LimitOrderRejectTransaction(Transaction, type=TransactionType('LIMIT_ORDER_REJECT')):
    """A LimitOrderRejectTransaction represents the rejection of the creation of a
    Limit Order.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The Limit Order's Instrument.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the Limit Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the Limit Order. The Limit Order will only be
            filled by a market price that is equal to or better than this price.
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the Limit Order.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the Limit Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: :class:`~async_v20.LimitOrderReason`
            The reason that the Limit Order was initiated
        client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        intended_replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        reject_reason: :class:`~async_v20.TransactionRejectReason`
            The reason that the Reject Transaction was created

    """

    def __init__(self, instrument: InstrumentName = sentinel, units: DecimalNumber = sentinel,
                 price: PriceValue = sentinel,
                 id: TransactionID = sentinel,
                 time: DateTime = sentinel, user_id: int = sentinel, account_id: AccountID = sentinel,
                 batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 time_in_force: TimeInForce = 'GTC',
                 gtd_time: DateTime = sentinel, position_fill: OrderPositionFill = 'DEFAULT',
                 trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: LimitOrderReason = sentinel,
                 client_extensions: ClientExtensions = sentinel, take_profit_on_fill: TakeProfitDetails = sentinel,
                 stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel, intended_replaces_order_id: OrderID = sentinel,
                 reject_reason: TransactionRejectReason = sentinel):
        Model.__init__(**locals())


class StopOrderRejectTransaction(Transaction, type=TransactionType('STOP_ORDER_REJECT')):
    """A StopOrderRejectTransaction represents the rejection of the creation of a
    Stop Order.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The Stop Order's Instrument.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the Stop Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: :class:`~async_v20.PriceValue`
            The price threshold specified for the Stop Order. The Stop Order will only be
            filled by a market price that is equal to or worse than this price.
        id: :class:`~async_v20.TransactionID`
            The Transaction's Identifier.
        time: :class:`~async_v20.DateTime`
            The date/time when the Transaction was created.
        user_id: :class:`int`
            The ID of the user that initiated the creation of the Transaction.
        account_id: :class:`~async_v20.AccountID`
            The ID of the Account the Transaction was created for.
        batch_id: :class:`~async_v20.TransactionID`
            The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: :class:`~async_v20.RequestID`
            The Request ID of the request which generated the transaction.
        price_bound: :class:`~async_v20.PriceValue`
            The worst market price that may be used to fill this Stop Order. If the market gaps and
            crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the Stop Order.
        gtd_time: :class:`~async_v20.DateTime`
            The date/time when the Stop Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: :class:`~async_v20.OrderTriggerCondition`
            Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: :class:`~async_v20.StopOrderReason`
            The reason that the Stop Order was initiated
        client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        intended_replaces_order_id: :class:`~async_v20.OrderID`
            The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        reject_reason: :class:`~async_v20.TransactionRejectReason`
            The reason that the Reject Transaction was created

    """

    def __init__(self, instrument: InstrumentName = sentinel, units: DecimalNumber = sentinel,
                 price: PriceValue = sentinel,
                 id: TransactionID = sentinel,
                 time: DateTime = sentinel, user_id: int = sentinel, account_id: AccountID = sentinel,
                 batch_id: TransactionID = sentinel, request_id: RequestID = sentinel,
                 price_bound: PriceValue = sentinel,
                 time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = sentinel,
                 position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                 reason: StopOrderReason = sentinel, client_extensions: ClientExtensions = sentinel,
                 take_profit_on_fill: TakeProfitDetails = sentinel, stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel, intended_replaces_order_id: OrderID = sentinel,
                 reject_reason: TransactionRejectReason = sentinel):
        Model.__init__(**locals())


class MarketOrder(Order, type=OrderType('MARKET')):
    """A MarketOrder is an order that is filled immediately upon creation using
    the current market price.

    Attributes:
        instrument: :class:`~async_v20.InstrumentName`
            The Market Order's Instrument.
        units: :class:`~async_v20.DecimalNumber`
            The quantity requested to be filled by the Market Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        id: :class:`~async_v20.OrderID`
            The Order's identifier, unique within the Order's Account.
        create_time: :class:`~async_v20.DateTime`
            The time when the Order was created.
        state: :class:`~async_v20.OrderState`
            The current state of the Order.
        client_extensions: :class:`~async_v20.ClientExtensions`
            The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        time_in_force: :class:`~async_v20.TimeInForce`
            The time-in-force requested for the Market Order.
            Restricted to FOK or IOC for a MarketOrder.
        price_bound: :class:`~async_v20.PriceValue`
            The worst price that the client is willing to have the Market Order filled at.
        position_fill: :class:`~async_v20.OrderPositionFill`
            Specification of how Positions in the Account
            are modified when the Order is filled.
        trade_close: :class:`~async_v20.MarketOrderTradeClose`
            Details of the Trade requested to be closed, only provided when
            the Market Order is being used to explicitly close a Trade.
        long_position_closeout: :class:`~async_v20.MarketOrderPositionCloseout`
            Details of the long Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a long Position.
        short_position_closeout: :class:`~async_v20.MarketOrderPositionCloseout`
            Details of the short Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a short Position.
        margin_closeout: :class:`~async_v20.MarketOrderMarginCloseout`
            Details of the Margin Closeout that this Market Order was created for
        delayed_trade_close: :class:`~async_v20.MarketOrderDelayedTradeClose`
            Details of the delayed Trade close that this Market Order was created for
        take_profit_on_fill: :class:`~async_v20.TakeProfitDetails`
            TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: :class:`~async_v20.StopLossDetails`
            StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: :class:`~async_v20.TrailingStopLossDetails`
            TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: :class:`~async_v20.ClientExtensions`
            Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.
        filling_transaction_id: :class:`~async_v20.TransactionID`
            ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filled_time: :class:`~async_v20.DateTime`
            Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        trade_opened_id: :class:`~async_v20.TradeID`
            Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        trade_reduced_id: :class:`~async_v20.TradeID`
            Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        trade_closed_ids: ( :class:`~async_v20.TradeID`, ...),
            Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancelling_transaction_id: :class:`~async_v20.TransactionID`
            ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelled_time: :class:`~async_v20.DateTime`
            Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)

    """

    def __init__(self, instrument: InstrumentName, units: DecimalNumber, id: OrderID = sentinel,
                 create_time: DateTime = sentinel,
                 state: OrderState = sentinel, client_extensions: ClientExtensions = sentinel,
                 time_in_force: TimeInForce = 'FOK', price_bound: PriceValue = sentinel,
                 position_fill: OrderPositionFill = 'DEFAULT', trade_close: MarketOrderTradeClose = sentinel,
                 long_position_closeout: MarketOrderPositionCloseout = sentinel,
                 short_position_closeout: MarketOrderPositionCloseout = sentinel,
                 margin_closeout: MarketOrderMarginCloseout = sentinel,
                 delayed_trade_close: MarketOrderDelayedTradeClose = sentinel,
                 take_profit_on_fill: TakeProfitDetails = sentinel, stop_loss_on_fill: StopLossDetails = sentinel,
                 trailing_stop_loss_on_fill: TrailingStopLossDetails = sentinel,
                 trade_client_extensions: ClientExtensions = sentinel, filling_transaction_id: TransactionID = sentinel,
                 filled_time: DateTime = sentinel, trade_opened_id: TradeID = sentinel,
                 trade_reduced_id: TradeID = sentinel,
                 trade_closed_ids: ArrayTradeID = sentinel, cancelling_transaction_id: TransactionID = sentinel,
                 cancelled_time: DateTime = sentinel):
        Model.__init__(**locals())
