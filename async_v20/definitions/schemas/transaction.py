from ..types import *
from ...endpoints.metaclass import Array

default = lambda x: x
required = True
boolean = bool
integer = int
string = str


class ClientConfigureRejectTransaction:
    """A ClientConfigureRejectTransaction represents the reject of
    configuration of an Account by a client.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “CLIENT_CONFIGURE_REJECT” in a
        # ClientConfigureRejectTransaction.
        'type': (TransactionType, default('CLIENT_CONFIGURE_REJECT')),
        # The client-provided alias for the Account.
        'alias': string,
        # The margin rate override for the Account.
        'marginRate': DecimalNumber,
        # The reason that the Reject Transaction was created
        'rejectReason': TransactionRejectReason}


class ClientConfigureTransaction:
    """A ClientConfigureTransaction represents the configuration
    of an Account by a client.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “CLIENT_CONFIGURE” in a
        # ClientConfigureTransaction.
        'type': (TransactionType, default('CLIENT_CONFIGURE')),
        # The client-provided alias for the Account.
        'alias': string,
        # The margin rate override for the Account.
        'marginRate': DecimalNumber}


class ClientExtensions:
    """A ClientExtensions Refactor allows a client to attach a clientID, tag and comment to Orders and Trades
    in their Account. Do not set, modify, or delete this field if your account is associated with MT4.
    """
    # JSON representation of object
    schema = {
        # The Client ID of the Order/Trade
        'id': ClientID,
        # A tag associated with the Order/Trade
        'tag': ClientTag,
        # A comment associated with the Order/Trade
        'comment': ClientComment}


class CloseTransaction:
    """A CloseTransaction represents the closing of an Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “CLOSE” in a CloseTransaction.
        'type': (TransactionType, default('CLOSE'))}


class CreateTransaction:
    """A CreateTransaction represents the creation of an Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “CREATE” in a
        # CreateTransaction.
        'type': (TransactionType, default('CREATE')),
        # The ID of the Division that the Account is in
        'divisionID': integer,
        # The ID of the Site that the Account was created at
        'siteID': integer,
        # The ID of the user that the Account was created for
        'accountUserID': integer,
        # The number of the Account within the site/division/user
        'accountNumber': integer,
        # The home currency of the Account
        'homeCurrency': Currency}


class DailyFinancingTransaction:
    """A DailyFinancingTransaction represents the daily
    payment/collection of financing for an Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “DAILY_FINANCING” for a
        # DailyFinancingTransaction.
        'type': (TransactionType, default('DAILY_FINANCING')),
        # The amount of financing paid/collected for the Account.
        'financing': AccountUnits,
        # The Account’s balance after daily financing.
        'accountBalance': AccountUnits,
        # The account financing mode at the time of the daily financing.
        'accountFinancingMode': AccountFinancingMode,
        # The financing paid/collected for each Position in the Account.
        'positionFinancings': (Array[PositionFinancing])}


class DelayedTradeClosureTransaction:
    """A DelayedTradeClosure Transaction is created administratively to indicate open trades that should have been closed but weren’t because the open trades’
    instruments were untradeable at the time. Open trades listed in this transaction will be closed once their respective instruments become tradeable.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “DELAYED_TRADE_CLOSURE” for an
        # DelayedTradeClosureTransaction.
        'type': (TransactionType, default('DELAYED_TRADE_CLOSURE')),
        # The reason for the delayed trade closure
        'reason': MarketOrderReason,
        # List of Trade ID’s identifying the open trades that will be closed when
        # their respective instruments become tradeable
        'tradeIDs': TradeID}


class LimitOrderRejectTransaction:
    """A LimitOrderRejectTransaction represents the rejection of
    the creation of a Limit Order.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “LIMIT_ORDER_REJECT” in a
        # LimitOrderRejectTransaction.
        'type': (TransactionType, default('LIMIT_ORDER_REJECT')),
        # The Limit Order’s Instrument.
        'instrument': (InstrumentName, required),
        # The quantity requested to be filled by the Limit Order. A posititive
        # number of units results in a long Order, and a negative number of units
        # results in a short Order.
        'units': (DecimalNumber, required),
        # The price threshold specified for the Limit Order. The Limit Order will
        # only be filled by a market price that is equal to or better than this
        # price.
        'price': (PriceValue, required),
        # The time-in-force requested for the Limit Order.
        'timeInForce': (TimeInForce, required, default('GTC')),
        # The date/time when the Limit Order will be cancelled if its timeInForce
        # is “GTD”.
        'gtdTime': DateTime,
        # Specification of how Positions in the Account are modified when the Order
        # is filled.
        'positionFill': (OrderPositionFill, required, default('DEFAULT')),
        # Specification of which price component should be used when determining if
        # an Order should be triggered and filled. This allows Orders to be
        # triggered based on the bid, ask, mid, default (ask for buy, bid for sell)
        # or inverse (ask for sell, bid for buy) price depending on the desired
        # behaviour. Orders are always filled using their default price component.
        # This feature is only provided through the REST API. Clients who choose to
        # specify a non-default trigger condition will not see it reflected in any
        # of OANDA’s proprietary or partner trading platforms, their transaction
        # history or their account statements. OANDA platforms always assume that
        # an Order’s trigger condition is set to the default value when indicating
        # the distance from an Order’s trigger price, and will always provide the
        # default trigger condition when creating or modifying an Order.
        'triggerCondition': (OrderTriggerCondition, required, default('DEFAULT')),
        # The reason that the Limit Order was initiated
        'reason': LimitOrderReason,
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        'clientExtensions': ClientExtensions,
        # The specification of the Take Profit Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'takeProfitOnFill': TakeProfitDetails,
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'stopLossOnFill': StopLossDetails,
        # The specification of the Trailing Stop Loss Order that should be created
        # for a Trade that is opened when the Order is filled (if such a Trade is
        # created).
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions,
        # The ID of the Order that this Order was intended to replace (only
        # provided if this Order was intended to replace an existing Order).
        'intendedReplacesOrderID': OrderID,
        # The reason that the Reject Transaction was created
        'rejectReason': TransactionRejectReason}


class LimitOrderTransaction:
    """A LimitOrderTransaction represents the creation of
    a Limit Order in the user’s Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “LIMIT_ORDER” in a
        # LimitOrderTransaction.
        'type': (TransactionType, default('LIMIT_ORDER')),
        # The Limit Order’s Instrument.
        'instrument': (InstrumentName, required),
        # The quantity requested to be filled by the Limit Order. A posititive
        # number of units results in a long Order, and a negative number of units
        # results in a short Order.
        'units': (DecimalNumber, required),
        # The price threshold specified for the Limit Order. The Limit Order will
        # only be filled by a market price that is equal to or better than this
        # price.
        'price': (PriceValue, required),
        # The time-in-force requested for the Limit Order.
        'timeInForce': (TimeInForce, required, default('GTC')),
        # The date/time when the Limit Order will be cancelled if its timeInForce
        # is “GTD”.
        'gtdTime': DateTime,
        # Specification of how Positions in the Account are modified when the Order
        # is filled.
        'positionFill': (OrderPositionFill, required, default('DEFAULT')),
        # Specification of which price component should be used when determining if
        # an Order should be triggered and filled. This allows Orders to be
        # triggered based on the bid, ask, mid, default (ask for buy, bid for sell)
        # or inverse (ask for sell, bid for buy) price depending on the desired
        # behaviour. Orders are always filled using their default price component.
        # This feature is only provided through the REST API. Clients who choose to
        # specify a non-default trigger condition will not see it reflected in any
        # of OANDA’s proprietary or partner trading platforms, their transaction
        # history or their account statements. OANDA platforms always assume that
        # an Order’s trigger condition is set to the default value when indicating
        # the distance from an Order’s trigger price, and will always provide the
        # default trigger condition when creating or modifying an Order.
        'triggerCondition': (OrderTriggerCondition, required, default('DEFAULT')),
        # The reason that the Limit Order was initiated
        'reason': LimitOrderReason,
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        'clientExtensions': ClientExtensions,
        # The specification of the Take Profit Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'takeProfitOnFill': TakeProfitDetails,
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'stopLossOnFill': StopLossDetails,
        # The specification of the Trailing Stop Loss Order that should be created
        # for a Trade that is opened when the Order is filled (if such a Trade is
        # created).
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions,
        # The ID of the Order that this Order replaces (only provided if this Order
        # replaces an existing Order).
        'replacesOrderID': OrderID,
        # The ID of the Transaction that cancels the replaced Order (only provided
        # if this Order replaces an existing Order).
        'cancellingTransactionID': TransactionID}


