from .decorators import endpoint, shortcut
from ..definitions.types import ClientExtensions
from ..definitions.types import ClientID
from ..definitions.types import DateTime
from ..definitions.types import InstrumentName
from ..definitions.types import LimitOrderRequest
from ..definitions.types import MarketIfTouchedOrderRequest
from ..definitions.types import MarketOrderRequest
from ..definitions.types import OrderID
from ..definitions.types import OrderPositionFill
from ..definitions.types import OrderRequest
from ..definitions.types import OrderSpecifier
from ..definitions.types import OrderStateFilter
from ..definitions.types import OrderTriggerCondition
from ..definitions.types import OrderType
from ..definitions.types import PriceValue
from ..definitions.types import StopLossDetails
from ..definitions.types import StopLossOrderRequest
from ..definitions.types import StopOrderRequest
from ..definitions.types import TakeProfitDetails
from ..definitions.types import TakeProfitOrderRequest
from ..definitions.types import TimeInForce
from ..definitions.types import TradeID
from ..definitions.types import TrailingStopLossDetails
from ..definitions.types import TrailingStopLossOrderRequest
from ..definitions.types import Unit
from ..endpoints.annotations import Count
from ..endpoints.annotations import Ids
from ..endpoints.annotations import TradeClientExtensions
from ..endpoints.order import *

__all__ = ['OrderInterface']


class OrderInterface(object):
    @endpoint(POSTOrders)
    def post_order(self, order_request: OrderRequest = ...):
        """
        Post an OrderRequest to an account

        Args:

            order_request:
                An OrderRequest or a class derived from OrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @shortcut
    def create_order(self, instrument: InstrumentName, units: Unit, type: OrderType = 'MARKET',
                     trade_id: TradeID = ..., price: PriceValue = ..., client_trade_id: ClientID = ...,
                     time_in_force: TimeInForce = ..., gtd_time: DateTime = ...,
                     trigger_condition: OrderTriggerCondition = ..., client_extensions: ClientExtensions = ...,
                     distance: PriceValue = ..., price_bound: PriceValue = ...,
                     position_fill: OrderPositionFill = ..., take_profit_on_fill: TakeProfitDetails = ...,
                     stop_loss_on_fill: StopLossDetails = ...,
                     trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                     trade_client_extensions: ClientExtensions = ...):
        """
        Shortcut to create an OrderRequest in an Account

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request

        """
        return self.post_order(
            order_request=OrderRequest(instrument=instrument, units=units, type=type, trade_id=trade_id, price=price,
                                       client_trade_id=client_trade_id, time_in_force=time_in_force, gtd_time=gtd_time,
                                       trigger_condition=trigger_condition, client_extensions=client_extensions,
                                       distance=distance, price_bound=price_bound, position_fill=position_fill,
                                       take_profit_on_fill=take_profit_on_fill, stop_loss_on_fill=stop_loss_on_fill,
                                       trailing_stop_loss_on_fill=trailing_stop_loss_on_fill,
                                       trade_client_extensions=trade_client_extensions))

    @endpoint(GETOrders)
    def list_orders(self,
                    ids: Ids = ...,
                    state: OrderStateFilter = ...,
                    instrument: InstrumentName = ...,
                    count: Count = ...,
                    before_id: OrderID = ...):
        """
        Get a list of Orders for an Account

        Args:

            ids:
                List of Order IDs to retrieve
            state:
                The state to filter the requested Orders by
            instrument:
                The instrument to filter the requested orders by
            count:
                The maximum number of Orders to return
            before_id:
                The maximum Order ID to return. If not provided the most recent
                Orders in the Account are returned

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETPendingOrders)
    def list_pending_orders(self):
        """
        List all pending Orders in an Account

        Args:


        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETOrderSpecifier)
    def get_order(self, order_specifier: OrderSpecifier = ...):
        """
        Get details for a single Order in an Account

        Args:

            order_specifier:
                The Order Specifier

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(PUTOrderSpecifier)
    def replace_order(self,
                      order_specifier: OrderSpecifier = ...,
                      order_request: OrderRequest = ...):
        """
        Replace an Order in an Account by simultaneously cancelling it and
        creating a replacement Order

        Args:

            order_specifier:
                The Order Specifier
            order:
                Specification of the replacing Order

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(PUTOrderSpecifierCancel)
    def cancel_order(self, order_specifier: OrderSpecifier = ...):
        """
        Cancel a pending Order in an Account

        Args:

            order_specifier:
                The Order Specifier

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(PUTClientExtensions)
    def set_client_extensions(self,
                              order_specifier: OrderSpecifier = ...,
                              client_extensions: ClientExtensions = ...,
                              trade_client_extensions: TradeClientExtensions = ...):
        """
        Update the Client Extensions for an Order in an Account. Do not set,
        modify, or delete clientExtensions if your account is associated with
        MT4.

        Args:

            order_specifier:
                The Order Specifier
            client_extensions:
                The Client Extensions to update for the Order. Do not set,
                modify, or delete clientExtensions if your account is
                associated with MT4.
            trade_client_extensions:
                The Client Extensions to update for the Trade created when the
                Order is filled. Do not set, modify, or delete clientExtensions
                if your account is associated with MT4.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @shortcut
    def market_order(self, instrument: InstrumentName, units: Unit,
                     time_in_force: TimeInForce = 'FOK', price_bound: PriceValue = ...,
                     position_fill: OrderPositionFill = 'DEFAULT', client_extensions: ClientExtensions = ...,
                     take_profit_on_fill: TakeProfitDetails = ..., stop_loss_on_fill: StopLossDetails = ...,
                     trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                     trade_client_extensions: ClientExtensions = ...):
        """
        Shortcut to create a Market Order in an Account
        MarketOrderRequest
        Args:
            kwargs : The arguments to create a MarketOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.post_order(
            order_request=MarketOrderRequest(instrument=instrument, units=units, time_in_force=time_in_force,
                                             price_bound=price_bound, position_fill=position_fill,
                                             client_extensions=client_extensions,
                                             take_profit_on_fill=take_profit_on_fill,
                                             stop_loss_on_fill=stop_loss_on_fill,
                                             trailing_stop_loss_on_fill=trailing_stop_loss_on_fill,
                                             trade_client_extensions=trade_client_extensions
                                             ))
    @shortcut
    def limit_order(self, instrument: InstrumentName, units: Unit, price: PriceValue,
                    time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                    position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                    client_extensions: ClientExtensions = ..., take_profit_on_fill: TakeProfitDetails = ...,
                    stop_loss_on_fill: StopLossDetails = ...,
                    trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                    trade_client_extensions: ClientExtensions = ...):
        """
        Shortcut to create a Limit Order in an Account

        Args:
            kwargs : The arguments to create a LimitOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.post_order(order_request=LimitOrderRequest(instrument=instrument, units=units, price=price,
                                                               time_in_force=time_in_force, gtd_time=gtd_time,
                                                               position_fill=position_fill,
                                                               trigger_condition=trigger_condition,
                                                               client_extensions=client_extensions,
                                                               take_profit_on_fill=take_profit_on_fill,
                                                               stop_loss_on_fill=stop_loss_on_fill,
                                                               trailing_stop_loss_on_fill=trailing_stop_loss_on_fill,
                                                               trade_client_extensions=trade_client_extensions
                                                               ))

    @endpoint(PUTOrderSpecifier)
    def limit_replace_order(self,
                            order_specifier: OrderSpecifier,
                            order: LimitOrderRequest):
        """
        Shortcut to replace a pending Limit Order in an Account

        Args:
            order_specifier : The ID of the Limit Order to replace
            kwargs : The arguments to create a LimitOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        pass

    @shortcut
    def stop_order(self, trade_id: TradeID, price: PriceValue,
                   client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                   trigger_condition: OrderTriggerCondition = 'DEFAULT', client_extensions: ClientExtensions = ...):
        """
        Shortcut to create a Stop Order in an Account

        Args:
            kwargs : The arguments to create a StopOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.post_order(
            order_request=StopLossOrderRequest(trade_id=trade_id, price=price, client_trade_id=client_trade_id,
                                               time_in_force=time_in_force, gtd_time=gtd_time,
                                               trigger_condition=trigger_condition, client_extensions=client_extensions
                                               ))

    @endpoint(PUTOrderSpecifier)
    def stop_replace_order(self,
                           order_specifier: OrderSpecifier,
                           order: StopOrderRequest):
        """
        Shortcut to replace a pending Stop Order in an Account

        Args:
            order_specifier : The ID of the Stop Order to replace
            kwargs : The arguments to create a StopOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        pass

    @shortcut
    def market_if_touched_order(self, instrument: InstrumentName, units: Unit, price: PriceValue,
                                price_bound: PriceValue = ...,
                                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                                position_fill: OrderPositionFill = 'DEFAULT',
                                trigger_condition: OrderTriggerCondition = 'DEFAULT',
                                client_extensions: ClientExtensions = ...,
                                take_profit_on_fill: TakeProfitDetails = ...,
                                stop_loss_on_fill: StopLossDetails = ...,
                                trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                                trade_client_extensions: ClientExtensions = ...):
        """
        Shortcut to create a MarketIfTouched Order in an Account

        Args:
            kwargs : The arguments to create a MarketIfTouchedOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.post_order(
            order_request=MarketIfTouchedOrderRequest(instrument=instrument, units=units, price=price,
                                                      price_bound=price_bound, time_in_force=time_in_force,
                                                      gtd_time=gtd_time, position_fill=position_fill,
                                                      trigger_condition=trigger_condition,
                                                      client_extensions=client_extensions,
                                                      take_profit_on_fill=take_profit_on_fill,
                                                      stop_loss_on_fill=stop_loss_on_fill,
                                                      trailing_stop_loss_on_fill=trailing_stop_loss_on_fill,
                                                      trade_client_extensions=trade_client_extensions
                                                      ))

    @endpoint(PUTOrderSpecifier)
    def market_if_touched_replace_order(self,
                                        order_specifier: OrderSpecifier,
                                        order: MarketIfTouchedOrderRequest):
        """
        Shortcut to replace a pending MarketIfTouched Order in an Account

        Args:
            order_specifier : The ID of the MarketIfTouched Order to replace
            kwargs : The arguments to create a MarketIfTouchedOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        pass

    @shortcut
    def take_profit_order(self, trade_id: TradeID, price: PriceValue,
                          client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC',
                          gtd_time: DateTime = ...,
                          trigger_condition: OrderTriggerCondition = 'DEFAULT',
                          client_extensions: ClientExtensions = ...):
        """
        Shortcut to create a Take Profit Order in an Account

        Args:
            kwargs : The arguments to create a TakeProfitOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.post_order(
            order_request=TakeProfitOrderRequest(trade_id=trade_id, price=price, client_trade_id=client_trade_id,
                                                 time_in_force=time_in_force, gtd_time=gtd_time,
                                                 trigger_condition=trigger_condition,
                                                 client_extensions=client_extensions
                                                 ))

    @endpoint(PUTOrderSpecifier)
    def take_profit_replace_order(self,
                                  order_specifier: OrderSpecifier,
                                  order: TakeProfitOrderRequest):
        """
        Shortcut to replace a pending Take Profit Order in an Account

        Args:
            order_specifier : The ID of the Take Profit Order to replace
            kwargs : The arguments to create a TakeProfitOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        pass

    @shortcut
    def stop_loss_order(self, trade_id: TradeID, price: PriceValue,
                        client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime = ...,
                        trigger_condition: OrderTriggerCondition = 'DEFAULT',
                        client_extensions: ClientExtensions = ...):
        """
        Shortcut to create a Stop Loss Order in an Account

        Args:
            kwargs : The arguments to create a StopLossOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.post_order(
            order_request=StopLossOrderRequest(trade_id=trade_id, price=price, client_trade_id=client_trade_id,
                                               time_in_force=time_in_force, gtd_time=gtd_time,
                                               trigger_condition=trigger_condition, client_extensions=client_extensions
                                               ))

    @endpoint(PUTOrderSpecifier)
    def stop_loss_replace_order(self, order_specifier: OrderSpecifier,
                                order: StopLossOrderRequest):
        """
        Shortcut to replace a pending Stop Loss Order in an Account

        Args:
            order_specifier : The ID of the Stop Loss Order to replace
            kwargs : The arguments to create a StopLossOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        pass

    @shortcut
    def trailing_stop_loss_order(self, trade_id: TradeID, distance: PriceValue,
                                 client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC',
                                 gtd_time: DateTime = ...,
                                 trigger_condition: OrderTriggerCondition = 'DEFAULT',
                                 client_extensions: ClientExtensions = ...):
        """
        Shortcut to create a Trailing Stop Loss Order in an Account

        Args:
            kwargs : The arguments to create a TrailingStopLossOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.post_order(order_request=TrailingStopLossOrderRequest(trade_id=trade_id, distance=distance,
                                                                          client_trade_id=client_trade_id,
                                                                          time_in_force=time_in_force,
                                                                          gtd_time=gtd_time,
                                                                          trigger_condition=trigger_condition,
                                                                          client_extensions=client_extensions
                                                                          ))

    @endpoint(PUTOrderSpecifier)
    def trailing_stop_loss_replace_order(self, order_specifier: OrderSpecifier,
                                         order: TrailingStopLossOrderRequest):
        """
        Shortcut to replace a pending Trailing Stop Loss Order in an Account

        Args:
            order_specifier : The ID of the Take Profit Order to replace
            kwargs : The arguments to create a TrailingStopLossOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        pass
