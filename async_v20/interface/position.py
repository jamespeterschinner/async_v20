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

        Args:


        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETOpenPositions)
    def list_open_positions(self):
        """
        List all open Positions for an Account. An open Position is a Position
        in an Account that currently has a Trade opened for it.

        Args:


        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETPositionsInstrument)
    def get_positions(self, instrument: InstrumentName):
        """
        Get the details of a single Instrument's Position in an Account. The
        Position may by open or not.

        Args:

            instrument:
                Name of the Instrument

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(PUTPositionsInstrumentClose)
    def close_position(self, instrument: InstrumentName, long_units: LongUnits,
                       long_client_extensions: LongClientExtensions,
                       short_units: ShortUnits, short_client_extensions: ShortClientExtensions):
        """
        Closeout the open Position for a specific instrument in an Account.

        Args:

            instrument:
                Name of the Instrument
            long_units:
                Indication of how much of the long Position to closeout. Either
                the string "ALL", the string "NONE", or a DecimalNumber
                representing how many units of the long position to close using
                a PositionCloseout MarketOrder. The units specified must always
                be positive.
            long_client_extensions:
                The client extensions to add to the MarketOrder used to close
                the long position.
            short_units:
                Indication of how much of the short Position to closeout.
                Either the string "ALL", the string "NONE", or a DecimalNumber
                representing how many units of the short position to close
                using a PositionCloseout MarketOrder. The units specified must
                always be positive.
            short_client_extensions:
                The client extensions to add to the MarketOrder used to close
                the short position.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass
