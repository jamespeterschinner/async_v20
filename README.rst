async_v20: Asynchronous OANDA v20 client
========================================
*A foreign exchange client*

.. image:: https://raw.githubusercontent.com/jamespeterschinner/async_v20/master/doc/source/_static/async_v20-icon-128x128.png
   :height: 64px
   :width: 64px
   :alt: async-v20 logo

.. image:: https://travis-ci.org/jamespeterschinner/async_v20.svg?branch=master
   :target: https://travis-ci.org/jamespeterschinner/async_v20
   :align: right

.. image:: https://codecov.io/gh/jamespeterschinner/async_v20/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/jamespeterschinner/async_v20

.. image:: https://readthedocs.org/projects/async-v20/badge/?version=latest
   :target: http://async-v20.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


Documentation
-------------

http://async-v20.readthedocs.io/

Disclaimer
----------

- Losses can exceed investment.
- async_v20 and its creator has no affiliation with OANDA. And is not endorsed by OANDA in any manner.
- async_v20 is in Beta stage and has not been tested on a live OANDA account
- Use at own risk

Features
---------

- Exposes the entire v20 API
- No `*args, **kwargs` In client methods. So no guessing what arguments a method takes
- Serialize objects directly into `pandas.Series` objects
- Construct *concurrent* trading algorithms



installation
------------

**REQUIRES:**

python >= 3.6

https://www.python.org/

    $ pip install async_v20


`async_v20` is built with `aiohttp <https://github.com/aio-libs/aiohttp>`_.
It is therefore recommended to also install `cchardet` and `aiodns` as per `aiohttp`
`documentation <http://aiohttp.readthedocs.io/en/stable/>`_ `

.. code-block:: bash

   $ pip install cchardet

   $ pip install aiodns

Why async_v20?
--------------

There are many OANDA clients for python already available. Why create another?
The main driver for creating async_v20 was to facilitate better risk management,
by allowing user's to concurrently monitor account status and trade currency's.

An unintended consequence of async_v20 is the ability to create clear segregation
between implementation ideas.

A simple example might contain a coroutine for the following:

    - Monitoring overall account status
    - Watching price stream and triggering buy/sell signals
    - Monitoring individual trades and closing movements against held positions

A synchronous implementation would require considerable effort to determine which
task communicates with the server next. async_v20 removes this burden by using
`aiohttp <https://github.com/aio-libs/aiohttp>`_

Further goals of async_v20 has been to lower the barrier of entry for algorithmic trading,
by providing a complete and simple to use interface.


Getting started
===============


Creating an Account
-------------------

To use `async_v20` you must have an account with *OANDA*

- Create an account

    https://www.oanda.com/account/login
- Create an API *token*

    https://www.oanda.com/demo-account/tpa/personal_token

Setting up environment
----------------------

- Install `async_v20` as per **installation**
- Create a new *environment variable* with the name 'OANDA_TOKEN' and value as the *token* generated from above


**Note:**

- It is considered best practice use a *virtual environment*
- It is not required to store the token in an *environment variable*. The token can be passed to OandaClient

Using async_v20
---------------

Once an account has been created as per *create-account*
and the environment is configured as per *setting-up-environment*
we are ready to begin.

Lets first take a look at this code example, then go though it line by line.


.. code-block:: python

   import asyncio

   from async_v20 import OandaClient


   async def get_account():
       async with OandaClient() as client:
           return await client.account()


   loop = asyncio.get_event_loop()
   account = loop.run_until_complete(get_account())

   # pandas Series
   print(account.series())

   # HTTP response state
   print(account)

   # JSON data in python dictionary format
   print(account.dict())


First we need to import *asyncio* this allows us to run our *coroutine*

.. code-block:: python

    import asyncio


We then import *OandaClient* which provides us the means to interact with OANDA

.. code-block:: python

    from async_v20 import OandaClient


Because *OandaClient* returns *coroutines* we use *async def*. This allows the use of the *await* syntax

.. code-block:: python

    async def get_account():


*OandaClient* is a *context manager*, we use *async with* to instantiate a
client instance. Doing so will automatically close the *http session* when we're done

.. code-block:: python

        async with OandaClient() as client:


We then create and *run* the *coroutine* by calling *client*. **get_account_details()**

.. code-block:: python

            return await client.account()


Now we have defined our *coroutine* we need to execute it.
To do so we need an event loop. Achieved using *asyncio*. **get_event_loop()**

.. code-block:: python

    loop = asyncio.get_event_loop()


The value returned by executing the `account()` *coroutine* is accessed through the event loop.

.. code-block:: python

    account = loop.run_until_complete(get_account())


`async_v20` objects have a **series()** method that returns a `pandas.Series`

.. code-block:: python

    print(account.series())


**Outputs**

.. code-block:: python

   alias                                                          Primary
   balance                                                        97801.9
   commission                                                           0
   created_by_user_id                                             1234567
   created_time                       2017-08-11 15:04:31.639182352+00:00
   currency                                                           AUD
   financing                                                      -3.5596
   hedging_enabled                                                  False
   id                                                 123-123-1234567-123
   last_margin_call_extension_time                                   None
   last_transaction_id                                               6360
   margin_available                                               97801.9
   margin_call_enter_time                                            None
   margin_call_extension_count                                       None
   margin_call_margin_used                                              0
   margin_call_percent                                                  0
   margin_closeout_margin_used                                          0
   margin_closeout_nav                                            97801.9
   margin_closeout_percent                                              0
   margin_closeout_position_value                                       0
   margin_closeout_unrealized_pl                                        0
   margin_rate                                                       0.02
   margin_used                                                          0
   nav                                                            97801.9
   open_position_count                                                  0
   open_trade_count                                                     0
   orders                                                              []
   pending_order_count                                                  0
   pl                                                            -2194.53
   position_value                                                       0
   positions                                                           []
   resettable_pl                                                 -2194.53
   resettabled_pl_time                                               None
   trades                                                              []
   unrealized_pl                                                        0
   withdrawal_limit                                               97801.9
   dtype: object