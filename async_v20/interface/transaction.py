from .decorators import endpoint
from ..definitions.types import TransactionID
from ..endpoints.annotations import FromTime
from ..endpoints.annotations import FromTransactionID
from ..endpoints.annotations import PageSize
from ..endpoints.annotations import ToTime
from ..endpoints.annotations import ToTransactionID
from ..endpoints.annotations import Type
from ..endpoints.transaction import *
from ..definitions.helpers import sentinel

__all__ = ['TransactionInterface']


class TransactionInterface(object):
    @endpoint(GETTransactions)
    def list_transactions(self,
                          from_time: FromTime = sentinel,  # TODO should default to account creation time
                          to_time: ToTime = sentinel,  # TODO should default to request time
                          page_size: PageSize = 100,
                          type_: Type = sentinel):
        """
        Get a list of Transactions pages that satisfy a time-based Transaction
        query.

        Args:

            from_time: :class:`~async_v20.endpoints.annotations.FromTime`
                The starting time (inclusive) of the time range for the
                Transactions being queried.
            to_time: :class:`~async_v20.endpoints.annotations.ToTime`
                The ending time (inclusive) of the time range for the
                Transactions being queried.
            page_size: :class:`~async_v20.endpoints.annotations.PageSize`
                The number of Transactions to include in each page of the
                results.
            type_: :class:`~async_v20.endpoints.annotations.Type`
                A filter for restricting the types of Transactions to retrieve.

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (from= :class:`~async_v20.DateTime`,
                to= :class:`~async_v20.DateTime`,
                pageSize= :class:`~builtins.int`,
                type=( :class:`~async_v20.TransactionFilter`, ...),
                count= :class:`~builtins.int`,
                pages=( :class:`str`, ...),
                lastTransactionID= :class:`~async_v20.TransactionID`)
        """
        pass

    @endpoint(GETTransactionID)
    def get_transaction(self, transaction_id: TransactionID):
        """
        Get the details of a single Account Transaction.

        Args:

            transaction_id: :class:`~async_v20.TransactionID`
                A Transaction ID

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (transaction= :class:`~async_v20.Transaction`,
                lastTransactionID= :class:`~async_v20.TransactionID`)
        """
        pass

    @endpoint(GETIDrange)
    def transaction_range(self,
                          from_transaction: FromTransactionID,
                          to_transaction: ToTransactionID,  # TODO make this default to now
                          type_: Type = sentinel):
        """
        Get a range of Transactions for an Account based on the Transaction
        IDs.

        Args:

            from_transaction: :class:`~async_v20.endpoints.annotations.FromTransactionID`
                The starting Transaction ID (inclusive) to fetch.
            to_transaction: :class:`~async_v20.endpoints.annotations.ToTransactionID`
                The ending Transaction ID (inclusive) to fetch.
            type_: :class:`~async_v20.endpoints.annotations.Type`
                The filter that restricts the types of Transactions to
                retrieve.

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (transactions=( :class:`~async_v20.Transaction`, ...),
                lastTransactionID= :class:`~async_v20.TransactionID`)
        """
        pass

    @endpoint(GETSinceID)
    def since_transaction(self, transaction_id: TransactionID = sentinel):
        """
        Get a range of Transactions for an Account starting at (but not
        including) a provided Transaction ID.

        Args:

            transaction_id: :class:`~async_v20.TransactionID`
                The ID of the last Transaction fetched. This query will return
                all Transactions newer than the TransactionID.

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (transactions=( :class:`~async_v20.Transaction`, ...),
                lastTransactionID= :class:`~async_v20.TransactionID`)
        """
        pass

    @endpoint(GETTransactionsStream)
    def stream_transactions(self):
        """
        Get a stream of Transactions for an Account starting from when the
        request is made.

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (transaction= :class:`~async_v20.Transaction`)


                **OR**


                :class:`~async_v20.interface.response.Response`
                (Heartbeat= :class:`~async_v20.TransactionHeartbeat`)
        """
        pass
