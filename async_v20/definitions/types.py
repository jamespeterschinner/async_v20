from .base import *
from .primitives import *

__all__ = ['OrderRequest', 'UnitsAvailableDetails',
           'UnitsAvailable', 'LiquidityRegenerationScheduleStep',
           'LiquidityRegenerationSchedule', 'CandlestickData', 'OrderIdentifier', 'QuoteHomeConversionFactors',
           'MarketOrderMarginCloseout', 'InstrumentCommission', 'OrderBookBucket', 'PositionBookBucket',
           'DynamicOrderState', 'CalculatedPositionState', 'PositionSide', 'Position', 'PriceBucket', 'ClientPrice',
           'PricingHeartbeat', 'CalculatedTradeState', 'MarketOrderDelayedTradeClose', 'MarketOrderPositionCloseout',
           'MarketOrderTradeClose', 'OpenTradeFinancing', 'PositionFinancing', 'ClientExtensions', 'TradeOpen',
           'VWAPReceipt', 'UserInfo', 'AccountProperties', 'Candlestick', 'OrderBook', 'PositionBook', 'Order',
           'StopLossDetails', 'TakeProfitDetails', 'TradeReduce', 'TrailingStopLossDetails', 'TransactionHeartbeat',
           'UserInfoExternal', 'TradeSummary', 'Transaction', 'AccountChanges', 'Instrument', 'CurrencyInstrument',
           'CFDInstrument', 'MetalInstrument', 'AccountChangesState',
           'Price', 'CloseTransaction', 'MarginCallEnterTransaction', 'MarginCallExitTransaction',
           'MarginCallExtendTransaction', 'ReopenTransaction', 'ResetResettablePLTransaction', 'StopLossOrderRequest',
           'TakeProfitOrderRequest', 'TrailingStopLossOrderRequest', 'CreateTransaction', 'ClientConfigureTransaction',
           'DelayedTradeClosureTransaction', 'OrderCancelTransaction', 'OrderClientExtensionsModifyTransaction',
           'DailyFinancingTransaction', 'TradeClientExtensionsModifyTransaction', 'AccountSummary',
           'MarketOrderRequest', 'TakeProfitOrderTransaction', 'TakeProfitOrder', 'StopLossOrder',
           'TrailingStopLossOrder', 'Trade', 'ClientConfigureRejectTransaction', 'OrderCancelRejectTransaction',
           'OrderClientExtensionsModifyRejectTransaction', 'TradeClientExtensionsModifyRejectTransaction',
           'TransferFundsTransaction', 'TransferFundsRejectTransaction', 'LimitOrderRequest',
           'MarketIfTouchedOrderRequest', 'StopOrderRequest', 'Account', 'MarketOrderTransaction',
           'MarketOrderRejectTransaction', 'StopLossOrderTransaction', 'TrailingStopLossOrderTransaction', 'LimitOrder',
           'MarketIfTouchedOrder', 'StopOrder', 'OrderFillTransaction', 'StopLossOrderRejectTransaction',
           'MarketIfTouchedOrderTransaction', 'LimitOrderTransaction', 'TakeProfitOrderRejectTransaction',
           'TrailingStopLossOrderRejectTransaction', 'StopOrderTransaction', 'MarketIfTouchedOrderRejectTransaction',
           'LimitOrderRejectTransaction', 'StopOrderRejectTransaction', 'MarketOrder']


class ClientExtensions(Model):
    """ClientExtensions(self, id: ClientID=None, tag: ClientTag=None, comment: ClientComment=None)
A ClientExtensions object allows a client to attach a clientID, tag and
    comment to Orders and Trades in their Account.  Do not set, modify, or
    delete this field if your account is associated with MT4.

    Attributes:
        id: -- The Client ID of the Order/Trade
        tag: -- A tag associated with the Order/Trade
        comment: -- A comment associated with the Order/Trade

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, id: ClientID = None, tag: ClientTag = None, comment: ClientComment = None):
        return Model.__new__(**locals())


class TakeProfitDetails(Model):
    """TakeProfitDetails(self, price: PriceValue=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, client_extensions: ClientExtensions=None)
TakeProfitDetails specifies the details of a Take Profit Order to be
    created on behalf of a client. This may happen when an Order is filled that
    opens a Trade requiring a Take Profit, or when a Trade's dependent Take
    Profit Order is modified directly through the Trade.

    Attributes:
        price: -- The price that the Take Profit Order will be triggered at.
        time_in_force: -- The time in force for the created Take Profit
            Order. This may only be GTC, GTD or GFD.
        gtd_time: -- The date when the Take Profit Order will be cancelled on if timeInForce is GTD.
        client_extensions: -- The Client Extensions to add to the Take Profit Order when created.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, price: PriceValue = None, time_in_force: TimeInForce = None, gtd_time: DateTime = None,
                client_extensions: ClientExtensions = None):
        return Model.__new__(**locals())


class StopLossDetails(Model):
    """StopLossDetails(self, price: PriceValue=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, client_extensions: ClientExtensions=None)
StopLossDetails specifies the details of a Stop Loss Order to be created on
    behalf of a client. This may happen when an Order is filled that opens a
    Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is
    modified directly through the Trade.

    Attributes:
        price: -- The price that the Stop Loss Order will be triggered at.
        time_in_force: -- The time in force for the created Stop Loss
            Order. This may only be GTC, GTD or GFD.
        gtd_time: -- The date when the Stop Loss Order will be cancelled on if timeInForce is GTD.
        client_extensions: -- The Client Extensions to add to the Stop Loss Order when created.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, price: PriceValue = None, time_in_force: TimeInForce = None, gtd_time: DateTime = None,
                client_extensions: ClientExtensions = None):
        return Model.__new__(**locals())


class TrailingStopLossDetails(Model):
    """TrailingStopLossDetails(self, distance: PriceValue=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, client_extensions: ClientExtensions=None)
TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order
    to be created on behalf of a client. This may happen when an Order is
    filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's
    dependent Trailing Stop Loss Order is modified directly through the Trade.

    Attributes:
        distance: -- The distance (in price units) from the Trade's fill price
            that the Trailing Stop Loss Order will be triggered at.
        time_in_force: -- The time in force for the created Trailing Stop
            Loss Order. This may only be GTC, GTD or GFD.
        gtd_time: -- The date when the Trailing Stop Loss Order
            will be cancelled on if timeInForce is GTD.
        client_extensions: -- The Client Extensions to add to the Trailing Stop Loss Order when created.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, distance: PriceValue = None, time_in_force: TimeInForce = None, gtd_time: DateTime = None,
                client_extensions: ClientExtensions = None):
        return Model.__new__(**locals())


class OrderRequest(Model):
    """OrderRequest(self)

    The base Order specification used when requesting that an Order be created.
    Each specific Order-type extends this definition.

    Attributes:

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, trade_id: TradeID = None, price: PriceValue = None, type: OrderType = None,
                client_trade_id: ClientID = None, time_in_force: TimeInForce = None, gtd_time: DateTime = None,
                trigger_condition: OrderTriggerCondition = None, client_extensions: ClientExtensions = None,
                distance: PriceValue = None, instrument: InstrumentName = None, units: Unit = None,
                price_bound: PriceValue = None, position_fill: OrderPositionFill = None,
                take_profit_on_fill: TakeProfitDetails = None, stop_loss_on_fill: StopLossDetails = None,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None):
        return Model.__new__(**locals())


class UnitsAvailableDetails(Model):
    """UnitsAvailableDetails(self, long: Unit=None, short: Unit=None)

    Representation of many units of an Instrument are available to be traded
    for both long and short Orders.

    Attributes:
        long: -- The units available for long Orders.
        short: -- The units available for short Orders.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, long: Unit = None, short: Unit = None):
        return Model.__new__(**locals())


class UnitsAvailable(Model):
    """UnitsAvailable(self, default: UnitsAvailableDetails=None, reduce_first: UnitsAvailableDetails=None, reduce_only: UnitsAvailableDetails=None, open_only: UnitsAvailableDetails=None)

    Representation of how many units of an Instrument are available to be
    traded by an Order depending on its position Fill option.

    Attributes:
        default: -- The number of units that are available to be traded using an Order with a positionFill option of
            "DEFAULT". For an Account with hedging enabled,
            this value will be the same as the "OPEN_ONLY" value. For an Account without hedging enabled,
            this value will be the same as the "REDUCE_FIRST" value.
        reduce_first: -- The number of units that may are available to be
            traded with an Order with a positionFill option of "REDUCE_FIRST".
        reduce_only: -- The number of units that may are available to be
            traded with an Order with a positionFill option of "REDUCE_ONLY".
        open_only: -- The number of units that may are available to be
            traded with an Order with a positionFill option of "OPEN_ONLY".

        """

    _summary_format = ''

    _name_format = ''

    def __new__(self, default: UnitsAvailableDetails = None, reduce_first: UnitsAvailableDetails = None,
                reduce_only: UnitsAvailableDetails = None, open_only: UnitsAvailableDetails = None):
        return Model.__new__(**locals())


class LiquidityRegenerationScheduleStep(Model):
    """LiquidityRegenerationScheduleStep(self, timestamp: DateTime=None, bid_liquidity_used: DecimalNumber=None, ask_liquidity_used: DecimalNumber=None)

    A liquidity regeneration schedule Step indicates the amount of bid and ask
    liquidity that is used by the Account at a certain time. These amounts will
    only change at the timestamp of the following step.

    Attributes:
        timestamp: -- The timestamp of the schedule step.
        bid_liquidity_used: -- The amount of bid liquidity used at this step in the schedule.
        ask_liquidity_used: -- The amount of ask liquidity used at this step in the schedule.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, timestamp: DateTime = None, bid_liquidity_used: DecimalNumber = None,
                ask_liquidity_used: DecimalNumber = None):
        return Model.__new__(**locals())


class LiquidityRegenerationSchedule(Model):
    """LiquidityRegenerationSchedule(self, steps: Array_LiquidityRegenerationScheduleStep=None)

    A LiquidityRegenerationSchedule indicates how liquidity that is used when
    filling an Order for an instrument is regenerated following the fill.  A
    liquidity regeneration schedule will be in effect until the timestamp of
    its final step, but may be replaced by a schedule created for an Order of
    the same instrument that is filled while it is still in effect.

    Attributes:
        steps: -- The steps in the Liquidity Regeneration Schedule

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, steps: Array(LiquidityRegenerationScheduleStep) = None):
        return Model.__new__(**locals())


class CandlestickData(Model):
    """CandlestickData(self, o: PriceValue=None, h: PriceValue=None, l: PriceValue=None, c: PriceValue=None)

    The price data (open, high, low, close) for the Candlestick representation.

    Attributes:
        o: -- The first (open) price in the time-range represented by the candlestick.
        h: -- The highest price in the time-range represented by the candlestick.
        l: -- The lowest price in the time-range represented by the candlestick.
        c: -- The last (closing) price in the time-range represented by the candlestick.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, o: PriceValue = None, h: PriceValue = None, l: PriceValue = None, c: PriceValue = None):
        return Model.__new__(**locals())


class OrderIdentifier(Model):
    """OrderIdentifier(self, order_id: OrderID=None, client_order_id: ClientID=None)
An OrderIdentifier is used to refer to an Order, and contains both the
    OrderID and the ClientOrderID.

    Attributes:
        order_id: -- The OANDA-assigned Order ID
        client_order_id: -- The client-provided client Order ID

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, order_id: OrderID = None, client_order_id: ClientID = None):
        return Model.__new__(**locals())


class QuoteHomeConversionFactors(Model):
    """QuoteHomeConversionFactors(self, positive_units: DecimalNumber=None, negative_units: DecimalNumber=None)
QuoteHomeConversionFactors represents the factors that can be used used to
    convert quantities of a Price's Instrument's quote currency into the
    Account's home currency.

    Attributes:
        positive_units: -- The factor used to convert a positive amount of the
            Price's Instrument's quote currency into a positive
            amount of the Account's home currency. Conversion is performed by multiplying
            the quote units by the conversion factor.
        negative_units: -- The factor used to convert a negative amount of the Price's Instrument's
            quote currency into a negative amount of the Account's home currency. Conversion is performed by
            multiplying the quote units by the conversion factor.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, positive_units: DecimalNumber = None, negative_units: DecimalNumber = None):
        return Model.__new__(**locals())


class MarketOrderMarginCloseout(Model):
    """MarketOrderMarginCloseout(self, reason: MarketOrderMarginCloseoutReason=None)
Details for the Market Order extensions specific to a Market Order placed
    that is part of a Market Order Margin Closeout in a client's account

    Attributes:
        reason: -- The reason the Market Order was created to perform a margin closeout

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, reason: MarketOrderMarginCloseoutReason = None):
        return Model.__new__(**locals())


class InstrumentCommission(Model):
    """InstrumentCommission(self, instrument: InstrumentName=None, commission: DecimalNumber=None, units_traded: Unit=None, minimum_commission: DecimalNumber=None)
An InstrumentCommission represents an instrument-specific commission

    Attributes:
        instrument: -- The name of the instrument
        commission: -- The commission amount (in the Account's home
            currency) charged per unitsTraded of the instrument
        units_traded: -- The number of units traded that the commission amount is based on.
        minimum_commission: -- The minimum commission amount (in the Account's home currency) that
            is charged when an Order is filled for this instrument.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, instrument: InstrumentName = None, commission: DecimalNumber = None, units_traded: Unit = None,
                minimum_commission: DecimalNumber = None):
        return Model.__new__(**locals())


class OrderBookBucket(Model):
    """OrderBookBucket(self, price: PriceValue=None, long_count_percent: DecimalNumber=None, short_count_percent: DecimalNumber=None)
The order book data for a partition of the instrument's prices.

    Attributes:
        price: -- The lowest price (inclusive) covered by the bucket. The bucket covers the
            price range from the price to price + the order book's bucketWidth.
        long_count_percent: -- The percentage of the total number of orders
            represented by the long orders found in this bucket.
        short_count_percent: -- The percentage of the total number of orders
            represented by the short orders found in this bucket.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, price: PriceValue = None, long_count_percent: DecimalNumber = None,
                short_count_percent: DecimalNumber = None):
        return Model.__new__(**locals())


class PositionBookBucket(Model):
    """PositionBookBucket(self, price: PriceValue=None, long_count_percent: DecimalNumber=None, short_count_percent: DecimalNumber=None)
The position book data for a partition of the instrument's prices.

    Attributes:
        price: -- The lowest price (inclusive) covered by the bucket. The bucket covers the
            price range from the price to price + the position book's bucketWidth.
        long_count_percent: -- The percentage of the total number of positions
            represented by the long positions found in this bucket.
        short_count_percent: -- The percentage of the total number of positions
            represented by the short positions found in this bucket.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, price: PriceValue = None, long_count_percent: DecimalNumber = None,
                short_count_percent: DecimalNumber = None):
        return Model.__new__(**locals())


class DynamicOrderState(Model):
    """DynamicOrderState(self, id: OrderID=None, trailing_stop_value: PriceValue=None, trigger_distance: PriceValue=None, is_trigger_distance_exact: bool=None)
The dynamic state of an Order. This is only relevant to TrailingStopLoss
    Orders, as no other Order type has dynamic state.

    Attributes:
        id: -- The Order's ID.
        trailing_stop_value: -- The Order's calculated trailing stop value.
        trigger_distance: -- The distance between the Trailing Stop Loss Order's trailingStopValue and the current
            Market Price. This represents the distance (in price
            units) of the Order from a triggering price. If the distance could not be determined,
            this value will not be set.
        is_trigger_distance_exact: -- True if an exact trigger distance could be calculated. If false,
            it means the provided trigger distance
            is a best estimate. If the distance could not be determined, this value will not be set.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, id: OrderID = None, trailing_stop_value: PriceValue = None, trigger_distance: PriceValue = None,
                is_trigger_distance_exact: bool = None):
        return Model.__new__(**locals())


class CalculatedPositionState(Model):
    """CalculatedPositionState(self, instrument: InstrumentName=None, net_unrealized_pl: AccountUnits=None, long_unrealized_pl: AccountUnits=None, short_unrealized_pl: AccountUnits=None)
The dynamic (calculated) state of a Position

    Attributes:
        instrument: -- The Position's Instrument.
        net_unrealized_pl: -- The Position's net unrealized profit/loss
        long_unrealized_pl: -- The unrealized profit/loss of the Position's long open Trades
        short_unrealized_pl: -- The unrealized profit/loss of the Position's short open Trades

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, instrument: InstrumentName = None, net_unrealized_pl: AccountUnits = None,
                long_unrealized_pl: AccountUnits = None, short_unrealized_pl: AccountUnits = None):
        return Model.__new__(**locals())


class PositionSide(Model):
    """PositionSide(self, units: Unit=None, average_price: PriceValue=None, trade_i_ds: Array_TradeID=None, pl: AccountUnits=None, unrealized_pl: AccountUnits=None, resettable_pl: AccountUnits=None, financing: DecimalNumber=None)
The representation of a Position for a single direction (long or short).

    Attributes:
        units: -- Number of units in the position (negative
            value indicates short position, positive indicates long position).
        average_price: -- Volume-weighted average of the underlying Trade open prices for the Position.
        trade_i_ds: -- List of the open Trade IDs which contribute to the open Position.
        pl: -- Profit/loss realized by the PositionSide over the lifetime of the Account.
        unrealized_pl: -- The unrealized profit/loss of all open
            Trades that contribute to this PositionSide.
        resettable_pl: -- Profit/loss realized by the PositionSide since the
            Account's resettablePL was last reset by the client.

    """

    _summary_format = '{units} @ {averagePrice}, {pl} PL {unrealizedPL} UPL'

    _name_format = ''

    def __new__(self, units: Unit = None, average_price: PriceValue = None, trade_i_ds: Array(TradeID) = None,
                pl: AccountUnits = None, unrealized_pl: AccountUnits = None, resettable_pl: AccountUnits = None,
                financing: DecimalNumber = None):
        return Model.__new__(**locals())


class Position(Model):
    """Position(self, instrument: InstrumentName=None, pl: AccountUnits=None, unrealized_pl: AccountUnits=None, resettable_pl: AccountUnits=None, commission: AccountUnits=None, long: PositionSide=None, short: PositionSide=None, financing: DecimalNumber=None)
The specification of a Position within an Account.

    Attributes:
        instrument: -- The Position's Instrument.
        pl: -- Profit/loss realized by the Position over the lifetime of the Account.
        unrealized_pl: -- The unrealized profit/loss of all open Trades that contribute to this Position.
        resettable_pl: -- Profit/loss realized by the Position since the
            Account's resettablePL was last reset by the client.
        commission: -- The total amount of commission paid for this instrument over
            the lifetime of the Account. Represented in the Account's home currency.
        long: -- The details of the long side of the Position.
        short: -- The details of the short side of the Position.

    """

    _summary_format = '{instrument}, {pl} PL {unrealizedPL} UPL'

    _name_format = '{instrument}, {pl} PL {unrealizedPL} UPL'

    def __new__(self, instrument: InstrumentName = None, pl: AccountUnits = None, unrealized_pl: AccountUnits = None,
                resettable_pl: AccountUnits = None, commission: AccountUnits = None, long: PositionSide = None,
                short: PositionSide = None, financing: DecimalNumber = None):
        return Model.__new__(**locals())


class PriceBucket(Model):
    """PriceBucket(self, price: PriceValue=None, liquidity: int=None)
A Price Bucket represents a price available for an amount of liquidity

    Attributes:
        price: -- The Price offered by the PriceBucket
        liquidity: -- The amount of liquidity offered by the PriceBucket

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, price: PriceValue = None, liquidity: int = None):
        return Model.__new__(**locals())


class ClientPrice(Model):
    """ClientPrice(self, bids: Array_PriceBucket=None, asks: Array_PriceBucket=None, closeout_bid: PriceValue=None, closeout_ask: PriceValue=None, timestamp: DateTime=None)
Client price for an Account.

    Attributes:
        bids: -- The list of prices and liquidity available on the Instrument's bid side. It is possible for this
            list to be empty if there is no bid liquidity currently available for the Instrument in the Account.
        asks: -- The list of prices and liquidity available on the Instrument's ask side. It is possible for this
            list to be empty if there is no ask liquidity currently available for the Instrument in the Account.
        closeout_bid: -- The closeout bid Price. This Price is used when a bid is required to closeout a Position
            (margin closeout
            or manual) yet there is no bid liquidity. The closeout bid is never used to open a new position.
        closeout_ask: -- The closeout ask Price. This Price is used when a ask is required to closeout a Position
            (margin closeout
            or manual) yet there is no ask liquidity. The closeout ask is never used to open a new position.
        timestamp: -- The date/time when the Price was created.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, bids: Array(PriceBucket) = None, asks: Array(PriceBucket) = None,
                closeout_bid: PriceValue = None, closeout_ask: PriceValue = None, timestamp: DateTime = None):
        return Model.__new__(**locals())


class PricingHeartbeat(Model):
    """PricingHeartbeat(self, type: str=HEARTBEAT, time: DateTime=None)
A PricingHeartbeat object is injected into the Pricing stream to ensure
    that the HTTP connection remains active.

    Attributes:
        type: -- The string "HEARTBEAT"
        time: -- The date/time when the Heartbeat was created.

    """

    _summary_format = 'Pricing Heartbeat {time}'

    _name_format = ''

    def __new__(self, type: str = None, time: DateTime = None):
        return Model.__new__(**locals())


class CalculatedTradeState(Model):
    """CalculatedTradeState(self, id: TradeID=None, unrealized_pl: AccountUnits=None)
The dynamic (calculated) state of an open Trade

    Attributes:
        id: -- The Trade's ID.
        unrealized_pl: -- The Trade's unrealized profit/loss.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, id: TradeID = None, unrealized_pl: AccountUnits = None):
        return Model.__new__(**locals())


class MarketOrderDelayedTradeClose(Model):
    """MarketOrderDelayedTradeClose(self, trade_id: TradeID=None, client_trade_id: TradeID=None, source_transaction_id: TransactionID=None)
Details for the Market Order extensions specific to a Market Order placed
    with the intent of fully closing a specific open trade that should have
    already been closed but wasn't due to halted market conditions

    Attributes:
        trade_id: -- The ID of the Trade being closed
        client_trade_id: -- The Client ID of the Trade being closed
        source_transaction_id: -- The Transaction ID of the DelayedTradeClosure transaction
            to which this Delayed Trade Close belongs to

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, trade_id: TradeID = None, client_trade_id: TradeID = None,
                source_transaction_id: TransactionID = None):
        return Model.__new__(**locals())


class MarketOrderPositionCloseout(Model):
    """MarketOrderPositionCloseout(self, instrument: InstrumentName=None, units: str=None)
A MarketOrderPositionCloseout specifies the extensions to a Market Order
    when it has been created to closeout a specific Position.

    Attributes:
        instrument: -- The instrument of the Position being closed out.
        units: -- Indication of how much of the Position to close. Either "ALL", or a DecimalNumber reflection a
            partial close of the Trade. The DecimalNumber must always be positive, and represent a number that doesn't exceed the absolute
            size of the Position.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, instrument: InstrumentName = None, units: str = None):
        return Model.__new__(**locals())


class MarketOrderTradeClose(Model):
    """MarketOrderTradeClose(self, trade_id: TradeID=None, client_trade_id: str=None, units: str=None)
A MarketOrderTradeClose specifies the extensions to a Market Order that has
    been created specifically to close a Trade.

    Attributes:
        trade_id: -- The ID of the Trade requested to be closed
        client_trade_id: -- The client ID of the Trade requested to be closed
        units: -- Indication of how much of the Trade to close. Either
            "ALL", or a DecimalNumber reflection a partial close of the Trade.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, trade_id: TradeID = None, client_trade_id: str = None, units: str = None):
        return Model.__new__(**locals())


class OpenTradeFinancing(Model):
    """OpenTradeFinancing(self, trade_id: TradeID=None, financing: AccountUnits=None)
OpenTradeFinancing is used to pay/collect daily financing charge for an
    open Trade within an Account

    Attributes:
        trade_id: -- The ID of the Trade that financing is being paid/collected for.
        financing: -- The amount of financing paid/collected for the Trade.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, trade_id: TradeID = None, financing: AccountUnits = None):
        return Model.__new__(**locals())


class PositionFinancing(Model):
    """PositionFinancing(self, instrument: InstrumentName=None, financing: AccountUnits=None, open_trade_financings: Array_OpenTradeFinancing=None)
OpenTradeFinancing is used to pay/collect daily financing charge for a
    Position within an Account

    Attributes:
        instrument: -- The instrument of the Position that financing is being paid/collected for.
        financing: -- The amount of financing paid/collected for the Position.
        open_trade_financings: -- The financing paid/collecte for each open Trade within the Position.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, instrument: InstrumentName = None, financing: AccountUnits = None,
                open_trade_financings: Array(OpenTradeFinancing) = None):
        return Model.__new__(**locals())


class TradeOpen(Model):
    """TradeOpen(self, trade_id: TradeID=None, units: Unit=None, client_extensions: ClientExtensions=None)
A TradeOpen object represents a Trade for an instrument that was opened in
    an Account. It is found embedded in Transactions that affect the position
    of an instrument in the Account, specifically the OrderFill Transaction.

    Attributes:
        trade_id: -- The ID of the Trade that was opened
        units: -- The number of units opened by the Trade
        client_extensions: -- The client extensions for the newly opened Trade

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, trade_id: TradeID = None, units: Unit = None, client_extensions: ClientExtensions = None):
        return Model.__new__(**locals())


class VWAPReceipt(Model):
    """VWAPReceipt(self, units: Unit=None, price: PriceValue=None)
A VWAP Receipt provides a record of how the price for an Order fill is
    constructed. If the Order is filled with multiple buckets in a depth of
    market, each bucket will be represented with a VWAP Receipt.

    Attributes:
        units: -- The number of units filled
        price: -- The price at which the units were filled

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, units: Unit = None, price: PriceValue = None):
        return Model.__new__(**locals())


class UserInfo(Model):
    """UserInfo(self)
A representation of user information, as provided to the user themself.

    Attributes:
        username: -- The user-provided username.
        user_id: -- The user's OANDA-assigned user ID.
        country: -- The country that the user is based in.
        email_address: -- The user's email address.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, ):
        return Model.__new__(**locals())


class AccountProperties(Model):
    """AccountProperties(self, id: AccountID=None, mt4_account_id: int=None, tags: Array_str=None)
Properties related to an Account.

    Attributes:
        id: -- The Account's identifier
        mt4account_id: -- The Account's associated MT4 Account ID. This field will not
            be present if the Account is not an MT4 account.
        tags: -- The Account's tags

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, id: AccountID = None, mt4_account_id: int = None, tags: Array(str) = None):
        return Model.__new__(**locals())


class Candlestick(Model):
    """Candlestick(self, time: DateTime=None, bid: CandlestickData=None, ask: CandlestickData=None, mid: CandlestickData=None, volume: int=None, complete: bool=None)
The Candlestick representation

    Attributes:
        time: -- The start time of the candlestick
        bid: -- The candlestick data based on bids.
            Only provided if bid-based candles were requested.
        ask: -- The candlestick data based on asks.
            Only provided if ask-based candles were requested.
        mid: -- The candlestick data based on midpoints.
            Only provided if midpoint-based candles were requested.
        volume: -- The number of prices created during
            the time-range represented by the candlestick.
        complete: -- A flag indicating if the candlestick is complete. A complete
            candlestick is one whose ending time is not in the future.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, time: DateTime = None, bid: CandlestickData = None, ask: CandlestickData = None,
                mid: CandlestickData = None, volume: int = None, complete: bool = None):
        return Model.__new__(**locals())


class OrderBook(Model):
    """OrderBook(self, instrument: InstrumentName=None, time: DateTime=None, price: PriceValue=None, bucket_width: PriceValue=None, buckets: Array_OrderBookBucket=None)
The representation of an instrument's order book at a point in time

    Attributes:
        instrument: -- The order book's instrument
        time: -- The time when the order book snapshot was created.
        price: -- The price (midpoint) for the order book's instrument
            at the time of the order book snapshot
        bucket_width: -- The price width for each bucket. Each bucket covers the price
            range from the bucket's price to the bucket's price + bucketWidth.
        buckets: -- The partitioned order book, divided into buckets using a default bucket width. These
            buckets are only provided for price ranges which actually contain order or position data.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, instrument: InstrumentName = None, time: DateTime = None, price: PriceValue = None,
                bucket_width: PriceValue = None, buckets: Array(OrderBookBucket) = None):
        return Model.__new__(**locals())


class PositionBook(Model):
    """PositionBook(self, instrument: InstrumentName=None, time: DateTime=None, price: PriceValue=None, bucket_width: PriceValue=None, buckets: Array_PositionBookBucket=None)
The representation of an instrument's position book at a point in time

    Attributes:
        instrument: -- The position book's instrument
        time: -- The time when the position book snapshot was created
        price: -- The price (midpoint) for the position book's instrument
            at the time of the position book snapshot
        bucket_width: -- The price width for each bucket. Each bucket covers the price
            range from the bucket's price to the bucket's price + bucketWidth.
        buckets: -- The partitioned position book, divided into buckets using a default bucket width. These
            buckets are only provided for price ranges which actually contain order or position data.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, instrument: InstrumentName = None, time: DateTime = None, price: PriceValue = None,
                bucket_width: PriceValue = None, buckets: Array(PositionBookBucket) = None):
        return Model.__new__(**locals())


class Order(Model):
    """Order(self, id: OrderID=None, create_time: DateTime=None, state: OrderState=None, client_extensions: ClientExtensions=None)
The base Order definition specifies the properties that are common to all
    Orders.

    Attributes:
        id: -- The Order's identifier, unique within the Order's Account.
        create_time: -- The time when the Order was created.
        state: -- The current state of the Order.
        client_extensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, id: OrderID = None, create_time: DateTime = None, state: OrderState = None,
                client_extensions: ClientExtensions = None, trade_id: TradeID = None, price: PriceValue = None,
                type: OrderType = None, client_trade_id: ClientID = None, time_in_force: TimeInForce = None,
                gtd_time: DateTime = None, trigger_condition: OrderTriggerCondition = None,
                filling_transaction_id: TransactionID = None, filled_time: DateTime = None,
                trade_opened_id: TradeID = None, trade_reduced_id: TradeID = None,
                trade_closed_i_ds: Array(TradeID) = None, cancelling_transaction_id: TransactionID = None,
                cancelled_time: DateTime = None, replaces_order_id: OrderID = None,
                replaced_by_order_id: OrderID = None, distance: PriceValue = None,
                trailing_stop_value: PriceValue = None, instrument: InstrumentName = None, units: Unit = None,
                position_fill: OrderPositionFill = None, take_profit_on_fill: TakeProfitDetails = None,
                stop_loss_on_fill: StopLossDetails = None, trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None, price_bound: PriceValue = None,
                initial_market_price: PriceValue = None, trade_close: MarketOrderTradeClose = None,
                long_position_closeout: MarketOrderPositionCloseout = None,
                short_position_closeout: MarketOrderPositionCloseout = None,
                margin_closeout: MarketOrderMarginCloseout = None,
                delayed_trade_close: MarketOrderDelayedTradeClose = None):
        return Model.__new__(**locals())


class TradeReduce(Model):
    """TradeReduce(self, trade_id: TradeID=None, units: Unit=None, realized_pl: AccountUnits=None, financing: AccountUnits=None)
A TradeReduce object represents a Trade for an instrument that was reduced
    (either partially or fully) in an Account. It is found embedded in
    Transactions that affect the position of an instrument in the account,
    specifically the OrderFill Transaction.

    Attributes:
        trade_id: -- The ID of the Trade that was reduced or closed
        units: -- The number of units that the Trade was reduced by
        realized_pl: -- The PL realized when reducing the Trade
        financing: -- The financing paid/collected when reducing the Trade

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, trade_id: TradeID = None, units: Unit = None, realized_pl: AccountUnits = None,
                financing: AccountUnits = None):
        return Model.__new__(**locals())


class TransactionHeartbeat(Model):
    """TransactionHeartbeat(self, type: str=HEARTBEAT, last_transaction_id: TransactionID=None, time: DateTime=None)
A TransactionHeartbeat object is injected into the Transaction stream to
    ensure that the HTTP connection remains active.

    Attributes:
        type: -- The string "HEARTBEAT"
        last_transaction_id: -- The ID of the most recent Transaction created for the Account
        time: -- The date/time when the TransactionHeartbeat was created.

    """

    _summary_format = 'Transaction Heartbeat {time}'

    _name_format = ''

    def __new__(self, type: str = None, last_transaction_id: TransactionID = None, time: DateTime = None):
        return Model.__new__(**locals())


class UserInfoExternal(Model):
    """UserInfoExternal(self)
A representation of user information, as available to external (3rd party)
    clients.

    Attributes:
        user_id: -- The user's OANDA-assigned user ID.
        country: -- The country that the user is based in.
        fifo: -- Flag indicating if the the user's Accounts adhere to FIFO execution rules.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, ):
        return Model.__new__(**locals())


class TradeSummary(Model):
    """TradeSummary(self, id: TradeID=None, instrument: InstrumentName=None, price: PriceValue=None, open_time: DateTime=None, state: TradeState=None, initial_units: Unit=None, current_units: Unit=None, realized_pl: AccountUnits=None, unrealized_pl: AccountUnits=None, average_close_price: PriceValue=None, closing_transaction_i_ds: Array_TransactionID=None, financing: AccountUnits=None, close_time: DateTime=None, client_extensions: ClientExtensions=None, take_profit_order_id: OrderID=None, stop_loss_order_id: OrderID=None, trailing_stop_loss_order_id: OrderID=None)
The summary of a Trade within an Account. This representation does not
    provide the full details of the Trade's dependent Orders.

    Attributes:
        id: -- The Trade's identifier, unique within the Trade's Account.
        instrument: -- The Trade's Instrument.
        price: -- The execution price of the Trade.
        open_time: -- The date/time when the Trade was opened.
        state: -- The current state of the Trade.
        initial_units: -- The initial size of the Trade. Negative values indicate
            a short Trade, and positive values indicate a long Trade.
        current_units: -- The number of units currently open for the Trade. This
            value is reduced to 0.0 as the Trade is closed.
        realized_pl: -- The total profit/loss realized on the closed portion of the Trade.
        unrealized_pl: -- The unrealized profit/loss on the open portion of the Trade.
        average_close_price: -- The average closing price of the Trade. Only present if
            the Trade has been closed or reduced at least once.
        closing_transaction_i_ds: -- The IDs of the Transactions that have closed portions of this Trade.
        financing: -- The financing paid/collected for this Trade.
        close_time: -- The date/time when the Trade was fully closed.
            Only provided for Trades whose state is CLOSED.
        client_extensions: -- The client extensions of the Trade.
        take_profit_order_id: -- ID of the Trade's Take Profit Order, only provided if such an Order exists.
        stop_loss_order_id: -- ID of the Trade's Stop Loss Order, only provided if such an Order exists.
        trailing_stop_loss_order_id: -- ID of the Trade's Trailing Stop Loss
            Order, only provided if such an Order exists.

    """

    _summary_format = '{currentUnits} ({initialUnits}) of {instrument} @ {price}'

    _name_format = '{currentUnits} ({initialUnits}) of {instrument} @ {price}'

    def __new__(self, id: TradeID = None, instrument: InstrumentName = None, price: PriceValue = None,
                open_time: DateTime = None, state: TradeState = None, initial_units: Unit = None,
                current_units: Unit = None, realized_pl: AccountUnits = None, unrealized_pl: AccountUnits = None,
                average_close_price: PriceValue = None, closing_transaction_i_ds: Array(TransactionID) = None,
                financing: AccountUnits = None, close_time: DateTime = None,
                client_extensions: ClientExtensions = None, take_profit_order_id: OrderID = None,
                stop_loss_order_id: OrderID = None, trailing_stop_loss_order_id: OrderID = None):
        return Model.__new__(**locals())


class Transaction(Model):
    """Transaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None)
The base Transaction specification. Specifies properties that are common
    between all Transaction.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = None, extension_number: int = None, division_id: int = None,
                site_id: int = None, account_user_id: int = None, account_number: int = None,
                home_currency: Currency = None, alias: str = None, margin_rate: DecimalNumber = None,
                reason: StopOrderReason = None, trade_i_ds: TradeID = None, order_id: OrderID = None,
                client_order_id: ClientID = None, replaced_by_order_id: OrderID = None,
                closed_trade_id: OrderID = None, trade_close_transaction_id: TransactionID = None,
                client_extensions_modify: ClientExtensions = None,
                trade_client_extensions_modify: ClientExtensions = None, financing: AccountUnits = None,
                account_balance: AccountUnits = None, account_financing_mode: AccountFinancingMode = None,
                position_financings: Array(PositionFinancing) = None, trade_id: TradeID = None,
                client_trade_id: ClientID = None, price: PriceValue = None, time_in_force: TimeInForce = None,
                gtd_time: DateTime = None, trigger_condition: OrderTriggerCondition = None,
                client_extensions: ClientExtensions = None, order_fill_transaction_id: TransactionID = None,
                replaces_order_id: OrderID = None, cancelling_transaction_id: TransactionID = None,
                reject_reason: TransactionRejectReason = None, amount: AccountUnits = None,
                funding_reason: FundingReason = None, comment: str = None, instrument: InstrumentName = None,
                units: Unit = None, price_bound: PriceValue = None, position_fill: OrderPositionFill = None,
                trade_close: MarketOrderTradeClose = None, long_position_closeout: MarketOrderPositionCloseout = None,
                short_position_closeout: MarketOrderPositionCloseout = None,
                margin_closeout: MarketOrderMarginCloseout = None,
                delayed_trade_close: MarketOrderDelayedTradeClose = None,
                take_profit_on_fill: TakeProfitDetails = None, stop_loss_on_fill: StopLossDetails = None,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None, distance: PriceValue = None,
                full_price: ClientPrice = None, pl: AccountUnits = None, commission: AccountUnits = None,
                trade_opened: TradeOpen = None, trades_closed: Array(TradeReduce) = None,
                trade_reduced: TradeReduce = None, intended_replaces_order_id: OrderID = None):
        return Model.__new__(**locals())


class AccountChanges(Model):
    """AccountChanges(self, orders_created: Array_Order=None, orders_cancelled: Array_Order=None, orders_filled: Array_Order=None, orders_triggered: Array_Order=None, trades_opened: Array_TradeSummary=None, trades_reduced: Array_TradeSummary=None, trades_closed: Array_TradeSummary=None, positions: Array_Position=None, transactions: Array_Transaction=None)
An AccountChanges Object is used to represent the changes to an Account's
    Orders, Trades and Positions since a specified Account TransactionID in the
    past.

    Attributes:
        orders_created: -- The Orders created. These Orders may have been
            filled, cancelled or triggered in the same period.
        orders_cancelled: -- The Orders cancelled.
        orders_filled: -- The Orders filled.
        orders_triggered: -- The Orders triggered.
        trades_opened: -- The Trades opened.
        trades_reduced: -- The Trades reduced.
        trades_closed: -- The Trades closed.
        positions: -- The Positions changed.
        transactions: -- The Transactions that have been generated.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, orders_created: Array(Order) = None, orders_cancelled: Array(Order) = None,
                orders_filled: Array(Order) = None, orders_triggered: Array(Order) = None,
                trades_opened: Array(TradeSummary) = None, trades_reduced: Array(TradeSummary) = None,
                trades_closed: Array(TradeSummary) = None, positions: Array(Position) = None,
                transactions: Array(Transaction) = None):
        return Model.__new__(**locals())


class Instrument(Model):
    """Instrument(self, name: InstrumentName=None, type: InstrumentType=None, display_name: str=None, pip_location: int=None, display_precision: int=None, trade_units_precision: int=None, minimum_trade_size: Unit=None, maximum_trailing_stop_distance: DecimalNumber=None, minimum_trailing_stop_distance: DecimalNumber=None, maximum_position_size: Unit=None, maximum_order_units: Unit=None, margin_rate: DecimalNumber=None, commission: InstrumentCommission=None)
Full specification of an Instrument.

    Attributes:
        name: -- The name of the Instrument
        type: -- The type of the Instrument
        display_name: -- The display name of the Instrument
        pip_location: -- The location of the "pip" for this instrument. The decimal position of the pip in this
            Instrument's price can be
            found at 10 ^ pipLocation (e.g. -4 pipLocation results in a decimal pip position of 10 ^ -4 = 0.0001).
        display_precision: -- The number of decimal places that should be used to display prices for this instrument.
            (e.g. a displayPrecision of 5 would result in a price of "1" being displayed as "1.00000")
        trade_units_precision: -- The amount of decimal places that may be provided
            when specifying the number of units traded for this instrument.
        minimum_trade_size: -- The smallest number of units allowed to be traded for this instrument.
        maximum_trailing_stop_distance: -- The maximum trailing stop distance allowed for a trailing
            stop loss created for this instrument. Specified in price units.
        minimum_trailing_stop_distance: -- The minimum trailing stop distance allowed for a trailing
            stop loss created for this instrument. Specified in price units.
        maximum_position_size: -- The maximum position size allowed for this instrument. Specified in units.
        maximum_order_units: -- The maximum units allowed for an Order
            placed for this instrument. Specified in units.
        margin_rate: -- The margin rate for this instrument.
        commission: -- The commission structure for this instrument.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, name: InstrumentName = None, type: InstrumentType = None, display_name: str = None,
                pip_location: int = None, display_precision: int = None, trade_units_precision: int = None,
                minimum_trade_size: Unit = None, maximum_trailing_stop_distance: Unit = None,
                minimum_trailing_stop_distance: Unit = None, maximum_position_size: Unit = None,
                maximum_order_units: Unit = None, margin_rate: DecimalNumber = None,
                commission: InstrumentCommission = None):
        return Model.__new__(**locals())


class CurrencyInstrument(Instrument):
    """CurrencyInstrument(self, name: InstrumentName=None, type: InstrumentType=CURRENCY, display_name: str=None, pip_location: int=None, display_precision: int=None, trade_units_precision: int=None, minimum_trade_size: Unit=None, maximum_trailing_stop_distance: DecimalNumber=None, minimum_trailing_stop_distance: DecimalNumber=None, maximum_position_size: Unit=None, maximum_order_units: Unit=None, margin_rate: DecimalNumber=None, commission: InstrumentCommission=None)
A Currency Instrument"""

    _summary_format = ''

    _name_format = ''

    def __new__(self, name: InstrumentName = None, type: InstrumentType = 'CURRENCY', display_name: str = None,
                pip_location: int = None, display_precision: int = None, trade_units_precision: int = None,
                minimum_trade_size: Unit = None, maximum_trailing_stop_distance: DecimalNumber = None,
                minimum_trailing_stop_distance: DecimalNumber = None, maximum_position_size: Unit = None,
                maximum_order_units: Unit = None, margin_rate: DecimalNumber = None,
                commission: InstrumentCommission = None):
        return Model.__new__(**locals())


class CFDInstrument(Instrument):
    """CFDInstrument(self, name: InstrumentName=None, type: InstrumentType=CFD, display_name: str=None, pip_location: int=None, display_precision: int=None, trade_units_precision: int=None, minimum_trade_size: Unit=None, maximum_trailing_stop_distance: Unit=None, minimum_trailing_stop_distance: Unit=None, maximum_position_size: Unit=None, maximum_order_units: Unit=None, margin_rate: DecimalNumber=None, commission: InstrumentCommission=None)
A Currency Instrument"""

    _summary_format = ''

    _name_format = ''

    def __new__(self, name: InstrumentName = None, type: InstrumentType = 'CFD', display_name: str = None,
                pip_location: int = None, display_precision: int = None, trade_units_precision: int = None,
                minimum_trade_size: Unit = None, maximum_trailing_stop_distance: Unit = None,
                minimum_trailing_stop_distance: Unit = None, maximum_position_size: Unit = None,
                maximum_order_units: Unit = None, margin_rate: DecimalNumber = None,
                commission: InstrumentCommission = None):
        return Model.__new__(**locals())


class MetalInstrument(Instrument):
    """MetalInstrument(self, name: InstrumentName=None, type: InstrumentType=METAL, display_name: str=None, pip_location: int=None, display_precision: int=None, trade_units_precision: int=None, minimum_trade_size: Unit=None, maximum_trailing_stop_distance: Unit=None, minimum_trailing_stop_distance: Unit=None, maximum_position_size: Unit=None, maximum_order_units: Unit=None, margin_rate: DecimalNumber=None, commission: InstrumentCommission=None)
A Currency Instrument"""

    _summary_format = ''

    _name_format = ''

    def __new__(self, name: InstrumentName = None, type: InstrumentType = 'METAL', display_name: str = None,
                pip_location: int = None, display_precision: int = None, trade_units_precision: int = None,
                minimum_trade_size: Unit = None, maximum_trailing_stop_distance: Unit = None,
                minimum_trailing_stop_distance: Unit = None, maximum_position_size: Unit = None,
                maximum_order_units: Unit = None, margin_rate: DecimalNumber = None,
                commission: InstrumentCommission = None):
        return Model.__new__(**locals())


class AccountChangesState(Model):
    """AccountChangesState(self, unrealized_pl: AccountUnits=None, nav: AccountUnits=None, margin_used: AccountUnits=None, margin_available: AccountUnits=None, position_value: AccountUnits=None, margin_closeout_unrealized_pl: AccountUnits=None, margin_closeout_nav: AccountUnits=None, margin_closeout_margin_used: AccountUnits=None, margin_closeout_percent: DecimalNumber=None, margin_closeout_position_value: DecimalNumber=None, withdrawal_limit: AccountUnits=None, margin_call_margin_used: AccountUnits=None, margin_call_percent: DecimalNumber=None, orders: Array_DynamicOrderState=None, trades: Array_CalculatedTradeState=None, positions: Array_CalculatedPositionState=None)
An AccountState Object is used to represent an Account's current price-
    dependent state. Price-dependent Account state is dependent on OANDA's
    current Prices, and includes things like unrealized PL, NAV and Trailing
    Stop Loss Order state.

    Attributes:
        unrealized_pl: -- The total unrealized profit/loss for all Trades currently open
            in the Account. Represented in the Account's home currency.
        nav: -- The net asset value of the Account. Equal to
            Account balance + unrealizedPL. Represented in the Account's home currency.
        margin_used: -- Margin currently used for the Account.
            Represented in the Account's home currency.
        margin_available: -- Margin available for Account. Represented in the Account's home currency.
        position_value: -- The value of the Account's open
            positions represented in the Account's home currency.
        margin_closeout_unrealized_pl: -- The Account's margin closeout unrealized PL.
        margin_closeout_nav: -- The Account's margin closeout NAV.
        margin_closeout_margin_used: -- The Account's margin closeout margin used.
        margin_closeout_percent: -- The Account's margin closeout percentage. When this value is 1.0
            or above the Account is in a margin closeout situation.
        margin_closeout_position_value: -- The value of the Account's open positions as used
            for margin closeout calculations represented in the Account's home currency.
        withdrawal_limit: -- The current WithdrawalLimit for the account which will be zero or
            a positive value indicating how much can be withdrawn from the account.
        margin_call_margin_used: -- The Account's margin call margin used.
        margin_call_percent: -- The Account's margin call percentage. When this value is 1.0
            or above the Account is in a margin call situation.
        orders: -- The price-dependent state of each pending Order in the Account.
        trades: -- The price-dependent state for each open Trade in the Account.
        positions: -- The price-dependent state for each open Position in the Account.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, unrealized_pl: AccountUnits = None, nav: AccountUnits = None, margin_used: AccountUnits = None,
                margin_available: AccountUnits = None, position_value: AccountUnits = None,
                margin_closeout_unrealized_pl: AccountUnits = None, margin_closeout_nav: AccountUnits = None,
                margin_closeout_margin_used: AccountUnits = None, margin_closeout_percent: DecimalNumber = None,
                margin_closeout_position_value: DecimalNumber = None, withdrawal_limit: AccountUnits = None,
                margin_call_margin_used: AccountUnits = None, margin_call_percent: DecimalNumber = None,
                orders: Array(DynamicOrderState) = None, trades: Array(CalculatedTradeState) = None,
                positions: Array(CalculatedPositionState) = None):
        return Model.__new__(**locals())


class Price(Model):
    """Price(self, type: str=PRICE, instrument: InstrumentName=None, time: DateTime=None, status: PriceStatus=None, tradeable: bool=None, bids: Array_PriceBucket=None, asks: Array_PriceBucket=None, closeout_bid: PriceValue=None, closeout_ask: PriceValue=None, quote_home_conversion_factors: QuoteHomeConversionFactors=None, units_available: UnitsAvailable=None)
The specification of an Account-specific Price.

    Attributes:
        type: -- The string "PRICE". Used to identify the a Price object when found in a stream.
        instrument: -- The Price's Instrument.
        time: -- The date/time when the Price was created
        status: -- The status of the Price.
        tradeable: -- Flag indicating if the Price is tradeable or not
        bids: -- The list of prices and liquidity available on the Instrument's bid side. It is possible for this
            list to be empty if there is no bid liquidity currently available for the Instrument in the Account.
        asks: -- The list of prices and liquidity available on the Instrument's ask side. It is possible for this
            list to be empty if there is no ask liquidity currently available for the Instrument in the Account.
        closeout_bid: -- The closeout bid Price. This Price is used when a bid is required to closeout a Position
            (margin closeout
            or manual) yet there is no bid liquidity. The closeout bid is never used to open a new position.
        closeout_ask: -- The closeout ask Price. This Price is used when a ask is required to closeout a Position
            (margin closeout
            or manual) yet there is no ask liquidity. The closeout ask is never used to open a new position.
        quote_home_conversion_factors: -- The factors used to convert quantities of this price's Instrument's
            quote currency into a quantity of the Account's home currency.
        units_available: -- Representation of how many units of an Instrument are available
            to be traded by an Order depending on its postionFill option.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, type: str = None, instrument: InstrumentName = None, time: DateTime = None,
                status: PriceStatus = None, tradeable: bool = None, bids: Array(PriceBucket) = None,
                asks: Array(PriceBucket) = None, closeout_bid: PriceValue = None, closeout_ask: PriceValue = None,
                quote_home_conversion_factors: QuoteHomeConversionFactors = None,
                units_available: UnitsAvailable = None):
        return Model.__new__(**locals())


class CloseTransaction(Transaction):
    """CloseTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=CLOSE)
A CloseTransaction represents the closing of an Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always set to "CLOSE" in a CloseTransaction.

    """

    _summary_format = 'Close Account {accountID}'

    _name_format = 'Close Account {accountID}'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'CLOSE'):
        return Model.__new__(**locals())


class MarginCallEnterTransaction(Transaction):
    """MarginCallEnterTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=MARGIN_CALL_ENTER)
A MarginCallEnterTransaction is created when an Account enters the margin
    call state.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "MARGIN_CALL_ENTER" for an MarginCallEnterTransaction.

    """

    _summary_format = 'Margin Call Enter'

    _name_format = 'Margin Call Enter'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'MARGIN_CALL_ENTER'):
        return Model.__new__(**locals())


class MarginCallExitTransaction(Transaction):
    """MarginCallExitTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=MARGIN_CALL_EXIT)
A MarginCallExitnterTransaction is created when an Account leaves the
    margin call state.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "MARGIN_CALL_EXIT" for an MarginCallExitTransaction.

    """

    _summary_format = 'Margin Call Exit'

    _name_format = 'Margin Call Exit'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'MARGIN_CALL_EXIT'):
        return Model.__new__(**locals())


class MarginCallExtendTransaction(Transaction):
    """MarginCallExtendTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=MARGIN_CALL_EXTEND, extension_number: int=None)
A MarginCallExtendTransaction is created when the margin call state for an
    Account has been extended.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "MARGIN_CALL_EXTEND" for an MarginCallExtendTransaction.
        extension_number: -- The number of the extensions to the Account's current margin call that have
            been applied. This value will be set to 1 for the first MarginCallExtend Transaction

    """

    _summary_format = 'Margin Call Enter'

    _name_format = 'Margin Call Enter'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'MARGIN_CALL_EXTEND', extension_number: int = None):
        return Model.__new__(**locals())


class ReopenTransaction(Transaction):
    """ReopenTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=REOPEN)
A ReopenTransaction represents the re-opening of a closed Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always set to "REOPEN" in a ReopenTransaction.

    """

    _summary_format = 'Reopen Account {accountID}'

    _name_format = 'Reopen Account {accountID}'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'REOPEN'):
        return Model.__new__(**locals())


class ResetResettablePLTransaction(Transaction):
    """ResetResettablePLTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=RESET_RESETTABLE_PL)
A ResetResettablePLTransaction represents the resetting of the Account's
    resettable PL counters.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "RESET_RESETTABLE_PL" for a ResetResettablePLTransaction.

    """

    _summary_format = 'PL Reset'

    _name_format = 'PL Reset'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'RESET_RESETTABLE_PL'):
        return Model.__new__(**locals())


class StopLossOrderRequest(OrderRequest):
    """StopLossOrderRequest(self, trade_id: TradeID, price: PriceValue, type: OrderType=STOP_LOSS, client_trade_id: ClientID=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, trigger_condition: OrderTriggerCondition=DEFAULT, client_extensions: ClientExtensions=None)
A StopLossOrderRequest specifies the parameters that may be set when
    creating a Stop Loss Order.

    Attributes:
        type: -- The type of the Order to Create. Must be
            set to "STOP_LOSS" when creating a Stop Loss Order.
        trade_id: -- The ID of the Trade to close when the price threshold is breached.
        client_trade_id: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the StopLoss Order. The associated Trade will be
            closed by a market price that is equal to or worse than this threshold.
        time_in_force: -- The time-in-force requested for the StopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for StopLoss Orders.
        gtd_time: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        client_extensions: -- The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.

    """

    _summary_format = 'Stop Loss for Trade {tradeID} @ {price}'

    _name_format = 'Stop Loss for Trade {tradeID} @ {price}'

    def __new__(self, trade_id: TradeID, price: PriceValue, type: OrderType = 'STOP_LOSS',
                client_trade_id: ClientID = None, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', client_extensions: ClientExtensions = None):
        return Model.__new__(**locals())


class TakeProfitOrderRequest(OrderRequest):
    """TakeProfitOrderRequest(self, trade_id: TradeID, price: PriceValue, type: OrderType=TAKE_PROFIT, client_trade_id: ClientID=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, trigger_condition: OrderTriggerCondition=DEFAULT, client_extensions: ClientExtensions=None)
A TakeProfitOrderRequest specifies the parameters that may be set when
    creating a Take Profit Order.

    Attributes:
        type: -- The type of the Order to Create. Must be
            set to "TAKE_PROFIT" when creating a Take Profit Order.
        trade_id: -- The ID of the Trade to close when the price threshold is breached.
        client_trade_id: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the TakeProfit Order. The associated Trade will be
            closed by a market price that is equal to or better than this threshold.
        time_in_force: -- The time-in-force requested for the TakeProfit Order. Restricted
            to "GTC", "GFD" and "GTD" for TakeProfit Orders.
        gtd_time: -- The date/time when the TakeProfit Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        client_extensions: -- The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.

    """

    _summary_format = 'Take Profit for Trade {tradeID} @ {price}'

    _name_format = 'Take Profit for Trade {tradeID} @ {price}'

    def __new__(self, trade_id: TradeID, price: PriceValue, type: OrderType = 'TAKE_PROFIT',
                client_trade_id: ClientID = None, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', client_extensions: ClientExtensions = None):
        return Model.__new__(**locals())


class TrailingStopLossOrderRequest(OrderRequest):
    """TrailingStopLossOrderRequest(self, trade_id: TradeID, distance: PriceValue, type: OrderType=TRAILING_STOP_LOSS, client_trade_id: ClientID=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, trigger_condition: OrderTriggerCondition=DEFAULT, client_extensions: ClientExtensions=None)
A TrailingStopLossOrderRequest specifies the parameters that may be set
    when creating a Trailing Stop Loss Order.

    Attributes:
        type: -- The type of the Order to Create. Must be
            set to "TRAILING_STOP_LOSS" when creating a Trailng Stop Loss Order.
        trade_id: -- The ID of the Trade to close when the price threshold is breached.
        client_trade_id: -- The client ID of the Trade to be closed when the price threshold is breached.
        distance: -- The price distance specified for the TrailingStopLoss Order.
        time_in_force: -- The time-in-force requested for the TrailingStopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
        gtd_time: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        client_extensions: -- The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.

    """

    _summary_format = 'Trailing Stop Loss for Trade {tradeID} @ {trailingStopValue}'

    _name_format = 'Trailing Stop Loss for Trade {tradeID} @ {trailingStopValue}'

    def __new__(self, trade_id: TradeID, distance: PriceValue, type: OrderType = 'TRAILING_STOP_LOSS',
                client_trade_id: ClientID = None, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', client_extensions: ClientExtensions = None):
        return Model.__new__(**locals())


class CreateTransaction(Transaction):
    """CreateTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=CREATE, division_id: int=None, site_id: int=None, account_user_id: int=None, account_number: int=None, home_currency: Currency=None)
A CreateTransaction represents the creation of an Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always set to "CREATE" in a CreateTransaction.
        division_id: -- The ID of the Division that the Account is in
        site_id: -- The ID of the Site that the Account was created at
        account_user_id: -- The ID of the user that the Account was created for
        account_number: -- The number of the Account within the site/division/user
        home_currency: -- The home currency of the Account

    """

    _summary_format = 'Create Account {accountID}'

    _name_format = 'Create Account {accountID}'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'CREATE', division_id: int = None, site_id: int = None,
                account_user_id: int = None, account_number: int = None, home_currency: Currency = None):
        return Model.__new__(**locals())


class ClientConfigureTransaction(Transaction):
    """ClientConfigureTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=CLIENT_CONFIGURE, alias: str=None, margin_rate: DecimalNumber=None)
A ClientConfigureTransaction represents the configuration of an Account by
    a client.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "CLIENT_CONFIGURE" in a ClientConfigureTransaction.
        alias: -- The client-provided alias for the Account.
        margin_rate: -- The margin rate override for the Account.

    """

    _summary_format = 'Client Configure'

    _name_format = 'Client Configure'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'CLIENT_CONFIGURE', alias: str = None, margin_rate: DecimalNumber = None):
        return Model.__new__(**locals())


class DelayedTradeClosureTransaction(Transaction):
    """DelayedTradeClosureTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=DELAYED_TRADE_CLOSURE, reason: MarketOrderReason=None, trade_i_ds: TradeID=None)
A DelayedTradeClosure Transaction is created administratively to indicate
    open trades that should have been closed but weren't because the open
    trades' instruments were untradeable at the time. Open trades listed in
    this transaction will be closed once their respective instruments become
    tradeable.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "DELAYED_TRADE_CLOSURE" for an DelayedTradeClosureTransaction.
        reason: -- The reason for the delayed trade closure
        trade_i_ds: -- List of Trade ID's identifying the open trades that
            will be closed when their respective instruments become tradeable

    """

    _summary_format = 'Delayed Trade Closure'

    _name_format = 'Delayed Trade Closure'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'DELAYED_TRADE_CLOSURE', reason: MarketOrderReason = None,
                trade_i_ds: TradeID = None):
        return Model.__new__(**locals())


class OrderCancelTransaction(Transaction):
    """OrderCancelTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=ORDER_CANCEL, order_id: OrderID=None, client_order_id: OrderID=None, reason: OrderCancelReason=None, replaced_by_order_id: OrderID=None, closed_trade_id: OrderID=None, trade_close_transaction_id: TransactionID=None)
An OrderCancelTransaction represents the cancellation of an Order in the
    client's Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "ORDER_CANCEL" for an OrderCancelTransaction.
        order_id: -- The ID of the Order cancelled
        client_order_id: -- The client ID of the Order cancelled (only
            provided if the Order has a client Order ID).
        reason: -- The reason that the Order was cancelled.
        replaced_by_order_id: -- The ID of the Order that replaced this Order
            (only provided if this Order was cancelled for replacement).

    """

    _summary_format = 'Cancel Order {orderID}'

    _name_format = 'Cancel Order {orderID}'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'ORDER_CANCEL', order_id: OrderID = None, client_order_id: OrderID = None,
                reason: OrderCancelReason = None, replaced_by_order_id: OrderID = None,
                closed_trade_id: OrderID = None, trade_close_transaction_id: TransactionID = None):
        return Model.__new__(**locals())


class OrderClientExtensionsModifyTransaction(Transaction):
    """OrderClientExtensionsModifyTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=ORDER_CLIENT_EXTENSIONS_MODIFY, order_id: OrderID=None, client_order_id: ClientID=None, client_extensions_modify: ClientExtensions=None, trade_client_extensions_modify: ClientExtensions=None)
A OrderClientExtensionsModifyTransaction represents the modification of an
    Order's Client Extensions.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "ORDER_CLIENT_EXTENSIONS_MODIFY" for a OrderClienteExtensionsModifyTransaction.
        order_id: -- The ID of the Order who's client extensions are to be modified.
        client_order_id: -- The original Client ID of the Order who's client extensions are to be modified.
        client_extensions_modify: -- The new Client Extensions for the Order.
        trade_client_extensions_modify: -- The new Client Extensions for the Order's Trade on fill.

    """

    _summary_format = 'Modify Order {orderID} Client Extensions'

    _name_format = 'Modify Order {orderID} Client Extensions'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'ORDER_CLIENT_EXTENSIONS_MODIFY', order_id: OrderID = None,
                client_order_id: ClientID = None, client_extensions_modify: ClientExtensions = None,
                trade_client_extensions_modify: ClientExtensions = None):
        return Model.__new__(**locals())


class DailyFinancingTransaction(Transaction):
    """DailyFinancingTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=DAILY_FINANCING, financing: AccountUnits=None, account_balance: AccountUnits=None, account_financing_mode: AccountFinancingMode=None, position_financings: Array_PositionFinancing=None)
A DailyFinancingTransaction represents the daily payment/collection of
    financing for an Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "DAILY_FINANCING" for a DailyFinancingTransaction.
        financing: -- The amount of financing paid/collected for the Account.
        account_balance: -- The Account's balance after daily financing.
        account_financing_mode: -- The account financing mode at the time of the daily financing.
        position_financings: -- The financing paid/collected for each Position in the Account.

    """

    _summary_format = 'Daily Account Financing ({financing})'

    _name_format = 'Daily Account Financing ({financing})'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'DAILY_FINANCING', financing: AccountUnits = None,
                account_balance: AccountUnits = None, account_financing_mode: AccountFinancingMode = None,
                position_financings: Array(PositionFinancing) = None):
        return Model.__new__(**locals())


class TradeClientExtensionsModifyTransaction(Transaction):
    """TradeClientExtensionsModifyTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=TRADE_CLIENT_EXTENSIONS_MODIFY, trade_id: TradeID=None, client_trade_id: ClientID=None, trade_client_extensions_modify: ClientExtensions=None)
A TradeClientExtensionsModifyTransaction represents the modification of a
    Trade's Client Extensions.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TRADE_CLIENT_EXTENSIONS_MODIFY" for a TradeClientExtensionsModifyTransaction.
        trade_id: -- The ID of the Trade who's client extensions are to be modified.
        client_trade_id: -- The original Client ID of the Trade who's client extensions are to be modified.
        trade_client_extensions_modify: -- The new Client Extensions for the Trade.

    """

    _summary_format = 'Modify Trade {tradeID} Client Extensions'

    _name_format = 'Modify Trade {tradeID} Client Extensions'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'TRADE_CLIENT_EXTENSIONS_MODIFY', trade_id: TradeID = None,
                client_trade_id: ClientID = None, trade_client_extensions_modify: ClientExtensions = None):
        return Model.__new__(**locals())


class AccountSummary(Model):
    """AccountSummary(self, id: AccountID=None, alias: str=None, currency: Currency=None, balance: AccountUnits=None, created_by_user_id: int=None, created_time: DateTime=None, pl: AccountUnits=None, resettable_pl: AccountUnits=None, resettabled_pl_time: DateTime=None, commission: AccountUnits=None, margin_rate: DecimalNumber=None, margin_call_enter_time: DateTime=None, margin_call_extension_count: int=None, last_margin_call_extension_time: DateTime=None, open_trade_count: int=None, open_position_count: int=None, pending_order_count: int=None, hedging_enabled: bool=None, unrealized_pl: AccountUnits=None, nav: AccountUnits=None, margin_used: AccountUnits=None, margin_available: AccountUnits=None, position_value: AccountUnits=None, margin_closeout_unrealized_pl: AccountUnits=None, margin_closeout_nav: AccountUnits=None, margin_closeout_margin_used: AccountUnits=None, margin_closeout_percent: DecimalNumber=None, margin_closeout_position_value: DecimalNumber=None, withdrawal_limit: AccountUnits=None, margin_call_margin_used: AccountUnits=None, margin_call_percent: DecimalNumber=None, last_transaction_id: TransactionID=None, financing: DecimalNumber=None)
A summary representation of a client's Account. The AccountSummary does not
    provide to full specification of pending Orders, open Trades and Positions.

    Attributes:
        id: -- The Account's identifier
        alias: -- Client-assigned alias for the Account. Only provided
            if the Account has an alias set
        currency: -- The home currency of the Account
        balance: -- The current balance of the Account. Represented in the Account's home currency.
        created_by_user_id: -- ID of the user that created the Account.
        created_time: -- The date/time when the Account was created.
        pl: -- The total profit/loss realized over the lifetime of
            the Account. Represented in the Account's home currency.
        resettable_pl: -- The total realized profit/loss for the Account since it was
            last reset by the client. Represented in the Account's home currency.
        resettabled_pl_time: -- The date/time that the Account's resettablePL was last reset.
        commission: -- The total amount of commission paid over the lifetime
            of the Account. Represented in the Account's home currency.
        margin_rate: -- Client-provided margin rate override for the Account. The effective margin rate of the Account
            is the lesser of this value and
            the OANDA margin rate for the Account's division. This value is only provided if a margin rate override
            exists for the Account.
        margin_call_enter_time: -- The date/time when the Account entered a margin call state.
            Only provided if the Account is in a margin call.
        margin_call_extension_count: -- The number of times that the Account's current margin call was extended.
        last_margin_call_extension_time: -- The date/time of the Account's last margin call extension.
        open_trade_count: -- The number of Trades currently open in the Account.
        open_position_count: -- The number of Positions currently open in the Account.
        pending_order_count: -- The number of Orders currently pending in the Account.
        hedging_enabled: -- Flag indicating that the Account has hedging enabled.
        unrealized_pl: -- The total unrealized profit/loss for all Trades currently open
            in the Account. Represented in the Account's home currency.
        nav: -- The net asset value of the Account. Equal to
            Account balance + unrealizedPL. Represented in the Account's home currency.
        margin_used: -- Margin currently used for the Account.
            Represented in the Account's home currency.
        margin_available: -- Margin available for Account. Represented in the Account's home currency.
        position_value: -- The value of the Account's open
            positions represented in the Account's home currency.
        margin_closeout_unrealized_pl: -- The Account's margin closeout unrealized PL.
        margin_closeout_nav: -- The Account's margin closeout NAV.
        margin_closeout_margin_used: -- The Account's margin closeout margin used.
        margin_closeout_percent: -- The Account's margin closeout percentage. When this value is 1.0
            or above the Account is in a margin closeout situation.
        margin_closeout_position_value: -- The value of the Account's open positions as used
            for margin closeout calculations represented in the Account's home currency.
        withdrawal_limit: -- The current WithdrawalLimit for the account which will be zero or
            a positive value indicating how much can be withdrawn from the account.
        margin_call_margin_used: -- The Account's margin call margin used.
        margin_call_percent: -- The Account's margin call percentage. When this value is 1.0
            or above the Account is in a margin call situation.
        last_transaction_id: -- The ID of the last Transaction created for the Account.

    """

    _summary_format = ''

    _name_format = ''

    def __new__(self, id: AccountID = None, alias: str = None, currency: Currency = None, balance: AccountUnits = None,
                created_by_user_id: int = None, created_time: DateTime = None, pl: AccountUnits = None,
                resettable_pl: AccountUnits = None, resettabled_pl_time: DateTime = None,
                commission: AccountUnits = None, margin_rate: DecimalNumber = None,
                margin_call_enter_time: DateTime = None, margin_call_extension_count: int = None,
                last_margin_call_extension_time: DateTime = None, open_trade_count: int = None,
                open_position_count: int = None, pending_order_count: int = None, hedging_enabled: bool = None,
                unrealized_pl: AccountUnits = None, nav: AccountUnits = None, margin_used: AccountUnits = None,
                margin_available: AccountUnits = None, position_value: AccountUnits = None,
                margin_closeout_unrealized_pl: AccountUnits = None, margin_closeout_nav: AccountUnits = None,
                margin_closeout_margin_used: AccountUnits = None, margin_closeout_percent: DecimalNumber = None,
                margin_closeout_position_value: DecimalNumber = None, withdrawal_limit: AccountUnits = None,
                margin_call_margin_used: AccountUnits = None, margin_call_percent: DecimalNumber = None,
                last_transaction_id: TransactionID = None, financing: DecimalNumber = None,
                trades: Array(TradeSummary) = None, positions: Array(Position) = None, orders: Array(Order) = None):
        return Model.__new__(**locals())


class MarketOrderRequest(OrderRequest):
    """MarketOrderRequest(self, instrument: InstrumentName, units: Unit, type: OrderType=MARKET, time_in_force: TimeInForce=FOK, price_bound: PriceValue=None, position_fill: OrderPositionFill=DEFAULT, client_extensions: ClientExtensions=None, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None)
A MarketOrderRequest specifies the parameters that may be set when creating
    a Market Order.

    Attributes:
        type: -- The type of the Order to Create. Must
            be set to "MARKET" when creating a Market Order.
        instrument: -- The Market Order's Instrument.
        units: -- The quantity requested to be filled by the Market Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        time_in_force: -- The time-in-force requested for the Market Order.
            Restricted to FOK or IOC for a MarketOrder.
        price_bound: -- The worst price that the client is willing to have the Market Order filled at.
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        client_extensions: -- The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.
        take_profit_on_fill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
            a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.

    """

    _summary_format = '{units} units of {instrument}'

    _name_format = '{units} units of {instrument}'

    def __new__(self, instrument: InstrumentName, units: Unit, type: OrderType = 'MARKET',
                time_in_force: TimeInForce = 'FOK', price_bound: PriceValue = None,
                position_fill: OrderPositionFill = 'DEFAULT', client_extensions: ClientExtensions = None,
                take_profit_on_fill: TakeProfitDetails = None, stop_loss_on_fill: StopLossDetails = None,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None):
        return Model.__new__(**locals())


