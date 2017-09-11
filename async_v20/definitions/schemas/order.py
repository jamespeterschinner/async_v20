from ..types import *
from ...endpoints.metaclass import Array

default = lambda x: x
required = True
boolean = bool
integer = int
string = str


class DynamicOrderState:
    """The dynamic state of an Order. This is only relevant
    to TrailingStopLoss Orders, as no other Order type has dynamic state.
    """
    # JSON representation of object
    schema = {
        # The Order’s ID.
        'id': OrderID,
        # The Order’s calculated trailing stop value.
        'trailingStopValue': PriceValue,
        # The distance between the Trailing Stop Loss Order’s trailingStopValue and
        # the current Market Price. This represents the distance (in price units)
        # of the Order from a triggering price. If the distance could not be
        # determined, this value will not be set.
        'triggerDistance': PriceValue,
        # True if an exact trigger distance could be calculated. If false, it means
        # the provided trigger distance is a best estimate. If the distance could
        # not be determined, this value will not be set.
        'isTriggerDistanceExact': boolean}


class LimitOrder:
    """A LimitOrder is an order that is created with a price threshold, and will
    only be filled by a price that is equal to or better than the threshold.
    """
    # JSON representation of object
    schema = {
        # The Order’s identifier, unique within the Order’s Account.
        'id': OrderID,
        # The time when the Order was created.
        'createTime': DateTime,
        # The current state of the Order.
        'state': OrderState,
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions,
        # The type of the Order. Always set to “LIMIT” for Limit Orders.
        'type': (OrderType, default('LIMIT')),
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
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is filled
        # that opens a Trade requiring a Take Profit, or when a Trade’s dependent
        # Take Profit Order is modified directly through the Trade.
        'takeProfitOnFill': TakeProfitDetails,
        # StopLossDetails specifies the details of a Stop Loss Order to be created
        # on behalf of a client. This may happen when an Order is filled that opens
        # a Trade requiring a Stop Loss, or when a Trade’s dependent Stop Loss
        # Order is modified directly through the Trade.
        'stopLossOnFill': StopLossDetails,
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an Order
        # is filled that opens a Trade requiring a Trailing Stop Loss, or when a
        # Trade’s dependent Trailing Stop Loss Order is modified directly through
        # the Trade.
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions,
        # ID of the Transaction that filled this Order (only provided when the
        # Order’s state is FILLED)
        'fillingTransactionID': TransactionID,
        # Date/time when the Order was filled (only provided when the Order’s state
        # is FILLED)
        'filledTime': DateTime,
        # Trade ID of Trade opened when the Order was filled (only provided when
        # the Order’s state is FILLED and a Trade was opened as a result of the
        # fill)
        'tradeOpenedID': TradeID,
        # Trade ID of Trade reduced when the Order was filled (only provided when
        # the Order’s state is FILLED and a Trade was reduced as a result of the
        # fill)
        'tradeReducedID': TradeID,
        # Trade IDs of Trades closed when the Order was filled (only provided when
        # the Order’s state is FILLED and one or more Trades were closed as a
        # result of the fill)
        'tradeClosedIDs': (Array[TradeID]),
        # ID of the Transaction that cancelled the Order (only provided when the
        # Order’s state is CANCELLED)
        'cancellingTransactionID': TransactionID,
        # Date/time when the Order was cancelled (only provided when the state of
        # the Order is CANCELLED)
        'cancelledTime': DateTime,
        # The ID of the Order that was replaced by this Order (only provided if
        # this Order was created as part of a cancel/replace).
        'replacesOrderID': OrderID,
        # The ID of the Order that replaced this Order (only provided if this Order
        # was cancelled as part of a cancel/replace).
        'replacedByOrderID': OrderID}


class LimitOrderRequest:
    """A LimitOrderRequest specifies the parameters that may
    be set when creating a Limit Order.
    """
    # JSON representation of object
    schema = {
        # The type of the Order to Create. Must be set to “LIMIT” when creating a
        # Market Order.
        'type': (OrderType, default('LIMIT')),
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
        # The client extensions to add to the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions,
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is filled
        # that opens a Trade requiring a Take Profit, or when a Trade’s dependent
        # Take Profit Order is modified directly through the Trade.
        'takeProfitOnFill': TakeProfitDetails,
        # StopLossDetails specifies the details of a Stop Loss Order to be created
        # on behalf of a client. This may happen when an Order is filled that opens
        # a Trade requiring a Stop Loss, or when a Trade’s dependent Stop Loss
        # Order is modified directly through the Trade.
        'stopLossOnFill': StopLossDetails,
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an Order
        # is filled that opens a Trade requiring a Trailing Stop Loss, or when a
        # Trade’s dependent Trailing Stop Loss Order is modified directly through
        # the Trade.
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions}


