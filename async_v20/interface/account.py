from .decorators import endpoint
from ..definitions.types import DecimalNumber
from ..endpoints.account import *
from ..endpoints.annotations import Alias
from ..endpoints.annotations import Instruments
from ..endpoints.annotations import SinceTransactionID

__all__ = ['AccountInterface']


class AccountInterface(object):
    @endpoint(GETAccounts, initialization_step=1)
    def list_accounts(self):
        """Get a list of all Accounts authorized for the provided token.
        """
        pass

    @endpoint(GETAccountID, initialization_step=2)
    def get_account_details(self):
        """
        Get the full details for a single Account that a client has access to.
        Full pending Order, open Trade and open Position representations are
        provided.
        """
        pass

    @endpoint(GETAccountIDSummary)
    def account_summary(self):
        """
        Get a summary for a single Account that a client has access to.
        """
        pass

    @endpoint(GETAccountIDInstruments)
    def account_instruments(self, instruments: Instruments = ...):
        """
        Get the list of tradeable instruments for the given Account. The list
        of tradeable instruments is dependent on the regulatory division that
        the Account is located in, thus should be the same for all Accounts
        owned by a single user.

        Args:

            instruments: :class:`~async_v20.endpoints.annotations.Instruments`
                List of instruments to query specifically.
        """
        pass

    @endpoint(PATCHAccountIDConfiguration)
    def configure_account(self, alias: Alias = ..., margin_rate: DecimalNumber = ...):
        """
        Set the client-configurable portions of an Account.

        Args:

            alias: :class:`~async_v20.endpoints.annotations.Alias`
                Client-defined alias (name) for the Account
            margin_rate: :class:`~async_v20.definitions.primitives.DecimalNumber`
                The string representation of a decimal number.
        """
        pass

    @endpoint(GETAccountIDChanges)
    def account_changes(self, since_transaction_id: SinceTransactionID = ...):
        """
        Endpoint used to poll an Account for its current state and changes
        since a specified TransactionID.

        Note:
            OandaClient will supply since_transaction_id if None is provided

        Args:
            since_transaction_id: :class:`~async_v20.endpoints.annotations.SinceTransactionID`
                ID of the Transaction to get Account changes since.
        """
        pass
