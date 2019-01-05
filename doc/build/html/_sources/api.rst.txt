.. _api-docs:

OandaClient API
===============

.. note::

      OandaClient will look for OANDA_TOKEN in the enviroment variables
      if no token is passed

.. _OandaClient:

OandaClient
-----------

.. autoclass:: async_v20.OandaClient

Account
-------

.. _account:
.. automethod:: async_v20.OandaClient.account
.. automethod:: async_v20.OandaClient.list_accounts
.. automethod:: async_v20.OandaClient.get_account_details
.. automethod:: async_v20.OandaClient.account_summary
.. automethod:: async_v20.OandaClient.account_instruments
.. automethod:: async_v20.OandaClient.configure_account
.. automethod:: async_v20.OandaClient.account_changes

Instrument
----------

.. automethod:: async_v20.OandaClient.get_candles
.. automethod:: async_v20.OandaClient.get_order_book
.. automethod:: async_v20.OandaClient.get_position_book

Order
-----

.. automethod:: async_v20.OandaClient.post_order
.. automethod:: async_v20.OandaClient.create_order
.. automethod:: async_v20.OandaClient.list_orders
.. automethod:: async_v20.OandaClient.list_pending_orders
.. automethod:: async_v20.OandaClient.get_order
.. automethod:: async_v20.OandaClient.replace_order
.. automethod:: async_v20.OandaClient.cancel_order
.. automethod:: async_v20.OandaClient.set_client_extensions
.. automethod:: async_v20.OandaClient.market_order
.. automethod:: async_v20.OandaClient.limit_order
.. automethod:: async_v20.OandaClient.limit_replace_order
.. automethod:: async_v20.OandaClient.stop_order
.. automethod:: async_v20.OandaClient.stop_replace_order
.. automethod:: async_v20.OandaClient.market_if_touched_order
.. automethod:: async_v20.OandaClient.market_if_touched_replace_order
.. automethod:: async_v20.OandaClient.take_profit_order
.. automethod:: async_v20.OandaClient.take_profit_replace_order
.. automethod:: async_v20.OandaClient.stop_loss_order
.. automethod:: async_v20.OandaClient.stop_loss_replace_order
.. automethod:: async_v20.OandaClient.trailing_stop_loss_order
.. automethod:: async_v20.OandaClient.trailing_stop_loss_replace_order


Position
--------

.. automethod:: async_v20.OandaClient.list_positions
.. automethod:: async_v20.OandaClient.list_open_positions
.. automethod:: async_v20.OandaClient.get_position
.. automethod:: async_v20.OandaClient.close_position

Pricing
-------

.. automethod:: async_v20.OandaClient.get_pricing
.. automethod:: async_v20.OandaClient.stream_pricing

Trade
-----

.. automethod:: async_v20.OandaClient.list_trades
.. automethod:: async_v20.OandaClient.list_open_trades
.. automethod:: async_v20.OandaClient.get_trade
.. automethod:: async_v20.OandaClient.close_trade
.. _close_all_trades:
.. automethod:: async_v20.OandaClient.close_all_trades
.. automethod:: async_v20.OandaClient.set_client_extensions_trade
.. automethod:: async_v20.OandaClient.set_dependent_orders_trade

Transaction
-----------

.. automethod:: async_v20.OandaClient.list_transactions
.. automethod:: async_v20.OandaClient.get_transaction
.. automethod:: async_v20.OandaClient.transaction_range
.. automethod:: async_v20.OandaClient.since_transaction
.. automethod:: async_v20.OandaClient.stream_transactions

User
----

.. automethod:: async_v20.OandaClient.get_user_info
.. automethod:: async_v20.OandaClient.get_external_user_info

.. _health:

Health
------

.. automethod:: async_v20.OandaClient.get_current_event
.. automethod:: async_v20.OandaClient.get_event
.. automethod:: async_v20.OandaClient.get_service
.. automethod:: async_v20.OandaClient.get_service_list
.. automethod:: async_v20.OandaClient.get_status
.. automethod:: async_v20.OandaClient.list_events
.. automethod:: async_v20.OandaClient.list_images
.. automethod:: async_v20.OandaClient.list_service_lists
.. automethod:: async_v20.OandaClient.list_services
.. automethod:: async_v20.OandaClient.list_statuses