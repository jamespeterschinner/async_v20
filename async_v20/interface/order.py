from .decorators import endpoint
from ..definitions.types import ClientExtensions
from ..definitions.types import InstrumentName
from ..definitions.types import LimitOrderRequest
from ..definitions.types import MarketIfTouchedOrderRequest
from ..definitions.types import MarketOrderRequest
from ..definitions.types import OrderID
from ..definitions.types import OrderRequest
from ..definitions.types import OrderSpecifier
from ..definitions.types import OrderStateFilter
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
    def create_order(self, order_request: OrderRequest = None):
        """
        Create an Order for an Account

        Args:

            order_request:
                Specification of the Order to create

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETOrders)
    def list_orders(self,
                    ids: Ids = None,
                    state: OrderStateFilter = None,
                    instrument: InstrumentName = None,
                    count: Count = None,
                    before_id: OrderID = None):
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
    def get_order(self, order_specifier: OrderSpecifier = None):
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
                      order_specifier: OrderSpecifier = None,
                      order: OrderRequest = None):
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
    def cancel_order(self, order_specifier: OrderSpecifier = None):
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
                              order_specifier: OrderSpecifier = None,
                              client_extensions: ClientExtensions = None,
                              trade_client_extensions: TradeClientExtensions = None):
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

    @endpoint(POSTOrders)
    def market_order(self, order: MarketOrderRequest):
        """
        Shortcut to create a Market Order in an Account
        MarketOrderRequest
        Args:
            kwargs : The arguments to create a MarketOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        pass

    @endpoint(POSTOrders)
    def limit_order(self, order: LimitOrderRequest):
        """
        Shortcut to create a Limit Order in an Account

        Args:
            kwargs : The arguments to create a LimitOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        pass

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

    @endpoint(POSTOrders)
    def stop_order(self, order: StopOrderRequest):
        """
        Shortcut to create a Stop Order in an Account

        Args:
            kwargs : The arguments to create a StopOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        pass

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

    @endpoint(POSTOrders)
    def market_if_touched_order(self, order: MarketIfTouchedOrderRequest):
        """
        Shortcut to create a MarketIfTouched Order in an Account

        Args:
            kwargs : The arguments to create a MarketIfTouchedOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        pass

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

    @endpoint(POSTOrders)
    def take_profit_order(self, order: TakeProfitOrderRequest):
        """
        Shortcut to create a Take Profit Order in an Account

        Args:
            kwargs : The arguments to create a TakeProfitOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        pass

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

    @endpoint(POSTOrders)
    def stop_loss_order(self, order: StopLossOrderRequest):
        """
        Shortcut to create a Stop Loss Order in an Account

        Args:
            kwargs : The arguments to create a StopLossOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        pass

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

    @endpoint(POSTOrders)
    def trailing_stop_loss_order(self, order: TrailingStopLossOrderRequest):
        """
        Shortcut to create a Trailing Stop Loss Order in an Account

        Args:
            kwargs : The arguments to create a TrailingStopLossOrderRequest

        Returns:
            async_v20.interface.parser.Response containing the results from submitting
            the request
        """
        pass

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
