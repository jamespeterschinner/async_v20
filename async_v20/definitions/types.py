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


###  PRIMITIVE ARRAYS ###
class ArrayStr(Array):
    _contains = str


class ArrayTradeID(Array):
    _contains = TradeID


class ArrayTransactionFilter(Array):
    _contains = TransactionFilter


class ArrayTransactionID(Array):
    _contains = TransactionID


class ClientExtensions(Model):
    """A ClientExtensions object allows a client to attach a clientID, tag and
    comment to Orders and Trades in their Account.  Do not set, modify, or
    delete this field if your account is associated with MT4.

    Attributes:
        id: -- The Client ID of the Order/Trade
        tag: -- A tag associated with the Order/Trade
        comment: -- A comment associated with the Order/Trade

    """

    def __new__(cls, id: ClientID = ..., tag: ClientTag = ..., comment: ClientComment = ...):
        return super().__new__(**ClientExtensions._preset_arguments, **locals())


class TakeProfitDetails(Model):
    """TakeProfitDetails specifies the details of a Take Profit Order to be
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

    def __new__(cls, price: PriceValue = ..., time_in_force: TimeInForce = ..., gtd_time: DateTime = ...,
                client_extensions: ClientExtensions = ...):
        return super().__new__(**TakeProfitDetails._preset_arguments, **locals())


class StopLossDetails(Model):
    """StopLossDetails specifies the details of a Stop Loss Order to be created on
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

    def __new__(cls, price: PriceValue = ..., time_in_force: TimeInForce = ..., gtd_time: DateTime = ...,
                client_extensions: ClientExtensions = ...):
        return super().__new__(**StopLossDetails._preset_arguments, **locals())


class TrailingStopLossDetails(Model):
    """TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order
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

    def __new__(cls, distance: PriceValue = ..., time_in_force: TimeInForce = ..., gtd_time: DateTime = ...,
                client_extensions: ClientExtensions = ...):
        return super().__new__(**TrailingStopLossDetails._preset_arguments, **locals())


class OrderRequest(Model):
    """The base Order specification used when requesting that an Order be created.

    Each specific Order-type extends this definition.

    Attributes:

    """

    def __new__(cls, trade_id: TradeID = ..., price: PriceValue = ..., type: OrderType = ...,
                client_trade_id: ClientID = ..., time_in_force: TimeInForce = ..., gtd_time: DateTime = ...,
                trigger_condition: OrderTriggerCondition = ..., client_extensions: ClientExtensions = ...,
                distance: PriceValue = ..., instrument: InstrumentName = ..., units: Unit = ...,
                price_bound: PriceValue = ..., position_fill: OrderPositionFill = ...,
                take_profit_on_fill: TakeProfitDetails = ..., stop_loss_on_fill: StopLossDetails = ...,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ...):
        return super().__new__(**OrderRequest._preset_arguments, **locals())


class UnitsAvailableDetails(Model):
    """Representation of many units of an Instrument are available to be traded
    for both long and short Orders.

    Attributes:
        long: -- The units available for long Orders.
        short: -- The units available for short Orders.

    """

    def __new__(cls, long: Unit = ..., short: Unit = ...):
        return super().__new__(**UnitsAvailableDetails._preset_arguments, **locals())


class UnitsAvailable(Model):
    """Representation of how many units of an Instrument are available to be
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

    def __new__(cls, default: UnitsAvailableDetails = ..., reduce_first: UnitsAvailableDetails = ...,
                reduce_only: UnitsAvailableDetails = ..., open_only: UnitsAvailableDetails = ...):
        return super().__new__(**UnitsAvailable._preset_arguments, **locals())


class LiquidityRegenerationScheduleStep(Model):
    """A liquidity regeneration schedule Step indicates the amount of bid and ask
    liquidity that is used by the Account at a certain time. These amounts will
    only change at the timestamp of the following step.

    Attributes:
        timestamp: -- The timestamp of the schedule step.
        bid_liquidity_used: -- The amount of bid liquidity used at this step in the schedule.
        ask_liquidity_used: -- The amount of ask liquidity used at this step in the schedule.

    """

    def __new__(cls, timestamp: DateTime = ..., bid_liquidity_used: DecimalNumber = ...,
                ask_liquidity_used: DecimalNumber = ...):
        return super().__new__(**LiquidityRegenerationScheduleStep._preset_arguments, **locals())


class ArrayLiquidityRegenerationScheduleStep(Array):
    _contains = LiquidityRegenerationScheduleStep


class LiquidityRegenerationSchedule(Model):
    """A LiquidityRegenerationSchedule indicates how liquidity that is used when
    filling an Order for an instrument is regenerated following the fill.  A
    liquidity regeneration schedule will be in effect until the timestamp of
    its final step, but may be replaced by a schedule created for an Order of
    the same instrument that is filled while it is still in effect.

    Attributes:
        steps: -- The steps in the Liquidity Regeneration Schedule

    """

    def __new__(cls, steps: ArrayLiquidityRegenerationScheduleStep = ...):
        return super().__new__(**LiquidityRegenerationSchedule._preset_arguments, **locals())


class CandlestickData(Model):
    """The price data (open, high, low, close) for the Candlestick representation.

    Attributes:
        o: -- The first (open) price in the time-range represented by the candlestick.
        h: -- The highest price in the time-range represented by the candlestick.
        l: -- The lowest price in the time-range represented by the candlestick.
        c: -- The last (closing) price in the time-range represented by the candlestick.

    """

    def __new__(cls, o: PriceValue = ..., h: PriceValue = ..., l: PriceValue = ..., c: PriceValue = ...):
        return super().__new__(**CandlestickData._preset_arguments, **locals())


class OrderIdentifier(Model):
    """An OrderIdentifier is used to refer to an Order, and contains both the
    OrderID and the ClientOrderID.

    Attributes:
        order_id: -- The OANDA-assigned Order ID
        client_order_id: -- The client-provided client Order ID

    """

    def __new__(cls, order_id: OrderID = ..., client_order_id: ClientID = ...):
        return super().__new__(**OrderIdentifier._preset_arguments, **locals())


class QuoteHomeConversionFactors(Model):
    """QuoteHomeConversionFactors represents the factors that can be used used to
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

    def __new__(cls, positive_units: DecimalNumber = ..., negative_units: DecimalNumber = ...):
        return super().__new__(**QuoteHomeConversionFactors._preset_arguments, **locals())


class MarketOrderMarginCloseout(Model):
    """Details for the Market Order extensions specific to a Market Order placed
    that is part of a Market Order Margin Closeout in a client's account

    Attributes:
        reason: -- The reason the Market Order was created to perform a margin closeout

    """

    def __new__(cls, reason: MarketOrderMarginCloseoutReason = ...):
        return super().__new__(**MarketOrderMarginCloseout._preset_arguments, **locals())


class InstrumentCommission(Model):
    """An InstrumentCommission represents an instrument-specific commission

    Attributes:
        instrument: -- The name of the instrument
        commission: -- The commission amount (in the Account's home
            currency) charged per unitsTraded of the instrument
        units_traded: -- The number of units traded that the commission amount is based on.
        minimum_commission: -- The minimum commission amount (in the Account's home currency) that
            is charged when an Order is filled for this instrument.

    """

    def __new__(cls, instrument: InstrumentName = ..., commission: DecimalNumber = ..., units_traded: Unit = ...,
                minimum_commission: DecimalNumber = ...):
        return super().__new__(**InstrumentCommission._preset_arguments, **locals())


class OrderBookBucket(Model):
    """The order book data for a partition of the instrument's prices.

    Attributes:
        price: -- The lowest price (inclusive) covered by the bucket. The bucket covers the
            price range from the price to price + the order book's bucketWidth.
        long_count_percent: -- The percentage of the total number of orders
            represented by the long orders found in this bucket.
        short_count_percent: -- The percentage of the total number of orders
            represented by the short orders found in this bucket.

    """

    def __new__(cls, price: PriceValue = ..., long_count_percent: DecimalNumber = ...,
                short_count_percent: DecimalNumber = ...):
        return super().__new__(**OrderBookBucket._preset_arguments, **locals())


class ArrayOrderBookBucket(Array):
    _contains = OrderBookBucket


class PositionBookBucket(Model):
    """The position book data for a partition of the instrument's prices.

    Attributes:
        price: -- The lowest price (inclusive) covered by the bucket. The bucket covers the
            price range from the price to price + the position book's bucketWidth.
        long_count_percent: -- The percentage of the total number of positions
            represented by the long positions found in this bucket.
        short_count_percent: -- The percentage of the total number of positions
            represented by the short positions found in this bucket.

    """

    def __new__(cls, price: PriceValue = ..., long_count_percent: DecimalNumber = ...,
                short_count_percent: DecimalNumber = ...):
        return super().__new__(**PositionBookBucket._preset_arguments, **locals())


class ArrayPositionBookBucket(Array):
    _contains = PositionBookBucket


class DynamicOrderState(Model):
    """The dynamic state of an Order. This is only relevant to TrailingStopLoss
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

    def __new__(cls, id: OrderID = ..., trailing_stop_value: PriceValue = ..., trigger_distance: PriceValue = ...,
                is_trigger_distance_exact: bool = ...):
        return super().__new__(**DynamicOrderState._preset_arguments, **locals())


class ArrayDynamicOrderState(Array):
    _contains = DynamicOrderState


class CalculatedPositionState(Model):
    """The dynamic (calculated) state of a Position

    Attributes:
        instrument: -- The Position's Instrument.
        net_unrealized_pl: -- The Position's net unrealized profit/loss
        long_unrealized_pl: -- The unrealized profit/loss of the Position's long open Trades
        short_unrealized_pl: -- The unrealized profit/loss of the Position's short open Trades

    """

    def __new__(cls, instrument: InstrumentName = ..., net_unrealized_pl: AccountUnits = ...,
                long_unrealized_pl: AccountUnits = ..., short_unrealized_pl: AccountUnits = ...):
        return super().__new__(**CalculatedPositionState._preset_arguments, **locals())


class ArrayCalculatedPositionState(Array):
    _contains = CalculatedPositionState


class PositionSide(Model):
    """The representation of a Position for a single direction (long or short).

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

    def __new__(cls, units: Unit = ..., average_price: PriceValue = ..., trade_i_ds: ArrayTradeID = ...,
                pl: AccountUnits = ..., unrealized_pl: AccountUnits = ..., resettable_pl: AccountUnits = ...,
                financing: DecimalNumber = ...):
        return super().__new__(**PositionSide._preset_arguments, **locals())


class Position(Model):
    """The specification of a Position within an Account.

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

    def __new__(cls, instrument: InstrumentName = ..., pl: AccountUnits = ..., unrealized_pl: AccountUnits = ...,
                resettable_pl: AccountUnits = ..., commission: AccountUnits = ..., long: PositionSide = ...,
                short: PositionSide = ..., financing: DecimalNumber = ...):
        return super().__new__(**Position._preset_arguments, **locals())


class ArrayPosition(Array):
    _contains = Position


class PriceBucket(Model):
    """A Price Bucket represents a price available for an amount of liquidity

    Attributes:
        price: -- The Price offered by the PriceBucket
        liquidity: -- The amount of liquidity offered by the PriceBucket

    """

    def __new__(cls, price: PriceValue = ..., liquidity: int = ...):
        return super().__new__(**PriceBucket._preset_arguments, **locals())


class ArrayPriceBucket(Array):
    _contains = PriceBucket


class ClientPrice(Model):
    """Client price for an Account.

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

    def __new__(cls, bids: ArrayPriceBucket = ..., asks: ArrayPriceBucket = ...,
                closeout_bid: PriceValue = ..., closeout_ask: PriceValue = ..., timestamp: DateTime = ...):
        return super().__new__(**ClientPrice._preset_arguments, **locals())


class PricingHeartbeat(Model):
    """A PricingHeartbeat object is injected into the Pricing stream to ensure
    that the HTTP connection remains active.

    Attributes:
        type: -- The string "HEARTBEAT"
        time: -- The date/time when the Heartbeat was created.

    """

    def __new__(cls, type: str = ..., time: DateTime = ...):
        return super().__new__(**PricingHeartbeat._preset_arguments, **locals())


class CalculatedTradeState(Model):
    """The dynamic (calculated) state of an open Trade

    Attributes:
        id: -- The Trade's ID.
        unrealized_pl: -- The Trade's unrealized profit/loss.

    """

    def __new__(cls, id: TradeID = ..., unrealized_pl: AccountUnits = ...):
        return super().__new__(**CalculatedTradeState._preset_arguments, **locals())


class ArrayCalculatedTradeState(Array):
    _contains = CalculatedTradeState


class MarketOrderDelayedTradeClose(Model):
    """Details for the Market Order extensions specific to a Market Order placed
    with the intent of fully closing a specific open trade that should have
    already been closed but wasn't due to halted market conditions

    Attributes:
        trade_id: -- The ID of the Trade being closed
        client_trade_id: -- The Client ID of the Trade being closed
        source_transaction_id: -- The Transaction ID of the DelayedTradeClosure transaction
            to which this Delayed Trade Close belongs to

    """

    def __new__(cls, trade_id: TradeID = ..., client_trade_id: TradeID = ...,
                source_transaction_id: TransactionID = ...):
        return super().__new__(**MarketOrderDelayedTradeClose._preset_arguments, **locals())


class MarketOrderPositionCloseout(Model):
    """A MarketOrderPositionCloseout specifies the extensions to a Market Order
    when it has been created to closeout a specific Position.

    Attributes:
        instrument: -- The instrument of the Position being closed out.
        units: -- Indication of how much of the Position to close. Either "ALL", or a DecimalNumber reflection a
            partial close of the Trade. The DecimalNumber must always be positive, and represent a number that doesn't exceed the absolute
            size of the Position.

    """

    def __new__(cls, instrument: InstrumentName = ..., units: str = ...):
        return super().__new__(**MarketOrderPositionCloseout._preset_arguments, **locals())


class MarketOrderTradeClose(Model):
    """A MarketOrderTradeClose specifies the extensions to a Market Order that has
    been created specifically to close a Trade.

    Attributes:
        trade_id: -- The ID of the Trade requested to be closed
        client_trade_id: -- The client ID of the Trade requested to be closed
        units: -- Indication of how much of the Trade to close. Either
            "ALL", or a DecimalNumber reflection a partial close of the Trade.

    """

    def __new__(cls, trade_id: TradeID = ..., client_trade_id: str = ..., units: str = ...):
        return super().__new__(**MarketOrderTradeClose._preset_arguments, **locals())


class OpenTradeFinancing(Model):
    """OpenTradeFinancing is used to pay/collect daily financing charge for an
    open Trade within an Account

    Attributes:
        trade_id: -- The ID of the Trade that financing is being paid/collected for.
        financing: -- The amount of financing paid/collected for the Trade.

    """

    def __new__(cls, trade_id: TradeID = ..., financing: AccountUnits = ...):
        return super().__new__(**OpenTradeFinancing._preset_arguments, **locals())


class ArrayOpenTradeFinancing(Array):
    _contains = OpenTradeFinancing


class PositionFinancing(Model):
    """OpenTradeFinancing is used to pay/collect daily financing charge for a
    Position within an Account

    Attributes:
        instrument: -- The instrument of the Position that financing is being paid/collected for.
        financing: -- The amount of financing paid/collected for the Position.
        open_trade_financings: -- The financing paid/collecte for each open Trade within the Position.

    """

    def __new__(cls, instrument: InstrumentName = ..., financing: AccountUnits = ...,
                open_trade_financings: ArrayOpenTradeFinancing = ...):
        return super().__new__(**PositionFinancing._preset_arguments, **locals())


class ArrayPositionFinancing(Array):
    _contains = PositionFinancing


class TradeOpen(Model):
    """A TradeOpen object represents a Trade for an instrument that was opened in
    an Account. It is found embedded in Transactions that affect the position
    of an instrument in the Account, specifically the OrderFill Transaction.

    Attributes:
        trade_id: -- The ID of the Trade that was opened
        units: -- The number of units opened by the Trade
        client_extensions: -- The client extensions for the newly opened Trade

    """

    def __new__(cls, trade_id: TradeID = ..., units: Unit = ..., client_extensions: ClientExtensions = ...):
        return super().__new__(**TradeOpen._preset_arguments, **locals())


class VWAPReceipt(Model):
    """A VWAP Receipt provides a record of how the price for an Order fill is
    constructed. If the Order is filled with multiple buckets in a depth of
    market, each bucket will be represented with a VWAP Receipt.

    Attributes:
        units: -- The number of units filled
        price: -- The price at which the units were filled

    """

    def __new__(cls, units: Unit = ..., price: PriceValue = ...):
        return super().__new__(**VWAPReceipt._preset_arguments, **locals())


class UserInfo(Model):
    """A representation of user information, as provided to the user themself.

    Attributes:
        username: -- The user-provided username.
        user_id: -- The user's OANDA-assigned user ID.
        country: -- The country that the user is based in.
        email_address: -- The user's email address.

    """

    def __new__(cls, username: str = ..., user_id: str = ..., country: str = ..., email_address: str = ...):
        return super().__new__(**UserInfo._preset_arguments, **locals())


class AccountProperties(Model):
    """Properties related to an Account.

    Attributes:
        id: -- The Account's identifier
        mt4account_id: -- The Account's associated MT4 Account ID. This field will not
            be present if the Account is not an MT4 account.
        tags: -- The Account's tags

    """

    def __new__(cls, id: AccountID = ..., mt4_account_id: int = ..., tags: ArrayStr = ...):
        return super().__new__(**AccountProperties._preset_arguments, **locals())


class ArrayAccountProperties(Array):
    _contains = AccountProperties


class Candlestick(Model):
    """The Candlestick representation

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

    def __new__(cls, time: DateTime = ..., bid: CandlestickData = ..., ask: CandlestickData = ...,
                mid: CandlestickData = ..., volume: int = ..., complete: bool = ...):
        return super().__new__(**Candlestick._preset_arguments, **locals())


class ArrayCandlestick(Array):
    _contains = Candlestick


class OrderBook(Model):
    """The representation of an instrument's order book at a point in time

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

    def __new__(cls, instrument: InstrumentName = ..., time: DateTime = ..., price: PriceValue = ...,
                bucket_width: PriceValue = ..., buckets: ArrayOrderBookBucket = ...):
        return super().__new__(**OrderBook._preset_arguments, **locals())


class PositionBook(Model):
    """The representation of an instrument's position book at a point in time

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

    def __new__(cls, instrument: InstrumentName = ..., time: DateTime = ..., price: PriceValue = ...,
                bucket_width: PriceValue = ..., buckets: ArrayPositionBookBucket = ...):
        return super().__new__(**PositionBook._preset_arguments, **locals())


class Order(Model):
    """The base Order definition specifies the properties that are common to all
    Orders.

    Attributes:
        id: -- The Order's identifier, unique within the Order's Account.
        create_time: -- The time when the Order was created.
        state: -- The current state of the Order.
        client_extensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.

    """

    # TODO: Update the annotation for partial_fill when OANDA responds to email

    def __new__(cls, id: OrderID = ..., create_time: DateTime = ..., state: OrderState = ...,
                client_extensions: ClientExtensions = ..., trade_id: TradeID = ..., price: PriceValue = ...,
                type: OrderType = ..., client_trade_id: ClientID = ..., time_in_force: TimeInForce = ...,
                gtd_time: DateTime = ..., trigger_condition: OrderTriggerCondition = ...,
                filling_transaction_id: TransactionID = ..., filled_time: DateTime = ...,
                trade_opened_id: TradeID = ..., trade_reduced_id: TradeID = ...,
                trade_closed_i_ds: ArrayTradeID = ..., cancelling_transaction_id: TransactionID = ...,
                cancelled_time: DateTime = ..., replaces_order_id: OrderID = ...,
                replaced_by_order_id: OrderID = ..., distance: PriceValue = ...,
                trailing_stop_value: PriceValue = ..., instrument: InstrumentName = ..., units: Unit = ...,
                partial_fill: str = ..., position_fill: OrderPositionFill = ...,
                take_profit_on_fill: TakeProfitDetails = ...,
                stop_loss_on_fill: StopLossDetails = ..., trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ..., price_bound: PriceValue = ...,
                initial_market_price: PriceValue = ..., trade_close: MarketOrderTradeClose = ...,
                long_position_closeout: MarketOrderPositionCloseout = ...,
                short_position_closeout: MarketOrderPositionCloseout = ...,
                margin_closeout: MarketOrderMarginCloseout = ...,
                delayed_trade_close: MarketOrderDelayedTradeClose = ...,
                trigger_distance: PriceValue = ..., is_trigger_distance_exact: bool = ...):
        return super().__new__(**Order._preset_arguments, **locals())


class ArrayOrder(Array):
    _contains = Order


class TradeReduce(Model):
    """A TradeReduce object represents a Trade for an instrument that was reduced
    (either partially or fully) in an Account. It is found embedded in
    Transactions that affect the position of an instrument in the account,
    specifically the OrderFill Transaction.

    Attributes:
        trade_id: -- The ID of the Trade that was reduced or closed
        units: -- The number of units that the Trade was reduced by
        realized_pl: -- The PL realized when reducing the Trade
        financing: -- The financing paid/collected when reducing the Trade

    """

    def __new__(cls, trade_id: TradeID = ..., units: Unit = ..., realized_pl: AccountUnits = ...,
                financing: AccountUnits = ...):
        return super().__new__(**TradeReduce._preset_arguments, **locals())


class ArrayTradeReduce(Array):
    _contains = TradeReduce


class TransactionHeartbeat(Model):
    """A TransactionHeartbeat object is injected into the Transaction stream to
    ensure that the HTTP connection remains active.

    Attributes:
        type: -- The string "HEARTBEAT"
        last_transaction_id: -- The ID of the most recent Transaction created for the Account
        time: -- The date/time when the TransactionHeartbeat was created.

    """

    def __new__(cls, type: str = ..., last_transaction_id: TransactionID = ..., time: DateTime = ...):
        return super().__new__(**TransactionHeartbeat._preset_arguments, **locals())


class UserInfoExternal(Model):
    """A representation of user information, as available to external (3rd party)
    clients.

    Attributes:
        user_id: -- The user's OANDA-assigned user ID.
        country: -- The country that the user is based in.
        fifo: -- Flag indicating if the the user's Accounts adhere to FIFO execution rules.

    """

    def __new__(cls, user_id: str = ..., country: str = ..., fifo: str = ...):
        return super().__new__(**UserInfoExternal._preset_arguments, **locals())


class TradeSummary(Model):
    """The summary of a Trade within an Account. This representation does not
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

    def __new__(cls, id: TradeID = ..., instrument: InstrumentName = ..., price: PriceValue = ...,
                open_time: DateTime = ..., state: TradeState = ..., initial_units: Unit = ...,
                current_units: Unit = ..., realized_pl: AccountUnits = ..., unrealized_pl: AccountUnits = ...,
                average_close_price: PriceValue = ..., closing_transaction_i_ds: ArrayTransactionID = ...,
                financing: AccountUnits = ..., close_time: DateTime = ...,
                client_extensions: ClientExtensions = ..., take_profit_order_id: OrderID = ...,
                stop_loss_order_id: OrderID = ..., trailing_stop_loss_order_id: OrderID = ...):
        return super().__new__(**TradeSummary._preset_arguments, **locals())


class ArrayTradeSummary(Array):
    _contains = TradeSummary


class Transaction(Model):
    """The base Transaction specification. Specifies properties that are common
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

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                type: TransactionType = ..., extension_number: int = ..., division_id: int = ...,
                site_id: int = ..., account_user_id: int = ..., account_number: int = ...,
                home_currency: Currency = ..., alias: str = ..., margin_rate: DecimalNumber = ...,
                reason: Reason = ..., trade_i_ds: TradeID = ..., order_id: OrderID = ...,
                client_order_id: ClientID = ..., replaced_by_order_id: OrderID = ...,
                closed_trade_id: OrderID = ..., trade_close_transaction_id: TransactionID = ...,
                client_extensions_modify: ClientExtensions = ...,
                trade_client_extensions_modify: ClientExtensions = ..., financing: AccountUnits = ...,
                account_balance: AccountUnits = ..., account_financing_mode: AccountFinancingMode = ...,
                position_financings: ArrayPositionFinancing = ..., trade_id: TradeID = ...,
                client_trade_id: ClientID = ..., price: PriceValue = ..., time_in_force: TimeInForce = ...,
                gtd_time: DateTime = ..., trigger_condition: OrderTriggerCondition = ...,
                client_extensions: ClientExtensions = ..., order_fill_transaction_id: TransactionID = ...,
                replaces_order_id: OrderID = ..., cancelling_transaction_id: TransactionID = ...,
                reject_reason: TransactionRejectReason = ..., amount: AccountUnits = ...,
                funding_reason: FundingReason = ..., comment: str = ..., instrument: InstrumentName = ...,
                units: Unit = ..., price_bound: PriceValue = ..., position_fill: OrderPositionFill = ...,
                trade_close: MarketOrderTradeClose = ..., long_position_closeout: MarketOrderPositionCloseout = ...,
                short_position_closeout: MarketOrderPositionCloseout = ...,
                margin_closeout: MarketOrderMarginCloseout = ...,
                delayed_trade_close: MarketOrderDelayedTradeClose = ...,
                take_profit_on_fill: TakeProfitDetails = ..., stop_loss_on_fill: StopLossDetails = ...,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ..., distance: PriceValue = ...,
                full_price: ClientPrice = ..., pl: AccountUnits = ..., commission: AccountUnits = ...,
                trade_opened: TradeOpen = ..., trades_closed: ArrayTradeReduce = ...,
                trade_reduced: TradeReduce = ..., intended_replaces_order_id: OrderID = ...):
        return super().__new__(**Transaction._preset_arguments, **locals())