class LiquidityRegenerationSchedule:
    """A LiquidityRegenerationSchedule indicates how liquidity that is used when filling an Order for an instrument is regenerated following the fill. A liquidity regeneration schedule will be in effect until
    the timestamp of its final step, but may be replaced by a schedule created for an Order of the same instrument that is filled while it is still in effect.
    """
    # JSON representation of object
    schema = {
        # The steps in the Liquidity Regeneration Schedule
        'steps': (Array[LiquidityRegenerationScheduleStep])}


class LiquidityRegenerationScheduleStep:
    """A liquidity regeneration schedule Step indicates the amount of bid and ask liquidity that is used by
    the Account at a certain time. These amounts will only change at the timestamp of the following step.
    """
    # JSON representation of object
    schema = {
        # The timestamp of the schedule step.
        'timestamp': DateTime,
        # The amount of bid liquidity used at this step in the schedule.
        'bidLiquidityUsed': DecimalNumber,
        # The amount of ask liquidity used at this step in the schedule.
        'askLiquidityUsed': DecimalNumber}


class MarginCallEnterTransaction:
    """A MarginCallEnterTransaction is created when an
    Account enters the margin call state.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “MARGIN_CALL_ENTER” for an
        # MarginCallEnterTransaction.
        'type': (TransactionType, default('MARGIN_CALL_ENTER'))}


class MarginCallExitTransaction:
    """A MarginCallExitnterTransaction is created when an
    Account leaves the margin call state.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “MARGIN_CALL_EXIT” for an
        # MarginCallExitTransaction.
        'type': (TransactionType, default('MARGIN_CALL_EXIT'))}


class MarginCallExtendTransaction:
    """A MarginCallExtendTransaction is created when the margin
    call state for an Account has been extended.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “MARGIN_CALL_EXTEND” for an
        # MarginCallExtendTransaction.
        'type': (TransactionType, default('MARGIN_CALL_EXTEND')),
        # The number of the extensions to the Account’s current margin call that
        # have been applied. This value will be set to 1 for the first
        # MarginCallExtend Transaction
        'extensionNumber': integer}


class MarketIfTouchedOrderRejectTransaction:
    """A MarketIfTouchedOrderRejectTransaction represents the rejection of
    the creation of a MarketIfTouched Order.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to
        # “MARKET_IF_TOUCHED_ORDER_REJECT” in a
        # MarketIfTouchedOrderRejectTransaction.
        'type': (TransactionType, default('MARKET_IF_TOUCHED_ORDER_REJECT')),
        # The MarketIfTouched Order’s Instrument.
        'instrument': (InstrumentName, required),
        # The quantity requested to be filled by the MarketIfTouched Order. A
        # posititive number of units results in a long Order, and a negative number
        # of units results in a short Order.
        'units': (DecimalNumber, required),
        # The price threshold specified for the MarketIfTouched Order. The
        # MarketIfTouched Order will only be filled by a market price that crosses
        # this price from the direction of the market price at the time when the
        # Order was created (the initialMarketPrice). Depending on the value of the
        # Order’s price and initialMarketPrice, the MarketIfTouchedOrder will
        # behave like a Limit or a Stop Order.
        'price': (PriceValue, required),
        # The worst market price that may be used to fill this MarketIfTouched
        # Order.
        'priceBound': PriceValue,
        # The time-in-force requested for the MarketIfTouched Order. Restricted to
        # “GTC”, “GFD” and “GTD” for MarketIfTouched Orders.
        'timeInForce': (TimeInForce, required, default('GTC')),
        # The date/time when the MarketIfTouched Order will be cancelled if its
        # timeInForce is “GTD”.
        'gtdTime': DateTime,
        # Specification of how Positions in the Account are modified when the Order
        # is filled.
        'positionFill': (OrderPositionFill, required, default('DEFAULT')),
        # Specification of which price component should be used when determining if
        # an Order should be triggered and filled. This allows Orders to be
        # triggered based on the bid, ask, mid, default (ask for buy, bid for sell)
        # or inverse (ask for sell, bid for buy) price depending on the desired
        # behaviour. Orders are always filled using their default price component.
        # This feature is only provided through the REST API. Clients who choose to
        # specify a non-default trigger condition will not see it reflected in any
        # of OANDA’s proprietary or partner trading platforms, their transaction
        # history or their account statements. OANDA platforms always assume that
        # an Order’s trigger condition is set to the default value when indicating
        # the distance from an Order’s trigger price, and will always provide the
        # default trigger condition when creating or modifying an Order.
        'triggerCondition': (OrderTriggerCondition, required, default('DEFAULT')),
        # The reason that the Market-if-touched Order was initiated
        'reason': MarketIfTouchedOrderReason,
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        'clientExtensions': ClientExtensions,
        # The specification of the Take Profit Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'takeProfitOnFill': TakeProfitDetails,
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'stopLossOnFill': StopLossDetails,
        # The specification of the Trailing Stop Loss Order that should be created
        # for a Trade that is opened when the Order is filled (if such a Trade is
        # created).
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions,
        # The ID of the Order that this Order was intended to replace (only
        # provided if this Order was intended to replace an existing Order).
        'intendedReplacesOrderID': OrderID,
        # The reason that the Reject Transaction was created
        'rejectReason': TransactionRejectReason}


class MarketIfTouchedOrderTransaction:
    """A MarketIfTouchedOrderTransaction represents the creation of
    a MarketIfTouched Order in the user’s Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “MARKET_IF_TOUCHED_ORDER” in a
        # MarketIfTouchedOrderTransaction.
        'type': (TransactionType, default('MARKET_IF_TOUCHED_ORDER')),
        # The MarketIfTouched Order’s Instrument.
        'instrument': (InstrumentName, required),
        # The quantity requested to be filled by the MarketIfTouched Order. A
        # posititive number of units results in a long Order, and a negative number
        # of units results in a short Order.
        'units': (DecimalNumber, required),
        # The price threshold specified for the MarketIfTouched Order. The
        # MarketIfTouched Order will only be filled by a market price that crosses
        # this price from the direction of the market price at the time when the
        # Order was created (the initialMarketPrice). Depending on the value of the
        # Order’s price and initialMarketPrice, the MarketIfTouchedOrder will
        # behave like a Limit or a Stop Order.
        'price': (PriceValue, required),
        # The worst market price that may be used to fill this MarketIfTouched
        # Order.
        'priceBound': PriceValue,
        # The time-in-force requested for the MarketIfTouched Order. Restricted to
        # “GTC”, “GFD” and “GTD” for MarketIfTouched Orders.
        'timeInForce': (TimeInForce, required, default('GTC')),
        # The date/time when the MarketIfTouched Order will be cancelled if its
        # timeInForce is “GTD”.
        'gtdTime': DateTime,
        # Specification of how Positions in the Account are modified when the Order
        # is filled.
        'positionFill': (OrderPositionFill, required, default('DEFAULT')),
        # Specification of which price component should be used when determining if
        # an Order should be triggered and filled. This allows Orders to be
        # triggered based on the bid, ask, mid, default (ask for buy, bid for sell)
        # or inverse (ask for sell, bid for buy) price depending on the desired
        # behaviour. Orders are always filled using their default price component.
        # This feature is only provided through the REST API. Clients who choose to
        # specify a non-default trigger condition will not see it reflected in any
        # of OANDA’s proprietary or partner trading platforms, their transaction
        # history or their account statements. OANDA platforms always assume that
        # an Order’s trigger condition is set to the default value when indicating
        # the distance from an Order’s trigger price, and will always provide the
        # default trigger condition when creating or modifying an Order.
        'triggerCondition': (OrderTriggerCondition, required, default('DEFAULT')),
        # The reason that the Market-if-touched Order was initiated
        'reason': MarketIfTouchedOrderReason,
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        'clientExtensions': ClientExtensions,
        # The specification of the Take Profit Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'takeProfitOnFill': TakeProfitDetails,
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'stopLossOnFill': StopLossDetails,
        # The specification of the Trailing Stop Loss Order that should be created
        # for a Trade that is opened when the Order is filled (if such a Trade is
        # created).
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions,
        # The ID of the Order that this Order replaces (only provided if this Order
        # replaces an existing Order).
        'replacesOrderID': OrderID,
        # The ID of the Transaction that cancels the replaced Order (only provided
        # if this Order replaces an existing Order).
        'cancellingTransactionID': TransactionID}


class MarketOrderDelayedTradeClose:
    """Details for the Market Order extensions specific to a Market Order placed with the intent of fully
    closing a specific open trade that should have already been closed but wasn’t due to halted market conditions
    """
    # JSON representation of object
    schema = {
        # The ID of the Trade being closed
        'tradeID': TradeID,
        # The Client ID of the Trade being closed
        'clientTradeID': TradeID,
        # The Transaction ID of the DelayedTradeClosure transaction to which this
        # Delayed Trade Close belongs to
        'sourceTransactionID': TransactionID}


class MarketOrderMarginCloseout:
    """Details for the Market Order extensions specific to a Market Order placed
    that is part of a Market Order Margin Closeout in a client’s account
    """
    # JSON representation of object
    schema = {
        # The reason the Market Order was created to perform a margin closeout
        'reason': MarketOrderMarginCloseoutReason}


class MarketOrderPositionCloseout:
    """A MarketOrderPositionCloseout specifies the extensions to a Market Order
    when it has been created to closeout a specific Position.
    """
    # JSON representation of object
    schema = {
        # The instrument of the Position being closed out.
        'instrument': InstrumentName,
        # Indication of how much of the Position to close. Either “ALL”, or a
        # DecimalNumber reflection a partial close of the Trade. The DecimalNumber
        # must always be positive, and represent a number that doesn’t exceed the
        # absolute size of the Position.
        'units': string}


class MarketOrderRejectTransaction:
    """A MarketOrderRejectTransaction represents the rejection of
    the creation of a Market Order.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “MARKET_ORDER_REJECT” in a
        # MarketOrderRejectTransaction.
        'type': (TransactionType, default('MARKET_ORDER_REJECT')),
        # The Market Order’s Instrument.
        'instrument': (InstrumentName, required),
        # The quantity requested to be filled by the Market Order. A posititive
        # number of units results in a long Order, and a negative number of units
        # results in a short Order.
        'units': (DecimalNumber, required),
        # The time-in-force requested for the Market Order. Restricted to FOK or
        # IOC for a MarketOrder.
        'timeInForce': (TimeInForce, required, default('FOK')),
        # The worst price that the client is willing to have the Market Order
        # filled at.
        'priceBound': PriceValue,
        # Specification of how Positions in the Account are modified when the Order
        # is filled.
        'positionFill': (OrderPositionFill, required, default('DEFAULT')),
        # Details of the Trade requested to be closed, only provided when the
        # Market Order is being used to explicitly close a Trade.
        'tradeClose': MarketOrderTradeClose,
        # Details of the long Position requested to be closed out, only provided
        # when a Market Order is being used to explicitly closeout a long Position.
        'longPositionCloseout': MarketOrderPositionCloseout,
        # Details of the short Position requested to be closed out, only provided
        # when a Market Order is being used to explicitly closeout a short
        # Position.
        'shortPositionCloseout': MarketOrderPositionCloseout,
        # Details of the Margin Closeout that this Market Order was created for
        'marginCloseout': MarketOrderMarginCloseout,
        # Details of the delayed Trade close that this Market Order was created for
        'delayedTradeClose': MarketOrderDelayedTradeClose,
        # The reason that the Market Order was created
        'reason': MarketOrderReason,
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        'clientExtensions': ClientExtensions,
        # The specification of the Take Profit Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'takeProfitOnFill': TakeProfitDetails,
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'stopLossOnFill': StopLossDetails,
        # The specification of the Trailing Stop Loss Order that should be created
        # for a Trade that is opened when the Order is filled (if such a Trade is
        # created).
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions,
        # The reason that the Reject Transaction was created
        'rejectReason': TransactionRejectReason}


class MarketOrderTradeClose:
    """A MarketOrderTradeClose specifies the extensions to a Market Order
    that has been created specifically to close a Trade.
    """
    # JSON representation of object
    schema = {
        # The ID of the Trade requested to be closed
        'tradeID': TradeID,
        # The client ID of the Trade requested to be closed
        'clientTradeID': string,
        # Indication of how much of the Trade to close. Either “ALL”, or a
        # DecimalNumber reflection a partial close of the Trade.
        'units': string}


class MarketOrderTransaction:
    """A MarketOrderTransaction represents the creation of a Market Order in the user’s account. A Market Order is an Order that is filled immediately at the current market price. Market
    Orders can be specialized when they are created to accomplish a specific task: to close a Trade, to closeout a Position or to particiate in in a Margin closeout.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “MARKET_ORDER” in a
        # MarketOrderTransaction.
        'type': (TransactionType, default('MARKET_ORDER')),
        # The Market Order’s Instrument.
        'instrument': (InstrumentName, required),
        # The quantity requested to be filled by the Market Order. A posititive
        # number of units results in a long Order, and a negative number of units
        # results in a short Order.
        'units': (DecimalNumber, required),
        # The time-in-force requested for the Market Order. Restricted to FOK or
        # IOC for a MarketOrder.
        'timeInForce': (TimeInForce, required, default('FOK')),
        # The worst price that the client is willing to have the Market Order
        # filled at.
        'priceBound': PriceValue,
        # Specification of how Positions in the Account are modified when the Order
        # is filled.
        'positionFill': (OrderPositionFill, required, default('DEFAULT')),
        # Details of the Trade requested to be closed, only provided when the
        # Market Order is being used to explicitly close a Trade.
        'tradeClose': MarketOrderTradeClose,
        # Details of the long Position requested to be closed out, only provided
        # when a Market Order is being used to explicitly closeout a long Position.
        'longPositionCloseout': MarketOrderPositionCloseout,
        # Details of the short Position requested to be closed out, only provided
        # when a Market Order is being used to explicitly closeout a short
        # Position.
        'shortPositionCloseout': MarketOrderPositionCloseout,
        # Details of the Margin Closeout that this Market Order was created for
        'marginCloseout': MarketOrderMarginCloseout,
        # Details of the delayed Trade close that this Market Order was created for
        'delayedTradeClose': MarketOrderDelayedTradeClose,
        # The reason that the Market Order was created
        'reason': MarketOrderReason,
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        'clientExtensions': ClientExtensions,
        # The specification of the Take Profit Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'takeProfitOnFill': TakeProfitDetails,
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'stopLossOnFill': StopLossDetails,
        # The specification of the Trailing Stop Loss Order that should be created
        # for a Trade that is opened when the Order is filled (if such a Trade is
        # created).
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions}


class OpenTradeFinancing:
    """OpenTradeFinancing is used to pay/collect daily financing
    charge for an open Trade within an Account
    """
    # JSON representation of object
    schema = {
        # The ID of the Trade that financing is being paid/collected for.
        'tradeID': TradeID,
        # The amount of financing paid/collected for the Trade.
        'financing': AccountUnits}


class OrderCancelRejectTransaction:
    """An OrderCancelRejectTransaction represents the rejection of the
    cancellation of an Order in the client’s Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “ORDER_CANCEL_REJECT” for an
        # OrderCancelRejectTransaction.
        'type': (TransactionType, default('ORDER_CANCEL_REJECT')),
        # The ID of the Order intended to be cancelled
        'orderID': OrderID,
        # The client ID of the Order intended to be cancelled (only provided if the
        # Order has a client Order ID).
        'clientOrderID': OrderID,
        # The reason that the Order was to be cancelled.
        'reason': OrderCancelReason,
        # The reason that the Reject Transaction was created
        'rejectReason': TransactionRejectReason}


class OrderCancelTransaction:
    """An OrderCancelTransaction represents the cancellation of
    an Order in the client’s Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “ORDER_CANCEL” for an
        # OrderCancelTransaction.
        'type': (TransactionType, default('ORDER_CANCEL')),
        # The ID of the Order cancelled
        'orderID': OrderID,
        # The client ID of the Order cancelled (only provided if the Order has a
        # client Order ID).
        'clientOrderID': OrderID,
        # The reason that the Order was cancelled.
        'reason': OrderCancelReason,
        # The ID of the Order that replaced this Order (only provided if this Order
        # was cancelled for replacement).
        'replacedByOrderID': OrderID}


class OrderClientExtensionsModifyRejectTransaction:
    """A OrderClientExtensionsModifyRejectTransaction represents the rejection of
    the modification of an Order’s Client Extensions.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to
        # “ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT” for a
        # OrderClientExtensionsModifyRejectTransaction.
        'type': (TransactionType, default('ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT')),
        # The ID of the Order who’s client extensions are to be modified.
        'orderID': OrderID,
        # The original Client ID of the Order who’s client extensions are to be
        # modified.
        'clientOrderID': ClientID,
        # The new Client Extensions for the Order.
        'clientExtensionsModify': ClientExtensions,
        # The new Client Extensions for the Order’s Trade on fill.
        'tradeClientExtensionsModify': ClientExtensions,
        # The reason that the Reject Transaction was created
        'rejectReason': TransactionRejectReason}


class OrderClientExtensionsModifyTransaction:
    """A OrderClientExtensionsModifyTransaction represents the modification
    of an Order’s Client Extensions.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to
        # “ORDER_CLIENT_EXTENSIONS_MODIFY” for a
        # OrderClienteExtensionsModifyTransaction.
        'type': (TransactionType, default('ORDER_CLIENT_EXTENSIONS_MODIFY')),
        # The ID of the Order who’s client extensions are to be modified.
        'orderID': OrderID,
        # The original Client ID of the Order who’s client extensions are to be
        # modified.
        'clientOrderID': ClientID,
        # The new Client Extensions for the Order.
        'clientExtensionsModify': ClientExtensions,
        # The new Client Extensions for the Order’s Trade on fill.
        'tradeClientExtensionsModify': ClientExtensions}


class OrderFillTransaction:
    """An OrderFillTransaction represents the filling of
    an Order in the client’s Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “ORDER_FILL” for an
        # OrderFillTransaction.
        'type': (TransactionType, default('ORDER_FILL')),
        # The ID of the Order filled.
        'orderID': OrderID,
        # The client Order ID of the Order filled (only provided if the client has
        # assigned one).
        'clientOrderID': ClientID,
        # The name of the filled Order’s instrument.
        'instrument': InstrumentName,
        # The number of units filled by the Order.
        'units': DecimalNumber,
        # The average market price that the Order was filled at.
        'price': PriceValue,
        # The price in effect for the account at the time of the Order fill.
        'fullPrice': ClientPrice,
        # The reason that an Order was filled
        'reason': OrderFillReason,
        # The profit or loss incurred when the Order was filled.
        'pl': AccountUnits,
        # The financing paid or collected when the Order was filled.
        'financing': AccountUnits,
        # The commission charged in the Account’s home currency as a result of
        # filling the Order. The commission is always represented as a positive
        # quantity of the Account’s home currency, however it reduces the balance
        # in the Account.
        'commission': AccountUnits,
        # The Account’s balance after the Order was filled.
        'accountBalance': AccountUnits,
        # The Trade that was opened when the Order was filled (only provided if
        # filling the Order resulted in a new Trade).
        'tradeOpened': TradeOpen,
        # The Trades that were closed when the Order was filled (only provided if
        # filling the Order resulted in a closing open Trades).
        'tradesClosed': (Array[TradeReduce]),
        # The Trade that was reduced when the Order was filled (only provided if
        # filling the Order resulted in reducing an open Trade).
        'tradeReduced': TradeReduce}


