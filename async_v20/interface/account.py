from .decorators import endpoint
from ..definitions.types import DecimalNumber
from ..endpoints.account import *
from ..endpoints.annotations import Alias
from ..endpoints.annotations import Instruments
from ..endpoints.annotations import SinceTransactionID
from ..definitions.helpers import sentinel

__all__ = ['AccountInterface']


class AccountInterface(object):
    @endpoint(GETAccounts, initialize_required=False)
    def list_accounts(self):
        """Get a list of all Accounts authorized for the provided token.

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (accounts=( :class:`~async_v20.AccountProperties`, ...),)

        """
        pass

    @endpoint(GETAccountID, initialize_required=False)
    def get_account_details(self):
        """
        Get the full details for a single Account that a client has access to.
        Full pending Order, open Trade and open Position representations are
        provided.

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (account= :class:`~async_v20.Account`,
                lastTransactionID= :class:`~async_v20.TransactionID`)
        """
        pass

    @endpoint(GETAccountIDSummary)
    def account_summary(self):
        """
        Get a summary for a single Account that a client has access to.

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (account= :class:`~async_v20.AccountSummary`,
                lastTransactionID= :class:`~async_v20.TransactionID`)
        """
        pass

    @endpoint(GETAccountIDInstruments)
    def account_instruments(self, instruments: Instruments = sentinel):
        """
        Get the list of tradeable instruments for the given Account. The list
        of tradeable instruments is dependent on the regulatory division that
        the Account is located in, thus should be the same for all Accounts
        owned by a single user.

        Args:

            instruments: :class:`~async_v20.endpoints.annotations.Instruments`
            list of instruments to query specifically.

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (instruments=( :class:`~async_v20.Instrument`, ...),
                lastTransactionID= :class:`~async_v20.TransactionID`)
        """
        pass

    @endpoint(PATCHAccountIDConfiguration)
    def configure_account(self, alias: Alias = sentinel, margin_rate: DecimalNumber = sentinel):
        """
        Set the client-configurable portions of an Account.

        Args:

            alias: :class:`~async_v20.endpoints.annotations.Alias`
                Client-defined alias (name) for the Account
            margin_rate: :class:`~async_v20.DecimalNumber`
                The string representation of a decimal number.

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (clientConfigureTransaction= :class:`~async_v20.ClientConfigureTransaction`,
                lastTransactionID= :class:`~async_v20.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (clientConfigureRejectTransaction= :class:`~async_v20.ClientConfigureRejectTransaction`,
                lastTransactionID= :class:`~async_v20.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [403]
                :class:`~async_v20.interface.response.Response`
                (clientConfigureRejectTransaction= :class:`~async_v20.ClientConfigureRejectTransaction`,
                lastTransactionID= :class:`~async_v20.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

        """
        pass

    @endpoint(GETAccountIDChanges, rest=True)
    def account_changes(self, since_transaction_id: SinceTransactionID = sentinel):
        """
        Endpoint used to poll an Account for its current state and changes
        since a specified TransactionID.

        Note:
            OandaClient will supply since_transaction_id if None is provided

        Args:
            since_transaction_id: :class:`~async_v20.endpoints.annotations.SinceTransactionID`
                ID of the Transaction to get Account changes since.

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (changes= :class:`~async_v20.AccountChanges`,
                state= :class:`~async_v20.AccountChangesState`,
                lastTransactionID= :class:`~async_v20.TransactionID`)
        """
        pass