class ArrayTransaction(Array):
    _contains = Transaction


class AccountChanges(Model):
    """An AccountChanges Object is used to represent the changes to an Account's
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

    def __new__(cls, orders_created: ArrayOrder = ..., orders_cancelled: ArrayOrder = ...,
                orders_filled: ArrayOrder = ..., orders_triggered: ArrayOrder = ...,
                trades_opened: ArrayTradeSummary = ..., trades_reduced: ArrayTradeSummary = ...,
                trades_closed: ArrayTradeSummary = ..., positions: ArrayPosition = ...,
                transactions: ArrayTransaction = ...):
        return super().__new__(**AccountChanges._preset_arguments, **locals())


class Instrument(Model):
    """Full specification of an Instrument.

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

    def __new__(cls, name: InstrumentName = ..., type: InstrumentType = ..., display_name: str = ...,
                pip_location: int = ..., display_precision: int = ..., trade_units_precision: int = ...,
                minimum_trade_size: Unit = ..., maximum_trailing_stop_distance: Unit = ...,
                minimum_trailing_stop_distance: Unit = ..., maximum_position_size: Unit = ...,
                maximum_order_units: Unit = ..., margin_rate: DecimalNumber = ...,
                commission: InstrumentCommission = ...):
        return super().__new__(**Instrument._preset_arguments, **locals())


class ArrayInstrument(Array):
    _contains = Instrument


class AccountChangesState(Model):
    """An AccountState Object is used to represent an Account's current price-
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

    def __new__(cls, unrealized_pl: AccountUnits = ..., nav: AccountUnits = ..., margin_used: AccountUnits = ...,
                margin_available: AccountUnits = ..., position_value: AccountUnits = ...,
                margin_closeout_unrealized_pl: AccountUnits = ..., margin_closeout_nav: AccountUnits = ...,
                margin_closeout_margin_used: AccountUnits = ..., margin_closeout_percent: DecimalNumber = ...,
                margin_closeout_position_value: DecimalNumber = ..., withdrawal_limit: AccountUnits = ...,
                margin_call_margin_used: AccountUnits = ..., margin_call_percent: DecimalNumber = ...,
                orders: ArrayDynamicOrderState = ..., trades: ArrayCalculatedTradeState = ...,
                positions: ArrayCalculatedPositionState = ...):
        return super().__new__(**AccountChangesState._preset_arguments, **locals())


class Price(Model):
    """The specification of an Account-specific Price.

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

    def __new__(cls, type: str = ..., instrument: InstrumentName = ..., time: DateTime = ...,
                status: PriceStatus = ..., tradeable: bool = ..., bids: ArrayPriceBucket = ...,
                asks: ArrayPriceBucket = ..., closeout_bid: PriceValue = ..., closeout_ask: PriceValue = ...,
                quote_home_conversion_factors: QuoteHomeConversionFactors = ...,
                units_available: UnitsAvailable = ...):
        return super().__new__(**Price._preset_arguments, **locals())


class ArrayPrice(Array):
    _contains = Price


class CloseTransaction(Transaction):
    """A CloseTransaction represents the closing of an Account.

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

    _preset_arguments = {'type': TransactionType('CLOSE')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...):
        return super().__new__(**CloseTransaction._preset_arguments, **locals())


class MarginCallEnterTransaction(Transaction):
    """A MarginCallEnterTransaction is created when an Account enters the margin
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

    _preset_arguments = {'type': TransactionType('MARGIN_CALL_ENTER')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...):
        return super().__new__(**MarginCallEnterTransaction._preset_arguments, **locals())


class MarginCallExitTransaction(Transaction):
    """A MarginCallExitnterTransaction is created when an Account leaves the
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

    _preset_arguments = {'type': TransactionType('MARGIN_CALL_EXIT')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...):
        return super().__new__(**MarginCallExitTransaction._preset_arguments, **locals())


class MarginCallExtendTransaction(Transaction):
    """A MarginCallExtendTransaction is created when the margin call state for an
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

    _preset_arguments = {'type': TransactionType('MARGIN_CALL_EXTEND')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                extension_number: int = ...):
        return super().__new__(**MarginCallExtendTransaction._preset_arguments, **locals())


class ReopenTransaction(Transaction):
    """A ReopenTransaction represents the re-opening of a closed Account.

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

    _preset_arguments = {'type': TransactionType('REOPEN')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...):
        return super().__new__(**ReopenTransaction._preset_arguments, **locals())


class ResetResettablePLTransaction(Transaction):
    """A ResetResettablePLTransaction represents the resetting of the Account's
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

    _preset_arguments = {'type': TransactionType('RESET_RESETTABLE_PL')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...):
        return super().__new__(**ResetResettablePLTransaction._preset_arguments, **locals())


