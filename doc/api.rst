API
---

System functionalities can be accessed and configured using a restful API.
For a detailed documentation of the API, please refer to the live documentation
accessible at the following `link`_  when the server is running.

It contains all the information about possible commands, the necessary parameters
as well as the result scheme.
In addition, clicking the button "Try it out" it is possible to send commands to the
server making the documentation page a very limited, but functional, UI.

.. _link: http://127.0.0.1:5000/docs

The reply from the server follows a pre-defined scheme: a dictionary serialized to JSON::

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

