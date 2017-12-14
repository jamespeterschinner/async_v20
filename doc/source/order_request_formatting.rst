Formatting Order Requests
=========================

:class:`~async_v20.OandaClient` provides the option to format :class:`~async_v20.definitions.types.OrderRequest`'s
in the context of the instrument the OrderRequest is for.

Confused? So was I, Let's have a look at an `instrument`. **series()**
representation of an :class:`~async_v20.definitions.types.Instrument`.

.. code-block:: python
    :emphasize-lines: 2,4-8,11

    display_name                      Brent Crude Oil
    display_precision                               3
    margin_rate                                  0.05
    maximum_order_units                        100000
    maximum_position_size                           0
    maximum_trailing_stop_distance                100
    minimum_trade_size                              1
    minimum_trailing_stop_distance               0.05
    name                                      BCO_USD
    pip_location                                   -2
    trade_units_precision                           0
    type                                          CFD
    dtype: object

The above instrument outlines the formatting of an *OrderRequest* for the *Instrument* (in this case *Brent Crude Oil*).
Take *Instrument*. **trade_units_precision** as an example, this attribute defines how many decimal places
:class:`~async_v20.definition.types.OrderRequest`. **units** may be used for this instrument (our example *0*).

You will also notice **minimum** and **maximum** values for other *OrderRequest* attributes.

*OandaClient*. **format_order_requests** is a boolean value which changes the degree to which
*OrderRequest*'s will be modified to comply with the instrument specification.
If **format_order_requests** is set to
:class:`True` *OandaClient* will modify values so that they are within
the valid range specified by the instrument.

.. note::
    I believe most users will want to use this feature as it dramatically
    reduces the complexity of placing valid OrderRequests. It is disabled by default.

    Only enable this feature if you understand that your `OrderRequest`. **stop_loss_on_fill**/
    **take_profit_on_fill**/**trailing_stop_loss_distance** and **price_bound** configuration may
    be altered to comply with the instruments valid ranges.

.. note::
    The precision of :class:`~async_v20.definitions.primitives.DecimalNumber` and
    :class:`~async_v20.definitions.primitive.PriceValue` will **always** be rounded
    to the correct precision for the instrument, regardless of *OandaClient*. **format_order_requests**
    value.


**Example:**

.. code-block:: python
    :emphasize-lines: 10-12,15,19

    >>> from async_v20 import OandaClient
    >>> import asyncio
    >>> client = OandaClient()
    >>> run = loop.run_until_complete
    >>> run(client.create_order('AUD_USD', 0))
    Traceback (most recent call last):
    ValueError: OrderRequest units 0.0 are less than the minimum trade size 1.0
    >>> run(client.create_order('AUD_USD', 1))
    <Status [201]: orderCreateTransaction, orderFillTransaction, relatedTransactionIDs, lastTransactionID>
    >>> client.format_order_requests
    False
    >>> client.format_order_requests = True
    >>> run(client.create_order('AUD_USD', 0))
    <Status [201]: orderCreateTransaction, orderFillTransaction, relatedTransactionIDs, lastTransactionID>
    >>> client.format_order_requests = False
    >>> run(client.create_order('AUD_USD', 1, trailing_stop_loss_on_fill=0))
    Traceback (most recent call last):
    ValueError: Trailing stop loss distance 0.0 is not within AUD_USD specified range 0.0005 - 1.0
    >>> client.format_order_requests = True
    >>> run(client.create_order('AUD_USD', 1, trailing_stop_loss_on_fill=0))
    <Status [201]: orderCreateTransaction, orderFillTransaction, relatedTransactionIDs, lastTransactionID>