class StopLossOrderRequest(OrderRequest):
    """A StopLossOrderRequest specifies the parameters that may be set when
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

    _preset_arguments = {'type': OrderType('STOP_LOSS')}

    def __new__(cls, trade_id: TradeID, price: PriceValue,
                client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', client_extensions: ClientExtensions = ...):
        return super().__new__(**StopLossOrderRequest._preset_arguments, **locals())


class TakeProfitOrderRequest(OrderRequest):
    """A TakeProfitOrderRequest specifies the parameters that may be set when
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

    _preset_arguments = {'type': OrderType('TAKE_PROFIT')}

    def __new__(cls, trade_id: TradeID, price: PriceValue,
                client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', client_extensions: ClientExtensions = ...):
        return super().__new__(**TakeProfitOrderRequest._preset_arguments, **locals())


class TrailingStopLossOrderRequest(OrderRequest):
    """A TrailingStopLossOrderRequest specifies the parameters that may be set
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

    _preset_arguments = {'type': OrderType('TRAILING_STOP_LOSS')}

    def __new__(cls, trade_id: TradeID, distance: PriceValue,
                client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', client_extensions: ClientExtensions = ...):
        return super().__new__(**TrailingStopLossOrderRequest._preset_arguments, **locals())


class CreateTransaction(Transaction):
    """A CreateTransaction represents the creation of an Account.

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

    _preset_arguments = {'type': TransactionType('CREATE')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                division_id: int = ..., site_id: int = ...,
                account_user_id: int = ..., account_number: int = ..., home_currency: Currency = ...):
        return super().__new__(**CreateTransaction._preset_arguments, **locals())


class ClientConfigureTransaction(Transaction):
    """A ClientConfigureTransaction represents the configuration of an Account by
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

    _preset_arguments = {'type': TransactionType('CLIENT_CONFIGURE')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                alias: str = ..., margin_rate: DecimalNumber = ...):
        return super().__new__(**ClientConfigureTransaction._preset_arguments, **locals())


class DelayedTradeClosureTransaction(Transaction):
    """A DelayedTradeClosure Transaction is created administratively to indicate
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

    _preset_arguments = {'type': TransactionType('DELAYED_TRADE_CLOSURE')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                reason: MarketOrderReason = ...,
                trade_i_ds: TradeID = ...):
        return super().__new__(**DelayedTradeClosureTransaction._preset_arguments, **locals())


class OrderCancelTransaction(Transaction):
    """An OrderCancelTransaction represents the cancellation of an Order in the
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

    _preset_arguments = {'type': TransactionType('ORDER_CANCEL')}

    # TODO wait for OANDA to confirm client_order_id: ClientID

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                order_id: OrderID = ..., client_order_id: ClientID = ...,
                reason: OrderCancelReason = ..., replaced_by_order_id: OrderID = ...,
                closed_trade_id: OrderID = ..., trade_close_transaction_id: TransactionID = ...):
        return super().__new__(**OrderCancelTransaction._preset_arguments, **locals())


class OrderClientExtensionsModifyTransaction(Transaction):
    """A OrderClientExtensionsModifyTransaction represents the modification of an
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

    _preset_arguments = {'type': TransactionType('ORDER_CLIENT_EXTENSIONS_MODIFY')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                order_id: OrderID = ...,
                client_order_id: ClientID = ..., client_extensions_modify: ClientExtensions = ...,
                trade_client_extensions_modify: ClientExtensions = ...):
        return super().__new__(**OrderClientExtensionsModifyTransaction._preset_arguments, **locals())


class DailyFinancingTransaction(Transaction):
    """A DailyFinancingTransaction represents the daily payment/collection of
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

    _preset_arguments = {'type': TransactionType('DAILY_FINANCING')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                financing: AccountUnits = ...,
                account_balance: AccountUnits = ..., account_financing_mode: AccountFinancingMode = ...,
                position_financings: ArrayPositionFinancing = ...):
        return super().__new__(**DailyFinancingTransaction._preset_arguments, **locals())


class TradeClientExtensionsModifyTransaction(Transaction):
    """A TradeClientExtensionsModifyTransaction represents the modification of a
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

    _preset_arguments = {'type': TransactionType('TRADE_CLIENT_EXTENSIONS_MODIFY')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                trade_id: TradeID = ...,
                client_trade_id: ClientID = ..., trade_client_extensions_modify: ClientExtensions = ...):
        return super().__new__(**TradeClientExtensionsModifyTransaction._preset_arguments, **locals())


class AccountSummary(Model):
    """A summary representation of a client's Account. The AccountSummary does not
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

    def __new__(cls, id: AccountID = ..., alias: str = ..., currency: Currency = ..., balance: AccountUnits = ...,
                created_by_user_id: int = ..., created_time: DateTime = ..., pl: AccountUnits = ...,
                resettable_pl: AccountUnits = ..., resettabled_pl_time: DateTime = ...,
                commission: AccountUnits = ..., margin_rate: DecimalNumber = ...,
                margin_call_enter_time: DateTime = ..., margin_call_extension_count: int = ...,
                last_margin_call_extension_time: DateTime = ..., open_trade_count: int = ...,
                open_position_count: int = ..., pending_order_count: int = ..., hedging_enabled: bool = ...,
                unrealized_pl: AccountUnits = ..., nav: AccountUnits = ..., margin_used: AccountUnits = ...,
                margin_available: AccountUnits = ..., position_value: AccountUnits = ...,
                margin_closeout_unrealized_pl: AccountUnits = ..., margin_closeout_nav: AccountUnits = ...,
                margin_closeout_margin_used: AccountUnits = ..., margin_closeout_percent: DecimalNumber = ...,
                margin_closeout_position_value: DecimalNumber = ..., withdrawal_limit: AccountUnits = ...,
                margin_call_margin_used: AccountUnits = ..., margin_call_percent: DecimalNumber = ...,
                last_transaction_id: TransactionID = ..., trades: ArrayTradeSummary = ...,
                positions: ArrayPosition = ..., orders: ArrayOrder = ..., financing: DecimalNumber = ...):
        return super().__new__(**AccountSummary._preset_arguments, **locals())


class MarketOrderRequest(OrderRequest):
    """A MarketOrderRequest specifies the parameters that may be set when creating
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

    _preset_arguments = {'type': OrderType('MARKET')}

    def __new__(cls, instrument: InstrumentName, units: Unit,
                time_in_force: TimeInForce = 'FOK', price_bound: PriceValue = ...,
                position_fill: OrderPositionFill = 'DEFAULT', client_extensions: ClientExtensions = ...,
                take_profit_on_fill: TakeProfitDetails = ..., stop_loss_on_fill: StopLossDetails = ...,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ...):
        return super().__new__(**MarketOrderRequest._preset_arguments, **locals())


class TakeProfitOrderTransaction(Transaction):
    """A TakeProfitOrderTransaction represents the creation of a TakeProfit Order
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

    _preset_arguments = {'type': TransactionType('TAKE_PROFIT_ORDER')}

    def __new__(cls, trade_id: TradeID, price: PriceValue, id: TransactionID = ..., time: DateTime = ...,
                user_id: int = ..., account_id: AccountID = ..., batch_id: TransactionID = ...,
                request_id: RequestID = ...,
                client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: TakeProfitOrderReason = ...,
                client_extensions: ClientExtensions = ..., order_fill_transaction_id: TransactionID = ...,
                replaces_order_id: OrderID = ..., cancelling_transaction_id: TransactionID = ...):
        return super().__new__(**TakeProfitOrderTransaction._preset_arguments, **locals())


class TakeProfitOrder(Order):
    """A TakeProfitOrder is an order that is linked to an open Trade and created
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

    _preset_arguments = {'type': OrderType('TAKE_PROFIT')}

    def __new__(cls, trade_id: TradeID, price: PriceValue, id: OrderID = ..., create_time: DateTime = ...,
                state: OrderState = ..., client_extensions: ClientExtensions = ...,
                client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', filling_transaction_id: TransactionID = ...,
                filled_time: DateTime = ..., trade_opened_id: TradeID = ..., trade_reduced_id: TradeID = ...,
                trade_closed_i_ds: ArrayTradeID = ..., cancelling_transaction_id: TransactionID = ...,
                cancelled_time: DateTime = ..., replaces_order_id: OrderID = ...,
                replaced_by_order_id: OrderID = ...):
        return super().__new__(**TakeProfitOrder._preset_arguments, **locals())


class StopLossOrder(Order):
    """A StopLossOrder is an order that is linked to an open Trade and created
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

    _preset_arguments = {'type': OrderType('STOP_LOSS')}

    def __new__(cls, trade_id: TradeID, price: PriceValue, id: OrderID = ..., create_time: DateTime = ...,
                state: OrderState = ..., client_extensions: ClientExtensions = ...,
                client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', filling_transaction_id: TransactionID = ...,
                filled_time: DateTime = ..., trade_opened_id: TradeID = ..., trade_reduced_id: TradeID = ...,
                trade_closed_i_ds: ArrayTradeID = ..., cancelling_transaction_id: TransactionID = ...,
                cancelled_time: DateTime = ..., replaces_order_id: OrderID = ...,
                replaced_by_order_id: OrderID = ...):
        return super().__new__(**StopLossOrder._preset_arguments, **locals())


class TrailingStopLossOrder(Order):
    """A TrailingStopLossOrder is an order that is linked to an open Trade and
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

    _preset_arguments = {'type': OrderType('TRAILING_STOP_LOSS')}

    def __new__(cls, trade_id: TradeID, distance: PriceValue, id: OrderID = ..., create_time: DateTime = ...,
                state: OrderState = ..., client_extensions: ClientExtensions = ..., client_trade_id: ClientID = ...,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', trailing_stop_value: PriceValue = ...,
                filling_transaction_id: TransactionID = ..., filled_time: DateTime = ...,
                trade_opened_id: TradeID = ..., trade_reduced_id: TradeID = ...,
                trade_closed_i_ds: ArrayTradeID = ..., cancelling_transaction_id: TransactionID = ...,
                cancelled_time: DateTime = ..., replaces_order_id: OrderID = ...,
                replaced_by_order_id: OrderID = ...):
        return super().__new__(**TrailingStopLossOrder._preset_arguments, **locals())


class Trade(Model):
    """The specification of a Trade within an Account. This includes the full
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

    def __new__(cls, id: TradeID = ..., instrument: InstrumentName = ..., price: PriceValue = ...,
                open_time: DateTime = ..., state: TradeState = ..., initial_units: Unit = ...,
                current_units: Unit = ..., realized_pl: AccountUnits = ...,
                unrealized_pl: AccountUnits = ..., average_close_price: PriceValue = ...,
                closing_transaction_i_ds: ArrayTransactionID = ..., financing: AccountUnits = ...,
                close_time: DateTime = ..., client_extensions: ClientExtensions = ...,
                take_profit_order: TakeProfitOrder = ..., stop_loss_order: StopLossOrder = ...,
                trailing_stop_loss_order: TrailingStopLossOrder = ...):
        return super().__new__(**Trade._preset_arguments, **locals())


class ArrayTrade(Array):
    _contains = Trade


class ClientConfigureRejectTransaction(Transaction):
    """A ClientConfigureRejectTransaction represents the reject of configuration
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

    _preset_arguments = {'type': TransactionType('CLIENT_CONFIGURE_REJECT')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                alias: str = ...,
                margin_rate: DecimalNumber = ..., reject_reason: TransactionRejectReason = ...):
        return super().__new__(**ClientConfigureRejectTransaction._preset_arguments, **locals())


class OrderCancelRejectTransaction(Transaction):
    """An OrderCancelRejectTransaction represents the rejection of the
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

    _preset_arguments = {'type': TransactionType('ORDER_CANCEL_REJECT')}

    # TODO wait for OANDA to confirm client_order_id: ClientID

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                order_id: OrderID = ...,
                client_order_id: ClientID = ..., reason: OrderCancelReason = ...,
                reject_reason: TransactionRejectReason = ...):
        return super().__new__(**OrderCancelRejectTransaction._preset_arguments, **locals())


class OrderClientExtensionsModifyRejectTransaction(Transaction):
    """A OrderClientExtensionsModifyRejectTransaction represents the rejection of
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

    _preset_arguments = {'type': TransactionType('ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT'),
                         'args_have_been_formatted': True}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                order_id: OrderID = ...,
                client_order_id: ClientID = ..., client_extensions_modify: ClientExtensions = ...,
                trade_client_extensions_modify: ClientExtensions = ...,
                reject_reason: TransactionRejectReason = ...):
        return super().__new__(**OrderClientExtensionsModifyRejectTransaction._preset_arguments, **locals())


