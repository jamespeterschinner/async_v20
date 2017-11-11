from .decorators import endpoint
from ..definitions.types import ClientExtensions
from ..definitions.types import InstrumentName
from ..definitions.types import StopLossDetails
from ..definitions.types import TakeProfitDetails
from ..definitions.types import TradeID
from ..definitions.types import TradeSpecifier
from ..definitions.types import TradeStateFilter
from ..definitions.types import TrailingStopLossDetails
from ..endpoints.annotations import Count
from ..endpoints.annotations import Ids
from ..endpoints.annotations import Units
from ..endpoints.trade import *

__all__ = ['TradeInterface']


class TradeInterface(object):
    @endpoint(GETTrades)
    def list_trades(self,
                    ids: Ids = None,
                    state: TradeStateFilter = None,
                    instrument: InstrumentName = None,
                    count: Count = None,
                    trade_id: TradeID = None):
        """
        Get a list of Trades for an Account

        Args:
            ids:
                List of Trade IDs to retrieve.
            state:
                The state to filter the requested Trades by.
            instrument:
                The instrument to filter the requested Trades by.
            count:
                The maximum number of Trades to return.
            before_id:
                The maximum Trade ID to return. If not provided the most recent
                Trades in the Account are returned.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETOpenTrades)
    def list_open_trades(self):
        """
        Get the list of open Trades for an Account

        Args:

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETTradeSpecifier)
    def get_trades(self, trade_specifier: TradeSpecifier = None):
        """
        Get the details of a specific Trade in an Account

        Args:
            trade_specifier:
                Specifier for the Trade

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(PUTTradeSpecifierClose)
    def close_trades(self,
                     trade_specifier: TradeSpecifier = None,
                     units: Units = None):
        """
        Close (partially or fully) a specific open Trade in an Account

        Args:
            trade_specifier:
                Specifier for the Trade
            units:
                Indication of how much of the Trade to close. Either the string
                "ALL" (indicating that all of the Trade should be closed), or a
                DecimalNumber representing the number of units of the open
                Trade to Close using a TradeClose MarketOrder. The units
                specified must always be positive, and the magnitude of the
                value cannot exceed the magnitude of the Trade's open units.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(PUTTradeSpecifierClientExtensions)
    def set_client_extensions_trade(self,
                                    trade_specifier: TradeSpecifier = None,
                                    client_extensions: ClientExtensions = None):
        """
        Update the Client Extensions for a Trade. Do not add, update, or delete
        the Client Extensions if your account is associated with MT4.

        Args:
            trade_specifier:
                Specifier for the Trade
            client_extensions:
                The Client Extensions to update the Trade with. Do not add,
                update, or delete the Client Extensions if your account is
                associated with MT4.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(PUTTradesSpecifierOrders)
    def set_dependent_orders_trade(self,
                                   trade_specifier: TradeSpecifier = None,
                                   take_profit: TakeProfitDetails = None,
                                   stop_loss: StopLossDetails = None,
                                   trailing_stop_loss: TrailingStopLossDetails = None):
        """
        Create, replace and cancel a Trade's dependent Orders (Take Profit,
        Stop Loss and Trailing Stop Loss) through the Trade itself

        Args:
            trade_specifier:
                Specifier for the Trade
            take_profit:
                The specification of the Take Profit to create/modify/cancel.
                If takeProfit is set to null, the Take Profit Order will be
                cancelled if it exists. If takeProfit is not provided, the
                existing Take Profit Order will not be modified. If a sub-
                field of takeProfit is not specified, that field will be set to
                a default value on create, and be inherited by the replacing
                order on modify.
            stop_loss:
                The specification of the Stop Loss to create/modify/cancel. If
                stopLoss is set to null, the Stop Loss Order will be cancelled
                if it exists. If stopLoss is not provided, the existing Stop
                Loss Order will not be modified. If a sub-field of stopLoss is
                not specified, that field will be set to a default value on
                create, and be inherited by the replacing order on modify.
            trailing_stop_loss:
                The specification of the Trailing Stop Loss to
                create/modify/cancel. If trailingStopLoss is set to null, the
                Trailing Stop Loss Order will be cancelled if it exists. If
                trailingStopLoss is not provided, the existing Trailing Stop
                Loss Order will not be modified. If a sub-field of
                trailingStopLoss is not specified, that field will be set to a
                default value on create, and be inherited by the replacing
                order on modify.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass
