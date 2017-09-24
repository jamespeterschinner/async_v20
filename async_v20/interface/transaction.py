from .decorators import endpoint
from ..definitions.types import TransactionID
from ..endpoints.annotations import FromDateTime
from ..endpoints.annotations import PageSize
from ..endpoints.annotations import ToDateTime
from ..endpoints.annotations import Type
from ..endpoints.transaction import *
from .base import Interface
__all__ = ['TransactionInterface']

class TransactionInterface(Interface):
    @endpoint(GETTransactions)
    def list_transactions(self, from_date_time: FromDateTime, to_date_time: ToDateTime, page_size: PageSize,
                          type_: Type):
        """
        Get a list of Transactions pages that satisfy a time-based Transaction
        query.

        Args:
            from_date_time:
                The starting time (inclusive) of the time range for the
                Transactions being queried.
            to_date_time:
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
    def transaction_range(self, from_date_time: FromDateTime, to_date_time: ToDateTime, type_: Type):
        """
        Get a range of Transactions for an Account based on the Transaction
        IDs.

        Args:
            from_date_time:
                The starting Transaction ID (inclusive) to fetch.
            to_date_time:
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
