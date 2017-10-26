async_v20: Asynchronous OANDA v20 client
========================================

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
- async_v20 is in Alpha stage and has not been tested on a live OANDA account
- This package currently does not have full unittest coverage.

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

It is also recommended to install pandas. This allows objects to be converted into *pandas*. **Series** objects
allowing for easier integration with python's powerful data analysis tool chain.

    $ pip install pandas


`async_v20` is built upon `aiohttp`.
It is therefore recommended to also install `cchardet` as per `aiohttp` documentation

http://aiohttp.readthedocs.io/en/stable/

    $ pip install cchardet



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


    async def account():
        async with OandaClient() as client:
            return await client.get_account_details()



    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(account())

    # pandas Series
    print(response['account'].series())


First we need to import *asyncio* this allows up to run our *coroutine*

.. code-block:: python

    import asyncio


We then import *OandaClient* which provides us the means to interact with OANDA

.. code-block:: python

    from async_v20 import OandaClient


Because *OandaClient* returns *coroutines* we use *async def*. This allows the use of the *await* syntax

.. code-block:: python

    async def account():


*OandaClient* is a *context manager*, we use *async with* to instantiate a
client instance. Doing so will automatically close the *http session* when we're done

.. code-block:: python

        async with OandaClient() as client:


We then create and *run* the *coroutine* by calling *client*. **get_account_details()**

.. code-block:: python

            return await client.get_account_details()


Now we have defined our *coroutine* we need to execute it.
To do so we need an event loop. Achieved using *asyncio*. **get_event_loop()**

.. code-block:: python

    loop = asyncio.get_event_loop()


The value returned by executing the `account()` *coroutine* is accessed through the event loop.

.. code-block:: python

    response = loop.run_until_complete(account())


`async_v20` objects have a **series()** method that returns a `pandas.Series`

.. code-block:: python

    print(response['account'].series())