class TradeClientExtensionsModifyRejectTransaction(Transaction):
    """A TradeClientExtensionsModifyRejectTransaction represents the rejection of
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

    _preset_arguments = {'type': TransactionType('TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT'),
                         'args_have_been_formatted': True}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                trade_id: TradeID = ...,
                client_trade_id: ClientID = ..., trade_client_extensions_modify: ClientExtensions = ...,
                reject_reason: TransactionRejectReason = ...):
        return super().__new__(**TradeClientExtensionsModifyRejectTransaction._preset_arguments, **locals())


class TransferFundsTransaction(Transaction):
    """A TransferFundsTransaction represents the transfer of funds in/out of an
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

    _preset_arguments = {'type': TransactionType('TRANSFER_FUNDS')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                amount: AccountUnits = ...,
                funding_reason: FundingReason = ..., comment: str = ..., account_balance: AccountUnits = ...):
        return super().__new__(**TransferFundsTransaction._preset_arguments, **locals())


class TransferFundsRejectTransaction(Transaction):
    """A TransferFundsRejectTransaction represents the rejection of the transfer
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

    _preset_arguments = {'type': TransactionType('TRANSFER_FUNDS_REJECT')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                amount: AccountUnits = ...,
                funding_reason: FundingReason = ..., comment: str = ...,
                reject_reason: TransactionRejectReason = ...):
        return super().__new__(**TransferFundsRejectTransaction._preset_arguments, **locals())


class LimitOrderRequest(OrderRequest):
    """A LimitOrderRequest specifies the parameters that may be set when creating
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

    _preset_arguments = {'type': OrderType('LIMIT')}

    def __new__(cls, instrument: InstrumentName, units: Unit, price: PriceValue,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                client_extensions: ClientExtensions = ..., take_profit_on_fill: TakeProfitDetails = ...,
                stop_loss_on_fill: StopLossDetails = ..., trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ...):
        return super().__new__(**LimitOrderRequest._preset_arguments, **locals())


class MarketIfTouchedOrderRequest(OrderRequest):
    """A MarketIfTouchedOrderRequest specifies the parameters that may be set when
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

    _preset_arguments = {'type': OrderType('MARKET_IF_TOUCHED')}

    def __new__(cls, instrument: InstrumentName, units: Unit, price: PriceValue, price_bound: PriceValue = ...,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                client_extensions: ClientExtensions = ..., take_profit_on_fill: TakeProfitDetails = ...,
                stop_loss_on_fill: StopLossDetails = ..., trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ...):
        return super().__new__(**MarketIfTouchedOrderRequest._preset_arguments, **locals())


class StopOrderRequest(OrderRequest):
    """A StopOrderRequest specifies the parameters that may be set when creating a
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

    _preset_arguments = {'type': OrderType('STOP')}

    def __new__(cls, instrument: InstrumentName, units: Unit, price: PriceValue,
                price_bound: PriceValue = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                client_extensions: ClientExtensions = ..., take_profit_on_fill: TakeProfitDetails = ...,
                stop_loss_on_fill: StopLossDetails = ..., trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ...):
        return super().__new__(**StopOrderRequest._preset_arguments, **locals())


class Account(AccountSummary):
    """The full details of a client's Account. This includes full open Trade, open
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

    def __new__(cls, id: AccountID = ..., alias: str = ..., currency: Currency = ..., balance: AccountUnits = ...,
                created_by_user_id: int = ..., created_time: DateTime = ..., pl: AccountUnits = ...,
                resettable_pl: AccountUnits = ..., resettabled_pl_time: DateTime = ...,
                commission: AccountUnits = ..., margin_rate: DecimalNumber = ...,
                margin_call_enter_time: DateTime = ..., margin_call_extension_count: int = ...,
                last_margin_call_extension_time: DateTime = ..., open_trade_count: int = ...,
                open_position_count: int = ..., pending_order_count: int = ..., hedging_enabled: bool = ...,
                unrealized_pl: AccountUnits = ..., nav: AccountUnits = ..., margin_used: AccountUnits = ...,
                margin_available: AccountUnits = ..., position_value: AccountUnits = ...,
                margin_closeout_unrealized_pl: AccountUnits = ..., margin_closeout_nav: AccountUnits = ...,
                margin_closeout_margin_used: AccountUnits = ..., margin_closeout_percent: DecimalNumber = ...,
                margin_closeout_position_value: DecimalNumber = ..., withdrawal_limit: AccountUnits = ...,
                margin_call_margin_used: AccountUnits = ..., margin_call_percent: DecimalNumber = ...,
                last_transaction_id: TransactionID = ..., trades: ArrayTradeSummary = ...,
                positions: ArrayPosition = ..., orders: ArrayOrder = ..., financing: DecimalNumber = ...):
        return super().__new__(**Account._preset_arguments, **locals())


class MarketOrderTransaction(Transaction):
    """A MarketOrderTransaction represents the creation of a Market Order in the
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

    _preset_arguments = {'type': TransactionType('MARKET_ORDER')}

    def __new__(cls, instrument: InstrumentName, units: Unit, id: TransactionID = ..., time: DateTime = ...,
                user_id: int = ..., account_id: AccountID = ..., batch_id: TransactionID = ...,
                request_id: RequestID = ...,
                time_in_force: TimeInForce = 'FOK', price_bound: PriceValue = ...,
                position_fill: OrderPositionFill = 'DEFAULT', trade_close: MarketOrderTradeClose = ...,
                long_position_closeout: MarketOrderPositionCloseout = ...,
                short_position_closeout: MarketOrderPositionCloseout = ...,
                margin_closeout: MarketOrderMarginCloseout = ...,
                delayed_trade_close: MarketOrderDelayedTradeClose = ..., reason: MarketOrderReason = ...,
                client_extensions: ClientExtensions = ..., take_profit_on_fill: TakeProfitDetails = ...,
                stop_loss_on_fill: StopLossDetails = ..., trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ...):
        return super().__new__(**MarketOrderTransaction._preset_arguments, **locals())


