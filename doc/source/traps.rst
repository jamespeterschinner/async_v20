Traps for young players
=======================

Listed here will be traps that have caught me out.
documented here so it doesn't catch you!

ERROR!
------

Have you written some error handling in the event
the client connection falls over?

This is a very broad category of errors.

It may be:

    - OANDA is down for maintenance
    - Someone unplugged your computer
    - The wifi dropped out
    - Network config issue. IP conflict, routing, firewall...
    - Your token expired (for some reason)

An Order is not an OrderRequest
-------------------------------

.. note::

      This is taken from the OANDA `docs <http://developer.oanda.com/rest-live-v20/order-df/>`_

      Orders

          - The specification of all Orders supported by the platform.

      Order Requests:

          - The request specification of all Orders supported by the platform. These objects are used by the API client to create Orders on the platform.

They key point here is that you need to use async_v20 objects that derive from
OrderRequest when passing an order request to the order_request argument
of:

   :meth:`~async_v20.client.OandaClient.post_order`

