Digging Deeper
==============

Under the hood
--------------

:term:`async_v20` attempted to follow OANDA's documentation as closely as possible.
This can be particularly use full when async_v20's documentation falls down.

In this section we will try and provide a basic understanding of how async_v20 works,
allowing you to find answers outside the scope of this documentation

Descriptors
-----------

OANDA's `docs <http://developer.oanda.com/rest-live-v20/introduction/>`_
define basic types. :term:`async_v20` implements these as :term:`descriptors`

These descriptors perform these functions:
    - :term:`type checking` and also :term:`domain checking`
    - define correct serialization to json

The Model
---------

:term:`async_v20` creates class definitions for all objects defined in
OANDA's `docs <http://developer.oanda.com/rest-live-v20/introduction/>`_


These definitions inherit the Model class

.. autoclass:: async_v20.definitions.base.Model

which in turn inherits from the metaclass ORM

.. autoclass:: async_v20.definitions.metaclass.ORM

This base structure and the class definitions in:



is responsible for converting received json into python objects and vise versa