class MarketOrderRejectTransaction(Transaction):
    """A MarketOrderRejectTransaction represents the rejection of the creation of
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

    _preset_arguments = {'type': TransactionType('MARKET_ORDER_REJECT')}

    def __new__(cls, instrument: InstrumentName, units: Unit, id: TransactionID = ..., time: DateTime = ...,
                user_id: int = ..., account_id: AccountID = ..., batch_id: TransactionID = ...,
                request_id: RequestID = ...,
                time_in_force: TimeInForce = 'FOK', price_bound: PriceValue = ...,
                position_fill: OrderPositionFill = 'DEFAULT', trade_close: MarketOrderTradeClose = ...,
                long_position_closeout: MarketOrderPositionCloseout = ...,
                short_position_closeout: MarketOrderPositionCloseout = ...,
                margin_closeout: MarketOrderMarginCloseout = ...,
                delayed_trade_close: MarketOrderDelayedTradeClose = ..., reason: MarketOrderReason = ...,
                client_extensions: ClientExtensions = ..., take_profit_on_fill: TakeProfitDetails = ...,
                stop_loss_on_fill: StopLossDetails = ..., trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ..., reject_reason: TransactionRejectReason = ...):
        return super().__new__(**MarketOrderRejectTransaction._preset_arguments, **locals())


class StopLossOrderTransaction(Transaction):
    """A StopLossOrderTransaction represents the creation of a StopLoss Order in
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

    _preset_arguments = {'type': TransactionType('STOP_LOSS_ORDER')}

    def __new__(cls, trade_id: TradeID, price: PriceValue, id: TransactionID = ..., time: DateTime = ...,
                user_id: int = ..., account_id: AccountID = ..., batch_id: TransactionID = ...,
                request_id: RequestID = ...,
                client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: StopLossOrderReason = ...,
                client_extensions: ClientExtensions = ..., order_fill_transaction_id: TransactionID = ...,
                replaces_order_id: OrderID = ..., cancelling_transaction_id: TransactionID = ...):
        return super().__new__(**StopLossOrderTransaction._preset_arguments, **locals())


class TrailingStopLossOrderTransaction(Transaction):
    """A TrailingStopLossOrderTransaction represents the creation of a
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

    _preset_arguments = {'type': TransactionType('TRAILING_STOP_LOSS_ORDER')}

    def __new__(cls, trade_id: TradeID, distance: PriceValue, id: TransactionID = ..., time: DateTime = ...,
                user_id: int = ..., account_id: AccountID = ..., batch_id: TransactionID = ...,
                request_id: RequestID = ...,
                client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: TrailingStopLossOrderReason = ...,
                client_extensions: ClientExtensions = ..., order_fill_transaction_id: TransactionID = ...,
                replaces_order_id: OrderID = ..., cancelling_transaction_id: TransactionID = ...):
        return super().__new__(**TrailingStopLossOrderTransaction._preset_arguments, **locals())


class LimitOrder(Order):
    """A LimitOrder is an order that is created with a price threshold, and will
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
    _preset_arguments = {'type': OrderType('LIMIT')}

    def __new__(cls, instrument: InstrumentName, units: Unit, price: PriceValue, id: OrderID = ...,
                create_time: DateTime = ..., state: OrderState = ..., client_extensions: ClientExtensions = ...,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                take_profit_on_fill: TakeProfitDetails = ..., stop_loss_on_fill: StopLossDetails = ...,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ..., filling_transaction_id: TransactionID = ...,
                filled_time: DateTime = ..., trade_opened_id: TradeID = ..., trade_reduced_id: TradeID = ...,
                trade_closed_i_ds: ArrayTradeID = ..., cancelling_transaction_id: TransactionID = ...,
                cancelled_time: DateTime = ..., replaces_order_id: OrderID = ...,
                replaced_by_order_id: OrderID = ...):
        return super().__new__(**LimitOrder._preset_arguments, **locals())


class MarketIfTouchedOrder(Order):
    """A MarketIfTouchedOrder is an order that is created with a price threshold,
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

    _preset_arguments = {'type': OrderType('MARKET_IF_TOUCHED')}

    def __new__(cls, instrument: InstrumentName, units: Unit, price: PriceValue, id: OrderID = ...,
                create_time: DateTime = ..., state: OrderState = ..., client_extensions: ClientExtensions = ...,
                price_bound: PriceValue = ...,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                initial_market_price: PriceValue = ..., take_profit_on_fill: TakeProfitDetails = ...,
                stop_loss_on_fill: StopLossDetails = ..., trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ..., filling_transaction_id: TransactionID = ...,
                filled_time: DateTime = ..., trade_opened_id: TradeID = ..., trade_reduced_id: TradeID = ...,
                trade_closed_i_ds: ArrayTradeID = ..., cancelling_transaction_id: TransactionID = ...,
                cancelled_time: DateTime = ..., replaces_order_id: OrderID = ...,
                replaced_by_order_id: OrderID = ...):
        return super().__new__(**MarketIfTouchedOrder._preset_arguments, **locals())


class StopOrder(Order):
    """A StopOrder is an order that is created with a price threshold, and will
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

    _preset_arguments = {'type': OrderType('STOP')}

    def __new__(cls, instrument: InstrumentName, units: Unit, price: PriceValue, id: OrderID = ...,
                create_time: DateTime = ..., state: OrderState = ..., client_extensions: ClientExtensions = ...,
                price_bound: PriceValue = ..., time_in_force: TimeInForce = 'GTC',
                gtd_time: DateTime = ..., position_fill: OrderPositionFill = 'DEFAULT',
                trigger_condition: OrderTriggerCondition = 'DEFAULT', take_profit_on_fill: TakeProfitDetails = ...,
                stop_loss_on_fill: StopLossDetails = ..., trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ..., filling_transaction_id: TransactionID = ...,
                filled_time: DateTime = ..., trade_opened_id: TradeID = ..., trade_reduced_id: TradeID = ...,
                trade_closed_i_ds: ArrayTradeID = ..., cancelling_transaction_id: TransactionID = ...,
                cancelled_time: DateTime = ..., replaces_order_id: OrderID = ...,
                replaced_by_order_id: OrderID = ...):
        return super().__new__(**StopOrder._preset_arguments, **locals())


class OrderFillTransaction(Transaction):
    """An OrderFillTransaction represents the filling of an Order in the client's
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

    _preset_arguments = {'type': TransactionType('ORDER_FILL')}

    def __new__(cls, id: TransactionID = ..., time: DateTime = ..., user_id: int = ...,
                account_id: AccountID = ..., batch_id: TransactionID = ..., request_id: RequestID = ...,
                order_id: OrderID = ..., client_order_id: ClientID = ...,
                instrument: InstrumentName = ..., units: Unit = ..., price: PriceValue = ...,
                full_price: ClientPrice = ..., reason: OrderFillReason = ..., pl: AccountUnits = ...,
                financing: AccountUnits = ..., commission: AccountUnits = ..., account_balance: AccountUnits = ...,
                trade_opened: TradeOpen = ..., trades_closed: ArrayTradeReduce = ...,
                trade_reduced: TradeReduce = ...):
        return super().__new__(**OrderFillTransaction._preset_arguments, **locals())


class StopLossOrderRejectTransaction(Transaction):
    """A StopLossOrderRejectTransaction represents the rejection of the creation
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

    _preset_arguments = {'type': TransactionType('STOP_LOSS_ORDER_REJECT')}

    def __new__(cls, trade_id: TradeID, price: PriceValue, id: TransactionID = ..., time: DateTime = ...,
                user_id: int = ..., account_id: AccountID = ..., batch_id: TransactionID = ...,
                request_id: RequestID = ...,
                client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: StopLossOrderReason = ...,
                client_extensions: ClientExtensions = ..., order_fill_transaction_id: TransactionID = ...,
                intended_replaces_order_id: OrderID = ..., reject_reason: TransactionRejectReason = ...):
        return super().__new__(**StopLossOrderRejectTransaction._preset_arguments, **locals())


class MarketIfTouchedOrderTransaction(Transaction):
    """A MarketIfTouchedOrderTransaction represents the creation of a
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

    _preset_arguments = {'type': TransactionType('MARKET_IF_TOUCHED_ORDER')}

    def __new__(cls, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID = ...,
                time: DateTime = ..., user_id: int = ..., account_id: AccountID = ...,
                batch_id: TransactionID = ..., request_id: RequestID = ..., price_bound: PriceValue = ...,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                reason: MarketIfTouchedOrderReason = ..., client_extensions: ClientExtensions = ...,
                take_profit_on_fill: TakeProfitDetails = ..., stop_loss_on_fill: StopLossDetails = ...,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ..., replaces_order_id: OrderID = ...,
                cancelling_transaction_id: TransactionID = ...):
        return super().__new__(**MarketIfTouchedOrderTransaction._preset_arguments, **locals())


class LimitOrderTransaction(Transaction):
    """A LimitOrderTransaction represents the creation of a Limit Order in the
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

    _preset_arguments = {'type': TransactionType('LIMIT_ORDER')}

    def __new__(cls, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID = ...,
                time: DateTime = ..., user_id: int = ..., account_id: AccountID = ...,
                batch_id: TransactionID = ..., request_id: RequestID = ...,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                reason: LimitOrderReason = ..., client_extensions: ClientExtensions = ...,
                take_profit_on_fill: TakeProfitDetails = ..., stop_loss_on_fill: StopLossDetails = ...,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ..., replaces_order_id: OrderID = ...,
                cancelling_transaction_id: TransactionID = ...):
        return super().__new__(**LimitOrderTransaction._preset_arguments, **locals())


class TakeProfitOrderRejectTransaction(Transaction):
    """A TakeProfitOrderRejectTransaction represents the rejection of the creation
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

    _preset_arguments = {'type': TransactionType('TAKE_PROFIT_ORDER_REJECT')}

    def __new__(cls, trade_id: TradeID, price: PriceValue, id: TransactionID = ..., time: DateTime = ...,
                user_id: int = ..., account_id: AccountID = ..., batch_id: TransactionID = ...,
                request_id: RequestID = ...,
                client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: TakeProfitOrderReason = ...,
                client_extensions: ClientExtensions = ..., order_fill_transaction_id: TransactionID = ...,
                intended_replaces_order_id: OrderID = ..., reject_reason: TransactionRejectReason = ...):
        return super().__new__(**TakeProfitOrderRejectTransaction._preset_arguments, **locals())


class TrailingStopLossOrderRejectTransaction(Transaction):
    """A TrailingStopLossOrderRejectTransaction represents the rejection of the
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

    _preset_arguments = {'type': TransactionType('TRAILING_STOP_LOSS_ORDER_REJECT')}

    def __new__(cls, trade_id: TradeID, distance: PriceValue, id: TransactionID = ..., time: DateTime = ...,
                user_id: int = ..., account_id: AccountID = ..., batch_id: TransactionID = ...,
                request_id: RequestID = ...,
                client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: TrailingStopLossOrderReason = ...,
                client_extensions: ClientExtensions = ..., order_fill_transaction_id: TransactionID = ...,
                intended_replaces_order_id: OrderID = ..., reject_reason: TransactionRejectReason = ...):
        return super().__new__(**TrailingStopLossOrderRejectTransaction._preset_arguments, **locals())


class StopOrderTransaction(Transaction):
    """A StopOrderTransaction represents the creation of a Stop Order in the
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

    _preset_arguments = {'type': TransactionType('STOP_ORDER')}

    def __new__(cls, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID = ...,
                time: DateTime = ..., user_id: int = ..., account_id: AccountID = ...,
                batch_id: TransactionID = ..., request_id: RequestID = ...,
                price_bound: PriceValue = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                reason: StopOrderReason = ..., client_extensions: ClientExtensions = ...,
                take_profit_on_fill: TakeProfitDetails = ..., stop_loss_on_fill: StopLossDetails = ...,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ..., replaces_order_id: OrderID = ...,
                cancelling_transaction_id: TransactionID = ...):
        return super().__new__(**StopOrderTransaction._preset_arguments, **locals())


class MarketIfTouchedOrderRejectTransaction(Transaction):
    """A MarketIfTouchedOrderRejectTransaction represents the rejection of the
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

    _preset_arguments = {'type': TransactionType('MARKET_IF_TOUCHED_ORDER_REJECT')}

    def __new__(cls, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID = ...,
                time: DateTime = ..., user_id: int = ..., account_id: AccountID = ...,
                batch_id: TransactionID = ..., request_id: RequestID = ..., price_bound: PriceValue = ...,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                reason: MarketIfTouchedOrderReason = ..., client_extensions: ClientExtensions = ...,
                take_profit_on_fill: TakeProfitDetails = ..., stop_loss_on_fill: StopLossDetails = ...,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ..., intended_replaces_order_id: OrderID = ...,
                reject_reason: TransactionRejectReason = ...):
        return super().__new__(**MarketIfTouchedOrderRejectTransaction._preset_arguments, **locals())


class LimitOrderRejectTransaction(Transaction):
    """A LimitOrderRejectTransaction represents the rejection of the creation of a
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

    _preset_arguments = {'type': TransactionType('LIMIT_ORDER_REJECT')}

    def __new__(cls, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID = ...,
                time: DateTime = ..., user_id: int = ..., account_id: AccountID = ...,
                batch_id: TransactionID = ..., request_id: RequestID = ..., time_in_force: TimeInForce = 'GTC',
                gtd_time: DateTime = ..., position_fill: OrderPositionFill = 'DEFAULT',
                trigger_condition: OrderTriggerCondition = 'DEFAULT', reason: LimitOrderReason = ...,
                client_extensions: ClientExtensions = ..., take_profit_on_fill: TakeProfitDetails = ...,
                stop_loss_on_fill: StopLossDetails = ..., trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ..., intended_replaces_order_id: OrderID = ...,
                reject_reason: TransactionRejectReason = ...):
        return super().__new__(**LimitOrderRejectTransaction._preset_arguments, **locals())


class StopOrderRejectTransaction(Transaction):
    """A StopOrderRejectTransaction represents the rejection of the creation of a
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

    _preset_arguments = {'type': TransactionType('STOP_ORDER_REJECT')}

    def __new__(cls, instrument: InstrumentName, units: Unit, price: PriceValue, id: TransactionID = ...,
                time: DateTime = ..., user_id: int = ..., account_id: AccountID = ...,
                batch_id: TransactionID = ..., request_id: RequestID = ..., price_bound: PriceValue = ...,
                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                reason: StopOrderReason = ..., client_extensions: ClientExtensions = ...,
                take_profit_on_fill: TakeProfitDetails = ..., stop_loss_on_fill: StopLossDetails = ...,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ..., intended_replaces_order_id: OrderID = ...,
                reject_reason: TransactionRejectReason = ...):
        return super().__new__(**StopOrderRejectTransaction._preset_arguments, **locals())


class MarketOrder(Order):
    """A MarketOrder is an order that is filled immediately upon creation using
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

    _preset_arguments = {'type': OrderType('MARKET')}

    def __new__(cls, instrument: InstrumentName, units: Unit, id: OrderID = ..., create_time: DateTime = ...,
                state: OrderState = ..., client_extensions: ClientExtensions = ...,
                time_in_force: TimeInForce = 'FOK', price_bound: PriceValue = ...,
                position_fill: OrderPositionFill = 'DEFAULT', trade_close: MarketOrderTradeClose = ...,
                long_position_closeout: MarketOrderPositionCloseout = ...,
                short_position_closeout: MarketOrderPositionCloseout = ...,
                margin_closeout: MarketOrderMarginCloseout = ...,
                delayed_trade_close: MarketOrderDelayedTradeClose = ...,
                take_profit_on_fill: TakeProfitDetails = ..., stop_loss_on_fill: StopLossDetails = ...,
                trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                trade_client_extensions: ClientExtensions = ..., filling_transaction_id: TransactionID = ...,
                filled_time: DateTime = ..., trade_opened_id: TradeID = ..., trade_reduced_id: TradeID = ...,
                trade_closed_i_ds: ArrayTradeID = ..., cancelling_transaction_id: TransactionID = ...,
                cancelled_time: DateTime = ...):
        return super().__new__(**MarketOrder._preset_arguments, **locals())
