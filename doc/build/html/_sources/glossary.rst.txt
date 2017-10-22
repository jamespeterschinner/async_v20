.. _glossary:


==========
 Glossary
==========

.. if you add new entries, keep the alphabetical sorting!

.. glossary::
   :sorted:

   aiohttp

      http client/server framework :term:`async_v20` use's to communicate asynchronously.

      http://aiohttp.readthedocs.io/en/stable/

   asyncio

      The library for writing single-threaded concurrent code using
      coroutines, multiplexing I/O access over sockets and other
      resources, running network clients and servers, and other
      related primitives.

      Reference implementation of :pep:`3156`

      https://pypi.python.org/pypi/asyncio/

   async_v20

      The name of the package this documentation is documenting

      https://github.com/jamespeterschinner/async_v20

   await

      Python syntax to execute a :term:`coroutine` inside an asynchronous function

   callable

      Any object that can be called. Use :func:`callable` to check
      that.


   cchardet

       cChardet is high speed universal character encoding detector -
       binding to charsetdetect.

       https://pypi.python.org/pypi/cchardet/

   concurrent

      The process by which a single threaded application switches between
      different tasks. Typically done to prevent waiting for I/O bound operations

   coroutine

      A python object that supports asynchronous execution

   context manager

      A Python programming concept that defines `enter` and `exit` methods. Used to handle set-up
      and tear-down tasks

   environment variable

      An environment variable is a dynamic-named value that can affect the way running processes
      will behave on a computer. They are part of the environment in which a process runs

   OANDA

      The name of the Foreign Exchange (FOREX) broker :term:`async_v20` communicates with

   OandaClient

      The client class definition :term:`async_v20` exposes

   pandas

      a Python package providing fast, flexible, and expressive data structures
      designed to make working with “relational” or “labeled” data both easy and intuitive

      http://pandas.pydata.org/

   token

      A 65 character string used to uniquely identify and authorise access to the OANDA v20 API

      Example:
         `810492ace47473fa9f72c0eeecd33657-1eae8a55f01431bdd370206f69071e5f`

   virtual environment

      A self-contained directory tree that contains a Python installation for a particular version of Python,
      plus a number of additional packages.

      https://docs.python.org/3/tutorial/venv.html