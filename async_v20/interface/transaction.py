from .decorators import endpoint
from ..definitions.types import TransactionID
from ..endpoints.annotations import FromTime
from ..endpoints.annotations import PageSize
from ..endpoints.annotations import ToTime
from ..endpoints.annotations import Type
from ..endpoints.annotations import FromTransactionID
from ..endpoints.annotations import ToTransactionID
from ..endpoints.transaction import *

__all__ = ['TransactionInterface']


class TransactionInterface(object):
    @endpoint(GETTransactions)
    def list_transactions(self, from_time: FromTime, to_time: ToTime, page_size: PageSize,
                          type_: Type):
        """
        Get a list of Transactions pages that satisfy a time-based Transaction
        query.

        Args:
            from_time:
                The starting time (inclusive) of the time range for the
                Transactions being queried.
            to_time:
                The ending time (inclusive) of the time range for the
                Transactions being queried.
            page_size:
                The number of Transactions to include in each page of the
                results.
            type_:
                A filter for restricting the types of Transactions to retrieve.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETTransactionID)
    def get_transactions(self, transaction_id: TransactionID):
        """
        Get the details of a single Account Transaction.

        Args:
            transaction_id:
                A Transaction ID

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETIDrange)
    def transaction_range(self, from_transaction: FromTransactionID, to_transaction: ToTransactionID, type_: Type):
        """
        Get a range of Transactions for an Account based on the Transaction
        IDs.

        Args:
            from_transaction:
                The starting Transaction ID (inclusive) to fetch.
            to_transaction:
                The ending Transaction ID (inclusive) to fetch.
            type_:
                The filter that restricts the types of Transactions to
                retrieve.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETSinceID)
    def since_transaction(self, transaction_id: TransactionID):
        """
        Get a range of Transactions for an Account starting at (but not
        including) a provided Transaction ID.

        Args:
            transaction_id:
                The ID of the last Transaction fetched. This query will return
                all Transactions newer than the TransactionID.

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass

    @endpoint(GETTransactionsStream)
    def stream_transactions(self):
        """
        Get a stream of Transactions for an Account starting from when the
        request is made.

        Args:

        Returns:
            async_v20.interface.parser.Response containing the results from submitting the
            request
        """
        pass
