Getting started
===============


.. _create-account:

Creating an Account
-------------------

To use :term:`async_v20` you must have an account with :term:`OANDA`

    - Create an account `HERE <https://www.oanda.com/account/login>`_
    - Create an API :term:`token` `ALSO HERE <https://www.oanda.com/demo-account/tpa/personal_token>`_

.. _setting-up-environment:

Setting up environment
----------------------

    - Install :term:`async_v20` as per :ref:`installation`
    - Create a new :term:`environment variable` with the name `OANDA_TOKEN` and value as
      the :term:`token` generated from :ref:`create-account`.

    .. toctree::
        environment_variables


    .. note::

        - It is considered best practice use a :term:`virtual environment`
        - It is not required to store the token in an :term:`environment variable`. The token can be passed to :ref:`OandaClient`

.. _tutorial:

Using async_v20
---------------

Once an account has been created as per :ref:`create-account`
and the environment is configured as per :ref:`setting-up-environment`,
we are ready to begin.

Lets first take a look at this code example, then go though it line by line.

.. literalinclude:: ../../bin/account.py
    :lines: 1-16


First we need to import :term:`asyncio` this allows us to run our :term:`coroutine`

.. literalinclude:: ../../bin/account.py
    :lines: 1

We then import `OandaClient` which provides us the means to interact with OANDA

.. literalinclude:: ../../bin/account.py
    :lines: 3

Because `OandaClient` returns `coroutines` we use `async def`. This allows the use of the `await` syntax

.. literalinclude:: ../../bin/account.py
    :lines: 6

`OandaClient` is a :term:`context manager`, we use `async with` to instantiate a
client instance. Doing so will automatically close the `http session` when we're done

.. literalinclude:: ../../bin/account.py
    :lines: 7

We then create and :term:`await` the :term:`coroutine` by calling `client`. **account()**

.. literalinclude:: ../../bin/account.py
    :lines: 8

Now we have defined our :term:`coroutine` we need to execute it.
To do so we need an event loop. Achieved using `asyncio`. **get_event_loop()**

.. literalinclude:: ../../bin/account.py
    :lines: 11

The value returned by executing the `account` :term:`coroutine` is accessed through the event loop.

.. literalinclude:: ../../bin/account.py
    :lines: 12

:term:`async_v20` objects have a `Model`. **series()** method that returns a :term:`pandas`. **Series**

.. literalinclude:: ../../bin/account.py
    :lines: 15

.. note::

    Each application should only instantiate **ONE** OandaClient instance per account.
    See :ref:`best-practices`.
