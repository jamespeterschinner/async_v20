.. _api-docs:

OandaClient API
===============

.. note::

      **methods** arguments annotated with 'TransactionID'
      will be passed the correct TransactionID implicitly.

.. note::

      OandaClient will look for OANDA_TOKEN in the enviroment variables
      if no token is passed

.. _OandaClient:

OandaClient
-----------

.. autoclass:: async_v20.OandaClient

Account
-------

.. autoclass:: async_v20.OandaClient
   :members: list_accounts, get_account_details, account_summary, account_instruments, configure_account, account_changes

Instrument
----------

.. autoclass:: async_v20.OandaClient
   :members: get_candles

Order
-----

.. autoclass:: async_v20.OandaClient
   :members: create_order,
            list_orders,
            list_pending_orders,
            get_order,
            replace_order,
            cancel_order,
            set_client_extensions,
            market_order,
            limit_order,
            limit_replace_order,
            stop_order,
            stop_replace_order,
            market_if_touched_order,
            market_if_touched_replace_order,
            take_profit_order,
            take_profit_replace_order,
            stop_loss_order,
            stop_loss_replace_order,
            trailing_stop_loss_order,
            trailing_stop_loss_replace_order


Position
--------

.. autoclass:: async_v20.OandaClient
   :members: list_positions,
            list_open_positions,
            get_positions,
            close_position

Pricing
-------

.. autoclass:: async_v20.OandaClient
   :members: get_pricing,
         stream_pricing

Trade
-----

.. autoclass:: async_v20.OandaClient
   :members: list_trades,
            list_open_trades,
            get_trades,
            close_trades,
            set_client_extensions_trade,
            set_dependent_orders_trade

Transaction
-----------

.. autoclass:: async_v20.OandaClient
   :members: list_transactions,
            get_transactions,
            transaction_range,
            since_transaction,
            stream_transactions

User
----

.. autoclass:: async_v20.OandaClient
   :members: get_user_info,
         get_external_user_info