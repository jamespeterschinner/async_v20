from .descriptors import *
from .metaclass import TypeModel


class OrderRequest(TypeModel):
    """The base Order specification used when requesting that an Order be created.
    Each specific Order-type extends this definition.

    Fields:

    """


class UnitsAvailable(TypeModel):
    """Representation of how many units of an Instrument are available to be
    traded by an Order depending on its postionFill option.

    Fields:
        default: -- The number of units that are available to be traded using an Order with a positionFill option of "DEFAULT". For an Account with hedging enabled,
            this value will be the same as the "OPEN_ONLY" value. For an Account without hedging enabled, this value will be the same as the "REDUCE_FIRST" value.
        reduceFirst: -- The number of units that may are available to be
            traded with an Order with a positionFill option of "REDUCE_FIRST".
        reduceOnly: -- The number of units that may are available to be
            traded with an Order with a positionFill option of "REDUCE_ONLY".
        openOnly: -- The number of units that may are available to be
            traded with an Order with a positionFill option of "OPEN_ONLY".

        """

    def __init__(self,
                 # default: UnitsAvailableDetails,
                 # reduceFirst: UnitsAvailableDetails,
                 # reduceOnly: UnitsAvailableDetails,
                 # openOnly: UnitsAvailableDetails
                 ):pass



class UnitsAvailableDetails(TypeModel):
    """Representation of many units of an Instrument are available to be traded
    for both long and short Orders.

    Fields:
        long: -- The units available for long Orders.
        short: -- The units available for short Orders.

    """

    def __init__(self,
                 long: DecimalNumber,
                 short: DecimalNumber
                 ):pass


class LiquidityRegenerationScheduleStep(TypeModel):
    """A liquidity regeneration schedule Step indicates the amount of bid and ask
    liquidity that is used by the Account at a certain time. These amounts will
    only change at the timestamp of the following step.

    Fields:
        timestamp: -- The timestamp of the schedule step.
        bidLiquidityUsed: -- The amount of bid liquidity used at this step in the schedule.
        askLiquidityUsed: -- The amount of ask liquidity used at this step in the schedule.

    """

    def __init__(self,
                 timestamp: DateTime,
                 bidLiquidityUsed: DecimalNumber,
                 askLiquidityUsed: DecimalNumber
                 ): pass


class LiquidityRegenerationSchedule(TypeModel):
    """A LiquidityRegenerationSchedule indicates how liquidity that is used when
    filling an Order for an instrument is regenerated following the fill.  A
    liquidity regeneration schedule will be in effect until the timestamp of
    its final step, but may be replaced by a schedule created for an Order of
    the same instrument that is filled while it is still in effect.

    Fields:
        steps: -- The steps in the Liquidity Regeneration Schedule

    """

    def __init__(self,
                 steps: LiquidityRegenerationScheduleStep
                 ): pass


class CandlestickData(TypeModel):
    """The price data (open, high, low, close) for the Candlestick representation.

    Fields:
        o: -- The first (open) price in the time-range represented by the candlestick.
        h: -- The highest price in the time-range represented by the candlestick.
        l: -- The lowest price in the time-range represented by the candlestick.
        c: -- The last (closing) price in the time-range represented by the candlestick.

    """

    def __init__(self,
                 o: PriceValue,
                 h: PriceValue,
                 l: PriceValue,
                 c: PriceValue
                 ): pass




class OrderIdentifier(TypeModel):
    """An OrderIdentifier is used to refer to an Order, and contains both the
    OrderID and the ClientOrderID.

    Fields:
        orderID: -- The OANDA-assigned Order ID
        clientOrderID: -- The client-provided client Order ID

    """

    def __init__(self,
                 orderID: OrderID,
                 clientOrderID: ClientID
                 ):pass




class QuoteHomeConversionFactors(TypeModel):
    """QuoteHomeConversionFactors represents the factors that can be used used to
    convert quantities of a Price's Instrument's quote currency into the
    Account's home currency.

    Fields:
        positiveUnits: -- The factor used to convert a positive amount of the Price's Instrument's quote currency into a positive
            amount of the Account's home currency. Conversion is performed by multiplying the quote units by the conversion factor.
        negativeUnits: -- The factor used to convert a negative amount of the Price's Instrument's quote currency into a negative
            amount of the Account's home currency. Conversion is performed by multiplying the quote units by the conversion factor.

    """

    def __init__(self,
                 positiveUnits: DecimalNumber,
                 negativeUnits: DecimalNumber
                 ): pass




class MarketOrderMarginCloseout(TypeModel):
    """Details for the Market Order extensions specific to a Market Order placed
    that is part of a Market Order Margin Closeout in a client's account

    Fields:
        reason: -- The reason the Market Order was created to perform a margin closeout

    """

    def __init__(self,
                 reason: MarketOrderMarginCloseoutReason
                 ): pass




class InstrumentCommission(TypeModel):
    """An InstrumentCommission represents an instrument-specific commission

    Fields:
        instrument: -- The name of the instrument
        commission: -- The commission amount (in the Account's home
            currency) charged per unitsTraded of the instrument
        unitsTraded: -- The number of units traded that the commission amount is based on.
        minimumCommission: -- The minimum commission amount (in the Account's home currency) that
            is charged when an Order is filled for this instrument.

    """

    def __init__(self,
                 instrument: InstrumentName,
                 commission: DecimalNumber,
                 unitsTraded: DecimalNumber,
                 minimumCommission: DecimalNumber
                 ): pass




class OrderBookBucket(TypeModel):
    """The order book data for a partition of the instrument's prices.

    Fields:
        price: -- The lowest price (inclusive) covered by the bucket. The bucket covers the
            price range from the price to price + the order book's bucketWidth.
        longCountPercent: -- The percentage of the total number of orders
            represented by the long orders found in this bucket.
        shortCountPercent: -- The percentage of the total number of orders
            represented by the short orders found in this bucket.

    """

    def __init__(self,
                 price: PriceValue,
                 longCountPercent: DecimalNumber,
                 shortCountPercent: DecimalNumber
                 ): pass




class PositionBookBucket(TypeModel):
    """The position book data for a partition of the instrument's prices.

    Fields:
        price: -- The lowest price (inclusive) covered by the bucket. The bucket covers the
            price range from the price to price + the position book's bucketWidth.
        longCountPercent: -- The percentage of the total number of positions
            represented by the long positions found in this bucket.
        shortCountPercent: -- The percentage of the total number of positions
            represented by the short positions found in this bucket.

    """

    def __init__(self,
                 price: PriceValue,
                 longCountPercent: DecimalNumber,
                 shortCountPercent: DecimalNumber
                 ): pass




class DynamicOrderState(TypeModel):
    """The dynamic state of an Order. This is only relevant to TrailingStopLoss
    Orders, as no other Order type has dynamic state.

    Fields:
        id: -- The Order's ID.
        trailingStopValue: -- The Order's calculated trailing stop value.
        triggerDistance: -- The distance between the Trailing Stop Loss Order's trailingStopValue and the current Market Price. This represents the distance (in price
            units) of the Order from a triggering price. If the distance could not be determined, this value will not be set.
        isTriggerDistanceExact: -- True if an exact trigger distance could be calculated. If false, it means the provided trigger distance
            is a best estimate. If the distance could not be determined, this value will not be set.

    """

    def __init__(self,
                 id: OrderID,
                 trailingStopValue: PriceValue,
                 triggerDistance: PriceValue,
                 isTriggerDistanceExact: bool
                 ):pass




class CalculatedPositionState(TypeModel):
    """The dynamic (calculated) state of a Position

    Fields:
        instrument: -- The Position's Instrument.
        netUnrealizedPL: -- The Position's net unrealized profit/loss
        longUnrealizedPL: -- The unrealized profit/loss of the Position's long open Trades
        shortUnrealizedPL: -- The unrealized profit/loss of the Position's short open Trades

    """

    def __init__(self,
                 instrument: InstrumentName,
                 netUnrealizedPL: AccountUnits,
                 longUnrealizedPL: AccountUnits,
                 shortUnrealizedPL: AccountUnits
                 ): pass


class PositionSide(TypeModel):
    """The representation of a Position for a single direction (long or short).

    Fields:
        units: -- Number of units in the position (negative
            value indicates short position, positive indicates long position).
        averagePrice: -- Volume-weighted average of the underlying Trade open prices for the Position.
        tradeIDs: -- List of the open Trade IDs which contribute to the open Position.
        pl: -- Profit/loss realized by the PositionSide over the lifetime of the Account.
        unrealizedPL: -- The unrealized profit/loss of all open
            Trades that contribute to this PositionSide.
        resettablePL: -- Profit/loss realized by the PositionSide since the
            Account's resettablePL was last reset by the client.

    """

    # Format string used when generating a summary for this object
    _summary_format = '{units} @ {averagePrice}, {pl} PL {unrealizedPL} UPL'

    def __init__(self,
                 units: DecimalNumber,
                 averagePrice: PriceValue,
                 tradeIDs: TradeID,
                 pl: AccountUnits,
                 unrealizedPL: AccountUnits,
                 resettablePL: AccountUnits
                 ): pass


class Position(TypeModel):
    """The specification of a Position within an Account.

    Fields:
        instrument: -- The Position's Instrument.
        pl: -- Profit/loss realized by the Position over the lifetime of the Account.
        unrealizedPL: -- The unrealized profit/loss of all open Trades that contribute to this Position.
        resettablePL: -- Profit/loss realized by the Position since the
            Account's resettablePL was last reset by the client.
        commission: -- The total amount of commission paid for this instrument over
            the lifetime of the Account. Represented in the Account's home currency.
        long: -- The details of the long side of the Position.
        short: -- The details of the short side of the Position.

    """

    # Format string used when generating a summary for this object
    _summary_format = '{instrument}, {pl} PL {unrealizedPL} UPL'

    # Format string used when generating a name for this object
    _name_format = '{instrument}, {pl} PL {unrealizedPL} UPL'

    def __init__(self,
                 instrument: InstrumentName,
                 pl: AccountUnits,
                 unrealizedPL: AccountUnits,
                 resettablePL: AccountUnits,
                 commission: AccountUnits,
                 long: PositionSide,
                 short: PositionSide
                 ): pass



class PriceBucket(TypeModel):
    """A Price Bucket represents a price available for an amount of liquidity

    Fields:
        price: -- The Price offered by the PriceBucket
        liquidity: -- The amount of liquidity offered by the PriceBucket

    """

    def __init__(self,
                 price: PriceValue,
                 liquidity: int
                 ): pass




class ClientPrice(TypeModel):
    """Client price for an Account.

    Fields:
        bids: -- The list of prices and liquidity available on the Instrument's bid side. It is possible for this
            list to be empty if there is no bid liquidity currently available for the Instrument in the Account.
        asks: -- The list of prices and liquidity available on the Instrument's ask side. It is possible for this
            list to be empty if there is no ask liquidity currently available for the Instrument in the Account.
        closeoutBid: -- The closeout bid Price. This Price is used when a bid is required to closeout a Position (margin closeout
            or manual) yet there is no bid liquidity. The closeout bid is never used to open a new position.
        closeoutAsk: -- The closeout ask Price. This Price is used when a ask is required to closeout a Position (margin closeout
            or manual) yet there is no ask liquidity. The closeout ask is never used to open a new position.
        timestamp: -- The date/time when the Price was created.

    """

    def __init__(self,
                 bids: PriceBucket,
                 asks: PriceBucket,
                 closeoutBid: PriceValue,
                 closeoutAsk: PriceValue,
                 timestamp: DateTime
                 ): pass




