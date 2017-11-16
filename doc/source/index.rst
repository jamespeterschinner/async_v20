.. _async_v20-home:


async_v20: Asynchronous OANDA v20 client
========================================

.. image:: https://raw.githubusercontent.com/jamespeterschinner/async_v20/master/doc/source/_static/async_v20-icon-128x128.png
    :alt: async-v20 logo

.. image:: https://travis-ci.org/jamespeterschinner/async_v20.svg?branch=master
  :target: https://travis-ci.org/jamespeterschinner/async_v20


.. image:: https://codecov.io/gh/jamespeterschinner/async_v20/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/jamespeterschinner/async_v20


.. image:: https://readthedocs.org/projects/async-v20/badge/?version=latest
  :target: http://async-v20.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

Disclaimer
----------

- Losses can exceed investment.
- async_v20 and its creator has no affiliation with OANDA. And is not endorsed by OANDA in any manner.
- async_v20 is in Alpha stage and has not been tested on a live OANDA account
- This package currently does not have full unittest coverage.

Features
---------

- Exposes the entire `v20 API <http://developer.oanda.com/rest-live-v20/introduction/>`_ `
- immutable objects
- No `*args, **kwargs` In client methods. So no guessing what arguments a method takes
- Serialize objects directly into :term:`pandas`. `Series <http://pandas.pydata.org/pandas-docs/stable/dsintro.html#series>`_ objects
- Construct :term:`concurrent` trading algorithms

.. _installation:

installation
------------

.. code-block:: bash

   $ pip install async_v20

:term:`async_v20` is built with `aiohttp <https://github.com/aio-libs/aiohttp>`_.
It is therefore recommended to also install :term:`cchardet` as per :term:`aiohttp`
`documentation <http://aiohttp.readthedocs.io/en/stable/>`_ `

.. code-block:: bash

   $ pip install cchardet

   $ pip install aiodns

Tutorial
--------

:ref:`tutorial`

Source code
-----------

Can be found on `GitHub <https://github.com/jamespeterschinner/async_v20>`_

Please feel free to file an issue on the bug tracker if you have found a bug
or have some suggestion in order to improve the client.


Dependencies
------------

- **python >= 3.6**
- aiohttp >= 2.2.5
- ujson >= 1.35'
- yarl >= 0.12.0'
- pandas

Contents
--------
.. toctree::

   getting_started
   best_practices
   particularly_pertinent
   beyond_getting_started
   traps
   api
   types
   primitives
   glossary

