Usage
-----
A Windows executable of the latest commit is available in the ``./dist`` folder for download.

For other OS (not tested) at the moment the only option is to clone the repository and start the program by running the script ::

    python myworld.py



The sever listens at the following local link::

    http://127.0.0.1:5000

The port can be change with the -p flag::

    python myworld.py -p 8000

The server is configured to answer also from remote devices, just change 127.0.0.1 with the IP address of your pc

In order to be able to transmit infrared signals to the trains, two things are needed:

* a configured Circuit playground express board
* a configuration file


To configure the board, copy the ``playground_firmware/transmitter_routine.py`` in the board memory
and rename the file into ``code.py``. The board will reload automatically.
In case of need in the ``playground_firmware/lib`` directory there is a copy of
the ``adafruit_irremote.py`` library. Newer version are available on adafruit website.

If no configuration file is provided, you have to register the serial port used to
communicate with the circuit playground.

The API call to set up, for example, COM3 as communication port, is the following::

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

You can refer to the live API for an overview of the available options: http://127.0.0.1:5000/docs
Change the IP number and the port according to your configuration.

