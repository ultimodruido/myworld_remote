Usage
-----
A Windows executable of the latest commit is available in the ``./dist`` folder for download.

For other OS (not tested) at the moment the only option is to clone the repository and start the program by running the script ::

    python myworld.py



The sever listens at the following link::

    http://127.0.0.1:5000

anyway the correct path is displayed also on the console, example::

    INFO:     Started server process [21068]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:5000 (Press CTRL+C to quit)


in order to be able to transmit, if no configuration file is provided, you have to register
the serial port used to communicate with the circuit playground.

The API call is to set up COM3 as communication port is the following::

    [POST] http://127.0.0.1:5000/register/remote/COM3


Now everything is set, refer to the `live API <http://127.0.0.1:8000/docs>`__ for an overview of the available options.

