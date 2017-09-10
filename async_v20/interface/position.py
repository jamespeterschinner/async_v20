from .decorators import endpoint
from ..endpoints.position import *

class PositionInterface(object):

    @endpoint(GETPositions)
    def list(self):
        """
        List all Positions for an Account. The Positions returned are for every
        instrument that has had a position during the lifetime of an the
        Account.

        Args:
            accountID:
                Account Identifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass


    @endpoint(GETOpenPositions)
    def list_open(self):
        """
        List all open Positions for an Account. An open Position is a Position
        in an Account that currently has a Trade opened for it.

        Args:
            accountID:
                Account Identifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass


    @endpoint(GETPositionsInstrument)
    def get(self, instrument):
        """
        Get the details of a single Instrument's Position in an Account. The
        Position may by open or not.

        Args:
            accountID:
                Account Identifier
            instrument:
                Name of the Instrument

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass


    @endpoint(PUTPositionsInstrumentClose)
    def close(self, instrument, longUnits, longClientExtensions, shortUnits, shortClientExtensions):
        """
        Closeout the open Position for a specific instrument in an Account.

        Args:
            accountID:
                Account Identifier
            instrument:
                Name of the Instrument
            longUnits:
                Indication of how much of the long Position to closeout. Either
                the string "ALL", the string "NONE", or a DecimalNumber
                representing how many units of the long position to close using
                a PositionCloseout MarketOrder. The units specified must always
                be positive.
            longClientExtensions:
                The client extensions to add to the MarketOrder used to close
                the long position.
            shortUnits:
                Indication of how much of the short Position to closeout.
                Either the string "ALL", the string "NONE", or a DecimalNumber
                representing how many units of the short position to close
                using a PositionCloseout MarketOrder. The units specified must
                always be positive.
            shortClientExtensions:
                The client extensions to add to the MarketOrder used to close
                the short position.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass
