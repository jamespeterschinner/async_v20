.. _best-practices:

Best Practices
==============

One OandaClient per application
-------------------------------

**Example**

.. literalinclude:: ../../bin/concurrent_example.py
    :emphasize-lines: 5

Initialize first
----------------

`OandaClient` requires initialization. The initialization procedure can delay execution of `OandaClient`. **methods**

In order to prevent this. It is recommended to preemptively initialize the OandaClient instance

.. literalinclude:: ../../bin/initialization.py
    :emphasize-lines: 8

