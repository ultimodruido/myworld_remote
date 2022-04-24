API
---

System functionalities can be accessed and configured using a restAPI provided from FastAPI.
FastAPI also creates a detailed documentation accessible from web browser at the
following `link`_ (only available when the server is running)

.. _link: http://127.0.0.1:5000/docs

The reply from the server follows a pre-defined pattern. A dictionary serialized to JSON::

    {
        "entry_point": "/remote_status",
        "result": True,
        "data": {
            "port": "COM3"
        }
    }


It has always "entry_point", "result" and "data" keys. Only the first two are always filled.

* "entry_point": useful to identify the call that originated the response
* "result": a boolean the inform about the result of the request

The "data" key is filled only when additional information has to be transferred back to the client.
Its content depends on the request.