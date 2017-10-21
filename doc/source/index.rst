.. async_v20 documentation master file, created by
   sphinx-quickstart on Sat Oct 21 19:19:01 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

async_v20: Asynchronous OANDA v20 client
========================================

.. _GitHub: https://github.com/jamespeterschinner/async_v20

Disclaimer
----------

- Losses can exceed investment.
- async_v20 and its creator has no affiliation with OANDA. And is not endorsed by OANDA in any manner.
- async_v20 is in Alpha stage and has not been tested on a live OANDA account
- This package currently does not have full unittest coverage.

Features
---------

- Exposes the entire `v20 API <http://developer.oanda.com/rest-live-v20/introduction/>`_ `
- Serialize objects directly into :term:`pandas`. `Series <http://pandas.pydata.org/pandas-docs/stable/dsintro.html#series>`_ ` objects
- Construct :term:`concurrent` trading algorithms

Installation
------------

.. code-block:: bash

   $ pip install async_v20

:term:`async_v20` is built upon :term:`aiohttp`.
It is therefor recommended to also install :term:`cchardet` as per :term:`aiohttp`
`documentation <http://aiohttp.readthedocs.io/en/stable/>`_ `

.. code-block:: bash

   $ pip install cchardet


Contents
--------
.. toctree::

   glossary

