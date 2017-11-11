from .decorators import endpoint
from ..definitions.types import DecimalNumber
from ..endpoints.account import *
from ..endpoints.annotations import *

__all__ = ['AccountInterface']


class AccountInterface(object):
    @endpoint(GETAccounts)
    def list_accounts(self):
        """Get a list of all Accounts authorized for the provided token.

        Args:

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETAccountID)
    def get_account_details(self):
        """
        Get the full details for a single Account that a client has access to.
        Full pending Order, open Trade and open Position representations are
        provided.

        Args:


        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETAccountIDSummary)
    def account_summary(self):
        """
        Get a summary for a single Account that a client has access to.

        Args:


        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETAccountIDInstruments)
    def account_instruments(self, instruments: Instruments = None):
        """
        Get the list of tradeable instruments for the given Account. The list
        of tradeable instruments is dependent on the regulatory division that
        the Account is located in, thus should be the same for all Accounts
        owned by a single user.

        Args:

            instruments:
                List of instruments to query specifically.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(PATCHAccountIDConfiguration)
    def configure_account(self, alias: Alias = None, margin_rate: DecimalNumber = None):
        """
        Set the client-configurable portions of an Account.

        Args:

            alias:
                Client-defined alias (name) for the Account
            margin_rate:
                The string representation of a decimal number.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETAccountIDChanges)
    def account_changes(self, since_transaction_id: LastTransactionID = None):
        """
        Endpoint used to poll an Account for its current state and changes
        since a specified TransactionID.

        Note:
            since_transaction_id is automatically handled by OandaClient

        Args:
            since_transaction_id:
                ID of the Transaction to get Account changes since.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass
