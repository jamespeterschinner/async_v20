from .decorators import endpoint
from ..endpoints.account import *

class AccountInterface(object):


    @endpoint(GETAccounts)
    def list(self):
        """
        Get a list of all Accounts authorized for the provided token.

        Args:

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETAccountID)
    def get(self):
        """
        Get the full details for a single Account that a client has access to.
        Full pending Order, open Trade and open Position representations are
        provided.

        Args:
            accountID:
                Account Identifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETAccountIDSummary)
    def summary(self):
        """
        Get a summary for a single Account that a client has access to.

        Args:
            accountID:
                Account Identifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETAccountIDInstruments)
    def instruments(self, instruments):
        """
        Get the list of tradeable instruments for the given Account. The list
        of tradeable instruments is dependent on the regulatory division that
        the Account is located in, thus should be the same for all Accounts
        owned by a single user.

        Args:
            accountID:
                Account Identifier
            instruments:
                List of instruments to query specifically.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(PATCHAccountIDConfiguration)
    def configure(self, alias, marginRate):
        """
        Set the client-configurable portions of an Account.

        Args:
            accountID:
                Account Identifier
            alias:
                Client-defined alias (name) for the Account
            marginRate:
                The string representation of a decimal number.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETAccountIDChanges)
    def changes(self, sinceTransactionID):
        """
        Endpoint used to poll an Account for its current state and changes
        since a specified TransactionID.

        Args:
            accountID:
                Account Identifier
            sinceTransactionID:
                ID of the Transaction to get Account changes since.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass