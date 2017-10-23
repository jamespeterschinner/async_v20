Beyond Getting Started
======================

So you have read :ref:`tutorial` and need to know more.

Your fist issue is knowing what method to use.

The :ref:`api-docs` contains all the exposed methods :term:`async_v20` provides.

What you need to know
---------------------

- :ref:`OandaClient` returns server responses in the equivalent :term:`python` dictionary:
    - dictionary responses contain the equivalent python objects. As defined in :ref:`class-definitions`
        - these objects are constructed from http response :term:`JSON` body

- *OandaClient*. **methods** that require:

    .. autoclass:: async_v20.definitions.descriptors.transaction.TransactionID

    will be passed the last **TransactionID** implicitly


- **OandaClient** by default will connect to the practice server:
    - OANDA's `docs <http://developer.oanda.com/rest-live-v20/>`_ Contain host information

What might be usefull
---------------------

.. _passing-arguments:

How Are Arguments Passed
________________________

All methods exposed by *async_v20*. **OandaClient** are written in a declarative fashion.

Lets take at look at an example:

.. literalinclude:: ..\..\async_v20\interface\instrument.py
    :lines: 20-33

.. Note::

    The :term:`docstring` has been left of this example for brevity.
        - This example is not complete without a `pass` statement

**First**
   - We define the endpoint:

    .. literalinclude:: ..\..\async_v20\interface\instrument.py
        :lines: 20
        :emphasize-lines: 1

**Then**
   - We define arguments to pass to the endpoint


    .. literalinclude:: ..\..\async_v20\interface\instrument.py
        :lines: 21-33
        :emphasize-lines: 2-12


You will notice that all :term:`arguments` have an :term:`annotation`.

async_v20 uses these annotations to format arguments into
the correct http request.

The http request formatting is defined by the *EndPoint*

**In this case**

    .. literalinclude:: ..\..\async_v20\endpoints\instrument.py
        :lines: 10-45

**Notice that**

    .. literalinclude:: ..\..\async_v20\endpoints\instrument.py
        :lines: 21
        :emphasize-lines: 1

Is a list of dictionary's. Each dictionary has a :term:`key` **'type'**
that corresponds to the annotation defined by *OandaClient*. **get_candles**

**This is the means by which arguments are passed**


How Responses are Constructed
_____________________________

This section assumes you have read :ref:`passing-arguments`

The :term:`http` response from :term:`OANDA` is handled by the `EndPoint`
each *OandaClient*. **method** defines.

     .. literalinclude:: ..\..\async_v20\endpoints\instrument.py
        :lines: 41-42
        :emphasize-lines: 1,2

`response` is a dictionary of dictionary's.

There is a two step process by which the response is constructed:
   - The http :term:`status` is used to look up the expected response
   - Each JSON object is constructed into the appropriate object

How Objects are Serialized
__________________________

One of the main problems :term:`async_v20` solves for you is correctly formatting
`objects` into JSON that OANDA's v20 API accepts.

The issue here is that OANDA defines objects with :term:`camelCase` :term:`attributes`.
Python programs typically reserve camelCase for :term:`class` definitions.

This means, in order to both satisfy python standards and OANDA,
objects as defined in :ref:`class-definitions` need to accept `camelCase` and :term:`snake_case`
arguments when being constructed

`objects` store there attributes as `snake_case` (as python programmers would expect),
which adds a further requirement to convert these into `camelCase` when being serialized.

To solve this the :term:`metaclass`:

   .. autoclass:: async_v20.definitions.metaclass.ORM

    **for** `async_v20.definitions.types.base`. **Model**
    constructs two dictionary's

       .. literalinclude:: ..\..\async_v20\definitions\metaclass.py
          :lines: 93,94
          :emphasize-lines: 1,2

- When creating objects, arguments are passed through `instance_attributes` dictionary
- When serializing objects, attributes are passed through `json_attributes` dictionary

