.. _best-practices:

Best Practices
==============

One OandaClient per application
-------------------------------

:ref:`tutorial` example, used :ref:`OandaClient` as a context manager. This is correct when
the client does not need to be shared between multiple :term:`coroutines`.

This is a an example of multiple coroutines using the **One** OandaClient instance:

.. literalinclude:: ../../bin/concurrent_example.py
    :emphasize-lines: 5

Initialize first
----------------

`OandaClient` requires initialization. The initialization procedure can delay execution of `OandaClient`. **methods**

If this is a concern for you, it is recommended to preemptively initialize the OandaClient instance.

.. literalinclude:: ../../bin/initialization.py
    :emphasize-lines: 8

Check Services
--------------

It is encouraged to check the service you wish to consume is available. See :ref:`health_api`.


