from .decorators import endpoint, add_signature
from ..definitions.types import ClientExtensions
from ..definitions.types import InstrumentName
from ..definitions.types import LimitOrderRequest
from ..definitions.types import MarketIfTouchedOrderRequest
from ..definitions.types import MarketOrderRequest
from ..definitions.types import OrderID
from ..definitions.types import OrderRequest
from ..definitions.types import OrderSpecifier
from ..definitions.types import OrderStateFilter
from ..definitions.types import StopLossOrderReason
from ..definitions.types import StopLossOrderRequest
from ..definitions.types import StopOrderRequest
from ..definitions.types import TakeProfitOrderRequest
from ..definitions.types import TrailingStopLossOrderRequest
from ..endpoints.annotations import Count
from ..endpoints.annotations import Ids
from ..endpoints.annotations import TradeClientExtensions
from ..endpoints.order import *

__all__ = ['OrderInterface']


class OrderInterface(object):
    @endpoint(POSTOrders)
    def create_order(self, order: OrderRequest, **kwargs):
        """
        Create an Order for an Account

        Args:

            order:
                Specification of the Order to create

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETOrders)
    def list_orders(self, ids: Ids, state: OrderStateFilter, instrument: InstrumentName, count: Count,
                    before_id: OrderID):
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
    def get_order(self, order_specifier: OrderSpecifier):
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
    def replace_order(self, order_specifier: OrderSpecifier, order: OrderRequest, **kwargs):
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
    def cancel_order(self, order_specifier: OrderSpecifier):
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
    def set_client_extensions(self, order_specifier: OrderSpecifier, client_extensions: ClientExtensions,
                              trade_client_extensions: TradeClientExtensions):
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

    @add_signature(MarketOrderRequest)
    def market_order(self, *args, **kwargs):
        """
        Shortcut to create a Market Order in an Account
        MarketOrderRequest
        Args:
            kwargs : The arguments to create a MarketOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.create_order(order=MarketOrderRequest(*args, **kwargs))

    @add_signature(LimitOrderRequest)
    def limit_order(self, *args, **kwargs):
        """
        Shortcut to create a Limit Order in an Account

        Args:
            kwargs : The arguments to create a LimitOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.create_order(order=LimitOrderRequest(*args, **kwargs))

    @add_signature(LimitOrderRequest)
    def limit_replace_order(self, order_id, *args, **kwargs):
        """
        Shortcut to replace a pending Limit Order in an Account

        Args:
            order_id : The ID of the Limit Order to replace
            kwargs : The arguments to create a LimitOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.replace_order(order_id, order=LimitOrderRequest(*args, **kwargs))

    @add_signature(StopOrderRequest)
    def stop_order(self, *args, **kwargs):
        """
        Shortcut to create a Stop Order in an Account

        Args:
            kwargs : The arguments to create a StopOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.create_order(order=StopOrderRequest(*args, **kwargs))

    @add_signature(StopOrderRequest)
    def stop_replace_order(self, order_id, *args, **kwargs):
        """
        Shortcut to replace a pending Stop Order in an Account

        Args:
            order_id : The ID of the Stop Order to replace
            kwargs : The arguments to create a StopOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.replace_order(order_id, order=StopOrderRequest(*args, **kwargs))

    @add_signature(MarketIfTouchedOrderRequest)
    def market_if_touched_order(self, *args, **kwargs):
        """
        Shortcut to create a MarketIfTouched Order in an Account

        Args:
            kwargs : The arguments to create a MarketIfTouchedOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.create_order(order=MarketIfTouchedOrderRequest(*args, **kwargs))

    @add_signature(MarketIfTouchedOrderRequest)
    def market_if_touched_replace_order(self, order_id, *args, **kwargs):
        """
        Shortcut to replace a pending MarketIfTouched Order in an Account

        Args:
            order_id : The ID of the MarketIfTouched Order to replace
            kwargs : The arguments to create a MarketIfTouchedOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.replace_order(order_id, order=MarketIfTouchedOrderRequest(*args, **kwargs))

    @add_signature(TakeProfitOrderRequest)
    def take_profit_order(self, *args, **kwargs):
        """
        Shortcut to create a Take Profit Order in an Account

        Args:
            kwargs : The arguments to create a TakeProfitOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.create_order(order=TakeProfitOrderRequest(*args, **kwargs))

    @add_signature(TakeProfitOrderRequest)
    def take_profit_replace_order(self, order_id, *args, **kwargs):
        """
        Shortcut to replace a pending Take Profit Order in an Account

        Args:
            order_id : The ID of the Take Profit Order to replace
            kwargs : The arguments to create a TakeProfitOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.replace_order(order_id, order=TakeProfitOrderRequest(*args, **kwargs))

    @add_signature(StopOrderRequest)
    def stop_loss_order(self, *args, **kwargs):
        """
        Shortcut to create a Stop Loss Order in an Account

        Args:
            kwargs : The arguments to create a StopLossOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.create_order(order=StopLossOrderRequest(*args, **kwargs))

    @add_signature(StopLossOrderReason)
    def stop_loss_replace_order(self, order_id, *args, **kwargs):
        """
        Shortcut to replace a pending Stop Loss Order in an Account

        Args:
            order_id : The ID of the Stop Loss Order to replace
            kwargs : The arguments to create a StopLossOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.replace_order(order_id, order=StopLossOrderRequest(*args, **kwargs))

    @add_signature(TrailingStopLossOrderRequest)
    def trailing_stop_loss_order(self, *args, **kwargs):
        """
        Shortcut to create a Trailing Stop Loss Order in an Account

        Args:
            kwargs : The arguments to create a TrailingStopLossOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.create_order(order=TrailingStopLossOrderRequest(*args, **kwargs))

    @add_signature(TrailingStopLossOrderRequest)
    def trailing_stop_loss_replace_order(self, order_id, *args, **kwargs):
        """
        Shortcut to replace a pending Trailing Stop Loss Order in an Account

        Args:
            order_id : The ID of the Take Profit Order to replace
            kwargs : The arguments to create a TrailingStopLossOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        return self.replace_order(order_id, order=TrailingStopLossOrderRequest(*args, **kwargs))