class PricingHeartbeat(TypeModel):
    """A PricingHeartbeat object is injected into the Pricing stream to ensure
    that the HTTP connection remains active.

    Fields:
        type: -- The string "HEARTBEAT"
        time: -- The date/time when the Heartbeat was created.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Pricing Heartbeat {time}'

    def __init__(self,
                 time: DateTime,
                 type: str = 'HEARTBEAT'
                 ): pass




class CalculatedTradeState(TypeModel):
    """The dynamic (calculated) state of an open Trade

    Fields:
        id: -- The Trade's ID.
        unrealizedPL: -- The Trade's unrealized profit/loss.

    """

    def __init__(self,
                 id: TradeID,
                 unrealizedPL: AccountUnits
                 ): pass


class MarketOrderDelayedTradeClose(TypeModel):
    """Details for the Market Order extensions specific to a Market Order placed
    with the intent of fully closing a specific open trade that should have
    already been closed but wasn't due to halted market conditions

    Fields:
        tradeID: -- The ID of the Trade being closed
        clientTradeID: -- The Client ID of the Trade being closed
        sourceTransactionID: -- The Transaction ID of the DelayedTradeClosure transaction
            to which this Delayed Trade Close belongs to

    """

    def __init__(self,
                 tradeID: TradeID,
                 clientTradeID: TradeID,
                 sourceTransactionID: TransactionID
                 ): pass




class MarketOrderPositionCloseout(TypeModel):
    """A MarketOrderPositionCloseout specifies the extensions to a Market Order
    when it has been created to closeout a specific Position.

    Fields:
        instrument: -- The instrument of the Position being closed out.
        units: -- Indication of how much of the Position to close. Either "ALL", or a DecimalNumber reflection a partial close of the
            Trade. The DecimalNumber must always be positive, and represent a number that doesn't exceed the absolute size of the Position.

    """

    def __init__(self,
                 instrument: InstrumentName,
                 units: str
                 ): pass




class MarketOrderTradeClose(TypeModel):
    """A MarketOrderTradeClose specifies the extensions to a Market Order that has
    been created specifically to close a Trade.

    Fields:
        tradeID: -- The ID of the Trade requested to be closed
        clientTradeID: -- The client ID of the Trade requested to be closed
        units: -- Indication of how much of the Trade to close. Either
            "ALL", or a DecimalNumber reflection a partial close of the Trade.

    """

    def __init__(self,
                 tradeID: TradeID,
                 clientTradeID: str,
                 units: str
                 ): pass




class OpenTradeFinancing(TypeModel):
    """OpenTradeFinancing is used to pay/collect daily financing charge for an
    open Trade within an Account

    Fields:
        tradeID: -- The ID of the Trade that financing is being paid/collected for.
        financing: -- The amount of financing paid/collected for the Trade.

    """

    def __init__(self,
                 tradeID: TradeID,
                 financing: AccountUnits
                 ): pass




class PositionFinancing(TypeModel):
    """OpenTradeFinancing is used to pay/collect daily financing charge for a
    Position within an Account

    Fields:
        instrument: -- The instrument of the Position that financing is being paid/collected for.
        financing: -- The amount of financing paid/collected for the Position.
        openTradeFinancings: -- The financing paid/collecte for each open Trade within the Position.

    """

    def __init__(self,
                 instrument: InstrumentName,
                 financing: AccountUnits,
                 openTradeFinancings: OpenTradeFinancing
                 ): pass


class ClientExtensions(TypeModel):
    """A ClientExtensions object allows a client to attach a clientID, tag and
    comment to Orders and Trades in their Account.  Do not set, modify, or
    delete this field if your account is associated with MT4.

    Fields:
        id: -- The Client ID of the Order/Trade
        tag: -- A tag associated with the Order/Trade
        comment: -- A comment associated with the Order/Trade

    """

    def __init__(self,
                 id: ClientID,
                 tag: ClientTag,
                 comment: ClientComment
                 ): pass



class TradeOpen(TypeModel):
    """A TradeOpen object represents a Trade for an instrument that was opened in
    an Account. It is found embedded in Transactions that affect the position
    of an instrument in the Account, specifically the OrderFill Transaction.

    Fields:
        tradeID: -- The ID of the Trade that was opened
        units: -- The number of units opened by the Trade
        clientExtensions: -- The client extensions for the newly opened Trade

    """

    def __init__(self,
                 tradeID: TradeID,
                 units: DecimalNumber,
                 clientExtensions: ClientExtensions
                 ): pass




class VWAPReceipt(TypeModel):
    """A VWAP Receipt provides a record of how the price for an Order fill is
    constructed. If the Order is filled with multiple buckets in a depth of
    market, each bucket will be represented with a VWAP Receipt.

    Fields:
        units: -- The number of units filled
        price: -- The price at which the units were filled

    """

    def __init__(self,
                 units: DecimalNumber,
                 price: PriceValue
                 ): pass






class UserInfo(TypeModel):
    """A representation of user information, as provided to the user themself.

    Fields:
        username: -- The user-provided username.
        userID: -- The user's OANDA-assigned user ID.
        country: -- The country that the user is based in.
        emailAddress: -- The user's email address.

    """

    def __init__(self,
                 username: str,
                 userID: int,
                 country: str,
                 emailAddress: str
                 ): pass




class AccountProperties(TypeModel):
    """Properties related to an Account.

    Fields:
        id: -- The Account's identifier
        mt4AccountID: -- The Account's associated MT4 Account ID. This field will not
            be present if the Account is not an MT4 account.
        tags: -- The Account's tags

    """

    def __init__(self,
                 id: AccountID,
                 mt4AccountID: int,
                 tags: str
                 ): pass




class Candlestick(TypeModel):
    """The Candlestick representation

    Fields:
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

    def __init__(self,
                 time: DateTime,
                 bid: CandlestickData,
                 ask: CandlestickData,
                 mid: CandlestickData,
                 volume: int,
                 complete: bool
                 ): pass


class OrderBook(TypeModel):
    """The representation of an instrument's order book at a point in time

    Fields:
        instrument: -- The order book's instrument
        time: -- The time when the order book snapshot was created.
        price: -- The price (midpoint) for the order book's instrument
            at the time of the order book snapshot
        bucketWidth: -- The price width for each bucket. Each bucket covers the price
            range from the bucket's price to the bucket's price + bucketWidth.
        buckets: -- The partitioned order book, divided into buckets using a default bucket width. These
            buckets are only provided for price ranges which actually contain order or position data.

    """

    def __init__(self,
                 instrument: InstrumentName,
                 time: DateTime,
                 price: PriceValue,
                 bucketWidth: PriceValue,
                 buckets: OrderBookBucket
                 ): pass




class PositionBook(TypeModel):
    """The representation of an instrument's position book at a point in time

    Fields:
        instrument: -- The position book's instrument
        time: -- The time when the position book snapshot was created
        price: -- The price (midpoint) for the position book's instrument
            at the time of the position book snapshot
        bucketWidth: -- The price width for each bucket. Each bucket covers the price
            range from the bucket's price to the bucket's price + bucketWidth.
        buckets: -- The partitioned position book, divided into buckets using a default bucket width. These
            buckets are only provided for price ranges which actually contain order or position data.

    """

    def __init__(self,
                 instrument: InstrumentName,
                 time: DateTime,
                 price: PriceValue,
                 bucketWidth: PriceValue,
                 buckets: PositionBookBucket
                 ): pass






class Order(TypeModel):
    """The base Order definition specifies the properties that are common to all
    Orders.

    Fields:
        id: -- The Order's identifier, unique within the Order's Account.
        createTime: -- The time when the Order was created.
        state: -- The current state of the Order.
        clientExtensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.

    """

    def __init__(self,
                 id: OrderID,
                 createTime: DateTime,
                 state: OrderState,
                 clientExtensions: ClientExtensions
                 ):pass


class StopLossDetails(TypeModel):
    """StopLossDetails specifies the details of a Stop Loss Order to be created on
    behalf of a client. This may happen when an Order is filled that opens a
    Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is
    modified directly through the Trade.

    Fields:
        price: -- The price that the Stop Loss Order will be triggered at.
        timeInForce: -- The time in force for the created Stop Loss
            Order. This may only be GTC, GTD or GFD.
        gtdTime: -- The date when the Stop Loss Order will be cancelled on if timeInForce is GTD.
        clientExtensions: -- The Client Extensions to add to the Stop Loss Order when created.

    """

    def __init__(self,
                 price: PriceValue,
                 gtdTime: DateTime,
                 clientExtensions: ClientExtensions,
                 timeInForce: TimeInForce = 'GTC'
                 ): pass




class TakeProfitDetails(TypeModel):
    """TakeProfitDetails specifies the details of a Take Profit Order to be
    created on behalf of a client. This may happen when an Order is filled that
    opens a Trade requiring a Take Profit, or when a Trade's dependent Take
    Profit Order is modified directly through the Trade.

    Fields:
        price: -- The price that the Take Profit Order will be triggered at.
        timeInForce: -- The time in force for the created Take Profit
            Order. This may only be GTC, GTD or GFD.
        gtdTime: -- The date when the Take Profit Order will be cancelled on if timeInForce is GTD.
        clientExtensions: -- The Client Extensions to add to the Take Profit Order when created.

    """

    def __init__(self,
                 price: PriceValue,
                 gtdTime: DateTime,
                 clientExtensions: ClientExtensions,
                 timeInForce: TimeInForce = 'GTC'
                 ): pass




class TradeReduce(TypeModel):
    """A TradeReduce object represents a Trade for an instrument that was reduced
    (either partially or fully) in an Account. It is found embedded in
    Transactions that affect the position of an instrument in the account,
    specifically the OrderFill Transaction.

    Fields:
        tradeID: -- The ID of the Trade that was reduced or closed
        units: -- The number of units that the Trade was reduced by
        realizedPL: -- The PL realized when reducing the Trade
        financing: -- The financing paid/collected when reducing the Trade

    """

    def __init__(self,
                 tradeID: TradeID,
                 units: DecimalNumber,
                 realizedPL: AccountUnits,
                 financing: AccountUnits
                 ): pass




class TrailingStopLossDetails(TypeModel):
    """TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order
    to be created on behalf of a client. This may happen when an Order is
    filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's
    dependent Trailing Stop Loss Order is modified directly through the Trade.

    Fields:
        distance: -- The distance (in price units) from the Trade's fill price
            that the Trailing Stop Loss Order will be triggered at.
        timeInForce: -- The time in force for the created Trailing Stop
            Loss Order. This may only be GTC, GTD or GFD.
        gtdTime: -- The date when the Trailing Stop Loss Order
            will be cancelled on if timeInForce is GTD.
        clientExtensions: -- The Client Extensions to add to the Trailing Stop Loss Order when created.

    """

    def __init__(self,
                 distance: PriceValue,
                 gtdTime: DateTime,
                 clientExtensions: ClientExtensions,
                 timeInForce: TimeInForce = 'GTC'
                 ): pass




