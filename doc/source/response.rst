The Response Object
===================

All API methods apart from :meth:`~async_v20.OandaClient.account` and
:meth:`~async_v20.OandaClient.close_all_trades` return
:class:`~async_v20.interface.response.Response` objects

The response object is a :class:`dict` with a few added methods:

    - Truth testing returns true when the Response contains an expected status
    - __repr__ displays all keys


.. autoclass:: async_v20.interface.response.Response
.. automethod:: async_v20.interface.response.Response.json
.. automethod:: async_v20.interface.response.Response.dict

