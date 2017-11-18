from .decorators import endpoint
from ..definitions.types import InstrumentName
from ..endpoints.annotations import LongClientExtensions
from ..endpoints.annotations import LongUnits
from ..endpoints.annotations import ShortClientExtensions
from ..endpoints.annotations import ShortUnits
from ..endpoints.position import *

__all__ = ['PositionInterface']


class PositionInterface(object):
    @endpoint(GETPositions)
    def list_positions(self):
        """
        List all Positions for an Account. The Positions returned are for every
        instrument that has had a position during the lifetime of an the
        Account.

        Returns:
            **status [200]**
            :class:`~async_v20.interface.response.Response`
            (positions= :class:`~async_v20.definitions.types.ArrayPosition`,
            lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

        """
        pass

    @endpoint(GETOpenPositions)
    def list_open_positions(self):
        """
        List all open Positions for an Account. An open Position is a Position
        in an Account that currently has a Trade opened for it.

        Returns:
            **status [200]**
            :class:`~async_v20.interface.response.Response`
            (positions= :class:`~async_v20.definitions.types.ArrayPosition`,
            lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

        """
        pass

    @endpoint(GETPositionsInstrument)
    def get_positions(self, instrument: InstrumentName = ...):
        """
        Get the details of a single Instrument's Position in an Account. The
        Position may by open or not.

        Args:

            instrument: :class:`~async_v20.definitions.primitives.InstrumentName`
                Name of the Instrument

        Returns:
            **status [200]**
            :class:`~async_v20.interface.response.Response`
            (position= :class:`~async_v20.definitions.types.Position`,
            lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

        """
        pass

    @endpoint(PUTPositionsInstrumentClose)
    def close_position(self,
                       instrument: InstrumentName = ...,
                   long_units: LongUnits = ...,
                   long_client_extensions: LongClientExtensions = ...,
                       short_units: ShortUnits = ...,
                       short_client_extensions: ShortClientExtensions = ...):
        """
        Closeout the open Position for a specific instrument in an Account.

        Args:

            instrument: :class:`~async_v20.definitions.primitives.InstrumentName`
                Name of the Instrument
            long_units: :class:`~async_v20.endpoints.annotations.LongUnits`
                Indication of how much of the long Position to closeout. Either
                the string "ALL", the string "NONE", or a DecimalNumber
                representing how many units of the long position to close using
                a PositionCloseout MarketOrder. The units specified must always
                be positive.
            long_client_extensions: :class:`~async_v20.endpoints.annotations.LongClientExtensions`
                The client extensions to add to the MarketOrder used to close
                the long position.
            short_units: :class:`~async_v20.endpoints.annotations.ShortUnits`
                Indication of how much of the short Position to closeout.
                Either the string "ALL", the string "NONE", or a DecimalNumber
                representing how many units of the short position to close
                using a PositionCloseout MarketOrder. The units specified must
                always be positive.
            short_client_extensions: :class:`~async_v20.endpoints.annotations.ShortClientExtensions`
                The client extensions to add to the MarketOrder used to close
                the short position.

        Returns:
            **status [200]**
            :class:`~async_v20.interface.response.Response`
            (longOrderCreateTransaction= :class:`~async_v20.definitions.types.MarketOrderTransaction`,
            longOrderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
            longOrderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
            shortOrderCreateTransaction= :class:`~async_v20.definitions.types.MarketOrderTransaction`,
            shortOrderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
            shortOrderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
            relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
            lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            **status [400]**
            :class:`~async_v20.interface.response.Response`
            (longOrderRejectTransaction= :class:`~async_v20.definitions.types.MarketOrderRejectTransaction`,
            shortOrderRejectTransaction= :class:`~async_v20.definitions.types.MarketOrderRejectTransaction`,
            relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
            lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
            errorCode= :class:`~builtins.str`,
            errorMessage= :class:`~builtins.str`)

            **status [401]**
            :class:`~async_v20.interface.response.Response`
            (longOrderRejectTransaction= :class:`~async_v20.definitions.types.MarketOrderRejectTransaction`,
            shortOrderRejectTransaction= :class:`~async_v20.definitions.types.MarketOrderRejectTransaction`,
            relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
            lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
            errorCode= :class:`~builtins.str`,
            errorMessage= :class:`~builtins.str`)
        """
        pass