class TransactionHeartbeat(TypeModel):
    """A TransactionHeartbeat object is injected into the Transaction stream to
    ensure that the HTTP connection remains active.

    Fields:
        type: -- The string "HEARTBEAT"
        lastTransactionID: -- The ID of the most recent Transaction created for the Account
        time: -- The date/time when the TransactionHeartbeat was created.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Transaction Heartbeat {time}'

    def __init__(self,
                 lastTransactionID: TransactionID,
                 time: DateTime,
                 type: str = 'HEARTBEAT'
                 ): pass




class UserInfoExternal(TypeModel):
    """A representation of user information, as available to external (3rd party)
    clients.

    Fields:
        userID: -- The user's OANDA-assigned user ID.
        country: -- The country that the user is based in.
        FIFO: -- Flag indicating if the the user's Accounts adhere to FIFO execution rules.

    """

    def __init__(self,
                 userID: int,
                 country: str,
                 FIFO: bool
                 ): pass




class TradeSummary(TypeModel):
    """The summary of a Trade within an Account. This representation does not
    provide the full details of the Trade's dependent Orders.

    Fields:
        id: -- The Trade's identifier, unique within the Trade's Account.
        instrument: -- The Trade's Instrument.
        price: -- The execution price of the Trade.
        openTime: -- The date/time when the Trade was opened.
        state: -- The current state of the Trade.
        initialUnits: -- The initial size of the Trade. Negative values indicate
            a short Trade, and positive values indicate a long Trade.
        currentUnits: -- The number of units currently open for the Trade. This
            value is reduced to 0.0 as the Trade is closed.
        realizedPL: -- The total profit/loss realized on the closed portion of the Trade.
        unrealizedPL: -- The unrealized profit/loss on the open portion of the Trade.
        averageClosePrice: -- The average closing price of the Trade. Only present if
            the Trade has been closed or reduced at least once.
        closingTransactionIDs: -- The IDs of the Transactions that have closed portions of this Trade.
        financing: -- The financing paid/collected for this Trade.
        closeTime: -- The date/time when the Trade was fully closed.
            Only provided for Trades whose state is CLOSED.
        clientExtensions: -- The client extensions of the Trade.
        takeProfitOrderID: -- ID of the Trade's Take Profit Order, only provided if such an Order exists.
        stopLossOrderID: -- ID of the Trade's Stop Loss Order, only provided if such an Order exists.
        trailingStopLossOrderID: -- ID of the Trade's Trailing Stop Loss
            Order, only provided if such an Order exists.

    """

    # Format string used when generating a summary for this object
    _summary_format = '{currentUnits} ({initialUnits}) of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = '{currentUnits} ({initialUnits}) of {instrument} @ {price}'

    def __init__(self,
                 id: TradeID,
                 instrument: InstrumentName,
                 price: PriceValue,
                 openTime: DateTime,
                 state: TradeState,
                 initialUnits: DecimalNumber,
                 currentUnits: DecimalNumber,
                 realizedPL: AccountUnits,
                 unrealizedPL: AccountUnits,
                 averageClosePrice: PriceValue,
                 closingTransactionIDs: TransactionID,
                 financing: AccountUnits,
                 closeTime: DateTime,
                 clientExtensions: ClientExtensions,
                 takeProfitOrderID: OrderID,
                 stopLossOrderID: OrderID,
                 trailingStopLossOrderID: OrderID
                 ): pass



class Transaction(TypeModel):
    """The base Transaction specification. Specifies properties that are common
    between all Transaction.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.

    """

    # Format string used when generating a name for this object
    _name_format = ''

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID
                 ): pass



class AccountChanges(TypeModel):
    """An AccountChanges Object is used to represent the changes to an Account's
    Orders, Trades and Positions since a specified Account TransactionID in the
    past.

    Fields:
        ordersCreated: -- The Orders created. These Orders may have been
            filled, cancelled or triggered in the same period.
        ordersCancelled: -- The Orders cancelled.
        ordersFilled: -- The Orders filled.
        ordersTriggered: -- The Orders triggered.
        tradesOpened: -- The Trades opened.
        tradesReduced: -- The Trades reduced.
        tradesClosed: -- The Trades closed.
        positions: -- The Positions changed.
        transactions: -- The Transactions that have been generated.

    """

    def __init__(self,
                 ordersCreated: Order,
                 ordersCancelled: Order,
                 ordersFilled: Order,
                 ordersTriggered: Order,
                 tradesOpened: TradeSummary,
                 tradesReduced: TradeSummary,
                 tradesClosed: TradeSummary,
                 positions: Position,
                 transactions: Transaction
                 ): pass


class Instrument(TypeModel):
    """Full specification of an Instrument.

    Fields:
        name: -- The name of the Instrument
        type: -- The type of the Instrument
        displayName: -- The display name of the Instrument
        pipLocation: -- The location of the "pip" for this instrument. The decimal position of the pip in this Instrument's price can be
            found at 10 ^ pipLocation (e.g. -4 pipLocation results in a decimal pip position of 10 ^ -4 = 0.0001).
        displayPrecision: -- The number of decimal places that should be used to display prices for this instrument.
            (e.g. a displayPrecision of 5 would result in a price of "1" being displayed as "1.00000")
        tradeUnitsPrecision: -- The amount of decimal places that may be provided
            when specifying the number of units traded for this instrument.
        minimumTradeSize: -- The smallest number of units allowed to be traded for this instrument.
        maximumTrailingStopDistance: -- The maximum trailing stop distance allowed for a trailing
            stop loss created for this instrument. Specified in price units.
        minimumTrailingStopDistance: -- The minimum trailing stop distance allowed for a trailing
            stop loss created for this instrument. Specified in price units.
        maximumPositionSize: -- The maximum position size allowed for this instrument. Specified in units.
        maximumOrderUnits: -- The maximum units allowed for an Order
            placed for this instrument. Specified in units.
        marginRate: -- The margin rate for this instrument.
        commission: -- The commission structure for this instrument.

    """

    def __init__(self,
                 name: InstrumentName,
                 type: InstrumentType,
                 displayName: str,
                 pipLocation: int,
                 displayPrecision: int,
                 tradeUnitsPrecision: int,
                 minimumTradeSize: DecimalNumber,
                 maximumTrailingStopDistance: DecimalNumber,
                 minimumTrailingStopDistance: DecimalNumber,
                 maximumPositionSize: DecimalNumber,
                 maximumOrderUnits: DecimalNumber,
                 marginRate: DecimalNumber,
                 commission: InstrumentCommission
                 ): pass



class AccountChangesState(TypeModel):
    """An AccountState Object is used to represent an Account's current price-
    dependent state. Price-dependent Account state is dependent on OANDA's
    current Prices, and includes things like unrealized PL, NAV and Trailing
    Stop Loss Order state.

    Fields:
        unrealizedPL: -- The total unrealized profit/loss for all Trades currently open
            in the Account. Represented in the Account's home currency.
        NAV: -- The net asset value of the Account. Equal to
            Account balance + unrealizedPL. Represented in the Account's home currency.
        marginUsed: -- Margin currently used for the Account.
            Represented in the Account's home currency.
        marginAvailable: -- Margin available for Account. Represented in the Account's home currency.
        positionValue: -- The value of the Account's open
            positions represented in the Account's home currency.
        marginCloseoutUnrealizedPL: -- The Account's margin closeout unrealized PL.
        marginCloseoutNAV: -- The Account's margin closeout NAV.
        marginCloseoutMarginUsed: -- The Account's margin closeout margin used.
        marginCloseoutPercent: -- The Account's margin closeout percentage. When this value is 1.0
            or above the Account is in a margin closeout situation.
        marginCloseoutPositionValue: -- The value of the Account's open positions as used
            for margin closeout calculations represented in the Account's home currency.
        withdrawalLimit: -- The current WithdrawalLimit for the account which will be zero or
            a positive value indicating how much can be withdrawn from the account.
        marginCallMarginUsed: -- The Account's margin call margin used.
        marginCallPercent: -- The Account's margin call percentage. When this value is 1.0
            or above the Account is in a margin call situation.
        orders: -- The price-dependent state of each pending Order in the Account.
        trades: -- The price-dependent state for each open Trade in the Account.
        positions: -- The price-dependent state for each open Position in the Account.

    """

    def __init__(self,
                 unrealizedPL: AccountUnits,
                 NAV: AccountUnits,
                 marginUsed: AccountUnits,
                 marginAvailable: AccountUnits,
                 positionValue: AccountUnits,
                 marginCloseoutUnrealizedPL: AccountUnits,
                 marginCloseoutNAV: AccountUnits,
                 marginCloseoutMarginUsed: AccountUnits,
                 marginCloseoutPercent: DecimalNumber,
                 marginCloseoutPositionValue: DecimalNumber,
                 withdrawalLimit: AccountUnits,
                 marginCallMarginUsed: AccountUnits,
                 marginCallPercent: DecimalNumber,
                 orders: DynamicOrderState,
                 trades: CalculatedTradeState,
                 positions: CalculatedPositionState
                 ): pass




class Price(TypeModel):
    """The specification of an Account-specific Price.

    Fields:
        type: -- The string "PRICE". Used to identify the a Price object when found in a stream.
        instrument: -- The Price's Instrument.
        time: -- The date/time when the Price was created
        status: -- The status of the Price.
        tradeable: -- Flag indicating if the Price is tradeable or not
        bids: -- The list of prices and liquidity available on the Instrument's bid side. It is possible for this
            list to be empty if there is no bid liquidity currently available for the Instrument in the Account.
        asks: -- The list of prices and liquidity available on the Instrument's ask side. It is possible for this
            list to be empty if there is no ask liquidity currently available for the Instrument in the Account.
        closeoutBid: -- The closeout bid Price. This Price is used when a bid is required to closeout a Position (margin closeout
            or manual) yet there is no bid liquidity. The closeout bid is never used to open a new position.
        closeoutAsk: -- The closeout ask Price. This Price is used when a ask is required to closeout a Position (margin closeout
            or manual) yet there is no ask liquidity. The closeout ask is never used to open a new position.
        quoteHomeConversionFactors: -- The factors used to convert quantities of this price's Instrument's
            quote currency into a quantity of the Account's home currency.
        unitsAvailable: -- Representation of how many units of an Instrument are available
            to be traded by an Order depending on its postionFill option.

    """

    def __init__(self,
                 instrument: InstrumentName,
                 time: DateTime,
                 status: PriceStatus,
                 tradeable: bool,
                 bids: PriceBucket,
                 asks: PriceBucket,
                 closeoutBid: PriceValue,
                 closeoutAsk: PriceValue,
                 quoteHomeConversionFactors: QuoteHomeConversionFactors,
                 unitsAvailable: UnitsAvailable,
                 type: str = 'PRICE'
                 ): pass






class CloseTransaction(TypeModel):
    """A CloseTransaction represents the closing of an Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always set to "CLOSE" in a CloseTransaction.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Close Account {accountID}'

    # Format string used when generating a name for this object
    _name_format = 'Close Account {accountID}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 type: TransactionType = 'CLOSE'
                 ): pass




class MarginCallEnterTransaction(TypeModel):
    """A MarginCallEnterTransaction is created when an Account enters the margin
    call state.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "MARGIN_CALL_ENTER" for an MarginCallEnterTransaction.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Margin Call Enter'

    # Format string used when generating a name for this object
    _name_format = 'Margin Call Enter'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 type: TransactionType = 'MARGIN_CALL_ENTER'
                 ): pass




class MarginCallExitTransaction(TypeModel):
    """A MarginCallExitnterTransaction is created when an Account leaves the
    margin call state.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "MARGIN_CALL_EXIT" for an MarginCallExitTransaction.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Margin Call Exit'

    # Format string used when generating a name for this object
    _name_format = 'Margin Call Exit'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 type: TransactionType = 'MARGIN_CALL_EXIT'
                 ): pass




class MarginCallExtendTransaction(TypeModel):
    """A MarginCallExtendTransaction is created when the margin call state for an
    Account has been extended.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "MARGIN_CALL_EXTEND" for an MarginCallExtendTransaction.
        extensionNumber: -- The number of the extensions to the Account's current margin call that have
            been applied. This value will be set to 1 for the first MarginCallExtend Transaction

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Margin Call Enter'

    # Format string used when generating a name for this object
    _name_format = 'Margin Call Enter'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 extensionNumber: int,
                 type: TransactionType = 'MARGIN_CALL_EXTEND'
                 ): pass




class ReopenTransaction(TypeModel):
    """A ReopenTransaction represents the re-opening of a closed Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always set to "REOPEN" in a ReopenTransaction.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Reopen Account {accountID}'

    # Format string used when generating a name for this object
    _name_format = 'Reopen Account {accountID}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 type: TransactionType = 'REOPEN'
                 ): pass




class ResetResettablePLTransaction(TypeModel):
    """A ResetResettablePLTransaction represents the resetting of the Account's
    resettable PL counters.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "RESET_RESETTABLE_PL" for a ResetResettablePLTransaction.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'PL Reset'

    # Format string used when generating a name for this object
    _name_format = 'PL Reset'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 type: TransactionType = 'RESET_RESETTABLE_PL'
                 ): pass




class StopLossOrderRequest(TypeModel):
    """A StopLossOrderRequest specifies the parameters that may be set when
    creating a Stop Loss Order.

    Fields:
        type: -- The type of the Order to Create. Must be
            set to "STOP_LOSS" when creating a Stop Loss Order.
        tradeID: -- The ID of the Trade to close when the price threshold is breached.
        clientTradeID: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the StopLoss Order. The associated Trade will be
            closed by a market price that is equal to or worse than this threshold.
        timeInForce: -- The time-in-force requested for the StopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for StopLoss Orders.
        gtdTime: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        clientExtensions: -- The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Stop Loss for Trade {tradeID} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Stop Loss for Trade {tradeID} @ {price}'

    def __init__(self,
                 tradeID: TradeID,
                 clientTradeID: ClientID,
                 price: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 triggerCondition: OrderTriggerCondition,
                 clientExtensions: ClientExtensions,
                 type: OrderType = 'STOP_LOSS'
                 ):pass




class TakeProfitOrderRequest(TypeModel):
    """A TakeProfitOrderRequest specifies the parameters that may be set when
    creating a Take Profit Order.

    Fields:
        type: -- The type of the Order to Create. Must be
            set to "TAKE_PROFIT" when creating a Take Profit Order.
        tradeID: -- The ID of the Trade to close when the price threshold is breached.
        clientTradeID: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the TakeProfit Order. The associated Trade will be
            closed by a market price that is equal to or better than this threshold.
        timeInForce: -- The time-in-force requested for the TakeProfit Order. Restricted
            to "GTC", "GFD" and "GTD" for TakeProfit Orders.
        gtdTime: -- The date/time when the TakeProfit Order will
            be cancelled if its timeInForce is "GTD".
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        clientExtensions: -- The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Take Profit for Trade {tradeID} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Take Profit for Trade {tradeID} @ {price}'

    def __init__(self,
                 tradeID: TradeID,
                 clientTradeID: ClientID,
                 price: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 triggerCondition: OrderTriggerCondition,
                 clientExtensions: ClientExtensions,
                 type: OrderType = 'TAKE_PROFIT'
                 ):pass




class TrailingStopLossOrderRequest(TypeModel):
    """A TrailingStopLossOrderRequest specifies the parameters that may be set
    when creating a Trailing Stop Loss Order.

    Fields:
        type: -- The type of the Order to Create. Must be
            set to "TRAILING_STOP_LOSS" when creating a Trailng Stop Loss Order.
        tradeID: -- The ID of the Trade to close when the price threshold is breached.
        clientTradeID: -- The client ID of the Trade to be closed when the price threshold is breached.
        distance: -- The price distance specified for the TrailingStopLoss Order.
        timeInForce: -- The time-in-force requested for the TrailingStopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
        gtdTime: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        clientExtensions: -- The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Trailing Stop Loss for Trade {tradeID} @ {trailingStopValue}'

    # Format string used when generating a name for this object
    _name_format = 'Trailing Stop Loss for Trade {tradeID} @ {trailingStopValue}'

    def __init__(self,
                 tradeID: TradeID,
                 clientTradeID: ClientID,
                 distance: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 triggerCondition: OrderTriggerCondition,
                 clientExtensions: ClientExtensions,
                 type: OrderType = 'TRAILING_STOP_LOSS'
                 ):pass




class CreateTransaction(TypeModel):
    """A CreateTransaction represents the creation of an Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always set to "CREATE" in a CreateTransaction.
        divisionID: -- The ID of the Division that the Account is in
        siteID: -- The ID of the Site that the Account was created at
        accountUserID: -- The ID of the user that the Account was created for
        accountNumber: -- The number of the Account within the site/division/user
        homeCurrency: -- The home currency of the Account

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Create Account {accountID}'

    # Format string used when generating a name for this object
    _name_format = 'Create Account {accountID}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 divisionID: int,
                 siteID: int,
                 accountUserID: int,
                 accountNumber: int,
                 homeCurrency: Currency,
                 type: TransactionType = 'CREATE'
                 ): pass






class ClientConfigureTransaction(TypeModel):
    """A ClientConfigureTransaction represents the configuration of an Account by
    a client.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "CLIENT_CONFIGURE" in a ClientConfigureTransaction.
        alias: -- The client-provided alias for the Account.
        marginRate: -- The margin rate override for the Account.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Client Configure'

    # Format string used when generating a name for this object
    _name_format = 'Client Configure'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 alias: str,
                 marginRate: DecimalNumber,
                 type: TransactionType = 'CLIENT_CONFIGURE'
                 ): pass




class DelayedTradeClosureTransaction(TypeModel):
    """A DelayedTradeClosure Transaction is created administratively to indicate
    open trades that should have been closed but weren't because the open
    trades' instruments were untradeable at the time. Open trades listed in
    this transaction will be closed once their respective instruments become
    tradeable.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "DELAYED_TRADE_CLOSURE" for an DelayedTradeClosureTransaction.
        reason: -- The reason for the delayed trade closure
        tradeIDs: -- List of Trade ID's identifying the open trades that
            will be closed when their respective instruments become tradeable

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Delayed Trade Closure'

    # Format string used when generating a name for this object
    _name_format = 'Delayed Trade Closure'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 reason: MarketOrderReason,
                 tradeIDs: TradeID,
                 type: TransactionType = 'DELAYED_TRADE_CLOSURE'
                 ): pass





class OrderCancelTransaction(TypeModel):
    """An OrderCancelTransaction represents the cancellation of an Order in the
    client's Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "ORDER_CANCEL" for an OrderCancelTransaction.
        orderID: -- The ID of the Order cancelled
        clientOrderID: -- The client ID of the Order cancelled (only
            provided if the Order has a client Order ID).
        reason: -- The reason that the Order was cancelled.
        replacedByOrderID: -- The ID of the Order that replaced this Order
            (only provided if this Order was cancelled for replacement).

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Cancel Order {orderID}'

    # Format string used when generating a name for this object
    _name_format = 'Cancel Order {orderID}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 orderID: OrderID,
                 clientOrderID: OrderID,
                 reason: OrderCancelReason,
                 replacedByOrderID: OrderID,
                 type: TransactionType = 'ORDER_CANCEL'
                 ): pass




class OrderClientExtensionsModifyTransaction(TypeModel):
    """A OrderClientExtensionsModifyTransaction represents the modification of an
    Order's Client Extensions.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "ORDER_CLIENT_EXTENSIONS_MODIFY" for a OrderClienteExtensionsModifyTransaction.
        orderID: -- The ID of the Order who's client extensions are to be modified.
        clientOrderID: -- The original Client ID of the Order who's client extensions are to be modified.
        clientExtensionsModify: -- The new Client Extensions for the Order.
        tradeClientExtensionsModify: -- The new Client Extensions for the Order's Trade on fill.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Modify Order {orderID} Client Extensions'

    # Format string used when generating a name for this object
    _name_format = 'Modify Order {orderID} Client Extensions'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 orderID: OrderID,
                 clientOrderID: ClientID,
                 clientExtensionsModify: ClientExtensions,
                 tradeClientExtensionsModify: ClientExtensions,
                 type: TransactionType = 'ORDER_CLIENT_EXTENSIONS_MODIFY'
                 ): pass




class DailyFinancingTransaction(TypeModel):
    """A DailyFinancingTransaction represents the daily payment/collection of
    financing for an Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "DAILY_FINANCING" for a DailyFinancingTransaction.
        financing: -- The amount of financing paid/collected for the Account.
        accountBalance: -- The Account's balance after daily financing.
        accountFinancingMode: -- The account financing mode at the time of the daily financing.
        positionFinancings: -- The financing paid/collected for each Position in the Account.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Daily Account Financing ({financing})'

    # Format string used when generating a name for this object
    _name_format = 'Daily Account Financing ({financing})'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 financing: AccountUnits,
                 accountBalance: AccountUnits,
                 accountFinancingMode: AccountFinancingMode,
                 positionFinancings: PositionFinancing,
                 type: TransactionType = 'DAILY_FINANCING'
                 ): pass




class TradeClientExtensionsModifyTransaction(TypeModel):
    """A TradeClientExtensionsModifyTransaction represents the modification of a
    Trade's Client Extensions.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TRADE_CLIENT_EXTENSIONS_MODIFY" for a TradeClientExtensionsModifyTransaction.
        tradeID: -- The ID of the Trade who's client extensions are to be modified.
        clientTradeID: -- The original Client ID of the Trade who's client extensions are to be modified.
        tradeClientExtensionsModify: -- The new Client Extensions for the Trade.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Modify Trade {tradeID} Client Extensions'

    # Format string used when generating a name for this object
    _name_format = 'Modify Trade {tradeID} Client Extensions'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 tradeID: TradeID,
                 clientTradeID: ClientID,
                 tradeClientExtensionsModify: ClientExtensions,
                 type: TransactionType = 'TRADE_CLIENT_EXTENSIONS_MODIFY'
                 ): pass




class AccountSummary(TypeModel):
    """A summary representation of a client's Account. The AccountSummary does not
    provide to full specification of pending Orders, open Trades and Positions.

    Fields:
        id: -- The Account's identifier
        alias: -- Client-assigned alias for the Account. Only provided
            if the Account has an alias set
        currency: -- The home currency of the Account
        balance: -- The current balance of the Account. Represented in the Account's home currency.
        createdByUserID: -- ID of the user that created the Account.
        createdTime: -- The date/time when the Account was created.
        pl: -- The total profit/loss realized over the lifetime of
            the Account. Represented in the Account's home currency.
        resettablePL: -- The total realized profit/loss for the Account since it was
            last reset by the client. Represented in the Account's home currency.
        resettabledPLTime: -- The date/time that the Account's resettablePL was last reset.
        commission: -- The total amount of commission paid over the lifetime
            of the Account. Represented in the Account's home currency.
        marginRate: -- Client-provided margin rate override for the Account. The effective margin rate of the Account is the lesser of this value and
            the OANDA margin rate for the Account's division. This value is only provided if a margin rate override exists for the Account.
        marginCallEnterTime: -- The date/time when the Account entered a margin call state.
            Only provided if the Account is in a margin call.
        marginCallExtensionCount: -- The number of times that the Account's current margin call was extended.
        lastMarginCallExtensionTime: -- The date/time of the Account's last margin call extension.
        openTradeCount: -- The number of Trades currently open in the Account.
        openPositionCount: -- The number of Positions currently open in the Account.
        pendingOrderCount: -- The number of Orders currently pending in the Account.
        hedgingEnabled: -- Flag indicating that the Account has hedging enabled.
        unrealizedPL: -- The total unrealized profit/loss for all Trades currently open
            in the Account. Represented in the Account's home currency.
        NAV: -- The net asset value of the Account. Equal to
            Account balance + unrealizedPL. Represented in the Account's home currency.
        marginUsed: -- Margin currently used for the Account.
            Represented in the Account's home currency.
        marginAvailable: -- Margin available for Account. Represented in the Account's home currency.
        positionValue: -- The value of the Account's open
            positions represented in the Account's home currency.
        marginCloseoutUnrealizedPL: -- The Account's margin closeout unrealized PL.
        marginCloseoutNAV: -- The Account's margin closeout NAV.
        marginCloseoutMarginUsed: -- The Account's margin closeout margin used.
        marginCloseoutPercent: -- The Account's margin closeout percentage. When this value is 1.0
            or above the Account is in a margin closeout situation.
        marginCloseoutPositionValue: -- The value of the Account's open positions as used
            for margin closeout calculations represented in the Account's home currency.
        withdrawalLimit: -- The current WithdrawalLimit for the account which will be zero or
            a positive value indicating how much can be withdrawn from the account.
        marginCallMarginUsed: -- The Account's margin call margin used.
        marginCallPercent: -- The Account's margin call percentage. When this value is 1.0
            or above the Account is in a margin call situation.
        lastTransactionID: -- The ID of the last Transaction created for the Account.

    """

    def __init__(self,
                 id: AccountID,
                 alias: str,
                 currency: Currency,
                 balance: AccountUnits,
                 createdByUserID: int,
                 createdTime: DateTime,
                 pl: AccountUnits,
                 resettablePL: AccountUnits,
                 resettabledPLTime: DateTime,
                 commission: AccountUnits,
                 marginRate: DecimalNumber,
                 marginCallEnterTime: DateTime,
                 marginCallExtensionCount: int,
                 lastMarginCallExtensionTime: DateTime,
                 openTradeCount: int,
                 openPositionCount: int,
                 pendingOrderCount: int,
                 hedgingEnabled: bool,
                 unrealizedPL: AccountUnits,
                 NAV: AccountUnits,
                 marginUsed: AccountUnits,
                 marginAvailable: AccountUnits,
                 positionValue: AccountUnits,
                 marginCloseoutUnrealizedPL: AccountUnits,
                 marginCloseoutNAV: AccountUnits,
                 marginCloseoutMarginUsed: AccountUnits,
                 marginCloseoutPercent: DecimalNumber,
                 marginCloseoutPositionValue: DecimalNumber,
                 withdrawalLimit: AccountUnits,
                 marginCallMarginUsed: AccountUnits,
                 marginCallPercent: DecimalNumber,
                 lastTransactionID: TransactionID
                 ): pass



class MarketOrderRequest(TypeModel):
    """A MarketOrderRequest specifies the parameters that may be set when creating
    a Market Order.

    Fields:
        type: -- The type of the Order to Create. Must
            be set to "MARKET" when creating a Market Order.
        instrument: -- The Market Order's Instrument.
        units: -- The quantity requested to be filled by the Market Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        timeInForce: -- The time-in-force requested for the Market Order.
            Restricted to FOK or IOC for a MarketOrder.
        priceBound: -- The worst price that the client is willing to have the Market Order filled at.
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        clientExtensions: -- The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.
        takeProfitOnFill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.
        stopLossOnFill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.
        trailingStopLossOnFill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.

    """

    # Format string used when generating a summary for this object
    _summary_format = '{units} units of {instrument}'

    # Format string used when generating a name for this object
    _name_format = '{units} units of {instrument}'

    def __init__(self,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 timeInForce: TimeInForce,
                 priceBound: PriceValue,
                 positionFill: OrderPositionFill,
                 clientExtensions: ClientExtensions,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 type: OrderType = 'MARKET'
                 ):pass


class TakeProfitOrderTransaction(TypeModel):
    """A TakeProfitOrderTransaction represents the creation of a TakeProfit Order
    in the user's Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TAKE_PROFIT_ORDER" in a TakeProfitOrderTransaction.
        tradeID: -- The ID of the Trade to close when the price threshold is breached.
        clientTradeID: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the TakeProfit Order. The associated Trade will be
            closed by a market price that is equal to or better than this threshold.
        timeInForce: -- The time-in-force requested for the TakeProfit Order. Restricted
            to "GTC", "GFD" and "GTD" for TakeProfit Orders.
        gtdTime: -- The date/time when the TakeProfit Order will
            be cancelled if its timeInForce is "GTD".
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Take Profit Order was initiated
        clientExtensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        orderFillTransactionID: -- The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        replacesOrderID: -- The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancellingTransactionID: -- The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Create Take Profit Order {id} ({reason}): Close Trade {tradeID} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Create Take Profit Order {id} ({reason}): Close Trade {tradeID} @ {price}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 tradeID: TradeID,
                 clientTradeID: ClientID,
                 price: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 triggerCondition: OrderTriggerCondition,
                 reason: TakeProfitOrderReason,
                 clientExtensions: ClientExtensions,
                 orderFillTransactionID: TransactionID,
                 replacesOrderID: OrderID,
                 cancellingTransactionID: TransactionID,
                 type: TransactionType = 'TAKE_PROFIT_ORDER'
                 ): pass


class TakeProfitOrder(TypeModel):
    """A TakeProfitOrder is an order that is linked to an open Trade and created
    with a price threshold. The Order will be filled (closing the Trade) by the
    first price that is equal to or better than the threshold. A
    TakeProfitOrder cannot be used to open a new Position.

    Fields:
        id: -- The Order's identifier, unique within the Order's Account.
        createTime: -- The time when the Order was created.
        state: -- The current state of the Order.
        clientExtensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        type: -- The type of the Order. Always set to "TAKE_PROFIT" for Take Profit Orders.
        tradeID: -- The ID of the Trade to close when the price threshold is breached.
        clientTradeID: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the TakeProfit Order. The associated Trade will be
            closed by a market price that is equal to or better than this threshold.
        timeInForce: -- The time-in-force requested for the TakeProfit Order. Restricted
            to "GTC", "GFD" and "GTD" for TakeProfit Orders.
        gtdTime: -- The date/time when the TakeProfit Order will
            be cancelled if its timeInForce is "GTD".
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        fillingTransactionID: -- ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filledTime: -- Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        tradeOpenedID: -- Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        tradeReducedID: -- Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        tradeClosedIDs: -- Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancellingTransactionID: -- ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelledTime: -- Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replacesOrderID: -- The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replacedByOrderID: -- The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Take Profit for Trade {tradeID} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Take Profit for Trade {tradeID} @ {price}'

    def __init__(self,
                 id: OrderID,
                 createTime: DateTime,
                 state: OrderState,
                 clientExtensions: ClientExtensions,
                 tradeID: TradeID,
                 clientTradeID: ClientID,
                 price: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 triggerCondition: OrderTriggerCondition,
                 fillingTransactionID: TransactionID,
                 filledTime: DateTime,
                 tradeOpenedID: TradeID,
                 tradeReducedID: TradeID,
                 tradeClosedIDs: TradeID,
                 cancellingTransactionID: TransactionID,
                 cancelledTime: DateTime,
                 replacesOrderID: OrderID,
                 replacedByOrderID: OrderID,
                 type: OrderType = 'TAKE_PROFIT'
                 ):pass


class StopLossOrder(TypeModel):
    """A StopLossOrder is an order that is linked to an open Trade and created
    with a price threshold. The Order will be filled (closing the Trade) by the
    first price that is equal to or worse than the threshold. A StopLossOrder
    cannot be used to open a new Position.

    Fields:
        id: -- The Order's identifier, unique within the Order's Account.
        createTime: -- The time when the Order was created.
        state: -- The current state of the Order.
        clientExtensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        type: -- The type of the Order. Always set to "STOP_LOSS" for Stop Loss Orders.
        tradeID: -- The ID of the Trade to close when the price threshold is breached.
        clientTradeID: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the StopLoss Order. The associated Trade will be
            closed by a market price that is equal to or worse than this threshold.
        timeInForce: -- The time-in-force requested for the StopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for StopLoss Orders.
        gtdTime: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        fillingTransactionID: -- ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filledTime: -- Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        tradeOpenedID: -- Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        tradeReducedID: -- Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        tradeClosedIDs: -- Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancellingTransactionID: -- ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelledTime: -- Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replacesOrderID: -- The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replacedByOrderID: -- The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

        """

    # Format string used when generating a summary for this object
    _summary_format = 'Stop Loss for Trade {tradeID} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Stop Loss for Trade {tradeID} @ {price}'

    def __init__(self,
                 id: OrderID,
                 createTime: DateTime,
                 state: OrderState,
                 clientExtensions: ClientExtensions,
                 tradeID: TradeID,
                 clientTradeID: ClientID,
                 price: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 triggerCondition: OrderTriggerCondition,
                 fillingTransactionID: TransactionID,
                 filledTime: DateTime,
                 tradeOpenedID: TradeID,
                 tradeReducedID: TradeID,
                 tradeClosedIDs: TradeID,
                 cancellingTransactionID: TransactionID,
                 cancelledTime: DateTime,
                 replacesOrderID: OrderID,
                 replacedByOrderID: OrderID,
                 type: OrderType = 'STOP_LOSS'
                 ):pass


class TrailingStopLossOrder(TypeModel):
    """A TrailingStopLossOrder is an order that is linked to an open Trade and
    created with a price distance. The price distance is used to calculate a
    trailing stop value for the order that is in the losing direction from the
    market price at the time of the order's creation. The trailing stop value
    will follow the market price as it moves in the winning direction, and the
    order will filled (closing the Trade) by the first price that is equal to
    or worse than the trailing stop value. A TrailingStopLossOrder cannot be
    used to open a new Position.

    Fields:
        id: -- The Order's identifier, unique within the Order's Account.
        createTime: -- The time when the Order was created.
        state: -- The current state of the Order.
        clientExtensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        type: -- The type of the Order. Always set
            to "TRAILING_STOP_LOSS" for Trailing Stop Loss Orders.
        tradeID: -- The ID of the Trade to close when the price threshold is breached.
        clientTradeID: -- The client ID of the Trade to be closed when the price threshold is breached.
        distance: -- The price distance specified for the TrailingStopLoss Order.
        timeInForce: -- The time-in-force requested for the TrailingStopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
        gtdTime: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        trailingStopValue: -- The trigger price for the Trailing Stop Loss Order. The trailing stop value will trail (follow) the market price by the TSL order's configured "distance" as the market price moves in the
            winning direction. If the market price moves to a level that is equal to or worse than the trailing stop value, the order will be filled and the Trade will be closed.
        fillingTransactionID: -- ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filledTime: -- Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        tradeOpenedID: -- Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        tradeReducedID: -- Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        tradeClosedIDs: -- Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancellingTransactionID: -- ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelledTime: -- Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replacesOrderID: -- The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replacedByOrderID: -- The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Trailing Stop Loss for Trade {tradeID} @ {trailingStopValue}'

    # Format string used when generating a name for this object
    _name_format = 'Trailing Stop Loss for Trade {tradeID} @ {trailingStopValue}'

    def __init__(self,
                 id: OrderID,
                 createTime: DateTime,
                 state: OrderState,
                 clientExtensions: ClientExtensions,
                 tradeID: TradeID,
                 clientTradeID: ClientID,
                 distance: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 triggerCondition: OrderTriggerCondition,
                 trailingStopValue: PriceValue,
                 fillingTransactionID: TransactionID,
                 filledTime: DateTime,
                 tradeOpenedID: TradeID,
                 tradeReducedID: TradeID,
                 tradeClosedIDs: TradeID,
                 cancellingTransactionID: TransactionID,
                 cancelledTime: DateTime,
                 replacesOrderID: OrderID,
                 replacedByOrderID: OrderID,
                 type: OrderType = 'TRAILING_STOP_LOSS'
                 ):pass


class Trade(TypeModel):
    """The specification of a Trade within an Account. This includes the full
    representation of the Trade's dependent Orders in addition to the IDs of
    those Orders.

    Fields:
        id: -- The Trade's identifier, unique within the Trade's Account.
        instrument: -- The Trade's Instrument.
        price: -- The execution price of the Trade.
        openTime: -- The date/time when the Trade was opened.
        state: -- The current state of the Trade.
        initialUnits: -- The initial size of the Trade. Negative values indicate
            a short Trade, and positive values indicate a long Trade.
        currentUnits: -- The number of units currently open for the Trade. This
            value is reduced to 0.0 as the Trade is closed.
        realizedPL: -- The total profit/loss realized on the closed portion of the Trade.
        unrealizedPL: -- The unrealized profit/loss on the open portion of the Trade.
        averageClosePrice: -- The average closing price of the Trade. Only present if
            the Trade has been closed or reduced at least once.
        closingTransactionIDs: -- The IDs of the Transactions that have closed portions of this Trade.
        financing: -- The financing paid/collected for this Trade.
        closeTime: -- The date/time when the Trade was fully closed.
            Only provided for Trades whose state is CLOSED.
        clientExtensions: -- The client extensions of the Trade.
        takeProfitOrder: -- Full representation of the Trade's Take Profit
            Order, only provided if such an Order exists.
        stopLossOrder: -- Full representation of the Trade's Stop Loss
            Order, only provided if such an Order exists.
        trailingStopLossOrder: -- Full representation of the Trade's Trailing Stop Loss
            Order, only provided if such an Order exists.

    """

    # Format string used when generating a summary for this object
    _summary_format = '{currentUnits} ({initialUnits}) of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = '{currentUnits} ({initialUnits}) of {instrument} @ {price}'

    def __init__(self,
                 id: TradeID,
                 instrument: InstrumentName,
                 price: PriceValue,
                 openTime: DateTime,
                 state: TradeState,
                 initialUnits: DecimalNumber,
                 currentUnits: DecimalNumber,
                 realizedPL: AccountUnits,
                 unrealizedPL: AccountUnits,
                 averageClosePrice: PriceValue,
                 closingTransactionIDs: TransactionID,
                 financing: AccountUnits,
                 closeTime: DateTime,
                 clientExtensions: ClientExtensions,
                 takeProfitOrder: TakeProfitOrder,
                 stopLossOrder: StopLossOrder,
                 trailingStopLossOrder: TrailingStopLossOrder
                 ): pass




class ClientConfigureRejectTransaction(TypeModel):
    """A ClientConfigureRejectTransaction represents the reject of configuration
    of an Account by a client.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "CLIENT_CONFIGURE_REJECT" in a ClientConfigureRejectTransaction.
        alias: -- The client-provided alias for the Account.
        marginRate: -- The margin rate override for the Account.
        rejectReason: -- The reason that the Reject Transaction was created

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Client Configure Reject'

    # Format string used when generating a name for this object
    _name_format = 'Client Configure Reject'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 alias: str,
                 marginRate: DecimalNumber,
                 rejectReason: TransactionRejectReason,
                 type: TransactionType = 'CLIENT_CONFIGURE_REJECT'
                 ): pass




class OrderCancelRejectTransaction(TypeModel):
    """An OrderCancelRejectTransaction represents the rejection of the
    cancellation of an Order in the client's Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "ORDER_CANCEL_REJECT" for an OrderCancelRejectTransaction.
        orderID: -- The ID of the Order intended to be cancelled
        clientOrderID: -- The client ID of the Order intended to be cancelled
            (only provided if the Order has a client Order ID).
        reason: -- The reason that the Order was to be cancelled.
        rejectReason: -- The reason that the Reject Transaction was created

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Order Cancel Reject {orderID}'

    # Format string used when generating a name for this object
    _name_format = 'Order Cancel Reject {orderID}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 orderID: OrderID,
                 clientOrderID: OrderID,
                 reason: OrderCancelReason,
                 rejectReason: TransactionRejectReason,
                 type: TransactionType = 'ORDER_CANCEL_REJECT'
                 ): pass




class OrderClientExtensionsModifyRejectTransaction(TypeModel):
    """A OrderClientExtensionsModifyRejectTransaction represents the rejection of
    the modification of an Order's Client Extensions.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT" for a OrderClientExtensionsModifyRejectTransaction.
        orderID: -- The ID of the Order who's client extensions are to be modified.
        clientOrderID: -- The original Client ID of the Order who's client extensions are to be modified.
        clientExtensionsModify: -- The new Client Extensions for the Order.
        tradeClientExtensionsModify: -- The new Client Extensions for the Order's Trade on fill.
        rejectReason: -- The reason that the Reject Transaction was created

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Reject Modify Order {orderID} Client Extensions'

    # Format string used when generating a name for this object
    _name_format = 'Reject Modify Order {orderID} Client Extensions'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 orderID: OrderID,
                 clientOrderID: ClientID,
                 clientExtensionsModify: ClientExtensions,
                 tradeClientExtensionsModify: ClientExtensions,
                 rejectReason: TransactionRejectReason,
                 type: TransactionType = 'ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT'
                 ): pass




class TradeClientExtensionsModifyRejectTransaction(TypeModel):
    """A TradeClientExtensionsModifyRejectTransaction represents the rejection of
    the modification of a Trade's Client Extensions.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT" for a TradeClientExtensionsModifyRejectTransaction.
        tradeID: -- The ID of the Trade who's client extensions are to be modified.
        clientTradeID: -- The original Client ID of the Trade who's client extensions are to be modified.
        tradeClientExtensionsModify: -- The new Client Extensions for the Trade.
        rejectReason: -- The reason that the Reject Transaction was created

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Reject Modify Trade {tradeID} Client Extensions'

    # Format string used when generating a name for this object
    _name_format = 'Reject Modify Trade {tradeID} Client Extensions'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 tradeID: TradeID,
                 clientTradeID: ClientID,
                 tradeClientExtensionsModify: ClientExtensions,
                 rejectReason: TransactionRejectReason,
                 type: TransactionType = 'TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT'
                 ): pass




class TransferFundsTransaction(TypeModel):
    """A TransferFundsTransaction represents the transfer of funds in/out of an
    Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TRANSFER_FUNDS" in a TransferFundsTransaction.
        amount: -- The amount to deposit/withdraw from the Account in the Account's home currency.
            A positive value indicates a deposit, a negative value indicates a withdrawal.
        fundingReason: -- The reason that an Account is being funded.
        comment: -- An optional comment that may be attached to a fund transfer for audit purposes
        accountBalance: -- The Account's balance after funds are transferred.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Account Transfer of {amount}'

    # Format string used when generating a name for this object
    _name_format = 'Account Transfer of {amount}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 amount: AccountUnits,
                 fundingReason: FundingReason,
                 comment: str,
                 accountBalance: AccountUnits,
                 type: TransactionType = 'TRANSFER_FUNDS'
                 ): pass




class TransferFundsRejectTransaction(TypeModel):
    """A TransferFundsRejectTransaction represents the rejection of the transfer
    of funds in/out of an Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TRANSFER_FUNDS_REJECT" in a TransferFundsRejectTransaction.
        amount: -- The amount to deposit/withdraw from the Account in the Account's home currency.
            A positive value indicates a deposit, a negative value indicates a withdrawal.
        fundingReason: -- The reason that an Account is being funded.
        comment: -- An optional comment that may be attached to a fund transfer for audit purposes
        rejectReason: -- The reason that the Reject Transaction was created

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Account Reject Transfer of {amount}'

    # Format string used when generating a name for this object
    _name_format = 'Account Reject Transfer of {amount}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 amount: AccountUnits,
                 fundingReason: FundingReason,
                 comment: str,
                 rejectReason: TransactionRejectReason,
                 type: TransactionType = 'TRANSFER_FUNDS_REJECT'
                 ): pass




class LimitOrderRequest(TypeModel):
    """A LimitOrderRequest specifies the parameters that may be set when creating
    a Limit Order.

    Fields:
        type: -- The type of the Order to Create. Must
            be set to "LIMIT" when creating a Market Order.
        instrument: -- The Limit Order's Instrument.
        units: -- The quantity requested to be filled by the Limit Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Limit Order. The Limit Order will only be
            filled by a market price that is equal to or better than this price.
        timeInForce: -- The time-in-force requested for the Limit Order.
        gtdTime: -- The date/time when the Limit Order will
            be cancelled if its timeInForce is "GTD".
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        clientExtensions: -- The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.
        takeProfitOnFill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.
        stopLossOnFill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.
        trailingStopLossOnFill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.

    """

    # Format string used when generating a summary for this object
    _summary_format = '{units} units of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = '{units} units of {instrument} @ {price}'

    def __init__(self,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 price: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 positionFill: OrderPositionFill,
                 triggerCondition: OrderTriggerCondition,
                 clientExtensions: ClientExtensions,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 type: OrderType = 'LIMIT'
                 ):pass




class MarketIfTouchedOrderRequest(TypeModel):
    """A MarketIfTouchedOrderRequest specifies the parameters that may be set when
    creating a Market-if-Touched Order.

    Fields:
        type: -- The type of the Order to Create. Must be
            set to "MARKET_IF_TOUCHED" when creating a Market If Touched Order.
        instrument: -- The MarketIfTouched Order's Instrument.
        units: -- The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be filled by a market price that crosses this price from the direction of the market price
            at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's price and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.
        priceBound: -- The worst market price that may be used to fill this MarketIfTouched Order.
        timeInForce: -- The time-in-force requested for the MarketIfTouched Order. Restricted
            to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
        gtdTime: -- The date/time when the MarketIfTouched Order will
            be cancelled if its timeInForce is "GTD".
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        clientExtensions: -- The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.
        takeProfitOnFill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.
        stopLossOnFill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.
        trailingStopLossOnFill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.

        """

    # Format string used when generating a summary for this object
    _summary_format = '{units} units of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = '{units} units of {instrument} @ {price}'

    def __init__(self,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 price: PriceValue,
                 priceBound: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 positionFill: OrderPositionFill,
                 triggerCondition: OrderTriggerCondition,
                 clientExtensions: ClientExtensions,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 type: OrderType = 'MARKET_IF_TOUCHED'
                 ):pass




class StopOrderRequest(TypeModel):
    """A StopOrderRequest specifies the parameters that may be set when creating a
    Stop Order.

    Fields:
        type: -- The type of the Order to Create. Must
            be set to "STOP" when creating a Stop Order.
        instrument: -- The Stop Order's Instrument.
        units: -- The quantity requested to be filled by the Stop Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Stop Order. The Stop Order will only be
            filled by a market price that is equal to or worse than this price.
        priceBound: -- The worst market price that may be used to fill this Stop Order. If the market gaps and
            crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.
        timeInForce: -- The time-in-force requested for the Stop Order.
        gtdTime: -- The date/time when the Stop Order will
            be cancelled if its timeInForce is "GTD".
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        clientExtensions: -- The client extensions to add to the Order. Do not set,
            modify, or delete clientExtensions if your account is associated with MT4.
        takeProfitOnFill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.
        stopLossOnFill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.
        trailingStopLossOnFill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.

    """

    # Format string used when generating a summary for this object
    _summary_format = '{units} units of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = '{units} units of {instrument} @ {price}'

    def __init__(self,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 price: PriceValue,
                 priceBound: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 positionFill: OrderPositionFill,
                 triggerCondition: OrderTriggerCondition,
                 clientExtensions: ClientExtensions,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 type: OrderType = 'STOP'
                 ):pass




class Account(TypeModel):
    """The full details of a client's Account. This includes full open Trade, open
    Position and pending Order representation.

    Fields:
        id: -- The Account's identifier
        alias: -- Client-assigned alias for the Account. Only provided
            if the Account has an alias set
        currency: -- The home currency of the Account
        balance: -- The current balance of the Account. Represented in the Account's home currency.
        createdByUserID: -- ID of the user that created the Account.
        createdTime: -- The date/time when the Account was created.
        pl: -- The total profit/loss realized over the lifetime of
            the Account. Represented in the Account's home currency.
        resettablePL: -- The total realized profit/loss for the Account since it was
            last reset by the client. Represented in the Account's home currency.
        resettabledPLTime: -- The date/time that the Account's resettablePL was last reset.
        commission: -- The total amount of commission paid over the lifetime
            of the Account. Represented in the Account's home currency.
        marginRate: -- Client-provided margin rate override for the Account. The effective margin rate of the Account is the lesser of this value and
            the OANDA margin rate for the Account's division. This value is only provided if a margin rate override exists for the Account.
        marginCallEnterTime: -- The date/time when the Account entered a margin call state.
            Only provided if the Account is in a margin call.
        marginCallExtensionCount: -- The number of times that the Account's current margin call was extended.
        lastMarginCallExtensionTime: -- The date/time of the Account's last margin call extension.
        openTradeCount: -- The number of Trades currently open in the Account.
        openPositionCount: -- The number of Positions currently open in the Account.
        pendingOrderCount: -- The number of Orders currently pending in the Account.
        hedgingEnabled: -- Flag indicating that the Account has hedging enabled.
        unrealizedPL: -- The total unrealized profit/loss for all Trades currently open
            in the Account. Represented in the Account's home currency.
        NAV: -- The net asset value of the Account. Equal to
            Account balance + unrealizedPL. Represented in the Account's home currency.
        marginUsed: -- Margin currently used for the Account.
            Represented in the Account's home currency.
        marginAvailable: -- Margin available for Account. Represented in the Account's home currency.
        positionValue: -- The value of the Account's open
            positions represented in the Account's home currency.
        marginCloseoutUnrealizedPL: -- The Account's margin closeout unrealized PL.
        marginCloseoutNAV: -- The Account's margin closeout NAV.
        marginCloseoutMarginUsed: -- The Account's margin closeout margin used.
        marginCloseoutPercent: -- The Account's margin closeout percentage. When this value is 1.0
            or above the Account is in a margin closeout situation.
        marginCloseoutPositionValue: -- The value of the Account's open positions as used
            for margin closeout calculations represented in the Account's home currency.
        withdrawalLimit: -- The current WithdrawalLimit for the account which will be zero or
            a positive value indicating how much can be withdrawn from the account.
        marginCallMarginUsed: -- The Account's margin call margin used.
        marginCallPercent: -- The Account's margin call percentage. When this value is 1.0
            or above the Account is in a margin call situation.
        lastTransactionID: -- The ID of the last Transaction created for the Account.
        trades: -- The details of the Trades currently open in the Account.
        positions: -- The details all Account Positions.
        orders: -- The details of the Orders currently pending in the Account.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Account {id}'

    def __init__(self,
                 id: AccountID,
                 alias: str,
                 currency: Currency,
                 balance: AccountUnits,
                 createdByUserID: int,
                 createdTime: DateTime,
                 pl: AccountUnits,
                 resettablePL: AccountUnits,
                 resettabledPLTime: DateTime,
                 commission: AccountUnits,
                 marginRate: DecimalNumber,
                 marginCallEnterTime: DateTime,
                 marginCallExtensionCount: int,
                 lastMarginCallExtensionTime: DateTime,
                 openTradeCount: int,
                 openPositionCount: int,
                 pendingOrderCount: int,
                 hedgingEnabled: bool,
                 unrealizedPL: AccountUnits,
                 NAV: AccountUnits,
                 marginUsed: AccountUnits,
                 marginAvailable: AccountUnits,
                 positionValue: AccountUnits,
                 marginCloseoutUnrealizedPL: AccountUnits,
                 marginCloseoutNAV: AccountUnits,
                 marginCloseoutMarginUsed: AccountUnits,
                 marginCloseoutPercent: DecimalNumber,
                 marginCloseoutPositionValue: DecimalNumber,
                 withdrawalLimit: AccountUnits,
                 marginCallMarginUsed: AccountUnits,
                 marginCallPercent: DecimalNumber,
                 lastTransactionID: TransactionID,
                 trades: TradeSummary,
                 positions: Position,
                 orders: Order
                 ): pass




class MarketOrderTransaction(TypeModel):
    """A MarketOrderTransaction represents the creation of a Market Order in the
    user's account. A Market Order is an Order that is filled immediately at
    the current market price. Market Orders can be specialized when they are
    created to accomplish a specific tas': 'to' close a Trade, to closeout a
    Position or to particiate in in a Margin closeout.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "MARKET_ORDER" in a MarketOrderTransaction.
        instrument: -- The Market Order's Instrument.
        units: -- The quantity requested to be filled by the Market Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        timeInForce: -- The time-in-force requested for the Market Order.
            Restricted to FOK or IOC for a MarketOrder.
        priceBound: -- The worst price that the client is willing to have the Market Order filled at.
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        tradeClose: -- Details of the Trade requested to be closed, only provided when
            the Market Order is being used to explicitly close a Trade.
        longPositionCloseout: -- Details of the long Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a long Position.
        shortPositionCloseout: -- Details of the short Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a short Position.
        marginCloseout: -- Details of the Margin Closeout that this Market Order was created for
        delayedTradeClose: -- Details of the delayed Trade close that this Market Order was created for
        reason: -- The reason that the Market Order was created
        clientExtensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        takeProfitOnFill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stopLossOnFill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailingStopLossOnFill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Create Market Order {id} ({reason}): {units} of {instrument}'

    # Format string used when generating a name for this object
    _name_format = 'Create Market Order {id} ({reason}): {units} of {instrument}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 timeInForce: TimeInForce,
                 priceBound: PriceValue,
                 positionFill: OrderPositionFill,
                 tradeClose: MarketOrderTradeClose,
                 longPositionCloseout: MarketOrderPositionCloseout,
                 shortPositionCloseout: MarketOrderPositionCloseout,
                 marginCloseout: MarketOrderMarginCloseout,
                 delayedTradeClose: MarketOrderDelayedTradeClose,
                 reason: MarketOrderReason,
                 clientExtensions: ClientExtensions,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 type: TransactionType = 'MARKET_ORDER'
                 ): pass




class MarketOrderRejectTransaction(TypeModel):
    """A MarketOrderRejectTransaction represents the rejection of the creation of
    a Market Order.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "MARKET_ORDER_REJECT" in a MarketOrderRejectTransaction.
        instrument: -- The Market Order's Instrument.
        units: -- The quantity requested to be filled by the Market Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        timeInForce: -- The time-in-force requested for the Market Order.
            Restricted to FOK or IOC for a MarketOrder.
        priceBound: -- The worst price that the client is willing to have the Market Order filled at.
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        tradeClose: -- Details of the Trade requested to be closed, only provided when
            the Market Order is being used to explicitly close a Trade.
        longPositionCloseout: -- Details of the long Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a long Position.
        shortPositionCloseout: -- Details of the short Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a short Position.
        marginCloseout: -- Details of the Margin Closeout that this Market Order was created for
        delayedTradeClose: -- Details of the delayed Trade close that this Market Order was created for
        reason: -- The reason that the Market Order was created
        clientExtensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        takeProfitOnFill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stopLossOnFill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailingStopLossOnFill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        rejectReason: -- The reason that the Reject Transaction was created

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Reject Market Order ({reason}): {units} of {instrument}'

    # Format string used when generating a name for this object
    _name_format = 'Reject Market Order ({reason}): {units} of {instrument}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 timeInForce: TimeInForce,
                 priceBound: PriceValue,
                 positionFill: OrderPositionFill,
                 tradeClose: MarketOrderTradeClose,
                 longPositionCloseout: MarketOrderPositionCloseout,
                 shortPositionCloseout: MarketOrderPositionCloseout,
                 marginCloseout: MarketOrderMarginCloseout,
                 delayedTradeClose: MarketOrderDelayedTradeClose,
                 reason: MarketOrderReason,
                 clientExtensions: ClientExtensions,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 rejectReason: TransactionRejectReason,
                 type: TransactionType = 'MARKET_ORDER_REJECT'
                 ): pass




class StopLossOrderTransaction(TypeModel):
    """A StopLossOrderTransaction represents the creation of a StopLoss Order in
    the user's Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "STOP_LOSS_ORDER" in a StopLossOrderTransaction.
        tradeID: -- The ID of the Trade to close when the price threshold is breached.
        clientTradeID: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the StopLoss Order. The associated Trade will be
            closed by a market price that is equal to or worse than this threshold.
        timeInForce: -- The time-in-force requested for the StopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for StopLoss Orders.
        gtdTime: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Stop Loss Order was initiated
        clientExtensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        orderFillTransactionID: -- The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        replacesOrderID: -- The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancellingTransactionID: -- The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Create Stop Loss Order {id} ({reason}): Close Trade {tradeID} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Create Stop Loss Order {id} ({reason}): Close Trade {tradeID} @ {price}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 tradeID: TradeID,
                 clientTradeID: ClientID,
                 price: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 triggerCondition: OrderTriggerCondition,
                 reason: StopLossOrderReason,
                 clientExtensions: ClientExtensions,
                 orderFillTransactionID: TransactionID,
                 replacesOrderID: OrderID,
                 cancellingTransactionID: TransactionID,
                 type: TransactionType = 'STOP_LOSS_ORDER'
                 ): pass


class TrailingStopLossOrderTransaction(TypeModel):
    """A TrailingStopLossOrderTransaction represents the creation of a
    TrailingStopLoss Order in the user's Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TRAILING_STOP_LOSS_ORDER" in a TrailingStopLossOrderTransaction.
        tradeID: -- The ID of the Trade to close when the price threshold is breached.
        clientTradeID: -- The client ID of the Trade to be closed when the price threshold is breached.
        distance: -- The price distance specified for the TrailingStopLoss Order.
        timeInForce: -- The time-in-force requested for the TrailingStopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
        gtdTime: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Trailing Stop Loss Order was initiated
        clientExtensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        orderFillTransactionID: -- The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        replacesOrderID: -- The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancellingTransactionID: -- The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Create Trailing Stop Loss Order {id} ({reason}): Close Trade {tradeID}'

    # Format string used when generating a name for this object
    _name_format = 'Create Trailing Stop Loss Order {id} ({reason}): Close Trade {tradeID}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 tradeID: TradeID,
                 clientTradeID: ClientID,
                 distance: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 triggerCondition: OrderTriggerCondition,
                 reason: TrailingStopLossOrderReason,
                 clientExtensions: ClientExtensions,
                 orderFillTransactionID: TransactionID,
                 replacesOrderID: OrderID,
                 cancellingTransactionID: TransactionID,
                 type: TransactionType = 'TRAILING_STOP_LOSS_ORDER'
                 ): pass




class LimitOrder(TypeModel):
    """A LimitOrder is an order that is created with a price threshold, and will
    only be filled by a price that is equal to or better than the threshold.

    Fields:
        id: -- The Order's identifier, unique within the Order's Account.
        createTime: -- The time when the Order was created.
        state: -- The current state of the Order.
        clientExtensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        type: -- The type of the Order. Always set to "LIMIT" for Limit Orders.
        instrument: -- The Limit Order's Instrument.
        units: -- The quantity requested to be filled by the Limit Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Limit Order. The Limit Order will only be
            filled by a market price that is equal to or better than this price.
        timeInForce: -- The time-in-force requested for the Limit Order.
        gtdTime: -- The date/time when the Limit Order will
            be cancelled if its timeInForce is "GTD".
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        takeProfitOnFill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.
        stopLossOnFill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.
        trailingStopLossOnFill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.
        fillingTransactionID: -- ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filledTime: -- Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        tradeOpenedID: -- Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        tradeReducedID: -- Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        tradeClosedIDs: -- Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancellingTransactionID: -- ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelledTime: -- Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replacesOrderID: -- The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replacedByOrderID: -- The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

        """

    # Format string used when generating a summary for this object
    _summary_format = '{units} units of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = '{units} units of {instrument} @ {price}'

    def __init__(self,
                 id: OrderID,
                 createTime: DateTime,
                 state: OrderState,
                 clientExtensions: ClientExtensions,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 price: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 positionFill: OrderPositionFill,
                 triggerCondition: OrderTriggerCondition,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 fillingTransactionID: TransactionID,
                 filledTime: DateTime,
                 tradeOpenedID: TradeID,
                 tradeReducedID: TradeID,
                 tradeClosedIDs: TradeID,
                 cancellingTransactionID: TransactionID,
                 cancelledTime: DateTime,
                 replacesOrderID: OrderID,
                 replacedByOrderID: OrderID,
                 type: OrderType = 'LIMIT'
                 ):pass




class MarketIfTouchedOrder(TypeModel):
    """A MarketIfTouchedOrder is an order that is created with a price threshold,
    and will only be filled by a market price that is touches or crosses the
    threshold.

    Fields:
        id: -- The Order's identifier, unique within the Order's Account.
        createTime: -- The time when the Order was created.
        state: -- The current state of the Order.
        clientExtensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        type: -- The type of the Order. Always set
            to "MARKET_IF_TOUCHED" for Market If Touched Orders.
        instrument: -- The MarketIfTouched Order's Instrument.
        units: -- The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be filled by a market price that crosses this price from the direction of the market price
            at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's price and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.
        priceBound: -- The worst market price that may be used to fill this MarketIfTouched Order.
        timeInForce: -- The time-in-force requested for the MarketIfTouched Order. Restricted
            to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
        gtdTime: -- The date/time when the MarketIfTouched Order will
            be cancelled if its timeInForce is "GTD".
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        initialMarketPrice: -- The Market price at the time when the MarketIfTouched Order was created.
        takeProfitOnFill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.
        stopLossOnFill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.
        trailingStopLossOnFill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.
        fillingTransactionID: -- ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filledTime: -- Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        tradeOpenedID: -- Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        tradeReducedID: -- Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        tradeClosedIDs: -- Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancellingTransactionID: -- ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelledTime: -- Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replacesOrderID: -- The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replacedByOrderID: -- The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

        """

    # Format string used when generating a summary for this object
    _summary_format = '{units} units of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = '{units} units of {instrument} @ {price}'

    def __init__(self,
                 id: OrderID,
                 createTime: DateTime,
                 state: OrderState,
                 clientExtensions: ClientExtensions,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 price: PriceValue,
                 priceBound: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 positionFill: OrderPositionFill,
                 triggerCondition: OrderTriggerCondition,
                 initialMarketPrice: PriceValue,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 fillingTransactionID: TransactionID,
                 filledTime: DateTime,
                 tradeOpenedID: TradeID,
                 tradeReducedID: TradeID,
                 tradeClosedIDs: TradeID,
                 cancellingTransactionID: TransactionID,
                 cancelledTime: DateTime,
                 replacesOrderID: OrderID,
                 replacedByOrderID: OrderID,
                 type: OrderType = 'MARKET_IF_TOUCHED'
                 ):pass




class StopOrder(TypeModel):
    """A StopOrder is an order that is created with a price threshold, and will
    only be filled by a price that is equal to or worse than the threshold.

    Fields:
        id: -- The Order's identifier, unique within the Order's Account.
        createTime: -- The time when the Order was created.
        state: -- The current state of the Order.
        clientExtensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        type: -- The type of the Order. Always set to "STOP" for Stop Orders.
        instrument: -- The Stop Order's Instrument.
        units: -- The quantity requested to be filled by the Stop Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Stop Order. The Stop Order will only be
            filled by a market price that is equal to or worse than this price.
        priceBound: -- The worst market price that may be used to fill this Stop Order. If the market gaps and
            crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.
        timeInForce: -- The time-in-force requested for the Stop Order.
        gtdTime: -- The date/time when the Stop Order will
            be cancelled if its timeInForce is "GTD".
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        takeProfitOnFill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.
        stopLossOnFill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.
        trailingStopLossOnFill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.
        fillingTransactionID: -- ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filledTime: -- Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        tradeOpenedID: -- Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        tradeReducedID: -- Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        tradeClosedIDs: -- Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancellingTransactionID: -- ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelledTime: -- Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)
        replacesOrderID: -- The ID of the Order that was replaced by this Order
            (only provided if this Order was created as part of a cancel/replace).
        replacedByOrderID: -- The ID of the Order that replaced this Order (only
            provided if this Order was cancelled as part of a cancel/replace).

    """

    # Format string used when generating a summary for this object
    _summary_format = '{units} units of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = '{units} units of {instrument} @ {price}'

    def __init__(self,
                 id: OrderID,
                 createTime: DateTime,
                 state: OrderState,
                 clientExtensions: ClientExtensions,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 price: PriceValue,
                 priceBound: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 positionFill: OrderPositionFill,
                 triggerCondition: OrderTriggerCondition,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 fillingTransactionID: TransactionID,
                 filledTime: DateTime,
                 tradeOpenedID: TradeID,
                 tradeReducedID: TradeID,
                 tradeClosedIDs: TradeID,
                 cancellingTransactionID: TransactionID,
                 cancelledTime: DateTime,
                 replacesOrderID: OrderID,
                 replacedByOrderID: OrderID,
                 type: OrderType = 'STOP'
                 ):pass




class OrderFillTransaction(TypeModel):
    """An OrderFillTransaction represents the filling of an Order in the client's
    Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "ORDER_FILL" for an OrderFillTransaction.
        orderID: -- The ID of the Order filled.
        clientOrderID: -- The client Order ID of the Order filled
            (only provided if the client has assigned one).
        instrument: -- The name of the filled Order's instrument.
        units: -- The number of units filled by the Order.
        price: -- The average market price that the Order was filled at.
        fullPrice: -- The price in effect for the account at the time of the Order fill.
        reason: -- The reason that an Order was filled
        pl: -- The profit or loss incurred when the Order was filled.
        financing: -- The financing paid or collected when the Order was filled.
        commission: -- The commission charged in the Account's home currency as a result of filling the Order. The commission is
            always represented as a positive quantity of the Account's home currency, however it reduces the balance in the Account.
        accountBalance: -- The Account's balance after the Order was filled.
        tradeOpened: -- The Trade that was opened when the Order was filled
            (only provided if filling the Order resulted in a new Trade).
        tradesClosed: -- The Trades that were closed when the Order was filled (only
            provided if filling the Order resulted in a closing open Trades).
        tradeReduced: -- The Trade that was reduced when the Order was filled (only
            provided if filling the Order resulted in reducing an open Trade).

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Fill Order {orderID} ({reason}): {units} of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Fill Order {orderID} ({reason}): {units} of {instrument} @ {price}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 orderID: OrderID,
                 clientOrderID: ClientID,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 price: PriceValue,
                 fullPrice: ClientPrice,
                 reason: OrderFillReason,
                 pl: AccountUnits,
                 financing: AccountUnits,
                 commission: AccountUnits,
                 accountBalance: AccountUnits,
                 tradeOpened: TradeOpen,
                 tradesClosed: TradeReduce,
                 tradeReduced: TradeReduce,
                 type: TransactionType = 'ORDER_FILL'
                 ): pass




class StopLossOrderRejectTransaction(TypeModel):
    """A StopLossOrderRejectTransaction represents the rejection of the creation
    of a StopLoss Order.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "STOP_LOSS_ORDER_REJECT" in a StopLossOrderRejectTransaction.
        tradeID: -- The ID of the Trade to close when the price threshold is breached.
        clientTradeID: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the StopLoss Order. The associated Trade will be
            closed by a market price that is equal to or worse than this threshold.
        timeInForce: -- The time-in-force requested for the StopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for StopLoss Orders.
        gtdTime: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Stop Loss Order was initiated
        clientExtensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        orderFillTransactionID: -- The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        intendedReplacesOrderID: -- The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        rejectReason: -- The reason that the Reject Transaction was created

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Reject Stop Loss Order ({reason}): Close Trade {tradeID} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Reject Stop Loss Order ({reason}): Close Trade {tradeID} @ {price}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 tradeID: TradeID,
                 clientTradeID: ClientID,
                 price: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 triggerCondition: OrderTriggerCondition,
                 reason: StopLossOrderReason,
                 clientExtensions: ClientExtensions,
                 orderFillTransactionID: TransactionID,
                 intendedReplacesOrderID: OrderID,
                 rejectReason: TransactionRejectReason,
                 type: TransactionType = 'STOP_LOSS_ORDER_REJECT'
                 ): pass




class MarketIfTouchedOrderTransaction(TypeModel):
    """A MarketIfTouchedOrderTransaction represents the creation of a
    MarketIfTouched Order in the user's Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "MARKET_IF_TOUCHED_ORDER" in a MarketIfTouchedOrderTransaction.
        instrument: -- The MarketIfTouched Order's Instrument.
        units: -- The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be filled by a market price that crosses this price from the direction of the market price
            at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's price and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.
        priceBound: -- The worst market price that may be used to fill this MarketIfTouched Order.
        timeInForce: -- The time-in-force requested for the MarketIfTouched Order. Restricted
            to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
        gtdTime: -- The date/time when the MarketIfTouched Order will
            be cancelled if its timeInForce is "GTD".
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Market-if-touched Order was initiated
        clientExtensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        takeProfitOnFill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stopLossOnFill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailingStopLossOnFill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        replacesOrderID: -- The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancellingTransactionID: -- The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Create MIT Order {id} ({reason}): {units} of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Create MIT Order {id} ({reason}): {units} of {instrument} @ {price}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 price: PriceValue,
                 priceBound: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 positionFill: OrderPositionFill,
                 triggerCondition: OrderTriggerCondition,
                 reason: MarketIfTouchedOrderReason,
                 clientExtensions: ClientExtensions,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 replacesOrderID: OrderID,
                 cancellingTransactionID: TransactionID,
                 type: TransactionType = 'MARKET_IF_TOUCHED_ORDER'
                 ): pass




class LimitOrderTransaction(TypeModel):
    """A LimitOrderTransaction represents the creation of a Limit Order in the
    user's Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "LIMIT_ORDER" in a LimitOrderTransaction.
        instrument: -- The Limit Order's Instrument.
        units: -- The quantity requested to be filled by the Limit Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Limit Order. The Limit Order will only be
            filled by a market price that is equal to or better than this price.
        timeInForce: -- The time-in-force requested for the Limit Order.
        gtdTime: -- The date/time when the Limit Order will
            be cancelled if its timeInForce is "GTD".
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Limit Order was initiated
        clientExtensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        takeProfitOnFill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stopLossOnFill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailingStopLossOnFill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        replacesOrderID: -- The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancellingTransactionID: -- The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Create Limit Order {id} ({reason}): {units} of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Create Limit Order {id} ({reason}): {units} of {instrument} @ {price}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 price: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 positionFill: OrderPositionFill,
                 triggerCondition: OrderTriggerCondition,
                 reason: LimitOrderReason,
                 clientExtensions: ClientExtensions,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 replacesOrderID: OrderID,
                 cancellingTransactionID: TransactionID,
                 type: TransactionType = 'LIMIT_ORDER'
                 ): pass




class TakeProfitOrderRejectTransaction(TypeModel):
    """A TakeProfitOrderRejectTransaction represents the rejection of the creation
    of a TakeProfit Order.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TAKE_PROFIT_ORDER_REJECT" in a TakeProfitOrderRejectTransaction.
        tradeID: -- The ID of the Trade to close when the price threshold is breached.
        clientTradeID: -- The client ID of the Trade to be closed when the price threshold is breached.
        price: -- The price threshold specified for the TakeProfit Order. The associated Trade will be
            closed by a market price that is equal to or better than this threshold.
        timeInForce: -- The time-in-force requested for the TakeProfit Order. Restricted
            to "GTC", "GFD" and "GTD" for TakeProfit Orders.
        gtdTime: -- The date/time when the TakeProfit Order will
            be cancelled if its timeInForce is "GTD".
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Take Profit Order was initiated
        clientExtensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        orderFillTransactionID: -- The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        intendedReplacesOrderID: -- The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        rejectReason: -- The reason that the Reject Transaction was created

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Reject Take Profit Order ({reason}): Close Trade {tradeID} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Reject Take Profit Order ({reason}): Close Trade {tradeID} @ {price}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 tradeID: TradeID,
                 clientTradeID: ClientID,
                 price: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 triggerCondition: OrderTriggerCondition,
                 reason: TakeProfitOrderReason,
                 clientExtensions: ClientExtensions,
                 orderFillTransactionID: TransactionID,
                 intendedReplacesOrderID: OrderID,
                 rejectReason: TransactionRejectReason,
                 type: TransactionType = 'TAKE_PROFIT_ORDER_REJECT'
                 ): pass