class TakeProfitOrderTransaction(Transaction):
    """TakeProfitOrderTransaction(self, trade_id: TradeID, price: PriceValue, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=TAKE_PROFIT_ORDER, client_trade_id: ClientID=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, trigger_condition: OrderTriggerCondition=DEFAULT, reason: TakeProfitOrderReason=None, client_extensions: ClientExtensions=None, order_fill_transaction_id: TransactionID=None, replaces_order_id: OrderID=None, cancelling_transaction_id: TransactionID=None)
A TakeProfitOrderTransaction represents the creation of a TakeProfit Order
    in the user's Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TAKE_PROFIT_ORDER" in a TakeProfitOrderTransaction.
        trade_id: -- The ID of the Trade to close when the price threshold is breached.
        client_trade_id: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the TakeProfit Order. The associated Trade will be
            closed by a market price that is equal to or better than this threshold.
        time_in_force: -- The time-in-force requested for the TakeProfit Order. Restricted
            to "GTC", "GFD" and "GTD" for TakeProfit Orders.
        gtd_time: -- The date/time when the TakeProfit Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Take Profit Order was initiated
        client_extensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        order_fill_transaction_id: -- The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        replaces_order_id: -- The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancelling_transaction_id: -- The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    _summary_format = 'Create Take Profit Order {id} ({reason}): Close Trade {tradeID} @ {price}'

    _name_format = 'Create Take Profit Order {id} ({reason}): Close Trade {tradeID} @ {price}'

    def __new__(self, trade_id: TradeID, price: PriceValue, id: TransactionID = None, time: DateTime = None,
                user_id: int = None, account_id: AccountID = None, batch_id: TransactionID = None,
                request_id: RequestID = None, type: TransactionType = 'TAKE_PROFIT_ORDER',
                client_trade_id: ClientID = None, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: TakeProfitOrderReason = None,
                client_extensions: ClientExtensions = None, order_fill_transaction_id: TransactionID = None,
                replaces_order_id: OrderID = None, cancelling_transaction_id: TransactionID = None):
        return Model.__new__(**locals())


class TakeProfitOrder(Order):
    """TakeProfitOrder(self, trade_id: TradeID, price: PriceValue, id: OrderID=None, create_time: DateTime=None, state: OrderState=None, client_extensions: ClientExtensions=None, type: OrderType=TAKE_PROFIT, client_trade_id: ClientID=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, trigger_condition: OrderTriggerCondition=DEFAULT, filling_transaction_id: TransactionID=None, filled_time: DateTime=None, trade_opened_id: TradeID=None, trade_reduced_id: TradeID=None, trade_closed_i_ds: Array_TradeID=None, cancelling_transaction_id: TransactionID=None, cancelled_time: DateTime=None, replaces_order_id: OrderID=None, replaced_by_order_id: OrderID=None)
A TakeProfitOrder is an order that is linked to an open Trade and created
    with a price threshold. The Order will be filled (closing the Trade) by the
    first price that is equal to or better than the threshold. A
    TakeProfitOrder cannot be used to open a new Position.

    Attributes:
        id: -- The Order's identifier, unique within the Order's Account.
        create_time: -- The time when the Order was created.
        state: -- The current state of the Order.
        client_extensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        type: -- The type of the Order. Always set to "TAKE_PROFIT" for Take Profit Orders.
        trade_id: -- The ID of the Trade to close when the price threshold is breached.
        client_trade_id: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the TakeProfit Order. The associated Trade will be
            closed by a market price that is equal to or better than this threshold.
        time_in_force: -- The time-in-force requested for the TakeProfit Order. Restricted
            to "GTC", "GFD" and "GTD" for TakeProfit Orders.
        gtd_time: -- The date/time when the TakeProfit Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        filling_transaction_id: -- ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filled_time: -- Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        trade_opened_id: -- Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        trade_reduced_id: -- Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        trade_closed_i_ds: -- Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancelling_transaction_id: -- ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelled_time: -- Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replaces_order_id: -- The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replaced_by_order_id: -- The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

    """

    _summary_format = 'Take Profit for Trade {tradeID} @ {price}'

    _name_format = 'Take Profit for Trade {tradeID} @ {price}'

    def __new__(self, trade_id: TradeID, price: PriceValue, id: OrderID = None, create_time: DateTime = None,
                state: OrderState = None, client_extensions: ClientExtensions = None, type: OrderType = 'TAKE_PROFIT',
                client_trade_id: ClientID = None, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', filling_transaction_id: TransactionID = None,
                filled_time: DateTime = None, trade_opened_id: TradeID = None, trade_reduced_id: TradeID = None,
                trade_closed_i_ds: Array(TradeID) = None, cancelling_transaction_id: TransactionID = None,
                cancelled_time: DateTime = None, replaces_order_id: OrderID = None,
                replaced_by_order_id: OrderID = None):
        return Model.__new__(**locals())


class StopLossOrder(Order):
    """StopLossOrder(self, trade_id: TradeID, price: PriceValue, id: OrderID=None, create_time: DateTime=None, state: OrderState=None, client_extensions: ClientExtensions=None, type: OrderType=STOP_LOSS, client_trade_id: ClientID=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, trigger_condition: OrderTriggerCondition=DEFAULT, filling_transaction_id: TransactionID=None, filled_time: DateTime=None, trade_opened_id: TradeID=None, trade_reduced_id: TradeID=None, trade_closed_i_ds: Array_TradeID=None, cancelling_transaction_id: TransactionID=None, cancelled_time: DateTime=None, replaces_order_id: OrderID=None, replaced_by_order_id: OrderID=None)
A StopLossOrder is an order that is linked to an open Trade and created
    with a price threshold. The Order will be filled (closing the Trade) by the
    first price that is equal to or worse than the threshold. A StopLossOrder
    cannot be used to open a new Position.

    Attributes:
        id: -- The Order's identifier, unique within the Order's Account.
        create_time: -- The time when the Order was created.
        state: -- The current state of the Order.
        client_extensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        type: -- The type of the Order. Always set to "STOP_LOSS" for Stop Loss Orders.
        trade_id: -- The ID of the Trade to close when the price threshold is breached.
        client_trade_id: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the StopLoss Order. The associated Trade will be
            closed by a market price that is equal to or worse than this threshold.
        time_in_force: -- The time-in-force requested for the StopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for StopLoss Orders.
        gtd_time: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        filling_transaction_id: -- ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filled_time: -- Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        trade_opened_id: -- Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        trade_reduced_id: -- Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        trade_closed_i_ds: -- Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancelling_transaction_id: -- ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelled_time: -- Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replaces_order_id: -- The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replaced_by_order_id: -- The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

        """

    _summary_format = 'Stop Loss for Trade {tradeID} @ {price}'

    _name_format = 'Stop Loss for Trade {tradeID} @ {price}'

    def __new__(self, trade_id: TradeID, price: PriceValue, id: OrderID = None, create_time: DateTime = None,
                state: OrderState = None, client_extensions: ClientExtensions = None, type: OrderType = 'STOP_LOSS',
                client_trade_id: ClientID = None, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', filling_transaction_id: TransactionID = None,
                filled_time: DateTime = None, trade_opened_id: TradeID = None, trade_reduced_id: TradeID = None,
                trade_closed_i_ds: Array(TradeID) = None, cancelling_transaction_id: TransactionID = None,
                cancelled_time: DateTime = None, replaces_order_id: OrderID = None,
                replaced_by_order_id: OrderID = None):
        return Model.__new__(**locals())


class TrailingStopLossOrder(Order):
    """TrailingStopLossOrder(self, trade_id: TradeID, distance: PriceValue, id: OrderID=None, create_time: DateTime=None, state: OrderState=None, client_extensions: ClientExtensions=None, type: OrderType=TRAILING_STOP_LOSS, client_trade_id: ClientID=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, trigger_condition: OrderTriggerCondition=DEFAULT, trailing_stop_value: PriceValue=None, filling_transaction_id: TransactionID=None, filled_time: DateTime=None, trade_opened_id: TradeID=None, trade_reduced_id: TradeID=None, trade_closed_i_ds: Array_TradeID=None, cancelling_transaction_id: TransactionID=None, cancelled_time: DateTime=None, replaces_order_id: OrderID=None, replaced_by_order_id: OrderID=None)
A TrailingStopLossOrder is an order that is linked to an open Trade and
    created with a price distance. The price distance is used to calculate a
    trailing stop value for the order that is in the losing direction from the
    market price at the time of the order's creation. The trailing stop value
    will follow the market price as it moves in the winning direction, and the
    order will filled (closing the Trade) by the first price that is equal to
    or worse than the trailing stop value. A TrailingStopLossOrder cannot be
    used to open a new Position.

    Attributes:
        id: -- The Order's identifier, unique within the Order's Account.
        create_time: -- The time when the Order was created.
        state: -- The current state of the Order.
        client_extensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        type: -- The type of the Order. Always set
            to "TRAILING_STOP_LOSS" for Trailing Stop Loss Orders.
        trade_id: -- The ID of the Trade to close when the price threshold is breached.
        client_trade_id: -- The client ID of the Trade to be closed when the price threshold is breached.
        distance: -- The price distance specified for the TrailingStopLoss Order.
        time_in_force: -- The time-in-force requested for the TrailingStopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
        gtd_time: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        trailing_stop_value: -- The trigger price for the Trailing Stop Loss Order. The trailing stop value will trail
            (follow) the market price by the TSL order's configured "distance" as the market price moves in the
            winning direction. If the market price moves to a level that is equal to or worse than the trailing stop
            value, the order will be filled and the Trade will be closed.
        filling_transaction_id: -- ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filled_time: -- Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        trade_opened_id: -- Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        trade_reduced_id: -- Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        trade_closed_i_ds: -- Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancelling_transaction_id: -- ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelled_time: -- Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replaces_order_id: -- The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replaced_by_order_id: -- The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

    """

    _summary_format = 'Trailing Stop Loss for Trade {tradeID} @ {trailingStopValue}'

    _name_format = 'Trailing Stop Loss for Trade {tradeID} @ {trailingStopValue}'

    def __new__(self, trade_id: TradeID, distance: PriceValue, id: OrderID = None, create_time: DateTime = None,
                state: OrderState = None, client_extensions: ClientExtensions = None,
                type: OrderType = 'TRAILING_STOP_LOSS', client_trade_id: ClientID = None,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', trailing_stop_value: PriceValue = None,
                filling_transaction_id: TransactionID = None, filled_time: DateTime = None,
                trade_opened_id: TradeID = None, trade_reduced_id: TradeID = None,
                trade_closed_i_ds: Array(TradeID) = None, cancelling_transaction_id: TransactionID = None,
                cancelled_time: DateTime = None, replaces_order_id: OrderID = None,
                replaced_by_order_id: OrderID = None):
        return Model.__new__(**locals())


class Trade(Model):
    """Trade(self, id: TradeID=None, instrument: InstrumentName=None, price: PriceValue=None, open_time: DateTime=None, state: TradeState=None, initial_units: DecimalNumber=None, current_units: DecimalNumber=None, realized_pl: AccountUnits=None, unrealized_pl: AccountUnits=None, average_close_price: PriceValue=None, closing_transaction_i_ds: Array_TransactionID=None, financing: AccountUnits=None, close_time: DateTime=None, client_extensions: ClientExtensions=None, take_profit_order: TakeProfitOrder=None, stop_loss_order: StopLossOrder=None, trailing_stop_loss_order: TrailingStopLossOrder=None)
The specification of a Trade within an Account. This includes the full
    representation of the Trade's dependent Orders in addition to the IDs of
    those Orders.

    Attributes:
        id: -- The Trade's identifier, unique within the Trade's Account.
        instrument: -- The Trade's Instrument.
        price: -- The execution price of the Trade.
        open_time: -- The date/time when the Trade was opened.
        state: -- The current state of the Trade.
        initial_units: -- The initial size of the Trade. Negative values indicate
            a short Trade, and positive values indicate a long Trade.
        current_units: -- The number of units currently open for the Trade. This
            value is reduced to 0.0 as the Trade is closed.
        realized_pl: -- The total profit/loss realized on the closed portion of the Trade.
        unrealized_pl: -- The unrealized profit/loss on the open portion of the Trade.
        average_close_price: -- The average closing price of the Trade. Only present if
            the Trade has been closed or reduced at least once.
        closing_transaction_i_ds: -- The IDs of the Transactions that have closed portions of this Trade.
        financing: -- The financing paid/collected for this Trade.
        close_time: -- The date/time when the Trade was fully closed.
            Only provided for Trades whose state is CLOSED.
        client_extensions: -- The client extensions of the Trade.
        take_profit_order: -- Full representation of the Trade's Take Profit
            Order, only provided if such an Order exists.
        stop_loss_order: -- Full representation of the Trade's Stop Loss
            Order, only provided if such an Order exists.
        trailing_stop_loss_order: -- Full representation of the Trade's Trailing Stop Loss
            Order, only provided if such an Order exists.

    """

    _summary_format = '{currentUnits} ({initialUnits}) of {instrument} @ {price}'

    _name_format = '{currentUnits} ({initialUnits}) of {instrument} @ {price}'

    def __new__(self, id: TradeID = None, instrument: InstrumentName = None, price: PriceValue = None,
                open_time: DateTime = None, state: TradeState = None, initial_units: DecimalNumber = None,
                current_units: DecimalNumber = None, realized_pl: AccountUnits = None,
                unrealized_pl: AccountUnits = None, average_close_price: PriceValue = None,
                closing_transaction_i_ds: Array(TransactionID) = None, financing: AccountUnits = None,
                close_time: DateTime = None, client_extensions: ClientExtensions = None,
                take_profit_order: TakeProfitOrder = None, stop_loss_order: StopLossOrder = None,
                trailing_stop_loss_order: TrailingStopLossOrder = None):
        return Model.__new__(**locals())


class ClientConfigureRejectTransaction(Transaction):
    """ClientConfigureRejectTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=CLIENT_CONFIGURE_REJECT, alias: str=None, margin_rate: DecimalNumber=None, reject_reason: TransactionRejectReason=None)
A ClientConfigureRejectTransaction represents the reject of configuration
    of an Account by a client.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "CLIENT_CONFIGURE_REJECT" in a ClientConfigureRejectTransaction.
        alias: -- The client-provided alias for the Account.
        margin_rate: -- The margin rate override for the Account.
        reject_reason: -- The reason that the Reject Transaction was created

    """

    _summary_format = 'Client Configure Reject'

    _name_format = 'Client Configure Reject'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'CLIENT_CONFIGURE_REJECT', alias: str = None,
                margin_rate: DecimalNumber = None, reject_reason: TransactionRejectReason = None):
        return Model.__new__(**locals())


class OrderCancelRejectTransaction(Transaction):
    """OrderCancelRejectTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=ORDER_CANCEL_REJECT, order_id: OrderID=None, client_order_id: OrderID=None, reason: OrderCancelReason=None, reject_reason: TransactionRejectReason=None)
An OrderCancelRejectTransaction represents the rejection of the
    cancellation of an Order in the client's Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "ORDER_CANCEL_REJECT" for an OrderCancelRejectTransaction.
        order_id: -- The ID of the Order intended to be cancelled
        client_order_id: -- The client ID of the Order intended to be cancelled
            (only provided if the Order has a client Order ID).
        reason: -- The reason that the Order was to be cancelled.
        reject_reason: -- The reason that the Reject Transaction was created

    """

    _summary_format = 'Order Cancel Reject {orderID}'

    _name_format = 'Order Cancel Reject {orderID}'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'ORDER_CANCEL_REJECT', order_id: OrderID = None,
                client_order_id: OrderID = None, reason: OrderCancelReason = None,
                reject_reason: TransactionRejectReason = None):
        return Model.__new__(**locals())


class OrderClientExtensionsModifyRejectTransaction(Transaction):
    """OrderClientExtensionsModifyRejectTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT, order_id: OrderID=None, client_order_id: ClientID=None, client_extensions_modify: ClientExtensions=None, trade_client_extensions_modify: ClientExtensions=None, reject_reason: TransactionRejectReason=None)
A OrderClientExtensionsModifyRejectTransaction represents the rejection of
    the modification of an Order's Client Extensions.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT" for a OrderClientExtensionsModifyRejectTransaction.
        order_id: -- The ID of the Order who's client extensions are to be modified.
        client_order_id: -- The original Client ID of the Order who's client extensions are to be modified.
        client_extensions_modify: -- The new Client Extensions for the Order.
        trade_client_extensions_modify: -- The new Client Extensions for the Order's Trade on fill.
        reject_reason: -- The reason that the Reject Transaction was created

    """

    _summary_format = 'Reject Modify Order {orderID} Client Extensions'

    _name_format = 'Reject Modify Order {orderID} Client Extensions'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT', order_id: OrderID = None,
                client_order_id: ClientID = None, client_extensions_modify: ClientExtensions = None,
                trade_client_extensions_modify: ClientExtensions = None,
                reject_reason: TransactionRejectReason = None):
        return Model.__new__(**locals())


class TradeClientExtensionsModifyRejectTransaction(Transaction):
    """TradeClientExtensionsModifyRejectTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT, trade_id: TradeID=None, client_trade_id: ClientID=None, trade_client_extensions_modify: ClientExtensions=None, reject_reason: TransactionRejectReason=None)
A TradeClientExtensionsModifyRejectTransaction represents the rejection of
    the modification of a Trade's Client Extensions.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT" for a TradeClientExtensionsModifyRejectTransaction.
        trade_id: -- The ID of the Trade who's client extensions are to be modified.
        client_trade_id: -- The original Client ID of the Trade who's client extensions are to be modified.
        trade_client_extensions_modify: -- The new Client Extensions for the Trade.
        reject_reason: -- The reason that the Reject Transaction was created

    """

    _summary_format = 'Reject Modify Trade {tradeID} Client Extensions'

    _name_format = 'Reject Modify Trade {tradeID} Client Extensions'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT', trade_id: TradeID = None,
                client_trade_id: ClientID = None, trade_client_extensions_modify: ClientExtensions = None,
                reject_reason: TransactionRejectReason = None):
        return Model.__new__(**locals())


class TransferFundsTransaction(Transaction):
    """TransferFundsTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=TRANSFER_FUNDS, amount: AccountUnits=None, funding_reason: FundingReason=None, comment: str=None, account_balance: AccountUnits=None)
