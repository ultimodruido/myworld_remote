Usage
-----
The sever listens at the following link::

    http://127.0.0.1:5000

anyway the correct path is displayed also on the console, example::

    INFO:     Started server process [21068]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:5000 (Press CTRL+C to quit)


in order to be able to transmit, if not configuration file is provided, then you have to register
the serial port used to communicate with the circuit playground.

The API call is to set up COM3 as communication port is the following::

    [POST] http://127.0.0.1:5000/register/remote/COM3

