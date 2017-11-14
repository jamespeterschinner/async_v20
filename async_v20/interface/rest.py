"""module dedicated to implementing the RESTful client"""

from itertools import chain
from async_v20.definitions.types import Account
from async_v20.definitions.types import AccountChanges
from async_v20.definitions.types import AccountChangesState
from async_v20.definitions.types import ArrayTransaction

def update_account(self, changes, changes_state):
    """Update an existing account with changes

    Args:
        account: -- The account instance to update
        transactions: -- An iterable of Transactions to append to
        changes: -- Changes from account_changes API call
        changes_state: ChangesState from account_changes API call

    Returns:
        (Account, ArrayTransaction)

    """

    # Add / Replace / Remove items from the AccountChanges object

    orders = [order if not changes.orders_filled.get_id(order.id)
              else changes.orders_filled.get_id(order.id)
              for order in chain(*self.orders, *changes.orders_created)
              if not changes.orders_cancelled.get_id(order.id)
              and not changes.orders_filled.get_id(order.id)]

    trades = [trade if not changes.trades_reduced.get_id(trade.id)
              else changes.trades_reduced.get_id(trade.id)
              for trade in chain(*self.trades, *changes.trades_opened)
              if not changes.trades_closed.get_id(trade.id)]

    positions = [*changes.positions]

    # Update the Dynamic state

    positions = []
    for position in changes.positions:
        calculated_position_state = changes_state.positions.get_instrument(position.instrument)
        if calculated_position_state:
            position = position.replace(
                unrealized_pl=calculated_position_state.net_unrealized_pl,
                long=position.long.replace(
                    unrealized_pl=calculated_position_state.long_unrealized_pl
                ),
                short=position.short.replace(
                    unrealized_pl=calculated_position_state.short_unrealized_pl)
            )
        positions.append(position)

    # get_account_details does not provide transaction history
    # Instead of adding them to account, we well return them
    transactions = ArrayTransaction(*[*self.transactions, *changes.transactions])

    updated_account = self._account.replace(
        **dict(changes_state.dict(json=False), **{'trades': trades, 'orders': orders, 'positions': positions})
    )
    return updated_account, transactions
