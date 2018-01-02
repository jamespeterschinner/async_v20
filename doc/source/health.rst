.. _health_api:

Health API
==========

async_v20 includes OANDA's v20 health `API <http://developer.oanda.com/rest-live-v20/health/>`_.

During the initialization of OandaClient the statuses of the services are checked.
A warning is logged for each service that is not currently up.

Users are encouraged to explicitly check the service they wish to use is available.

see :ref:`health` for complete list of API calls.

Example:

.. code-block:: python

    >>> from async_v20 import OandaClient
    >>> import asyncio
    >>> client = OandaClient()
    >>> loop = asyncio.get_event_loop()
    >>> run = loop.run_until_complete
    >>> rsp = run(client.list_services())
    >>> rsp
    # <Status [200]: services>
    >>> rsp.services
    # (<Service: id=fxtrade-practice-rest-api>,
    # <Service: id=fxtrade-practice-streaming-api>,
    # <Service: id=fxtrade-rest-api>,
    # <Service: id=fxtrade-streaming-api>)
    >>> rsp.services.get_id('fxtrade-practice-streaming-api')
    # <Service: id=fxtrade-practice-streaming-api>
    >>> rsp.services.get_id('fxtrade-practice-streaming-api').current_event.status.description
    # 'The service is up'