class PositionFinancing:
    """OpenTradeFinancing is used to pay/collect daily financing
    charge for a Position within an Account
    """
    # JSON representation of object
    schema = {
        # The instrument of the Position that financing is being paid/collected
        # for.
        'instrument': InstrumentName,
        # The amount of financing paid/collected for the Position.
        'financing': AccountUnits,
        # The financing paid/collecte for each open Trade within the Position.
        'openTradeFinancings': (Array[OpenTradeFinancing])}


class ReopenTransaction:
    """A ReopenTransaction represents the re-opening of a closed Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “REOPEN” in a
        # ReopenTransaction.
        'type': (TransactionType, default('REOPEN'))}


class ResetResettablePLTransaction:
    """A ResetResettablePLTransaction represents the resetting
    of the Account’s resettable PL counters.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “RESET_RESETTABLE_PL” for a
        # ResetResettablePLTransaction.
        'type': (TransactionType, default('RESET_RESETTABLE_PL'))}


class StopLossDetails:
    """StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order
    is filled that opens a Trade requiring a Stop Loss, or when a Trade’s dependent Stop Loss Order is modified directly through the Trade.
    """
    # JSON representation of object
    schema = {
        # The price that the Stop Loss Order will be triggered at.
        'price': PriceValue,
        # The time in force for the created Stop Loss Order. This may only be GTC,
        # GTD or GFD.
        'timeInForce': (TimeInForce, default('GTC')),
        # The date when the Stop Loss Order will be cancelled on if timeInForce is
        # GTD.
        'gtdTime': DateTime,
        # The Client Extensions to add to the Stop Loss Order when created.
        'clientExtensions': ClientExtensions}


class StopLossOrderRejectTransaction:
    """A StopLossOrderRejectTransaction represents the rejection of
    the creation of a StopLoss Order.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “STOP_LOSS_ORDER_REJECT” in a
        # StopLossOrderRejectTransaction.
        'type': (TransactionType, default('STOP_LOSS_ORDER_REJECT')),
        # The ID of the Trade to close when the price threshold is breached.
        'tradeID': (TradeID, required),
        # The client ID of the Trade to be closed when the price threshold is
        # breached.
        'clientTradeID': ClientID,
        # The price threshold specified for the StopLoss Order. The associated
        # Trade will be closed by a market price that is equal to or worse than
        # this threshold.
        'price': (PriceValue, required),
        # The time-in-force requested for the StopLoss Order. Restricted to “GTC”,
        # “GFD” and “GTD” for StopLoss Orders.
        'timeInForce': (TimeInForce, required, default('GTC')),
        # The date/time when the StopLoss Order will be cancelled if its
        # timeInForce is “GTD”.
        'gtdTime': DateTime,
        # Specification of which price component should be used when determining if
        # an Order should be triggered and filled. This allows Orders to be
        # triggered based on the bid, ask, mid, default (ask for buy, bid for sell)
        # or inverse (ask for sell, bid for buy) price depending on the desired
        # behaviour. Orders are always filled using their default price component.
        # This feature is only provided through the REST API. Clients who choose to
        # specify a non-default trigger condition will not see it reflected in any
        # of OANDA’s proprietary or partner trading platforms, their transaction
        # history or their account statements. OANDA platforms always assume that
        # an Order’s trigger condition is set to the default value when indicating
        # the distance from an Order’s trigger price, and will always provide the
        # default trigger condition when creating or modifying an Order.
        'triggerCondition': (OrderTriggerCondition, required, default('DEFAULT')),
        # The reason that the Stop Loss Order was initiated
        'reason': StopLossOrderReason,
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        'clientExtensions': ClientExtensions,
        # The ID of the OrderFill Transaction that caused this Order to be created
        # (only provided if this Order was created automatically when another Order
        # was filled).
        'orderFillTransactionID': TransactionID,
        # The ID of the Order that this Order was intended to replace (only
        # provided if this Order was intended to replace an existing Order).
        'intendedReplacesOrderID': OrderID,
        # The reason that the Reject Transaction was created
        'rejectReason': TransactionRejectReason}


class StopLossOrderTransaction:
    """A StopLossOrderTransaction represents the creation of
    a StopLoss Order in the user’s Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “STOP_LOSS_ORDER” in a
        # StopLossOrderTransaction.
        'type': (TransactionType, default('STOP_LOSS_ORDER')),
        # The ID of the Trade to close when the price threshold is breached.
        'tradeID': (TradeID, required),
        # The client ID of the Trade to be closed when the price threshold is
        # breached.
        'clientTradeID': ClientID,
        # The price threshold specified for the StopLoss Order. The associated
        # Trade will be closed by a market price that is equal to or worse than
        # this threshold.
        'price': (PriceValue, required),
        # The time-in-force requested for the StopLoss Order. Restricted to “GTC”,
        # “GFD” and “GTD” for StopLoss Orders.
        'timeInForce': (TimeInForce, required, default('GTC')),
        # The date/time when the StopLoss Order will be cancelled if its
        # timeInForce is “GTD”.
        'gtdTime': DateTime,
        # Specification of which price component should be used when determining if
        # an Order should be triggered and filled. This allows Orders to be
        # triggered based on the bid, ask, mid, default (ask for buy, bid for sell)
        # or inverse (ask for sell, bid for buy) price depending on the desired
        # behaviour. Orders are always filled using their default price component.
        # This feature is only provided through the REST API. Clients who choose to
        # specify a non-default trigger condition will not see it reflected in any
        # of OANDA’s proprietary or partner trading platforms, their transaction
        # history or their account statements. OANDA platforms always assume that
        # an Order’s trigger condition is set to the default value when indicating
        # the distance from an Order’s trigger price, and will always provide the
        # default trigger condition when creating or modifying an Order.
        'triggerCondition': (OrderTriggerCondition, required, default('DEFAULT')),
        # The reason that the Stop Loss Order was initiated
        'reason': StopLossOrderReason,
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        'clientExtensions': ClientExtensions,
        # The ID of the OrderFill Transaction that caused this Order to be created
        # (only provided if this Order was created automatically when another Order
        # was filled).
        'orderFillTransactionID': TransactionID,
        # The ID of the Order that this Order replaces (only provided if this Order
        # replaces an existing Order).
        'replacesOrderID': OrderID,
        # The ID of the Transaction that cancels the replaced Order (only provided
        # if this Order replaces an existing Order).
        'cancellingTransactionID': TransactionID}