class MarketIfTouchedOrder:
    """A MarketIfTouchedOrder is an order that is created with a price threshold, and will
    only be filled by a market price that is touches or crosses the threshold.
    """
    # JSON representation of object
    schema = {
        # The Order’s identifier, unique within the Order’s Account.
        'id': OrderID,
        # The time when the Order was created.
        'createTime': DateTime,
        # The current state of the Order.
        'state': OrderState,
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions,
        # The type of the Order. Always set to “MARKET_IF_TOUCHED” for Market If
        # Touched Orders.
        'type': (OrderType, default('MARKET_IF_TOUCHED')),
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
        # The Market price at the time when the MarketIfTouched Order was created.
        'initialMarketPrice': PriceValue,
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is filled
        # that opens a Trade requiring a Take Profit, or when a Trade’s dependent
        # Take Profit Order is modified directly through the Trade.
        'takeProfitOnFill': TakeProfitDetails,
        # StopLossDetails specifies the details of a Stop Loss Order to be created
        # on behalf of a client. This may happen when an Order is filled that opens
        # a Trade requiring a Stop Loss, or when a Trade’s dependent Stop Loss
        # Order is modified directly through the Trade.
        'stopLossOnFill': StopLossDetails,
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an Order
        # is filled that opens a Trade requiring a Trailing Stop Loss, or when a
        # Trade’s dependent Trailing Stop Loss Order is modified directly through
        # the Trade.
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions,
        # ID of the Transaction that filled this Order (only provided when the
        # Order’s state is FILLED)
        'fillingTransactionID': TransactionID,
        # Date/time when the Order was filled (only provided when the Order’s state
        # is FILLED)
        'filledTime': DateTime,
        # Trade ID of Trade opened when the Order was filled (only provided when
        # the Order’s state is FILLED and a Trade was opened as a result of the
        # fill)
        'tradeOpenedID': TradeID,
        # Trade ID of Trade reduced when the Order was filled (only provided when
        # the Order’s state is FILLED and a Trade was reduced as a result of the
        # fill)
        'tradeReducedID': TradeID,
        # Trade IDs of Trades closed when the Order was filled (only provided when
        # the Order’s state is FILLED and one or more Trades were closed as a
        # result of the fill)
        'tradeClosedIDs': (Array[TradeID]),
        # ID of the Transaction that cancelled the Order (only provided when the
        # Order’s state is CANCELLED)
        'cancellingTransactionID': TransactionID,
        # Date/time when the Order was cancelled (only provided when the state of
        # the Order is CANCELLED)
        'cancelledTime': DateTime,
        # The ID of the Order that was replaced by this Order (only provided if
        # this Order was created as part of a cancel/replace).
        'replacesOrderID': OrderID,
        # The ID of the Order that replaced this Order (only provided if this Order
        # was cancelled as part of a cancel/replace).
        'replacedByOrderID': OrderID}


class MarketIfTouchedOrderRequest:
    """A MarketIfTouchedOrderRequest specifies the parameters that may
    be set when creating a Market-if-Touched Order.
    """
    # JSON representation of object
    schema = {
        # The type of the Order to Create. Must be set to “MARKET_IF_TOUCHED” when
        # creating a Market If Touched Order.
        'type': (OrderType, default('MARKET_IF_TOUCHED')),
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
        # The client extensions to add to the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions,
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is filled
        # that opens a Trade requiring a Take Profit, or when a Trade’s dependent
        # Take Profit Order is modified directly through the Trade.
        'takeProfitOnFill': TakeProfitDetails,
        # StopLossDetails specifies the details of a Stop Loss Order to be created
        # on behalf of a client. This may happen when an Order is filled that opens
        # a Trade requiring a Stop Loss, or when a Trade’s dependent Stop Loss
        # Order is modified directly through the Trade.
        'stopLossOnFill': StopLossDetails,
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an Order
        # is filled that opens a Trade requiring a Trailing Stop Loss, or when a
        # Trade’s dependent Trailing Stop Loss Order is modified directly through
        # the Trade.
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions}


class MarketOrder:
    """A MarketOrder is an order that is filled
    immediately upon creation using the current market price.
    """
    # JSON representation of object
    schema = {
        # The Order’s identifier, unique within the Order’s Account.
        'id': OrderID,
        # The time when the Order was created.
        'createTime': DateTime,
        # The current state of the Order.
        'state': OrderState,
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions,
        # The type of the Order. Always set to “MARKET” for Market Orders.
        'type': (OrderType, default('MARKET')),
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
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is filled
        # that opens a Trade requiring a Take Profit, or when a Trade’s dependent
        # Take Profit Order is modified directly through the Trade.
        'takeProfitOnFill': TakeProfitDetails,
        # StopLossDetails specifies the details of a Stop Loss Order to be created
        # on behalf of a client. This may happen when an Order is filled that opens
        # a Trade requiring a Stop Loss, or when a Trade’s dependent Stop Loss
        # Order is modified directly through the Trade.
        'stopLossOnFill': StopLossDetails,
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an Order
        # is filled that opens a Trade requiring a Trailing Stop Loss, or when a
        # Trade’s dependent Trailing Stop Loss Order is modified directly through
        # the Trade.
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions,
        # ID of the Transaction that filled this Order (only provided when the
        # Order’s state is FILLED)
        'fillingTransactionID': TransactionID,
        # Date/time when the Order was filled (only provided when the Order’s state
        # is FILLED)
        'filledTime': DateTime,
        # Trade ID of Trade opened when the Order was filled (only provided when
        # the Order’s state is FILLED and a Trade was opened as a result of the
        # fill)
        'tradeOpenedID': TradeID,
        # Trade ID of Trade reduced when the Order was filled (only provided when
        # the Order’s state is FILLED and a Trade was reduced as a result of the
        # fill)
        'tradeReducedID': TradeID,
        # Trade IDs of Trades closed when the Order was filled (only provided when
        # the Order’s state is FILLED and one or more Trades were closed as a
        # result of the fill)
        'tradeClosedIDs': (Array[TradeID]),
        # ID of the Transaction that cancelled the Order (only provided when the
        # Order’s state is CANCELLED)
        'cancellingTransactionID': TransactionID,
        # Date/time when the Order was cancelled (only provided when the state of
        # the Order is CANCELLED)
        'cancelledTime': DateTime}


class MarketOrderRequest:
    """A MarketOrderRequest specifies the parameters that may
    be set when creating a Market Order.
    """
    # JSON representation of object
    schema = {
        # The type of the Order to Create. Must be set to “MARKET” when creating a
        # Market Order.
        'type': (OrderType, default('MARKET')),
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
        # The client extensions to add to the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions,
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is filled
        # that opens a Trade requiring a Take Profit, or when a Trade’s dependent
        # Take Profit Order is modified directly through the Trade.
        'takeProfitOnFill': TakeProfitDetails,
        # StopLossDetails specifies the details of a Stop Loss Order to be created
        # on behalf of a client. This may happen when an Order is filled that opens
        # a Trade requiring a Stop Loss, or when a Trade’s dependent Stop Loss
        # Order is modified directly through the Trade.
        'stopLossOnFill': StopLossDetails,
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an Order
        # is filled that opens a Trade requiring a Trailing Stop Loss, or when a
        # Trade’s dependent Trailing Stop Loss Order is modified directly through
        # the Trade.
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions}


class Order:
    """The base Order definition specifies the
    properties that are common to all Orders.
    """
    # JSON representation of object
    schema = {
        # The Order’s identifier, unique within the Order’s Account.
        'id': OrderID,
        # The time when the Order was created.
        'createTime': DateTime,
        # The current state of the Order.
        'state': OrderState,
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions}


class OrderIdentifier:
    """An OrderIdentifier is used to refer to an
    Order, and contains both the OrderID and the ClientOrderID.
    """
    # JSON representation of object
    schema = {
        # The OANDA-assigned Order ID
        'orderID': OrderID,
        # The client-provided client Order ID
        'clientOrderID': ClientID}