A TransferFundsTransaction represents the transfer of funds in/out of an
    Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TRANSFER_FUNDS" in a TransferFundsTransaction.
        amount: -- The amount to deposit/withdraw from the Account in the Account's home currency.
            A positive value indicates a deposit, a negative value indicates a withdrawal.
        funding_reason: -- The reason that an Account is being funded.
        comment: -- An optional comment that may be attached to a fund transfer for audit purposes
        account_balance: -- The Account's balance after funds are transferred.

    """

    _summary_format = 'Account Transfer of {amount}'

    _name_format = 'Account Transfer of {amount}'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'TRANSFER_FUNDS', amount: AccountUnits = None,
                funding_reason: FundingReason = None, comment: str = None, account_balance: AccountUnits = None):
        return Model.__new__(**locals())


class TransferFundsRejectTransaction(Transaction):
    """TransferFundsRejectTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=TRANSFER_FUNDS_REJECT, amount: AccountUnits=None, funding_reason: FundingReason=None, comment: str=None, reject_reason: TransactionRejectReason=None)
A TransferFundsRejectTransaction represents the rejection of the transfer
    of funds in/out of an Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TRANSFER_FUNDS_REJECT" in a TransferFundsRejectTransaction.
        amount: -- The amount to deposit/withdraw from the Account in the Account's home currency.
            A positive value indicates a deposit, a negative value indicates a withdrawal.
        funding_reason: -- The reason that an Account is being funded.
        comment: -- An optional comment that may be attached to a fund transfer for audit purposes
        reject_reason: -- The reason that the Reject Transaction was created

    """

    _summary_format = 'Account Reject Transfer of {amount}'

    _name_format = 'Account Reject Transfer of {amount}'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'TRANSFER_FUNDS_REJECT', amount: AccountUnits = None,
                funding_reason: FundingReason = None, comment: str = None,
                reject_reason: TransactionRejectReason = None):
        return Model.__new__(**locals())


class LimitOrderRequest(OrderRequest):
    """LimitOrderRequest(self, instrument: InstrumentName, units: Unit, price: PriceValue, type: OrderType=LIMIT, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, position_fill: OrderPositionFill=DEFAULT, trigger_condition: OrderTriggerCondition=DEFAULT, client_extensions: ClientExtensions=None, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None)
A LimitOrderRequest specifies the parameters that may be set when creating
    a Limit Order.

    Attributes:
        type: -- The type of the Order to Create. Must
            be set to "LIMIT" when creating a Market Order.
        instrument: -- The Limit Order's Instrument.
        units: -- The quantity requested to be filled by the Limit Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Limit Order. The Limit Order will only be
            filled by a market price that is equal to or better than this price.
        time_in_force: -- The time-in-force requested for the Limit Order.
        gtd_time: -- The date/time when the Limit Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        client_extensions: -- The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.
        take_profit_on_fill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
            a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.

    """

    _summary_format = '{units} units of {instrument} @ {price}'

    _name_format = '{units} units of {instrument} @ {price}'

    def __new__(self, instrument: InstrumentName, units: Unit, price: PriceValue, type: OrderType = 'LIMIT',
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                client_extensions: ClientExtensions = None, take_profit_on_fill: TakeProfitDetails = None,
                stop_loss_on_fill: StopLossDetails = None, trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None):
        return Model.__new__(**locals())


class MarketIfTouchedOrderRequest(OrderRequest):
    """MarketIfTouchedOrderRequest(self, instrument: InstrumentName, units: Unit, price: PriceValue, type: OrderType=MARKET_IF_TOUCHED, price_bound: PriceValue=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, position_fill: OrderPositionFill=DEFAULT, trigger_condition: OrderTriggerCondition=DEFAULT, client_extensions: ClientExtensions=None, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None)
A MarketIfTouchedOrderRequest specifies the parameters that may be set when
    creating a Market-if-Touched Order.

    Attributes:
        type: -- The type of the Order to Create. Must be
            set to "MARKET_IF_TOUCHED" when creating a Market If Touched Order.
        instrument: -- The MarketIfTouched Order's Instrument.
        units: -- The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be
            filled by a market price that crosses this price from the direction of the market price
            at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's
            price and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.
        price_bound: -- The worst market price that may be used to fill this MarketIfTouched Order.
        time_in_force: -- The time-in-force requested for the MarketIfTouched Order. Restricted
            to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
        gtd_time: -- The date/time when the MarketIfTouched Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        client_extensions: -- The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.
        take_profit_on_fill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
            a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.

        """

    _summary_format = '{units} units of {instrument} @ {price}'

    _name_format = '{units} units of {instrument} @ {price}'

    def __new__(self, instrument: InstrumentName, units: Unit, price: PriceValue,
                type: OrderType = 'MARKET_IF_TOUCHED', price_bound: PriceValue = None,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                client_extensions: ClientExtensions = None, take_profit_on_fill: TakeProfitDetails = None,
                stop_loss_on_fill: StopLossDetails = None, trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None):
        return Model.__new__(**locals())


class StopOrderRequest(OrderRequest):
    """StopOrderRequest(self, instrument: InstrumentName, units: Unit, price: PriceValue, type: OrderType=STOP, price_bound: PriceValue=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, position_fill: OrderPositionFill=DEFAULT, trigger_condition: OrderTriggerCondition=DEFAULT, client_extensions: ClientExtensions=None, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None)
A StopOrderRequest specifies the parameters that may be set when creating a
    Stop Order.

    Attributes:
        type: -- The type of the Order to Create. Must
            be set to "STOP" when creating a Stop Order.
        instrument: -- The Stop Order's Instrument.
        units: -- The quantity requested to be filled by the Stop Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Stop Order. The Stop Order will only be
            filled by a market price that is equal to or worse than this price.
        price_bound: -- The worst market price that may be used to fill this Stop Order. If the market gaps and
            crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.
        time_in_force: -- The time-in-force requested for the Stop Order.
        gtd_time: -- The date/time when the Stop Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        client_extensions: -- The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.
        take_profit_on_fill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
            a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.

    """

    _summary_format = '{units} units of {instrument} @ {price}'

    _name_format = '{units} units of {instrument} @ {price}'

    def __new__(self, instrument: InstrumentName, units: Unit, price: PriceValue, type: OrderType = 'STOP',
                price_bound: PriceValue = None, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                client_extensions: ClientExtensions = None, take_profit_on_fill: TakeProfitDetails = None,
                stop_loss_on_fill: StopLossDetails = None, trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None):
        return Model.__new__(**locals())


class Account(AccountSummary):
    """Account(self, id: AccountID=None, alias: str=None, currency: Currency=None, balance: AccountUnits=None, created_by_user_id: int=None, created_time: DateTime=None, pl: AccountUnits=None, resettable_pl: AccountUnits=None, resettabled_pl_time: DateTime=None, commission: AccountUnits=None, margin_rate: DecimalNumber=None, margin_call_enter_time: DateTime=None, margin_call_extension_count: int=None, last_margin_call_extension_time: DateTime=None, open_trade_count: int=None, open_position_count: int=None, pending_order_count: int=None, hedging_enabled: bool=None, unrealized_pl: AccountUnits=None, nav: AccountUnits=None, margin_used: AccountUnits=None, margin_available: AccountUnits=None, position_value: AccountUnits=None, margin_closeout_unrealized_pl: AccountUnits=None, margin_closeout_nav: AccountUnits=None, margin_closeout_margin_used: AccountUnits=None, margin_closeout_percent: DecimalNumber=None, margin_closeout_position_value: DecimalNumber=None, withdrawal_limit: AccountUnits=None, margin_call_margin_used: AccountUnits=None, margin_call_percent: DecimalNumber=None, last_transaction_id: TransactionID=None, trades: Array_TradeSummary=None, positions: Array_Position=None, orders: Array_Order=None, financing: DecimalNumber=None)
The full details of a client's Account. This includes full open Trade, open
    Position and pending Order representation.

    Attributes:
        id: -- The Account's identifier
        alias: -- Client-assigned alias for the Account. Only provided
            if the Account has an alias set
        currency: -- The home currency of the Account
        balance: -- The current balance of the Account. Represented in the Account's home currency.
        created_by_user_id: -- ID of the user that created the Account.
        created_time: -- The date/time when the Account was created.
        pl: -- The total profit/loss realized over the lifetime of
            the Account. Represented in the Account's home currency.
        resettable_pl: -- The total realized profit/loss for the Account since it was
            last reset by the client. Represented in the Account's home currency.
        resettabled_pl_time: -- The date/time that the Account's resettablePL was last reset.
        commission: -- The total amount of commission paid over the lifetime
            of the Account. Represented in the Account's home currency.
        margin_rate: -- Client-provided margin rate override for the Account. The effective margin rate of the Account
            is the lesser of this value and
            the OANDA margin rate for the Account's division. This value is only provided if a margin rate override
            exists for the Account.
        margin_call_enter_time: -- The date/time when the Account entered a margin call state.
            Only provided if the Account is in a margin call.
        margin_call_extension_count: -- The number of times that the Account's current margin call was extended.
        last_margin_call_extension_time: -- The date/time of the Account's last margin call extension.
        open_trade_count: -- The number of Trades currently open in the Account.
        open_position_count: -- The number of Positions currently open in the Account.
        pending_order_count: -- The number of Orders currently pending in the Account.
        hedging_enabled: -- Flag indicating that the Account has hedging enabled.
        unrealized_pl: -- The total unrealized profit/loss for all Trades currently open
            in the Account. Represented in the Account's home currency.
        nav: -- The net asset value of the Account. Equal to
            Account balance + unrealizedPL. Represented in the Account's home currency.
        margin_used: -- Margin currently used for the Account.
            Represented in the Account's home currency.
        margin_available: -- Margin available for Account. Represented in the Account's home currency.
        position_value: -- The value of the Account's open
            positions represented in the Account's home currency.
        margin_closeout_unrealized_pl: -- The Account's margin closeout unrealized PL.
        margin_closeout_nav: -- The Account's margin closeout NAV.
        margin_closeout_margin_used: -- The Account's margin closeout margin used.
        margin_closeout_percent: -- The Account's margin closeout percentage. When this value is 1.0
            or above the Account is in a margin closeout situation.
        margin_closeout_position_value: -- The value of the Account's open positions as used
            for margin closeout calculations represented in the Account's home currency.
        withdrawal_limit: -- The current WithdrawalLimit for the account which will be zero or
            a positive value indicating how much can be withdrawn from the account.
        margin_call_margin_used: -- The Account's margin call margin used.
        margin_call_percent: -- The Account's margin call percentage. When this value is 1.0
            or above the Account is in a margin call situation.
        last_transaction_id: -- The ID of the last Transaction created for the Account.
        trades: -- The details of the Trades currently open in the Account.
        positions: -- The details all Account Positions.
        orders: -- The details of the Orders currently pending in the Account.

    """

    _summary_format = 'Account {id}'

    _name_format = ''

    def __new__(self, id: AccountID = None, alias: str = None, currency: Currency = None, balance: AccountUnits = None,
                created_by_user_id: int = None, created_time: DateTime = None, pl: AccountUnits = None,
                resettable_pl: AccountUnits = None, resettabled_pl_time: DateTime = None,
                commission: AccountUnits = None, margin_rate: DecimalNumber = None,
                margin_call_enter_time: DateTime = None, margin_call_extension_count: int = None,
                last_margin_call_extension_time: DateTime = None, open_trade_count: int = None,
                open_position_count: int = None, pending_order_count: int = None, hedging_enabled: bool = None,
                unrealized_pl: AccountUnits = None, nav: AccountUnits = None, margin_used: AccountUnits = None,
                margin_available: AccountUnits = None, position_value: AccountUnits = None,
                margin_closeout_unrealized_pl: AccountUnits = None, margin_closeout_nav: AccountUnits = None,
                margin_closeout_margin_used: AccountUnits = None, margin_closeout_percent: DecimalNumber = None,
                margin_closeout_position_value: DecimalNumber = None, withdrawal_limit: AccountUnits = None,
                margin_call_margin_used: AccountUnits = None, margin_call_percent: DecimalNumber = None,
                last_transaction_id: TransactionID = None, trades: Array(TradeSummary) = None,
                positions: Array(Position) = None, orders: Array(Order) = None, financing: DecimalNumber = None):

        return Model.__new__(**locals())


class MarketOrderTransaction(Transaction):
    """MarketOrderTransaction(self, instrument: InstrumentName, units: Unit, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=MARKET_ORDER, time_in_force: TimeInForce=FOK, price_bound: PriceValue=None, position_fill: OrderPositionFill=DEFAULT, trade_close: MarketOrderTradeClose=None, long_position_closeout: MarketOrderPositionCloseout=None, short_position_closeout: MarketOrderPositionCloseout=None, margin_closeout: MarketOrderMarginCloseout=None, delayed_trade_close: MarketOrderDelayedTradeClose=None, reason: MarketOrderReason=None, client_extensions: ClientExtensions=None, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None)
A MarketOrderTransaction represents the creation of a Market Order in the
    user's account. A Market Order is an Order that is filled immediately at
    the current market price. Market Orders can be specialized when they are
    created to accomplish a specific tas': 'to' close a Trade, to closeout a
    Position or to particiate in in a Margin closeout.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "MARKET_ORDER" in a MarketOrderTransaction.
        instrument: -- The Market Order's Instrument.
        units: -- The quantity requested to be filled by the Market Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        time_in_force: -- The time-in-force requested for the Market Order.
            Restricted to FOK or IOC for a MarketOrder.
        price_bound: -- The worst price that the client is willing to have the Market Order filled at.
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trade_close: -- Details of the Trade requested to be closed, only provided when
            the Market Order is being used to explicitly close a Trade.
        long_position_closeout: -- Details of the long Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a long Position.
        short_position_closeout: -- Details of the short Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a short Position.
        margin_closeout: -- Details of the Margin Closeout that this Market Order was created for
        delayed_trade_close: -- Details of the delayed Trade close that this Market Order was created for
        reason: -- The reason that the Market Order was created
        client_extensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.

    """

    _summary_format = 'Create Market Order {id} ({reason}): {units} of {instrument}'

    _name_format = 'Create Market Order {id} ({reason}): {units} of {instrument}'

    def __new__(self, instrument: InstrumentName, units: Unit, id: TransactionID = None, time: DateTime = None,
                user_id: int = None, account_id: AccountID = None, batch_id: TransactionID = None,
                request_id: RequestID = None, type: TransactionType = 'MARKET_ORDER',
                time_in_force: TimeInForce = 'FOK', price_bound: PriceValue = None,
                position_fill: OrderPositionFill = 'DEFAULT', trade_close: MarketOrderTradeClose = None,
                long_position_closeout: MarketOrderPositionCloseout = None,
                short_position_closeout: MarketOrderPositionCloseout = None,
                margin_closeout: MarketOrderMarginCloseout = None,
                delayed_trade_close: MarketOrderDelayedTradeClose = None, reason: MarketOrderReason = None,
                client_extensions: ClientExtensions = None, take_profit_on_fill: TakeProfitDetails = None,
                stop_loss_on_fill: StopLossDetails = None, trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None):
        return Model.__new__(**locals())


class MarketOrderRejectTransaction(Transaction):
    """MarketOrderRejectTransaction(self, instrument: InstrumentName, units: Unit, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=MARKET_ORDER_REJECT, time_in_force: TimeInForce=FOK, price_bound: PriceValue=None, position_fill: OrderPositionFill=DEFAULT, trade_close: MarketOrderTradeClose=None, long_position_closeout: MarketOrderPositionCloseout=None, short_position_closeout: MarketOrderPositionCloseout=None, margin_closeout: MarketOrderMarginCloseout=None, delayed_trade_close: MarketOrderDelayedTradeClose=None, reason: MarketOrderReason=None, client_extensions: ClientExtensions=None, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None, reject_reason: TransactionRejectReason=None)
A MarketOrderRejectTransaction represents the rejection of the creation of
    a Market Order.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "MARKET_ORDER_REJECT" in a MarketOrderRejectTransaction.
        instrument: -- The Market Order's Instrument.
        units: -- The quantity requested to be filled by the Market Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        time_in_force: -- The time-in-force requested for the Market Order.
            Restricted to FOK or IOC for a MarketOrder.
        price_bound: -- The worst price that the client is willing to have the Market Order filled at.
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trade_close: -- Details of the Trade requested to be closed, only provided when
            the Market Order is being used to explicitly close a Trade.
        long_position_closeout: -- Details of the long Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a long Position.
        short_position_closeout: -- Details of the short Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a short Position.
        margin_closeout: -- Details of the Margin Closeout that this Market Order was created for
        delayed_trade_close: -- Details of the delayed Trade close that this Market Order was created for
        reason: -- The reason that the Market Order was created
        client_extensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        reject_reason: -- The reason that the Reject Transaction was created

    """

    _summary_format = 'Reject Market Order ({reason}): {units} of {instrument}'

    _name_format = 'Reject Market Order ({reason}): {units} of {instrument}'

    def __new__(self, instrument: InstrumentName, units: Unit, id: TransactionID = None, time: DateTime = None,
                user_id: int = None, account_id: AccountID = None, batch_id: TransactionID = None,
                request_id: RequestID = None, type: TransactionType = 'MARKET_ORDER_REJECT',
                time_in_force: TimeInForce = 'FOK', price_bound: PriceValue = None,
                position_fill: OrderPositionFill = 'DEFAULT', trade_close: MarketOrderTradeClose = None,
                long_position_closeout: MarketOrderPositionCloseout = None,
                short_position_closeout: MarketOrderPositionCloseout = None,
                margin_closeout: MarketOrderMarginCloseout = None,
                delayed_trade_close: MarketOrderDelayedTradeClose = None, reason: MarketOrderReason = None,
                client_extensions: ClientExtensions = None, take_profit_on_fill: TakeProfitDetails = None,
                stop_loss_on_fill: StopLossDetails = None, trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None, reject_reason: TransactionRejectReason = None):
        return Model.__new__(**locals())


class StopLossOrderTransaction(Transaction):
    """StopLossOrderTransaction(self, trade_id: TradeID, price: PriceValue, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=STOP_LOSS_ORDER, client_trade_id: ClientID=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, trigger_condition: OrderTriggerCondition=DEFAULT, reason: StopLossOrderReason=None, client_extensions: ClientExtensions=None, order_fill_transaction_id: TransactionID=None, replaces_order_id: OrderID=None, cancelling_transaction_id: TransactionID=None)
A StopLossOrderTransaction represents the creation of a StopLoss Order in
    the user's Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "STOP_LOSS_ORDER" in a StopLossOrderTransaction.
        trade_id: -- The ID of the Trade to close when the price threshold is breached.
        client_trade_id: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the StopLoss Order. The associated Trade will be
            closed by a market price that is equal to or worse than this threshold.
        time_in_force: -- The time-in-force requested for the StopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for StopLoss Orders.
        gtd_time: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Stop Loss Order was initiated
        client_extensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        order_fill_transaction_id: -- The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        replaces_order_id: -- The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancelling_transaction_id: -- The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    _summary_format = 'Create Stop Loss Order {id} ({reason}): Close Trade {tradeID} @ {price}'

    _name_format = 'Create Stop Loss Order {id} ({reason}): Close Trade {tradeID} @ {price}'

    def __new__(self, trade_id: TradeID, price: PriceValue, id: TransactionID = None, time: DateTime = None,
                user_id: int = None, account_id: AccountID = None, batch_id: TransactionID = None,
                request_id: RequestID = None, type: TransactionType = 'STOP_LOSS_ORDER',
                client_trade_id: ClientID = None, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: StopLossOrderReason = None,
                client_extensions: ClientExtensions = None, order_fill_transaction_id: TransactionID = None,
                replaces_order_id: OrderID = None, cancelling_transaction_id: TransactionID = None):
        return Model.__new__(**locals())


class TrailingStopLossOrderTransaction(Transaction):
    """TrailingStopLossOrderTransaction(self, trade_id: TradeID, distance: PriceValue, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=TRAILING_STOP_LOSS_ORDER, client_trade_id: ClientID=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, trigger_condition: OrderTriggerCondition=DEFAULT, reason: TrailingStopLossOrderReason=None, client_extensions: ClientExtensions=None, order_fill_transaction_id: TransactionID=None, replaces_order_id: OrderID=None, cancelling_transaction_id: TransactionID=None)
A TrailingStopLossOrderTransaction represents the creation of a
    TrailingStopLoss Order in the user's Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TRAILING_STOP_LOSS_ORDER" in a TrailingStopLossOrderTransaction.
        trade_id: -- The ID of the Trade to close when the price threshold is breached.
        client_trade_id: -- The client ID of the Trade to be closed when the price threshold is breached.
        distance: -- The price distance specified for the TrailingStopLoss Order.
        time_in_force: -- The time-in-force requested for the TrailingStopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
        gtd_time: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Trailing Stop Loss Order was initiated
        client_extensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        order_fill_transaction_id: -- The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        replaces_order_id: -- The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancelling_transaction_id: -- The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    _summary_format = 'Create Trailing Stop Loss Order {id} ({reason}): Close Trade {tradeID}'

    _name_format = 'Create Trailing Stop Loss Order {id} ({reason}): Close Trade {tradeID}'

    def __new__(self, trade_id: TradeID, distance: PriceValue, id: TransactionID = None, time: DateTime = None,
                user_id: int = None, account_id: AccountID = None, batch_id: TransactionID = None,
                request_id: RequestID = None, type: TransactionType = 'TRAILING_STOP_LOSS_ORDER',
                client_trade_id: ClientID = None, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: TrailingStopLossOrderReason = None,
                client_extensions: ClientExtensions = None, order_fill_transaction_id: TransactionID = None,
                replaces_order_id: OrderID = None, cancelling_transaction_id: TransactionID = None):
        return Model.__new__(**locals())


class LimitOrder(Order):
    """LimitOrder(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: OrderID=None, create_time: DateTime=None, state: OrderState=None, client_extensions: ClientExtensions=None, type: OrderType=LIMIT, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, position_fill: OrderPositionFill=DEFAULT, trigger_condition: OrderTriggerCondition=DEFAULT, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None, filling_transaction_id: TransactionID=None, filled_time: DateTime=None, trade_opened_id: TradeID=None, trade_reduced_id: TradeID=None, trade_closed_i_ds: Array_TradeID=None, cancelling_transaction_id: TransactionID=None, cancelled_time: DateTime=None, replaces_order_id: OrderID=None, replaced_by_order_id: OrderID=None)
A LimitOrder is an order that is created with a price threshold, and will
    only be filled by a price that is equal to or better than the threshold.

    Attributes:
        id: -- The Order's identifier, unique within the Order's Account.
        create_time: -- The time when the Order was created.
        state: -- The current state of the Order.
        client_extensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        type: -- The type of the Order. Always set to "LIMIT" for Limit Orders.
        instrument: -- The Limit Order's Instrument.
        units: -- The quantity requested to be filled by the Limit Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Limit Order. The Limit Order will only be
            filled by a market price that is equal to or better than this price.
        time_in_force: -- The time-in-force requested for the Limit Order.
        gtd_time: -- The date/time when the Limit Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        take_profit_on_fill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
            a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.
        filling_transaction_id: -- ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filled_time: -- Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        trade_opened_id: -- Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        trade_reduced_id: -- Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        trade_closed_i_ds: -- Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancelling_transaction_id: -- ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelled_time: -- Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replaces_order_id: -- The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replaced_by_order_id: -- The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

        """

    _summary_format = '{units} units of {instrument} @ {price}'

    _name_format = '{units} units of {instrument} @ {price}'

    def __new__(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: OrderID = None,
                create_time: DateTime = None, state: OrderState = None, client_extensions: ClientExtensions = None,
                type: OrderType = 'LIMIT', time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                take_profit_on_fill: TakeProfitDetails = None, stop_loss_on_fill: StopLossDetails = None,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None, filling_transaction_id: TransactionID = None,
                filled_time: DateTime = None, trade_opened_id: TradeID = None, trade_reduced_id: TradeID = None,
                trade_closed_i_ds: Array(TradeID) = None, cancelling_transaction_id: TransactionID = None,
                cancelled_time: DateTime = None, replaces_order_id: OrderID = None,
                replaced_by_order_id: OrderID = None):
        return Model.__new__(**locals())


class MarketIfTouchedOrder(Order):
    """MarketIfTouchedOrder(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: OrderID=None, create_time: DateTime=None, state: OrderState=None, client_extensions: ClientExtensions=None, type: OrderType=MARKET_IF_TOUCHED, price_bound: PriceValue=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, position_fill: OrderPositionFill=DEFAULT, trigger_condition: OrderTriggerCondition=DEFAULT, initial_market_price: PriceValue=None, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None, filling_transaction_id: TransactionID=None, filled_time: DateTime=None, trade_opened_id: TradeID=None, trade_reduced_id: TradeID=None, trade_closed_i_ds: Array_TradeID=None, cancelling_transaction_id: TransactionID=None, cancelled_time: DateTime=None, replaces_order_id: OrderID=None, replaced_by_order_id: OrderID=None)
A MarketIfTouchedOrder is an order that is created with a price threshold,
    and will only be filled by a market price that is touches or crosses the
    threshold.

    Attributes:
        id: -- The Order's identifier, unique within the Order's Account.
        create_time: -- The time when the Order was created.
        state: -- The current state of the Order.
        client_extensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        type: -- The type of the Order. Always set
            to "MARKET_IF_TOUCHED" for Market If Touched Orders.
        instrument: -- The MarketIfTouched Order's Instrument.
        units: -- The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be
            filled by a market price that crosses this price from the direction of the market price
            at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's
            price and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.
        price_bound: -- The worst market price that may be used to fill this MarketIfTouched Order.
        time_in_force: -- The time-in-force requested for the MarketIfTouched Order. Restricted
            to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
        gtd_time: -- The date/time when the MarketIfTouched Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        initial_market_price: -- The Market price at the time when the MarketIfTouched Order was created.
        take_profit_on_fill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
            a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.
        filling_transaction_id: -- ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filled_time: -- Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        trade_opened_id: -- Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        trade_reduced_id: -- Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        trade_closed_i_ds: -- Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancelling_transaction_id: -- ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelled_time: -- Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replaces_order_id: -- The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replaced_by_order_id: -- The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

        """

    _summary_format = '{units} units of {instrument} @ {price}'

    _name_format = '{units} units of {instrument} @ {price}'

    def __new__(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: OrderID = None,
                create_time: DateTime = None, state: OrderState = None, client_extensions: ClientExtensions = None,
                type: OrderType = 'MARKET_IF_TOUCHED', price_bound: PriceValue = None,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                initial_market_price: PriceValue = None, take_profit_on_fill: TakeProfitDetails = None,
                stop_loss_on_fill: StopLossDetails = None, trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None, filling_transaction_id: TransactionID = None,
                filled_time: DateTime = None, trade_opened_id: TradeID = None, trade_reduced_id: TradeID = None,
                trade_closed_i_ds: Array(TradeID) = None, cancelling_transaction_id: TransactionID = None,
                cancelled_time: DateTime = None, replaces_order_id: OrderID = None,
                replaced_by_order_id: OrderID = None):
        return Model.__new__(**locals())


class StopOrder(Order):
    """StopOrder(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: OrderID=None, create_time: DateTime=None, state: OrderState=None, client_extensions: ClientExtensions=None, type: OrderType=STOP, price_bound: PriceValue=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, position_fill: OrderPositionFill=DEFAULT, trigger_condition: OrderTriggerCondition=DEFAULT, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None, filling_transaction_id: TransactionID=None, filled_time: DateTime=None, trade_opened_id: TradeID=None, trade_reduced_id: TradeID=None, trade_closed_i_ds: Array_TradeID=None, cancelling_transaction_id: TransactionID=None, cancelled_time: DateTime=None, replaces_order_id: OrderID=None, replaced_by_order_id: OrderID=None)
A StopOrder is an order that is created with a price threshold, and will
    only be filled by a price that is equal to or worse than the threshold.

    Attributes:
        id: -- The Order's identifier, unique within the Order's Account.
        create_time: -- The time when the Order was created.
        state: -- The current state of the Order.
        client_extensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        type: -- The type of the Order. Always set to "STOP" for Stop Orders.
        instrument: -- The Stop Order's Instrument.
        units: -- The quantity requested to be filled by the Stop Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Stop Order. The Stop Order will only be
            filled by a market price that is equal to or worse than this price.
        price_bound: -- The worst market price that may be used to fill this Stop Order. If the market gaps and
            crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.
        time_in_force: -- The time-in-force requested for the Stop Order.
        gtd_time: -- The date/time when the Stop Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        take_profit_on_fill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
            a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.
        filling_transaction_id: -- ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filled_time: -- Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        trade_opened_id: -- Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        trade_reduced_id: -- Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        trade_closed_i_ds: -- Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancelling_transaction_id: -- ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelled_time: -- Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replaces_order_id: -- The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replaced_by_order_id: -- The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

    """

    _summary_format = '{units} units of {instrument} @ {price}'

    _name_format = '{units} units of {instrument} @ {price}'

    def __new__(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: OrderID = None,
                create_time: DateTime = None, state: OrderState = None, client_extensions: ClientExtensions = None,
                type: OrderType = 'STOP', price_bound: PriceValue = None, time_in_force: TimeInForce = 'GTC',
                gtd_time: DateTime = None, position_fill: OrderPositionFill = 'DEFAULT',
                trigger_condition: OrderTriggerCondition = 'DEFAULT', take_profit_on_fill: TakeProfitDetails = None,
                stop_loss_on_fill: StopLossDetails = None, trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None, filling_transaction_id: TransactionID = None,
                filled_time: DateTime = None, trade_opened_id: TradeID = None, trade_reduced_id: TradeID = None,
                trade_closed_i_ds: Array(TradeID) = None, cancelling_transaction_id: TransactionID = None,
                cancelled_time: DateTime = None, replaces_order_id: OrderID = None,
                replaced_by_order_id: OrderID = None):
        return Model.__new__(**locals())


class OrderFillTransaction(Transaction):
    """OrderFillTransaction(self, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=ORDER_FILL, order_id: OrderID=None, client_order_id: ClientID=None, instrument: InstrumentName=None, units: Unit=None, price: PriceValue=None, full_price: ClientPrice=None, reason: OrderFillReason=None, pl: AccountUnits=None, financing: AccountUnits=None, commission: AccountUnits=None, account_balance: AccountUnits=None, trade_opened: TradeOpen=None, trades_closed: Array_TradeReduce=None, trade_reduced: TradeReduce=None)
An OrderFillTransaction represents the filling of an Order in the client's
    Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "ORDER_FILL" for an OrderFillTransaction.
        order_id: -- The ID of the Order filled.
        client_order_id: -- The client Order ID of the Order filled
            (only provided if the client has assigned one).
        instrument: -- The name of the filled Order's instrument.
        units: -- The number of units filled by the Order.
        price: -- The average market price that the Order was filled at.
        full_price: -- The price in effect for the account at the time of the Order fill.
        reason: -- The reason that an Order was filled
        pl: -- The profit or loss incurred when the Order was filled.
        financing: -- The financing paid or collected when the Order was filled.
        commission: -- The commission charged in the Account's home currency as a result of filling the Order. The
            commission is
            always represented as a positive quantity of the Account's home currency, however it reduces the balance in
            the Account.
        account_balance: -- The Account's balance after the Order was filled.
        trade_opened: -- The Trade that was opened when the Order was filled
            (only provided if filling the Order resulted in a new Trade).
        trades_closed: -- The Trades that were closed when the Order was filled (only
            provided if filling the Order resulted in a closing open Trades).
        trade_reduced: -- The Trade that was reduced when the Order was filled (only
            provided if filling the Order resulted in reducing an open Trade).

    """

    _summary_format = 'Fill Order {orderID} ({reason}): {units} of {instrument} @ {price}'

    _name_format = 'Fill Order {orderID} ({reason}): {units} of {instrument} @ {price}'

    def __new__(self, id: TransactionID = None, time: DateTime = None, user_id: int = None,
                account_id: AccountID = None, batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'ORDER_FILL', order_id: OrderID = None, client_order_id: ClientID = None,
                instrument: InstrumentName = None, units: Unit = None, price: PriceValue = None,
                full_price: ClientPrice = None, reason: OrderFillReason = None, pl: AccountUnits = None,
                financing: AccountUnits = None, commission: AccountUnits = None, account_balance: AccountUnits = None,
                trade_opened: TradeOpen = None, trades_closed: Array(TradeReduce) = None,
                trade_reduced: TradeReduce = None):
        return Model.__new__(**locals())


class StopLossOrderRejectTransaction(Transaction):
    """StopLossOrderRejectTransaction(self, trade_id: TradeID, price: PriceValue, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=STOP_LOSS_ORDER_REJECT, client_trade_id: ClientID=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, trigger_condition: OrderTriggerCondition=DEFAULT, reason: StopLossOrderReason=None, client_extensions: ClientExtensions=None, order_fill_transaction_id: TransactionID=None, intended_replaces_order_id: OrderID=None, reject_reason: TransactionRejectReason=None)
A StopLossOrderRejectTransaction represents the rejection of the creation
    of a StopLoss Order.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "STOP_LOSS_ORDER_REJECT" in a StopLossOrderRejectTransaction.
        trade_id: -- The ID of the Trade to close when the price threshold is breached.
        client_trade_id: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the StopLoss Order. The associated Trade will be
            closed by a market price that is equal to or worse than this threshold.
        time_in_force: -- The time-in-force requested for the StopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for StopLoss Orders.
        gtd_time: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Stop Loss Order was initiated
        client_extensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        order_fill_transaction_id: -- The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        intended_replaces_order_id: -- The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        reject_reason: -- The reason that the Reject Transaction was created

    """

    _summary_format = 'Reject Stop Loss Order ({reason}): Close Trade {tradeID} @ {price}'

    _name_format = 'Reject Stop Loss Order ({reason}): Close Trade {tradeID} @ {price}'

    def __new__(self, trade_id: TradeID, price: PriceValue, id: TransactionID = None, time: DateTime = None,
                user_id: int = None, account_id: AccountID = None, batch_id: TransactionID = None,
                request_id: RequestID = None, type: TransactionType = 'STOP_LOSS_ORDER_REJECT',
                client_trade_id: ClientID = None, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: StopLossOrderReason = None,
                client_extensions: ClientExtensions = None, order_fill_transaction_id: TransactionID = None,
                intended_replaces_order_id: OrderID = None, reject_reason: TransactionRejectReason = None):
        return Model.__new__(**locals())


class MarketIfTouchedOrderTransaction(Transaction):
    """MarketIfTouchedOrderTransaction(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=MARKET_IF_TOUCHED_ORDER, price_bound: PriceValue=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, position_fill: OrderPositionFill=DEFAULT, trigger_condition: OrderTriggerCondition=DEFAULT, reason: MarketIfTouchedOrderReason=None, client_extensions: ClientExtensions=None, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None, replaces_order_id: OrderID=None, cancelling_transaction_id: TransactionID=None)
A MarketIfTouchedOrderTransaction represents the creation of a
    MarketIfTouched Order in the user's Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "MARKET_IF_TOUCHED_ORDER" in a MarketIfTouchedOrderTransaction.
        instrument: -- The MarketIfTouched Order's Instrument.
        units: -- The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be
            filled by a market price that crosses this price from the direction of the market price
            at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's price
            and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.
        price_bound: -- The worst market price that may be used to fill this MarketIfTouched Order.
        time_in_force: -- The time-in-force requested for the MarketIfTouched Order. Restricted
            to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
        gtd_time: -- The date/time when the MarketIfTouched Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Market-if-touched Order was initiated
        client_extensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        replaces_order_id: -- The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancelling_transaction_id: -- The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    _summary_format = 'Create MIT Order {id} ({reason}): {units} of {instrument} @ {price}'

    _name_format = 'Create MIT Order {id} ({reason}): {units} of {instrument} @ {price}'

    def __new__(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID = None,
                time: DateTime = None, user_id: int = None, account_id: AccountID = None,
                batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'MARKET_IF_TOUCHED_ORDER', price_bound: PriceValue = None,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                reason: MarketIfTouchedOrderReason = None, client_extensions: ClientExtensions = None,
                take_profit_on_fill: TakeProfitDetails = None, stop_loss_on_fill: StopLossDetails = None,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None, replaces_order_id: OrderID = None,
                cancelling_transaction_id: TransactionID = None):
        return Model.__new__(**locals())