class StopOrderRejectTransaction:
    """A StopOrderRejectTransaction represents the rejection of
    the creation of a Stop Order.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “STOP_ORDER_REJECT” in a
        # StopOrderRejectTransaction.
        'type': (TransactionType, default('STOP_ORDER_REJECT')),
        # The Stop Order’s Instrument.
        'instrument': (InstrumentName, required),
        # The quantity requested to be filled by the Stop Order. A posititive
        # number of units results in a long Order, and a negative number of units
        # results in a short Order.
        'units': (DecimalNumber, required),
        # The price threshold specified for the Stop Order. The Stop Order will
        # only be filled by a market price that is equal to or worse than this
        # price.
        'price': (PriceValue, required),
        # The worst market price that may be used to fill this Stop Order. If the
        # market gaps and crosses through both the price and the priceBound, the
        # Stop Order will be cancelled instead of being filled.
        'priceBound': PriceValue,
        # The time-in-force requested for the Stop Order.
        'timeInForce': (TimeInForce, required, default('GTC')),
        # The date/time when the Stop Order will be cancelled if its timeInForce is
        # “GTD”.
        'gtdTime': DateTime,
        # Specification of how Positions in the Account are modified when the Order
        # is filled.
        'positionFill': (OrderPositionFill, required, default('DEFAULT')),
        # Specification of which price component should be used when determining if
        # an Order should be triggered and filled. This allows Orders to be
        # triggered based on the bid, ask, mid, default (ask for buy, bid for sell)
        # or inverse (ask for sell, bid for buy) price depending on the desired
        # behaviour. Orders are always filled using their default price component.
        # This feature is only provided through the REST API. Clients who choose to
        # specify a non-default trigger condition will not see it reflected in any
        # of OANDA’s proprietary or partner trading platforms, their transaction
        # history or their account statements. OANDA platforms always assume that
        # an Order’s trigger condition is set to the default value when indicating
        # the distance from an Order’s trigger price, and will always provide the
        # default trigger condition when creating or modifying an Order.
        'triggerCondition': (OrderTriggerCondition, required, default('DEFAULT')),
        # The reason that the Stop Order was initiated
        'reason': StopOrderReason,
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        'clientExtensions': ClientExtensions,
        # The specification of the Take Profit Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'takeProfitOnFill': TakeProfitDetails,
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'stopLossOnFill': StopLossDetails,
        # The specification of the Trailing Stop Loss Order that should be created
        # for a Trade that is opened when the Order is filled (if such a Trade is
        # created).
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions,
        # The ID of the Order that this Order was intended to replace (only
        # provided if this Order was intended to replace an existing Order).
        'intendedReplacesOrderID': OrderID,
        # The reason that the Reject Transaction was created
        'rejectReason': TransactionRejectReason}


class StopOrderTransaction:
    """A StopOrderTransaction represents the creation of
    a Stop Order in the user’s Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “STOP_ORDER” in a
        # StopOrderTransaction.
        'type': (TransactionType, default('STOP_ORDER')),
        # The Stop Order’s Instrument.
        'instrument': (InstrumentName, required),
        # The quantity requested to be filled by the Stop Order. A posititive
        # number of units results in a long Order, and a negative number of units
        # results in a short Order.
        'units': (DecimalNumber, required),
        # The price threshold specified for the Stop Order. The Stop Order will
        # only be filled by a market price that is equal to or worse than this
        # price.
        'price': (PriceValue, required),
        # The worst market price that may be used to fill this Stop Order. If the
        # market gaps and crosses through both the price and the priceBound, the
        # Stop Order will be cancelled instead of being filled.
        'priceBound': PriceValue,
        # The time-in-force requested for the Stop Order.
        'timeInForce': (TimeInForce, required, default('GTC')),
        # The date/time when the Stop Order will be cancelled if its timeInForce is
        # “GTD”.
        'gtdTime': DateTime,
        # Specification of how Positions in the Account are modified when the Order
        # is filled.
        'positionFill': (OrderPositionFill, required, default('DEFAULT')),
        # Specification of which price component should be used when determining if
        # an Order should be triggered and filled. This allows Orders to be
        # triggered based on the bid, ask, mid, default (ask for buy, bid for sell)
        # or inverse (ask for sell, bid for buy) price depending on the desired
        # behaviour. Orders are always filled using their default price component.
        # This feature is only provided through the REST API. Clients who choose to
        # specify a non-default trigger condition will not see it reflected in any
        # of OANDA’s proprietary or partner trading platforms, their transaction
        # history or their account statements. OANDA platforms always assume that
        # an Order’s trigger condition is set to the default value when indicating
        # the distance from an Order’s trigger price, and will always provide the
        # default trigger condition when creating or modifying an Order.
        'triggerCondition': (OrderTriggerCondition, required, default('DEFAULT')),
        # The reason that the Stop Order was initiated
        'reason': StopOrderReason,
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        'clientExtensions': ClientExtensions,
        # The specification of the Take Profit Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'takeProfitOnFill': TakeProfitDetails,
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        'stopLossOnFill': StopLossDetails,
        # The specification of the Trailing Stop Loss Order that should be created
        # for a Trade that is opened when the Order is filled (if such a Trade is
        # created).
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions,
        # The ID of the Order that this Order replaces (only provided if this Order
        # replaces an existing Order).
        'replacesOrderID': OrderID,
        # The ID of the Transaction that cancels the replaced Order (only provided
        # if this Order replaces an existing Order).
        'cancellingTransactionID': TransactionID}


class TakeProfitDetails:
    """TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order
    is filled that opens a Trade requiring a Take Profit, or when a Trade’s dependent Take Profit Order is modified directly through the Trade.
    """
    # JSON representation of object
    schema = {
        # The price that the Take Profit Order will be triggered at.
        'price': PriceValue,
        # The time in force for the created Take Profit Order. This may only be
        # GTC, GTD or GFD.
        'timeInForce': (TimeInForce, default('GTC')),
        # The date when the Take Profit Order will be cancelled on if timeInForce
        # is GTD.
        'gtdTime': DateTime,
        # The Client Extensions to add to the Take Profit Order when created.
        'clientExtensions': ClientExtensions}


