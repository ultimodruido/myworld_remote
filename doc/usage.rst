Usage
-----
A Windows executable of the latest commit is available in the ``./dist`` folder for download.

For other OS (not tested) at the moment the only option is to clone the repository and start the program by running the script ::

    python myworld.py



The sever listens at the following link::

    http://127.0.0.1:5000

anyway the correct path is printed also on the console, example::

    INFO:     Started server process [21068]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:5000 (Press CTRL+C to quit)


in order to be able to transmit infrared signals to the trains, if no configuration file is provided,
you have to register the serial port used to communicate with the circuit playground.

The API call to set up COM3 as communication port is the following::

    [POST] http://127.0.0.1:5000/register/remote/COM3


To register a new train, it is necessary to specify

* a reference *name* (transmitted to the UI)
* the *frequency* used for the protocol

as follows::

    [POST] http://127.0.0.1:5000//register/newtrain/{name}/{frequency}

To get the list of registered train::

    [GET] http://127.0.0.1:5000/train_list

The train commands can bet sent through the following commands::

    [POST] http://127.0.0.1:5000/train/{train_id}/speed/{speed_value}
    [POST] http://127.0.0.1:5000/train/{train_id}/light
    [POST] http://127.0.0.1:5000/train/{train_id}/horn
    [POST] http://127.0.0.1:5000/train/{train_id}/sound1
    [POST] http://127.0.0.1:5000/train/{train_id}/sound2

You can refer to the `live API <http://127.0.0.1:8000/docs>`__ for an overview of the available options.