class LimitOrderTransaction(Transaction):
    """LimitOrderTransaction(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=LIMIT_ORDER, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, position_fill: OrderPositionFill=DEFAULT, trigger_condition: OrderTriggerCondition=DEFAULT, reason: LimitOrderReason=None, client_extensions: ClientExtensions=None, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None, replaces_order_id: OrderID=None, cancelling_transaction_id: TransactionID=None)
A LimitOrderTransaction represents the creation of a Limit Order in the
    user's Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "LIMIT_ORDER" in a LimitOrderTransaction.
        instrument: -- The Limit Order's Instrument.
        units: -- The quantity requested to be filled by the Limit Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Limit Order. The Limit Order will only be
            filled by a market price that is equal to or better than this price.
        time_in_force: -- The time-in-force requested for the Limit Order.
        gtd_time: -- The date/time when the Limit Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Limit Order was initiated
        client_extensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        replaces_order_id: -- The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancelling_transaction_id: -- The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    _summary_format = 'Create Limit Order {id} ({reason}): {units} of {instrument} @ {price}'

    _name_format = 'Create Limit Order {id} ({reason}): {units} of {instrument} @ {price}'

    def __new__(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID = None,
                time: DateTime = None, user_id: int = None, account_id: AccountID = None,
                batch_id: TransactionID = None, request_id: RequestID = None, type: TransactionType = 'LIMIT_ORDER',
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                reason: LimitOrderReason = None, client_extensions: ClientExtensions = None,
                take_profit_on_fill: TakeProfitDetails = None, stop_loss_on_fill: StopLossDetails = None,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None, replaces_order_id: OrderID = None,
                cancelling_transaction_id: TransactionID = None):
        return Model.__new__(**locals())


class TakeProfitOrderRejectTransaction(Transaction):
    """TakeProfitOrderRejectTransaction(self, trade_id: TradeID, price: PriceValue, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=TAKE_PROFIT_ORDER_REJECT, client_trade_id: ClientID=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, trigger_condition: OrderTriggerCondition=DEFAULT, reason: TakeProfitOrderReason=None, client_extensions: ClientExtensions=None, order_fill_transaction_id: TransactionID=None, intended_replaces_order_id: OrderID=None, reject_reason: TransactionRejectReason=None)
A TakeProfitOrderRejectTransaction represents the rejection of the creation
    of a TakeProfit Order.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TAKE_PROFIT_ORDER_REJECT" in a TakeProfitOrderRejectTransaction.
        trade_id: -- The ID of the Trade to close when the price threshold is breached.
        client_trade_id: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the TakeProfit Order. The associated Trade will be
            closed by a market price that is equal to or better than this threshold.
        time_in_force: -- The time-in-force requested for the TakeProfit Order. Restricted
            to "GTC", "GFD" and "GTD" for TakeProfit Orders.
        gtd_time: -- The date/time when the TakeProfit Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Take Profit Order was initiated
        client_extensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        order_fill_transaction_id: -- The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        intended_replaces_order_id: -- The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        reject_reason: -- The reason that the Reject Transaction was created

    """

    _summary_format = 'Reject Take Profit Order ({reason}): Close Trade {tradeID} @ {price}'

    _name_format = 'Reject Take Profit Order ({reason}): Close Trade {tradeID} @ {price}'

    def __new__(self, trade_id: TradeID, price: PriceValue, id: TransactionID = None, time: DateTime = None,
                user_id: int = None, account_id: AccountID = None, batch_id: TransactionID = None,
                request_id: RequestID = None, type: TransactionType = 'TAKE_PROFIT_ORDER_REJECT',
                client_trade_id: ClientID = None, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: TakeProfitOrderReason = None,
                client_extensions: ClientExtensions = None, order_fill_transaction_id: TransactionID = None,
                intended_replaces_order_id: OrderID = None, reject_reason: TransactionRejectReason = None):
        return Model.__new__(**locals())


class TrailingStopLossOrderRejectTransaction(Transaction):
    """TrailingStopLossOrderRejectTransaction(self, trade_id: TradeID, distance: PriceValue, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=TRAILING_STOP_LOSS_ORDER_REJECT, client_trade_id: ClientID=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, trigger_condition: OrderTriggerCondition=DEFAULT, reason: TrailingStopLossOrderReason=None, client_extensions: ClientExtensions=None, order_fill_transaction_id: TransactionID=None, intended_replaces_order_id: OrderID=None, reject_reason: TransactionRejectReason=None)
A TrailingStopLossOrderRejectTransaction represents the rejection of the
    creation of a TrailingStopLoss Order.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TRAILING_STOP_LOSS_ORDER_REJECT" in a TrailingStopLossOrderRejectTransaction.
        trade_id: -- The ID of the Trade to close when the price threshold is breached.
        client_trade_id: -- The client ID of the Trade to be closed when the price threshold is breached.
        distance: -- The price distance specified for the TrailingStopLoss Order.
        time_in_force: -- The time-in-force requested for the TrailingStopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
        gtd_time: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Trailing Stop Loss Order was initiated
        client_extensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        order_fill_transaction_id: -- The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        intended_replaces_order_id: -- The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        reject_reason: -- The reason that the Reject Transaction was created

    """

    _summary_format = 'Reject Trailing Stop Loss Order ({reason}): Close Trade {tradeID}'

    _name_format = 'Reject Trailing Stop Loss Order ({reason}): Close Trade {tradeID}'

    def __new__(self, trade_id: TradeID, distance: PriceValue, id: TransactionID = None, time: DateTime = None,
                user_id: int = None, account_id: AccountID = None, batch_id: TransactionID = None,
                request_id: RequestID = None, type: TransactionType = 'TRAILING_STOP_LOSS_ORDER_REJECT',
                client_trade_id: ClientID = None, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: TrailingStopLossOrderReason = None,
                client_extensions: ClientExtensions = None, order_fill_transaction_id: TransactionID = None,
                intended_replaces_order_id: OrderID = None, reject_reason: TransactionRejectReason = None):
        return Model.__new__(**locals())


class StopOrderTransaction(Transaction):
    """StopOrderTransaction(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=STOP_ORDER, price_bound: PriceValue=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, position_fill: OrderPositionFill=DEFAULT, trigger_condition: OrderTriggerCondition=DEFAULT, reason: StopOrderReason=None, client_extensions: ClientExtensions=None, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None, replaces_order_id: OrderID=None, cancelling_transaction_id: TransactionID=None)
A StopOrderTransaction represents the creation of a Stop Order in the
    user's Account.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "STOP_ORDER" in a StopOrderTransaction.
        instrument: -- The Stop Order's Instrument.
        units: -- The quantity requested to be filled by the Stop Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Stop Order. The Stop Order will only be
            filled by a market price that is equal to or worse than this price.
        price_bound: -- The worst market price that may be used to fill this Stop Order. If the market gaps and
            crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.
        time_in_force: -- The time-in-force requested for the Stop Order.
        gtd_time: -- The date/time when the Stop Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Stop Order was initiated
        client_extensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        replaces_order_id: -- The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancelling_transaction_id: -- The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    _summary_format = 'Create Stop Order {id} ({reason}): {units} of {instrument} @ {price}'

    _name_format = 'Create Stop Order {id} ({reason}): {units} of {instrument} @ {price}'

    def __new__(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID = None,
                time: DateTime = None, user_id: int = None, account_id: AccountID = None,
                batch_id: TransactionID = None, request_id: RequestID = None, type: TransactionType = 'STOP_ORDER',
                price_bound: PriceValue = None, time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                reason: StopOrderReason = None, client_extensions: ClientExtensions = None,
                take_profit_on_fill: TakeProfitDetails = None, stop_loss_on_fill: StopLossDetails = None,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None, replaces_order_id: OrderID = None,
                cancelling_transaction_id: TransactionID = None):
        return Model.__new__(**locals())


class MarketIfTouchedOrderRejectTransaction(Transaction):
    """MarketIfTouchedOrderRejectTransaction(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=MARKET_IF_TOUCHED_ORDER_REJECT, price_bound: PriceValue=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, position_fill: OrderPositionFill=DEFAULT, trigger_condition: OrderTriggerCondition=DEFAULT, reason: MarketIfTouchedOrderReason=None, client_extensions: ClientExtensions=None, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None, intended_replaces_order_id: OrderID=None, reject_reason: TransactionRejectReason=None)
A MarketIfTouchedOrderRejectTransaction represents the rejection of the
    creation of a MarketIfTouched Order.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "MARKET_IF_TOUCHED_ORDER_REJECT" in a MarketIfTouchedOrderRejectTransaction.
        instrument: -- The MarketIfTouched Order's Instrument.
        units: -- The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be
            filled by a market price that crosses this price from the direction of the market price
            at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's price
            and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.
        price_bound: -- The worst market price that may be used to fill this MarketIfTouched Order.
        time_in_force: -- The time-in-force requested for the MarketIfTouched Order. Restricted
            to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
        gtd_time: -- The date/time when the MarketIfTouched Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Market-if-touched Order was initiated
        client_extensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        intended_replaces_order_id: -- The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        reject_reason: -- The reason that the Reject Transaction was created

    """

    _summary_format = 'Reject MIT Order ({reason}): {units} of {instrument} @ {price}'

    _name_format = 'Reject MIT Order ({reason}): {units} of {instrument} @ {price}'

    def __new__(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID = None,
                time: DateTime = None, user_id: int = None, account_id: AccountID = None,
                batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'MARKET_IF_TOUCHED_ORDER_REJECT', price_bound: PriceValue = None,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                reason: MarketIfTouchedOrderReason = None, client_extensions: ClientExtensions = None,
                take_profit_on_fill: TakeProfitDetails = None, stop_loss_on_fill: StopLossDetails = None,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None, intended_replaces_order_id: OrderID = None,
                reject_reason: TransactionRejectReason = None):
        return Model.__new__(**locals())


class LimitOrderRejectTransaction(Transaction):
    """LimitOrderRejectTransaction(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=LIMIT_ORDER_REJECT, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, position_fill: OrderPositionFill=DEFAULT, trigger_condition: OrderTriggerCondition=DEFAULT, reason: LimitOrderReason=None, client_extensions: ClientExtensions=None, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None, intended_replaces_order_id: OrderID=None, reject_reason: TransactionRejectReason=None)
A LimitOrderRejectTransaction represents the rejection of the creation of a
    Limit Order.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "LIMIT_ORDER_REJECT" in a LimitOrderRejectTransaction.
        instrument: -- The Limit Order's Instrument.
        units: -- The quantity requested to be filled by the Limit Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Limit Order. The Limit Order will only be
            filled by a market price that is equal to or better than this price.
        time_in_force: -- The time-in-force requested for the Limit Order.
        gtd_time: -- The date/time when the Limit Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Limit Order was initiated
        client_extensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        intended_replaces_order_id: -- The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        reject_reason: -- The reason that the Reject Transaction was created

    """

    _summary_format = 'Reject Limit Order ({reason}): {units} of {instrument} @ {price}'

    _name_format = 'Reject Limit Order ({reason}): {units} of {instrument} @ {price}'

    def __new__(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID = None,
                time: DateTime = None, user_id: int = None, account_id: AccountID = None,
                batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'LIMIT_ORDER_REJECT', time_in_force: TimeInForce = 'GTC',
                gtd_time: DateTime = None, position_fill: OrderPositionFill = 'DEFAULT',
                trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: LimitOrderReason = None,
                client_extensions: ClientExtensions = None, take_profit_on_fill: TakeProfitDetails = None,
                stop_loss_on_fill: StopLossDetails = None, trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None, intended_replaces_order_id: OrderID = None,
                reject_reason: TransactionRejectReason = None):
        return Model.__new__(**locals())


class StopOrderRejectTransaction(Transaction):
    """StopOrderRejectTransaction(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID=None, time: DateTime=None, user_id: int=None, account_id: AccountID=None, batch_id: TransactionID=None, request_id: RequestID=None, type: TransactionType=STOP_ORDER_REJECT, price_bound: PriceValue=None, time_in_force: TimeInForce=GTC, gtd_time: DateTime=None, position_fill: OrderPositionFill=DEFAULT, trigger_condition: OrderTriggerCondition=DEFAULT, reason: StopOrderReason=None, client_extensions: ClientExtensions=None, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None, intended_replaces_order_id: OrderID=None, reject_reason: TransactionRejectReason=None)
A StopOrderRejectTransaction represents the rejection of the creation of a
    Stop Order.

    Attributes:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        user_id: -- The ID of the user that initiated the creation of the Transaction.
        account_id: -- The ID of the Account the Transaction was created for.
        batch_id: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        request_id: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "STOP_ORDER_REJECT" in a StopOrderRejectTransaction.
        instrument: -- The Stop Order's Instrument.
        units: -- The quantity requested to be filled by the Stop Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Stop Order. The Stop Order will only be
            filled by a market price that is equal to or worse than this price.
        price_bound: -- The worst market price that may be used to fill this Stop Order. If the market gaps and
            crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.
        time_in_force: -- The time-in-force requested for the Stop Order.
        gtd_time: -- The date/time when the Stop Order will
            be cancelled if its timeInForce is "GTD".
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trigger_condition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Stop Order was initiated
        client_extensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        take_profit_on_fill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stop_loss_on_fill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailing_stop_loss_on_fill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        intended_replaces_order_id: -- The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        reject_reason: -- The reason that the Reject Transaction was created

    """

    _summary_format = 'Reject Stop Order ({reason}): {units} of {instrument} @ {price}'

    _name_format = 'Reject Stop Order ({reason}): {units} of {instrument} @ {price}'

    def __new__(self, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID = None,
                time: DateTime = None, user_id: int = None, account_id: AccountID = None,
                batch_id: TransactionID = None, request_id: RequestID = None,
                type: TransactionType = 'STOP_ORDER_REJECT', price_bound: PriceValue = None,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = None,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                reason: StopOrderReason = None, client_extensions: ClientExtensions = None,
                take_profit_on_fill: TakeProfitDetails = None, stop_loss_on_fill: StopLossDetails = None,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None, intended_replaces_order_id: OrderID = None,
                reject_reason: TransactionRejectReason = None):
        return Model.__new__(**locals())


class MarketOrder(Order):
    """MarketOrder(self, instrument: InstrumentName, units: Unit, id: OrderID=None, create_time: DateTime=None, state: OrderState=None, client_extensions: ClientExtensions=None, type: OrderType=MARKET, time_in_force: TimeInForce=FOK, price_bound: PriceValue=None, position_fill: OrderPositionFill=DEFAULT, trade_close: MarketOrderTradeClose=None, long_position_closeout: MarketOrderPositionCloseout=None, short_position_closeout: MarketOrderPositionCloseout=None, margin_closeout: MarketOrderMarginCloseout=None, delayed_trade_close: MarketOrderDelayedTradeClose=None, take_profit_on_fill: TakeProfitDetails=None, stop_loss_on_fill: StopLossDetails=None, trailing_stop_loss_on_fill: TrailingStopLossDetails=None, trade_client_extensions: ClientExtensions=None, filling_transaction_id: TransactionID=None, filled_time: DateTime=None, trade_opened_id: TradeID=None, trade_reduced_id: TradeID=None, trade_closed_i_ds: Array_TradeID=None, cancelling_transaction_id: TransactionID=None, cancelled_time: DateTime=None)
A MarketOrder is an order that is filled immediately upon creation using
    the current market price.

    Attributes:
        id: -- The Order's identifier, unique within the Order's Account.
        create_time: -- The time when the Order was created.
        state: -- The current state of the Order.
        client_extensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        type: -- The type of the Order. Always set to "MARKET" for Market Orders.
        instrument: -- The Market Order's Instrument.
        units: -- The quantity requested to be filled by the Market Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        time_in_force: -- The time-in-force requested for the Market Order.
            Restricted to FOK or IOC for a MarketOrder.
        price_bound: -- The worst price that the client is willing to have the Market Order filled at.
        position_fill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        trade_close: -- Details of the Trade requested to be closed, only provided when
            the Market Order is being used to explicitly close a Trade.
        long_position_closeout: -- Details of the long Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a long Position.
        short_position_closeout: -- Details of the short Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a short Position.
        margin_closeout: -- Details of the Margin Closeout that this Market Order was created for
        delayed_trade_close: -- Details of the delayed Trade close that this Market Order was created for
        take_profit_on_fill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
            modified directly through the Trade.
        stop_loss_on_fill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
            client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
            directly through the Trade.
        trailing_stop_loss_on_fill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
            created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
            Order is modified directly through the Trade.
        trade_client_extensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
            MT4.
        filling_transaction_id: -- ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filled_time: -- Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        trade_opened_id: -- Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        trade_reduced_id: -- Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        trade_closed_i_ds: -- Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancelling_transaction_id: -- ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelled_time: -- Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)

    """

    _summary_format = '{units} units of {instrument}'

    _name_format = '{units} units of {instrument}'

    def __new__(self, instrument: InstrumentName, units: Unit, id: OrderID = None, create_time: DateTime = None,
                state: OrderState = None, client_extensions: ClientExtensions = None, type: OrderType = 'MARKET',
                time_in_force: TimeInForce = 'FOK', price_bound: PriceValue = None,
                position_fill: OrderPositionFill = 'DEFAULT', trade_close: MarketOrderTradeClose = None,
                long_position_closeout: MarketOrderPositionCloseout = None,
                short_position_closeout: MarketOrderPositionCloseout = None,
                margin_closeout: MarketOrderMarginCloseout = None,
                delayed_trade_close: MarketOrderDelayedTradeClose = None,
                take_profit_on_fill: TakeProfitDetails = None, stop_loss_on_fill: StopLossDetails = None,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = None,
                trade_client_extensions: ClientExtensions = None, filling_transaction_id: TransactionID = None,
                filled_time: DateTime = None, trade_opened_id: TradeID = None, trade_reduced_id: TradeID = None,
                trade_closed_i_ds: Array(TradeID) = None, cancelling_transaction_id: TransactionID = None,
                cancelled_time: DateTime = None):
        return Model.__new__(**locals())