class TakeProfitOrderRejectTransaction:
    """A TakeProfitOrderRejectTransaction represents the rejection of
    the creation of a TakeProfit Order.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “TAKE_PROFIT_ORDER_REJECT” in
        # a TakeProfitOrderRejectTransaction.
        'type': (TransactionType, default('TAKE_PROFIT_ORDER_REJECT')),
        # The ID of the Trade to close when the price threshold is breached.
        'tradeID': (TradeID, required),
        # The client ID of the Trade to be closed when the price threshold is
        # breached.
        'clientTradeID': ClientID,
        # The price threshold specified for the TakeProfit Order. The associated
        # Trade will be closed by a market price that is equal to or better than
        # this threshold.
        'price': (PriceValue, required),
        # The time-in-force requested for the TakeProfit Order. Restricted to
        # “GTC”, “GFD” and “GTD” for TakeProfit Orders.
        'timeInForce': (TimeInForce, required, default('GTC')),
        # The date/time when the TakeProfit Order will be cancelled if its
        # timeInForce is “GTD”.
        'gtdTime': DateTime,
        # Specification of which price component should be used when determining if
        # an Order should be triggered and filled. This allows Orders to be
        # triggered based on the bid, ask, mid, default (ask for buy, bid for sell)
        # or inverse (ask for sell, bid for buy) price depending on the desired
        # behaviour. Orders are always filled using their default price component.
        # This feature is only provided through the REST API. Clients who choose to
        # specify a non-default trigger condition will not see it reflected in any
        # of OANDA’s proprietary or partner trading platforms, their transaction
        # history or their account statements. OANDA platforms always assume that
        # an Order’s trigger condition is set to the default value when indicating
        # the distance from an Order’s trigger price, and will always provide the
        # default trigger condition when creating or modifying an Order.
        'triggerCondition': (OrderTriggerCondition, required, default('DEFAULT')),
        # The reason that the Take Profit Order was initiated
        'reason': TakeProfitOrderReason,
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        'clientExtensions': ClientExtensions,
        # The ID of the OrderFill Transaction that caused this Order to be created
        # (only provided if this Order was created automatically when another Order
        # was filled).
        'orderFillTransactionID': TransactionID,
        # The ID of the Order that this Order was intended to replace (only
        # provided if this Order was intended to replace an existing Order).
        'intendedReplacesOrderID': OrderID,
        # The reason that the Reject Transaction was created
        'rejectReason': TransactionRejectReason}


class TakeProfitOrderTransaction:
    """A TakeProfitOrderTransaction represents the creation of
    a TakeProfit Order in the user’s Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “TAKE_PROFIT_ORDER” in a
        # TakeProfitOrderTransaction.
        'type': (TransactionType, default('TAKE_PROFIT_ORDER')),
        # The ID of the Trade to close when the price threshold is breached.
        'tradeID': (TradeID, required),
        # The client ID of the Trade to be closed when the price threshold is
        # breached.
        'clientTradeID': ClientID,
        # The price threshold specified for the TakeProfit Order. The associated
        # Trade will be closed by a market price that is equal to or better than
        # this threshold.
        'price': (PriceValue, required),
        # The time-in-force requested for the TakeProfit Order. Restricted to
        # “GTC”, “GFD” and “GTD” for TakeProfit Orders.
        'timeInForce': (TimeInForce, required, default('GTC')),
        # The date/time when the TakeProfit Order will be cancelled if its
        # timeInForce is “GTD”.
        'gtdTime': DateTime,
        # Specification of which price component should be used when determining if
        # an Order should be triggered and filled. This allows Orders to be
        # triggered based on the bid, ask, mid, default (ask for buy, bid for sell)
        # or inverse (ask for sell, bid for buy) price depending on the desired
        # behaviour. Orders are always filled using their default price component.
        # This feature is only provided through the REST API. Clients who choose to
        # specify a non-default trigger condition will not see it reflected in any
        # of OANDA’s proprietary or partner trading platforms, their transaction
        # history or their account statements. OANDA platforms always assume that
        # an Order’s trigger condition is set to the default value when indicating
        # the distance from an Order’s trigger price, and will always provide the
        # default trigger condition when creating or modifying an Order.
        'triggerCondition': (OrderTriggerCondition, required, default('DEFAULT')),
        # The reason that the Take Profit Order was initiated
        'reason': TakeProfitOrderReason,
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        'clientExtensions': ClientExtensions,
        # The ID of the OrderFill Transaction that caused this Order to be created
        # (only provided if this Order was created automatically when another Order
        # was filled).
        'orderFillTransactionID': TransactionID,
        # The ID of the Order that this Order replaces (only provided if this Order
        # replaces an existing Order).
        'replacesOrderID': OrderID,
        # The ID of the Transaction that cancels the replaced Order (only provided
        # if this Order replaces an existing Order).
        'cancellingTransactionID': TransactionID}


class TradeClientExtensionsModifyRejectTransaction:
    """A TradeClientExtensionsModifyRejectTransaction represents the rejection of
    the modification of a Trade’s Client Extensions.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to
        # “TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT” for a
        # TradeClientExtensionsModifyRejectTransaction.
        'type': (TransactionType, default('TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT')),
        # The ID of the Trade who’s client extensions are to be modified.
        'tradeID': TradeID,
        # The original Client ID of the Trade who’s client extensions are to be
        # modified.
        'clientTradeID': ClientID,
        # The new Client Extensions for the Trade.
        'tradeClientExtensionsModify': ClientExtensions,
        # The reason that the Reject Transaction was created
        'rejectReason': TransactionRejectReason}


class TradeClientExtensionsModifyTransaction:
    """A TradeClientExtensionsModifyTransaction represents the modification
    of a Trade’s Client Extensions.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to
        # “TRADE_CLIENT_EXTENSIONS_MODIFY” for a
        # TradeClientExtensionsModifyTransaction.
        'type': (TransactionType, default('TRADE_CLIENT_EXTENSIONS_MODIFY')),
        # The ID of the Trade who’s client extensions are to be modified.
        'tradeID': TradeID,
        # The original Client ID of the Trade who’s client extensions are to be
        # modified.
        'clientTradeID': ClientID,
        # The new Client Extensions for the Trade.
        'tradeClientExtensionsModify': ClientExtensions}


class TradeOpen:
    """A TradeOpen Refactor represents a Trade for an instrument that was opened in an Account. It is
    found embedded in Transactions that affect the position of an instrument in the Account, specifically the OrderFill Transaction.
    """
    # JSON representation of object
    schema = {
        # The ID of the Trade that was opened
        'tradeID': TradeID,
        # The number of units opened by the Trade
        'units': DecimalNumber,
        # The client extensions for the newly opened Trade
        'clientExtensions': ClientExtensions}


class TradeReduce:
    """A TradeReduce Refactor represents a Trade for an instrument that was reduced (either partially or fully) in an Account.
    It is found embedded in Transactions that affect the position of an instrument in the account, specifically the OrderFill Transaction.
    """
    # JSON representation of object
    schema = {
        # The ID of the Trade that was reduced or closed
        'tradeID': TradeID,
        # The number of units that the Trade was reduced by
        'units': DecimalNumber,
        # The PL realized when reducing the Trade
        'realizedPL': AccountUnits,
        # The financing paid/collected when reducing the Trade
        'financing': AccountUnits}


class TrailingStopLossDetails:
    """TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is
    filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade’s dependent Trailing Stop Loss Order is modified directly through the Trade.
    """
    # JSON representation of object
    schema = {
        # The distance (in price units) from the Trade’s fill price that the
        # Trailing Stop Loss Order will be triggered at.
        'distance': PriceValue,
        # The time in force for the created Trailing Stop Loss Order. This may only
        # be GTC, GTD or GFD.
        'timeInForce': (TimeInForce, default('GTC')),
        # The date when the Trailing Stop Loss Order will be cancelled on if
        # timeInForce is GTD.
        'gtdTime': DateTime,
        # The Client Extensions to add to the Trailing Stop Loss Order when
        # created.
        'clientExtensions': ClientExtensions}


class TrailingStopLossOrderRejectTransaction:
    """A TrailingStopLossOrderRejectTransaction represents the rejection of
    the creation of a TrailingStopLoss Order.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to
        # “TRAILING_STOP_LOSS_ORDER_REJECT” in a
        # TrailingStopLossOrderRejectTransaction.
        'type': (TransactionType, default('TRAILING_STOP_LOSS_ORDER_REJECT')),
        # The ID of the Trade to close when the price threshold is breached.
        'tradeID': (TradeID, required),
        # The client ID of the Trade to be closed when the price threshold is
        # breached.
        'clientTradeID': ClientID,
        # The price distance specified for the TrailingStopLoss Order.
        'distance': (PriceValue, required),
        # The time-in-force requested for the TrailingStopLoss Order. Restricted to
        # “GTC”, “GFD” and “GTD” for TrailingStopLoss Orders.
        'timeInForce': (TimeInForce, required, default('GTC')),
        # The date/time when the StopLoss Order will be cancelled if its
        # timeInForce is “GTD”.
        'gtdTime': DateTime,
        # Specification of which price component should be used when determining if
        # an Order should be triggered and filled. This allows Orders to be
        # triggered based on the bid, ask, mid, default (ask for buy, bid for sell)
        # or inverse (ask for sell, bid for buy) price depending on the desired
        # behaviour. Orders are always filled using their default price component.
        # This feature is only provided through the REST API. Clients who choose to
        # specify a non-default trigger condition will not see it reflected in any
        # of OANDA’s proprietary or partner trading platforms, their transaction
        # history or their account statements. OANDA platforms always assume that
        # an Order’s trigger condition is set to the default value when indicating
        # the distance from an Order’s trigger price, and will always provide the
        # default trigger condition when creating or modifying an Order.
        'triggerCondition': (OrderTriggerCondition, required, default('DEFAULT')),
        # The reason that the Trailing Stop Loss Order was initiated
        'reason': TrailingStopLossOrderReason,
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        'clientExtensions': ClientExtensions,
        # The ID of the OrderFill Transaction that caused this Order to be created
        # (only provided if this Order was created automatically when another Order
        # was filled).
        'orderFillTransactionID': TransactionID,
        # The ID of the Order that this Order was intended to replace (only
        # provided if this Order was intended to replace an existing Order).
        'intendedReplacesOrderID': OrderID,
        # The reason that the Reject Transaction was created
        'rejectReason': TransactionRejectReason}


class TrailingStopLossOrderTransaction:
    """A TrailingStopLossOrderTransaction represents the creation of
    a TrailingStopLoss Order in the user’s Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “TRAILING_STOP_LOSS_ORDER” in
        # a TrailingStopLossOrderTransaction.
        'type': (TransactionType, default('TRAILING_STOP_LOSS_ORDER')),
        # The ID of the Trade to close when the price threshold is breached.
        'tradeID': (TradeID, required),
        # The client ID of the Trade to be closed when the price threshold is
        # breached.
        'clientTradeID': ClientID,
        # The price distance specified for the TrailingStopLoss Order.
        'distance': (PriceValue, required),
        # The time-in-force requested for the TrailingStopLoss Order. Restricted to
        # “GTC”, “GFD” and “GTD” for TrailingStopLoss Orders.
        'timeInForce': (TimeInForce, required, default('GTC')),
        # The date/time when the StopLoss Order will be cancelled if its
        # timeInForce is “GTD”.
        'gtdTime': DateTime,
        # Specification of which price component should be used when determining if
        # an Order should be triggered and filled. This allows Orders to be
        # triggered based on the bid, ask, mid, default (ask for buy, bid for sell)
        # or inverse (ask for sell, bid for buy) price depending on the desired
        # behaviour. Orders are always filled using their default price component.
        # This feature is only provided through the REST API. Clients who choose to
        # specify a non-default trigger condition will not see it reflected in any
        # of OANDA’s proprietary or partner trading platforms, their transaction
        # history or their account statements. OANDA platforms always assume that
        # an Order’s trigger condition is set to the default value when indicating
        # the distance from an Order’s trigger price, and will always provide the
        # default trigger condition when creating or modifying an Order.
        'triggerCondition': (OrderTriggerCondition, required, default('DEFAULT')),
        # The reason that the Trailing Stop Loss Order was initiated
        'reason': TrailingStopLossOrderReason,
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        'clientExtensions': ClientExtensions,
        # The ID of the OrderFill Transaction that caused this Order to be created
        # (only provided if this Order was created automatically when another Order
        # was filled).
        'orderFillTransactionID': TransactionID,
        # The ID of the Order that this Order replaces (only provided if this Order
        # replaces an existing Order).
        'replacesOrderID': OrderID,
        # The ID of the Transaction that cancels the replaced Order (only provided
        # if this Order replaces an existing Order).
        'cancellingTransactionID': TransactionID}


class Transaction:
    """The base Transaction specification. Specifies properties
    that are common between all Transaction.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID}


class TransactionHeartbeat:
    """A TransactionHeartbeat Refactor is injected into the Transaction
    stream to ensure that the HTTP connection remains active.
    """
    # JSON representation of object
    schema = {
        # The string “HEARTBEAT”
        'type': (string, default('HEARTBEAT')),
        # The ID of the most recent Transaction created for the Account
        'lastTransactionID': TransactionID,
        # The date/time when the TransactionHeartbeat was created.
        'time': DateTime}


class TransferFundsRejectTransaction:
    """A TransferFundsRejectTransaction represents the rejection of the
    transfer of funds in/out of an Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “TRANSFER_FUNDS_REJECT” in a
        # TransferFundsRejectTransaction.
        'type': (TransactionType, default('TRANSFER_FUNDS_REJECT')),
        # The amount to deposit/withdraw from the Account in the Account’s home
        # currency. A positive value indicates a deposit, a negative value
        # indicates a withdrawal.
        'amount': AccountUnits,
        # The reason that an Account is being funded.
        'fundingReason': FundingReason,
        # An optional comment that may be attached to a fund transfer for audit
        # purposes
        'comment': string,
        # The reason that the Reject Transaction was created
        'rejectReason': TransactionRejectReason}


class TransferFundsTransaction:
    """A TransferFundsTransaction represents the transfer
    of funds in/out of an Account.
    """
    # JSON representation of object
    schema = {
        # The Transaction’s Identifier.
        'id': TransactionID,
        # The date/time when the Transaction was created.
        'time': DateTime,
        # The ID of the user that initiated the creation of the Transaction.
        'userID': integer,
        # The ID of the Account the Transaction was created for.
        'accountID': AccountID,
        # The ID of the “batch” that the Transaction belongs to. Transactions in
        # the same batch are applied to the Account simultaneously.
        'batchID': TransactionID,
        # The Request ID of the request which generated the transaction.
        'requestID': RequestID,
        # The Type of the Transaction. Always set to “TRANSFER_FUNDS” in a
        # TransferFundsTransaction.
        'type': (TransactionType, default('TRANSFER_FUNDS')),
        # The amount to deposit/withdraw from the Account in the Account’s home
        # currency. A positive value indicates a deposit, a negative value
        # indicates a withdrawal.
        'amount': AccountUnits,
        # The reason that an Account is being funded.
        'fundingReason': FundingReason,
        # An optional comment that may be attached to a fund transfer for audit
        # purposes
        'comment': string,
        # The Account’s balance after funds are transferred.
        'accountBalance': AccountUnits}


class VWAPReceipt:
    """A VWAP Receipt provides a record of how the price for an Order fill is constructed. If the Order
    is filled with multiple buckets in a depth of market, each bucket will be represented with a VWAP Receipt.
    """
    # JSON representation of object
    schema = {
        # The number of units filled
        'units': DecimalNumber,
        # The price at which the units were filled
        'price': PriceValue}