class StopLossOrder:
    """A StopLossOrder is an order that is linked to an open
    Trade and created with a price threshold. The Order will be filled (closing
    the Trade) by the first price that is equal to or worse than the threshold.
    A StopLossOrder cannot be used to open a new Position.
    """
    # JSON representation of object
    schema = {
        # The Order’s identifier, unique within the Order’s Account.
        'id': OrderID,
        # The time when the Order was created.
        'createTime': DateTime,
        # The current state of the Order.
        'state': OrderState,
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions,
        # The type of the Order. Always set to “STOP_LOSS” for Stop Loss Orders.
        'type': (OrderType, default('STOP_LOSS')),
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
        # ID of the Transaction that filled this Order (only provided when the
        # Order’s state is FILLED)
        'fillingTransactionID': TransactionID,
        # Date/time when the Order was filled (only provided when the Order’s state
        # is FILLED)
        'filledTime': DateTime,
        # Trade ID of Trade opened when the Order was filled (only provided when
        # the Order’s state is FILLED and a Trade was opened as a result of the
        # fill)
        'tradeOpenedID': TradeID,
        # Trade ID of Trade reduced when the Order was filled (only provided when
        # the Order’s state is FILLED and a Trade was reduced as a result of the
        # fill)
        'tradeReducedID': TradeID,
        # Trade IDs of Trades closed when the Order was filled (only provided when
        # the Order’s state is FILLED and one or more Trades were closed as a
        # result of the fill)
        'tradeClosedIDs': (Array[TradeID]),
        # ID of the Transaction that cancelled the Order (only provided when the
        # Order’s state is CANCELLED)
        'cancellingTransactionID': TransactionID,
        # Date/time when the Order was cancelled (only provided when the state of
        # the Order is CANCELLED)
        'cancelledTime': DateTime,
        # The ID of the Order that was replaced by this Order (only provided if
        # this Order was created as part of a cancel/replace).
        'replacesOrderID': OrderID,
        # The ID of the Order that replaced this Order (only provided if this Order
        # was cancelled as part of a cancel/replace).
        'replacedByOrderID': OrderID}


class StopLossOrderRequest:
    """A StopLossOrderRequest specifies the parameters that may
    be set when creating a Stop Loss Order.
    """
    # JSON representation of object
    schema = {
        # The type of the Order to Create. Must be set to “STOP_LOSS” when creating
        # a Stop Loss Order.
        'type': (OrderType, default('STOP_LOSS')),
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
        # The client extensions to add to the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions}


class StopOrder:
    """A StopOrder is an order that is created with a price threshold, and will
    only be filled by a price that is equal to or worse than the threshold.
    """
    # JSON representation of object
    schema = {
        # The Order’s identifier, unique within the Order’s Account.
        'id': OrderID,
        # The time when the Order was created.
        'createTime': DateTime,
        # The current state of the Order.
        'state': OrderState,
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions,
        # The type of the Order. Always set to “STOP” for Stop Orders.
        'type': (OrderType, default('STOP')),
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
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is filled
        # that opens a Trade requiring a Take Profit, or when a Trade’s dependent
        # Take Profit Order is modified directly through the Trade.
        'takeProfitOnFill': TakeProfitDetails,
        # StopLossDetails specifies the details of a Stop Loss Order to be created
        # on behalf of a client. This may happen when an Order is filled that opens
        # a Trade requiring a Stop Loss, or when a Trade’s dependent Stop Loss
        # Order is modified directly through the Trade.
        'stopLossOnFill': StopLossDetails,
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an Order
        # is filled that opens a Trade requiring a Trailing Stop Loss, or when a
        # Trade’s dependent Trailing Stop Loss Order is modified directly through
        # the Trade.
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions,
        # ID of the Transaction that filled this Order (only provided when the
        # Order’s state is FILLED)
        'fillingTransactionID': TransactionID,
        # Date/time when the Order was filled (only provided when the Order’s state
        # is FILLED)
        'filledTime': DateTime,
        # Trade ID of Trade opened when the Order was filled (only provided when
        # the Order’s state is FILLED and a Trade was opened as a result of the
        # fill)
        'tradeOpenedID': TradeID,
        # Trade ID of Trade reduced when the Order was filled (only provided when
        # the Order’s state is FILLED and a Trade was reduced as a result of the
        # fill)
        'tradeReducedID': TradeID,
        # Trade IDs of Trades closed when the Order was filled (only provided when
        # the Order’s state is FILLED and one or more Trades were closed as a
        # result of the fill)
        'tradeClosedIDs': (Array[TradeID]),
        # ID of the Transaction that cancelled the Order (only provided when the
        # Order’s state is CANCELLED)
        'cancellingTransactionID': TransactionID,
        # Date/time when the Order was cancelled (only provided when the state of
        # the Order is CANCELLED)
        'cancelledTime': DateTime,
        # The ID of the Order that was replaced by this Order (only provided if
        # this Order was created as part of a cancel/replace).
        'replacesOrderID': OrderID,
        # The ID of the Order that replaced this Order (only provided if this Order
        # was cancelled as part of a cancel/replace).
        'replacedByOrderID': OrderID}


class StopOrderRequest:
    """A StopOrderRequest specifies the parameters that may
    be set when creating a Stop Order.
    """
    # JSON representation of object
    schema = {
        # The type of the Order to Create. Must be set to “STOP” when creating a
        # Stop Order.
        'type': (OrderType, default('STOP')),
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
        # The client extensions to add to the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions,
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is filled
        # that opens a Trade requiring a Take Profit, or when a Trade’s dependent
        # Take Profit Order is modified directly through the Trade.
        'takeProfitOnFill': TakeProfitDetails,
        # StopLossDetails specifies the details of a Stop Loss Order to be created
        # on behalf of a client. This may happen when an Order is filled that opens
        # a Trade requiring a Stop Loss, or when a Trade’s dependent Stop Loss
        # Order is modified directly through the Trade.
        'stopLossOnFill': StopLossDetails,
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an Order
        # is filled that opens a Trade requiring a Trailing Stop Loss, or when a
        # Trade’s dependent Trailing Stop Loss Order is modified directly through
        # the Trade.
        'trailingStopLossOnFill': TrailingStopLossDetails,
        # Client Extensions to add to the Trade created when the Order is filled
        # (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        'tradeClientExtensions': ClientExtensions}


class TakeProfitOrder:
    """A TakeProfitOrder is an order that is linked to an open Trade and
    created with a price threshold. The Order will be filled (closing
    the Trade) by the first price that is equal to or better than the threshold.
    A TakeProfitOrder cannot be used to open a new Position.
    """
    # JSON representation of object
    schema = {
        # The Order’s identifier, unique within the Order’s Account.
        'id': OrderID,
        # The time when the Order was created.
        'createTime': DateTime,
        # The current state of the Order.
        'state': OrderState,
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions,
        # The type of the Order. Always set to “TAKE_PROFIT” for Take Profit
        # Orders.
        'type': (OrderType, default('TAKE_PROFIT')),
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
        # ID of the Transaction that filled this Order (only provided when the
        # Order’s state is FILLED)
        'fillingTransactionID': TransactionID,
        # Date/time when the Order was filled (only provided when the Order’s state
        # is FILLED)
        'filledTime': DateTime,
        # Trade ID of Trade opened when the Order was filled (only provided when
        # the Order’s state is FILLED and a Trade was opened as a result of the
        # fill)
        'tradeOpenedID': TradeID,
        # Trade ID of Trade reduced when the Order was filled (only provided when
        # the Order’s state is FILLED and a Trade was reduced as a result of the
        # fill)
        'tradeReducedID': TradeID,
        # Trade IDs of Trades closed when the Order was filled (only provided when
        # the Order’s state is FILLED and one or more Trades were closed as a
        # result of the fill)
        'tradeClosedIDs': (Array[TradeID]),
        # ID of the Transaction that cancelled the Order (only provided when the
        # Order’s state is CANCELLED)
        'cancellingTransactionID': TransactionID,
        # Date/time when the Order was cancelled (only provided when the state of
        # the Order is CANCELLED)
        'cancelledTime': DateTime,
        # The ID of the Order that was replaced by this Order (only provided if
        # this Order was created as part of a cancel/replace).
        'replacesOrderID': OrderID,
        # The ID of the Order that replaced this Order (only provided if this Order
        # was cancelled as part of a cancel/replace).
        'replacedByOrderID': OrderID}


class TakeProfitOrderRequest:
    """A TakeProfitOrderRequest specifies the parameters that may
    be set when creating a Take Profit Order.
    """
    # JSON representation of object
    schema = {
        # The type of the Order to Create. Must be set to “TAKE_PROFIT” when
        # creating a Take Profit Order.
        'type': (OrderType, default('TAKE_PROFIT')),
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
        # The client extensions to add to the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions}


class TrailingStopLossOrder:
    """A TrailingStopLossOrder is an order that is linked to an open Trade and created with a price distance.
    The price distance is used to calculate a trailing stop value for the order that is in the losing direction
    from the market price at the time of the order’s creation.
    The trailing stop value will follow the market price as it moves in the winning direction,
    and the order will filled (closing the Trade) by the first price that is equal to or worse than the
    trailing stop value. A TrailingStopLossOrder cannot be used to open a new Position.
    """
    # JSON representation of object
    schema = {
        # The Order’s identifier, unique within the Order’s Account.
        'id': OrderID,
        # The time when the Order was created.
        'createTime': DateTime,
        # The current state of the Order.
        'state': OrderState,
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions,
        # The type of the Order. Always set to “TRAILING_STOP_LOSS” for Trailing
        # Stop Loss Orders.
        'type': (OrderType, default('TRAILING_STOP_LOSS')),
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
        # The trigger price for the Trailing Stop Loss Order. The trailing stop
        # value will trail follow the market price by the TSL order’s configured
        # “distance” as the market price moves in the winning direction. If the
        # market price moves to a level that is equal to or worse than the trailing
        # stop value, the order will be filled and the Trade will be closed.
        'trailingStopValue': PriceValue,
        # ID of the Transaction that filled this Order (only provided when the
        # Order’s state is FILLED)
        'fillingTransactionID': TransactionID,
        # Date/time when the Order was filled (only provided when the Order’s state
        # is FILLED)
        'filledTime': DateTime,
        # Trade ID of Trade opened when the Order was filled (only provided when
        # the Order’s state is FILLED and a Trade was opened as a result of the
        # fill)
        'tradeOpenedID': TradeID,
        # Trade ID of Trade reduced when the Order was filled (only provided when
        # the Order’s state is FILLED and a Trade was reduced as a result of the
        # fill)
        'tradeReducedID': TradeID,
        # Trade IDs of Trades closed when the Order was filled (only provided when
        # the Order’s state is FILLED and one or more Trades were closed as a
        # result of the fill)
        'tradeClosedIDs': (Array[TradeID]),
        # ID of the Transaction that cancelled the Order (only provided when the
        # Order’s state is CANCELLED)
        'cancellingTransactionID': TransactionID,
        # Date/time when the Order was cancelled (only provided when the state of
        # the Order is CANCELLED)
        'cancelledTime': DateTime,
        # The ID of the Order that was replaced by this Order (only provided if
        # this Order was created as part of a cancel/replace).
        'replacesOrderID': OrderID,
        # The ID of the Order that replaced this Order (only provided if this Order
        # was cancelled as part of a cancel/replace).
        'replacedByOrderID': OrderID}


class TrailingStopLossOrderRequest:
    """A TrailingStopLossOrderRequest specifies the parameters that may be
    set when creating a Trailing Stop Loss Order.
    """
    # JSON representation of object
    schema = {
        # The type of the Order to Create. Must be set to “TRAILING_STOP_LOSS” when
        # creating a Trailng Stop Loss Order.
        'type': (OrderType, default('TRAILING_STOP_LOSS')),
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
        # The client extensions to add to the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        'clientExtensions': ClientExtensions}


class UnitsAvailable:
    """Representation of how many units of an Instrument are available
    to be traded by an Order depending on its postionFill option.
    """
    # JSON representation of object
    schema = {
        # The number of units that are available to be traded using an Order with a
        # positionFill option of “DEFAULT”. For an Account with hedging enabled,
        # this value will be the same as the “OPEN_ONLY” value. For an Account
        # without hedging enabled, this value will be the same as the
        # “REDUCE_FIRST” value.
        'default': UnitsAvailableDetails,
        # The number of units that may are available to be traded with an Order
        # with a positionFill option of “REDUCE_FIRST”.
        'reduceFirst': UnitsAvailableDetails,
        # The number of units that may are available to be traded with an Order
        # with a positionFill option of “REDUCE_ONLY”.
        'reduceOnly': UnitsAvailableDetails,
        # The number of units that may are available to be traded with an Order
        # with a positionFill option of “OPEN_ONLY”.
        'openOnly': UnitsAvailableDetails}


class UnitsAvailableDetails:
    """Representation of many units of an Instrument are available
    to be traded for both long and short Orders.
    """
    # JSON representation of object
    schema = {
        # The units available for long Orders.
        'long': DecimalNumber,
        # The units available for short Orders.
        'short': DecimalNumber}
