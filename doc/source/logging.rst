Logging
=======

async_v20 employs the `logging.getLogger(__name__)` standard for all it's modules.
Hence the base logger for async_v20 is 'async_v20'

:class:`~async_v20.OandaClient` has a `debug` attribute for enabling the logging of debug level messages.

**Example**

.. code-block:: python

    >>> from async_v20 import OandaClient
    >>> import asyncio
    >>> import logging
    >>> loop = asyncio.get_event_loop()
    >>> run = loop.run_until_complete
    >>> import logging
    >>> logger = logging.getLogger('async_v20')
    >>> handler = logging.StreamHandler()
    >>> logger.addHandler(handler)
    >>> logger.setLevel(logging.INFO)
    >>> client = OandaClient()
    >>> rsp = run(client.close_all_trades())
    # close_all_trades()
    # Initializing client
    # Initializing session
    # list_services(args=(), kwargs={})
    # list_accounts(args=(), kwargs={})
    # get_account_details(args=(), kwargs={})
    # account_instruments(args=(), kwargs={})
    # list_open_trades(args=(), kwargs={})
    # list_open_trades(args=(), kwargs={})