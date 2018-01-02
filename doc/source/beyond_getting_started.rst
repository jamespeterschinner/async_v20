Beyond Getting Started
======================

So you have read :ref:`tutorial` and need to know more.

Your first issue is knowing what methods to use.

The :ref:`api-docs` docs contains all the exposed methods :term:`async_v20` provides.

What you need to know
---------------------

- :ref:`OandaClient` returns v20 API calls in :class:`~async_v20.interface.response.Response` objects
    The `response` is a python dictionary and designed to reflect the responses defined by the v20
    `docs <http://developer.oanda.com/rest-live-v20/introduction/>`_ :

    - responses contain the equivalent python objects. As defined in :ref:`class-definitions`

- *OandaClient*. Automatically supplys arguments to endpoints that require the following:

    .. autoclass:: async_v20.definitions.primitives.AccountID
        :noindex:
    .. autoclass:: async_v20.endpoints.annotations.Authorization
        :noindex:
    .. autoclass:: async_v20.endpoints.annotations.LastTransactionID
        :noindex:
    .. autoclass:: async_v20.endpoints.annotations.SinceTransactionID
        :noindex:


- **OandaClient** by default will connect to the practice server:
    - OANDA's `docs <http://developer.oanda.com/rest-live-v20/introduction/>`_ Contain host information


Underling Principles
--------------------

All arguments passed to :ref:`api-docs` methods are used to create instances of the parameters annotation.
Why is this useful?

    - Prevents you from importing required class' and instantiating them manually
    - HTTP requests are formatted based upon the objects the endpoint accepts. See :ref:`passing-arguments`
    - The base class :class:`~async_v20.definitions.base.Model` will convert the object into valid :term:`JSON`
    - Invalid arguments will raise :class:`~async_v20.exceptions.InvalidValue` catching mistakes earlier
    - Provides flexibility when passing arguments

Here is an Example

.. literalinclude:: ../../bin/passing_arguments.py

.. note::

    Executing this example **will** create a long position of the AUD/USD currency pair
    worth 30 units.


What might be useful
--------------------

.. _passing-arguments:

How Are Arguments Passed
________________________

All methods exposed by *async_v20*. **OandaClient** are written in a declarative fashion.

Lets take at look at an example:

.. literalinclude:: ../../async_v20/interface/instrument.py
    :lines: 19-32

.. Note::

    The :term:`docstring` has been left of this example for brevity.
        - This example is not complete without a `pass` statement

**First**
   - We define the endpoint:

    .. literalinclude:: ../../async_v20/interface/instrument.py
        :lines: 20
        :emphasize-lines: 1

**Then**
   - We define arguments to pass to the endpoint


    .. literalinclude:: ../../async_v20/interface/instrument.py
        :lines: 20-32
        :emphasize-lines: 2-13


You will notice that all :term:`arguments` have an :term:`annotation`.

async_v20 uses these annotations to format arguments into
the correct http request.

The http request formatting is defined by the *EndPoint*

**In this case**

    .. literalinclude:: ../../async_v20/endpoints/instrument.py
        :lines: 9-33

**Notice that**

    .. literalinclude:: ../../async_v20/endpoints/instrument.py
        :lines: 20
        :emphasize-lines: 1

    Contains :term:`key` entries that coincide with the methods annotations.
    The annotation is then used to lookup up location of the argument in the HTTP request
    and the corresponding key that will be used with the passed data to create the
    correct key/value pair.


How Responses are Constructed
_____________________________

The :term:`http` response from :term:`OANDA` is handled by the `EndPoint`
each *OandaClient*. **method** defines.

There is a two step process by which the response is constructed:
   - The http :term:`status` is used to look up the expected response
   - Each JSON object is constructed into the appropriate python object

How Objects are Serialized
__________________________

One of the main problems :term:`async_v20` solves for you is correctly formatting
`objects` into JSON that OANDA's v20 API accepts.

The issue here is that OANDA defines objects with :term:`camelCase` :term:`attributes`.
Python programs typically reserve camelCase for :term:`class` definitions.

This means, in order to both satisfy python standards and OANDA,
objects (as defined in :ref:`class-definitions`) need to accept `camelCase` and :term:`snake_case`
arguments when being constructed.

`Objects` store there attributes as `snake_case` (as python programmers would expect),
which adds a further requirement to convert these into `camelCase` when being serialized.

To solve this the :mod:`async_v20.definitions.attributes` module
contains two dictionaries. :attr:`~async_v20.definitions.attributes.instance_attributes`
& :attr:`~async_v20.definitions.attributes.json_attributes`:

   - When creating objects, arguments are passed through `instance_attributes` dictionary
   - When serializing objects, attributes are passed through `json_attributes` dictionary

