from .decorators import endpoint
from ..endpoints.trade import *


class TradeInterface(object):
    @endpoint(GETTrades)
    def list_trades(self, ids: Ids, state: TradeStateFilter, instrument: InstrumentName, count: Count, beforeID: TradeID):
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
            beforeID:
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
    def get_trades(self, tradeSpecifier: TradeSpecifier):
        """
        Get the details of a specific Trade in an Account

        Args:
            tradeSpecifier:
                Specifier for the Trade

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    # TODO fix the return docstrings
    @endpoint(PUTTradeSpecifierClose)
    def close_trades(self, tradeSpecifier: TradeStateFilter, units: Units):
        """
        Close (partially or fully) a specific open Trade in an Account

        Args:
            tradeSpecifier:
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
    def set_client_extensions_trade(self, tradeSpecifier: TradeSpecifier, clientExtensions: ClientExtensions):
        """
        Update the Client Extensions for a Trade. Do not add, update, or delete
        the Client Extensions if your account is associated with MT4.

        Args:
            tradeSpecifier:
                Specifier for the Trade
            clientExtensions:
                The Client Extensions to update the Trade with. Do not add,
                update, or delete the Client Extensions if your account is
                associated with MT4.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    # TODO Check each methods arguments against the docstring
    @endpoint(PUTTradesSpecifierOrders)
    def set_dependent_orders_trade(self, tradeSpecifier: TradeSpecifier, takeProfit: TakeProfitDetails,
                             stopLoss: StopLossDetails, trailingStopLoss: TrailingStopLossDetails):
        """
        Create, replace and cancel a Trade's dependent Orders (Take Profit,
        Stop Loss and Trailing Stop Loss) through the Trade itself

        Args:
            tradeSpecifier:
                Specifier for the Trade
            takeProfit:
                The specification of the Take Profit to create/modify/cancel.
                If takeProfit is set to null, the Take Profit Order will be
                cancelled if it exists. If takeProfit is not provided, the
                existing Take Profit Order will not be modified. If a sub-
                field of takeProfit is not specified, that field will be set to
                a default value on create, and be inherited by the replacing
                order on modify.
            stopLoss:
                The specification of the Stop Loss to create/modify/cancel. If
                stopLoss is set to null, the Stop Loss Order will be cancelled
                if it exists. If stopLoss is not provided, the existing Stop
                Loss Order will not be modified. If a sub-field of stopLoss is
                not specified, that field will be set to a default value on
                create, and be inherited by the replacing order on modify.
            trailingStopLoss:
                The specification of the Trailing Stop Loss to
                create/modify/cancel. If trailingStopLoss is set to null, the
                Trailing Stop Loss Order will be cancelled if it exists. If
                trailingStopLoss is not provided, the existing Trailing Stop
                Loss Order will not be modified. If a sub-field of
                trailngStopLoss is not specified, that field will be set to a
                default value on create, and be inherited by the replacing
                order on modify.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass
