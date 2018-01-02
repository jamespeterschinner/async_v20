.. _particularly_pertinent:

Particularly Pertinent Programming Interface
============================================

There are two additional helper methods that :ref:`OandaClient` exposes, beyond OANDA's
own `v20 <https://github.com/oanda/v20-python/tree/master/src>`_ client;
:meth:`~async_v20.OandaClient.account`, :meth:`~async_v20.OandaClient.close_all_trades`.

Getting the Account Status
--------------------------

OANDA's v20 API is a RESTful service. Meaning that the server only sends the changes to the account,
rather then the full account. This is useful, in that it reduces network traffic,
but requires addition computation on the client side. As changes sent from the server must be
incorporated locally.

This functionality is implemented in the :meth:`~async_v20.OandaClient.account` method.

In order to check the status of the account. Use the await syntax, like so:

.. literalinclude:: ../../bin/account.py
    :lines: 5-8

.. note::

    The :meth:`~async_v20.OandaClient.account` method uses the response from
    :meth:`~async_v20.OandaClient.account_changes` to update the local account object.
    the response from :meth:`~async_v20.OandaClient.account_changes` contains more information
    than the :class:`~async_v20.definitions.types.Account` specifies. Meaning that some
    information contained in the :meth:`~async_v20.OandaClient.account_changes` response
    is lost when updating the account. It has been chosen to only keep
    :class:`~async_v20.definitions.types.Order`'s
    :class:`~async_v20.definitions.types.Trade`'s
    :class:`~async_v20.definitions.types.Position`'s,
    in the account that are currently open.
    This is to resemble the behaviour of OANDA's Web based browser interface

    :class:`~async_v20.definitions.types.Transaction`'s are stored on the
    client as :attr:`~async_v20.OandaClient.transactions`

Closing all Trades
------------------

The :meth:`~async_v20.OandaClient.close_all_trades` method is provided to help facilitate
your risk management policy. async_v20 is intended to be used as an algorithmic trading platform,
which naturally raises concerns of run away losses, to the unbeknown user.

:meth:`~async_v20.OandaClient.close_all_trades` is intended to help mitigate this concern by allowing
users to programme a `global` :term:`stop loss` by which all trades can be terminated.

.. note::
    Users who implement this feature should account for the **Two** possible outcomes.

    - A :class:`~async_v20.exceptions.CloseAllTradesFailure` is raised

    **OR**

    - returns (**True**, `closed_trade_responses`) - All trades were closed