class TrailingStopLossOrderRejectTransaction(TypeModel):
    """A TrailingStopLossOrderRejectTransaction represents the rejection of the
    creation of a TrailingStopLoss Order.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "TRAILING_STOP_LOSS_ORDER_REJECT" in a TrailingStopLossOrderRejectTransaction.
        tradeID: -- The ID of the Trade to close when the price threshold is breached.
        clientTradeID: -- The client ID of the Trade to be closed when the price threshold is breached.
        distance: -- The price distance specified for the TrailingStopLoss Order.
        timeInForce: -- The time-in-force requested for the TrailingStopLoss Order. Restricted
            to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
        gtdTime: -- The date/time when the StopLoss Order will
            be cancelled if its timeInForce is "GTD".
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Trailing Stop Loss Order was initiated
        clientExtensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        orderFillTransactionID: -- The ID of the OrderFill Transaction that caused this Order to be created
            (only provided if this Order was created automatically when another Order was filled).
        intendedReplacesOrderID: -- The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        rejectReason: -- The reason that the Reject Transaction was created

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Reject Trailing Stop Loss Order ({reason}): Close Trade {tradeID}'

    # Format string used when generating a name for this object
    _name_format = 'Reject Trailing Stop Loss Order ({reason}): Close Trade {tradeID}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 tradeID: TradeID,
                 clientTradeID: ClientID,
                 distance: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 triggerCondition: OrderTriggerCondition,
                 reason: TrailingStopLossOrderReason,
                 clientExtensions: ClientExtensions,
                 orderFillTransactionID: TransactionID,
                 intendedReplacesOrderID: OrderID,
                 rejectReason: TransactionRejectReason,
                 type: TransactionType = 'TRAILING_STOP_LOSS_ORDER_REJECT'
                 ): pass




class StopOrderTransaction(TypeModel):
    """A StopOrderTransaction represents the creation of a Stop Order in the
    user's Account.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "STOP_ORDER" in a StopOrderTransaction.
        instrument: -- The Stop Order's Instrument.
        units: -- The quantity requested to be filled by the Stop Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Stop Order. The Stop Order will only be
            filled by a market price that is equal to or worse than this price.
        priceBound: -- The worst market price that may be used to fill this Stop Order. If the market gaps and
            crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.
        timeInForce: -- The time-in-force requested for the Stop Order.
        gtdTime: -- The date/time when the Stop Order will
            be cancelled if its timeInForce is "GTD".
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Stop Order was initiated
        clientExtensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        takeProfitOnFill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stopLossOnFill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailingStopLossOnFill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        replacesOrderID: -- The ID of the Order that this Order replaces
            (only provided if this Order replaces an existing Order).
        cancellingTransactionID: -- The ID of the Transaction that cancels the replaced
            Order (only provided if this Order replaces an existing Order).

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Create Stop Order {id} ({reason}): {units} of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Create Stop Order {id} ({reason}): {units} of {instrument} @ {price}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 price: PriceValue,
                 priceBound: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 positionFill: OrderPositionFill,
                 triggerCondition: OrderTriggerCondition,
                 reason: StopOrderReason,
                 clientExtensions: ClientExtensions,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 replacesOrderID: OrderID,
                 cancellingTransactionID: TransactionID,
                 type: TransactionType = 'STOP_ORDER'
                 ): pass




class MarketIfTouchedOrderRejectTransaction(TypeModel):
    """A MarketIfTouchedOrderRejectTransaction represents the rejection of the
    creation of a MarketIfTouched Order.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "MARKET_IF_TOUCHED_ORDER_REJECT" in a MarketIfTouchedOrderRejectTransaction.
        instrument: -- The MarketIfTouched Order's Instrument.
        units: -- The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be filled by a market price that crosses this price from the direction of the market price
            at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's price and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.
        priceBound: -- The worst market price that may be used to fill this MarketIfTouched Order.
        timeInForce: -- The time-in-force requested for the MarketIfTouched Order. Restricted
            to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
        gtdTime: -- The date/time when the MarketIfTouched Order will
            be cancelled if its timeInForce is "GTD".
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Market-if-touched Order was initiated
        clientExtensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        takeProfitOnFill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stopLossOnFill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailingStopLossOnFill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        intendedReplacesOrderID: -- The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        rejectReason: -- The reason that the Reject Transaction was created

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Reject MIT Order ({reason}): {units} of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Reject MIT Order ({reason}): {units} of {instrument} @ {price}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 price: PriceValue,
                 priceBound: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 positionFill: OrderPositionFill,
                 triggerCondition: OrderTriggerCondition,
                 reason: MarketIfTouchedOrderReason,
                 clientExtensions: ClientExtensions,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 intendedReplacesOrderID: OrderID,
                 rejectReason: TransactionRejectReason,
                 type: TransactionType = 'MARKET_IF_TOUCHED_ORDER_REJECT'
                 ): pass




class LimitOrderRejectTransaction(TypeModel):
    """A LimitOrderRejectTransaction represents the rejection of the creation of a
    Limit Order.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "LIMIT_ORDER_REJECT" in a LimitOrderRejectTransaction.
        instrument: -- The Limit Order's Instrument.
        units: -- The quantity requested to be filled by the Limit Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Limit Order. The Limit Order will only be
            filled by a market price that is equal to or better than this price.
        timeInForce: -- The time-in-force requested for the Limit Order.
        gtdTime: -- The date/time when the Limit Order will
            be cancelled if its timeInForce is "GTD".
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Limit Order was initiated
        clientExtensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        takeProfitOnFill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stopLossOnFill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailingStopLossOnFill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        intendedReplacesOrderID: -- The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        rejectReason: -- The reason that the Reject Transaction was created

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Reject Limit Order ({reason}): {units} of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Reject Limit Order ({reason}): {units} of {instrument} @ {price}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 price: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 positionFill: OrderPositionFill,
                 triggerCondition: OrderTriggerCondition,
                 reason: LimitOrderReason,
                 clientExtensions: ClientExtensions,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 intendedReplacesOrderID: OrderID,
                 rejectReason: TransactionRejectReason,
                 type: TransactionType = 'LIMIT_ORDER_REJECT'
                 ): pass




class StopOrderRejectTransaction(TypeModel):
    """A StopOrderRejectTransaction represents the rejection of the creation of a
    Stop Order.

    Fields:
        id: -- The Transaction's Identifier.
        time: -- The date/time when the Transaction was created.
        userID: -- The ID of the user that initiated the creation of the Transaction.
        accountID: -- The ID of the Account the Transaction was created for.
        batchID: -- The ID of the "batch" that the Transaction belongs to.
            Transactions in the same batch are applied to the Account simultaneously.
        requestID: -- The Request ID of the request which generated the transaction.
        type: -- The Type of the Transaction. Always
            set to "STOP_ORDER_REJECT" in a StopOrderRejectTransaction.
        instrument: -- The Stop Order's Instrument.
        units: -- The quantity requested to be filled by the Stop Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        price: -- The price threshold specified for the Stop Order. The Stop Order will only be
            filled by a market price that is equal to or worse than this price.
        priceBound: -- The worst market price that may be used to fill this Stop Order. If the market gaps and
            crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.
        timeInForce: -- The time-in-force requested for the Stop Order.
        gtdTime: -- The date/time when the Stop Order will
            be cancelled if its timeInForce is "GTD".
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        triggerCondition: -- Specification of what component of a price should be used
            for comparison when determining if the Order should be filled.
        reason: -- The reason that the Stop Order was initiated
        clientExtensions: -- Client Extensions to add to the Order (only provided
            if the Order is being created with client extensions).
        takeProfitOnFill: -- The specification of the Take Profit Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        stopLossOnFill: -- The specification of the Stop Loss Order that should be created for a
            Trade opened when the Order is filled (if such a Trade is created).
        trailingStopLossOnFill: -- The specification of the Trailing Stop Loss Order that should be created for a
            Trade that is opened when the Order is filled (if such a Trade is created).
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.
        intendedReplacesOrderID: -- The ID of the Order that this Order was intended to replace
            (only provided if this Order was intended to replace an existing Order).
        rejectReason: -- The reason that the Reject Transaction was created

    """

    # Format string used when generating a summary for this object
    _summary_format = 'Reject Stop Order ({reason}): {units} of {instrument} @ {price}'

    # Format string used when generating a name for this object
    _name_format = 'Reject Stop Order ({reason}): {units} of {instrument} @ {price}'

    def __init__(self,
                 id: TransactionID,
                 time: DateTime,
                 userID: int,
                 accountID: AccountID,
                 batchID: TransactionID,
                 requestID: RequestID,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 price: PriceValue,
                 priceBound: PriceValue,
                 timeInForce: TimeInForce,
                 gtdTime: DateTime,
                 positionFill: OrderPositionFill,
                 triggerCondition: OrderTriggerCondition,
                 reason: StopOrderReason,
                 clientExtensions: ClientExtensions,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 intendedReplacesOrderID: OrderID,
                 rejectReason: TransactionRejectReason,
                 type: TransactionType = 'STOP_ORDER_REJECT'
                 ): pass




class MarketOrder(TypeModel):
    """A MarketOrder is an order that is filled immediately upon creation using
    the current market price.

    Fields:
        id: -- The Order's identifier, unique within the Order's Account.
        createTime: -- The time when the Order was created.
        state: -- The current state of the Order.
        clientExtensions: -- The client extensions of the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        type: -- The type of the Order. Always set to "MARKET" for Market Orders.
        instrument: -- The Market Order's Instrument.
        units: -- The quantity requested to be filled by the Market Order. A posititive number of units
            results in a long Order, and a negative number of units results in a short Order.
        timeInForce: -- The time-in-force requested for the Market Order.
            Restricted to FOK or IOC for a MarketOrder.
        priceBound: -- The worst price that the client is willing to have the Market Order filled at.
        positionFill: -- Specification of how Positions in the Account
            are modified when the Order is filled.
        tradeClose: -- Details of the Trade requested to be closed, only provided when
            the Market Order is being used to explicitly close a Trade.
        longPositionCloseout: -- Details of the long Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a long Position.
        shortPositionCloseout: -- Details of the short Position requested to be closed out, only provided
            when a Market Order is being used to explicitly closeout a short Position.
        marginCloseout: -- Details of the Margin Closeout that this Market Order was created for
        delayedTradeClose: -- Details of the delayed Trade close that this Market Order was created for
        takeProfitOnFill: -- TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.
        stopLossOnFill: -- StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order
            is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.
        trailingStopLossOnFill: -- TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is
            filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.
        tradeClientExtensions: -- Client Extensions to add to the Trade created when the Order is filled (if such a
            Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.
        fillingTransactionID: -- ID of the Transaction that filled this Order
            (only provided when the Order's state is FILLED)
        filledTime: -- Date/time when the Order was filled (only
            provided when the Order's state is FILLED)
        tradeOpenedID: -- Trade ID of Trade opened when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was opened as a result of the fill)
        tradeReducedID: -- Trade ID of Trade reduced when the Order was filled (only provided when the
            Order's state is FILLED and a Trade was reduced as a result of the fill)
        tradeClosedIDs: -- Trade IDs of Trades closed when the Order was filled (only provided when the Order's
            state is FILLED and one or more Trades were closed as a result of the fill)
        cancellingTransactionID: -- ID of the Transaction that cancelled the Order
            (only provided when the Order's state is CANCELLED)
        cancelledTime: -- Date/time when the Order was cancelled (only provided
            when the state of the Order is CANCELLED)

    """

    # Format string used when generating a summary for this object
    _summary_format = '{units} units of {instrument}'

    # Format string used when generating a name for this object
    _name_format = '{units} units of {instrument}'

    def __init__(self,
                 id: OrderID,
                 createTime: DateTime,
                 state: OrderState,
                 clientExtensions: ClientExtensions,
                 instrument: InstrumentName,
                 units: DecimalNumber,
                 timeInForce: TimeInForce,
                 priceBound: PriceValue,
                 positionFill: OrderPositionFill,
                 tradeClose: MarketOrderTradeClose,
                 longPositionCloseout: MarketOrderPositionCloseout,
                 shortPositionCloseout: MarketOrderPositionCloseout,
                 marginCloseout: MarketOrderMarginCloseout,
                 delayedTradeClose: MarketOrderDelayedTradeClose,
                 takeProfitOnFill: TakeProfitDetails,
                 stopLossOnFill: StopLossDetails,
                 trailingStopLossOnFill: TrailingStopLossDetails,
                 tradeClientExtensions: ClientExtensions,
                 fillingTransactionID: TransactionID,
                 filledTime: DateTime,
                 tradeOpenedID: TradeID,
                 tradeReducedID: TradeID,
                 tradeClosedIDs: TradeID,
                 cancellingTransactionID: TransactionID,
                 cancelledTime: DateTime,
                 type: OrderType = 'MARKET'
                 ):pass


