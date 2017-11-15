"""module dedicated to implementing the RESTful client"""

from itertools import chain

from async_v20.definitions.types import ArrayTransaction


def update_account(self, changes, changes_state):
    """Update an existing account with changes

    Args:
        self: -- OandaClient instance
        changes: -- Changes from account_changes API call
        changes_state: ChangesState from account_changes API call

    Returns: None
    """

    # Add / Replace / Remove items from the AccountChanges object
    orders = (order if not changes.orders_filled.get_id(order.id)
              else changes.orders_filled.get_id(order.id)
              for order in chain(self._account.orders, changes.orders_created)
              if not changes.orders_cancelled.get_id(order.id)
              and not changes.orders_filled.get_id(order.id))

    trades = (trade if not changes.trades_reduced.get_id(trade.id)
              else changes.trades_reduced.get_id(trade.id)
              for trade in chain(self._account.trades, changes.trades_opened)
              if not changes.trades_closed.get_id(trade.id))

    positions = ((position, changes_state.positions.get_instrument(position.instrument))
                 for position in changes.positions)

    # Update the Dynamic state
    orders = tuple(order if not changes_state.orders.get_id(order.id)
                   else order.replace(**changes_state.orders.get_id(order.id).dict())
                   for order in orders)

    trades = tuple(trade if not changes_state.trades.get_id(trade.id)
                   else trade.replace(**changes_state.trades.get_id(trade.id).dict())
                   for trade in trades)

    positions = tuple(position if not state else position.replace(unrealized_pl=state.net_unrealized_pl,
                                                                  long=position.long.replace(
                                                                      unrealized_pl=state.long_unrealized_pl),
                                                                  short=position.short.replace(
                                                                      unrealized_pl=state.short_unrealized_pl))
                      for position, state in positions)
    #

    self._account = self._account.replace(**dict(changes_state.dict(json=False),
                                                 orders=orders, trades=trades, positions=positions))

    self.transactions = ArrayTransaction(*sorted((changes.transactions+self.transactions)
                                         [-self.max_transaction_history:],reverse=True))
