Maerklin MyWorld universal remote
=================================

version number: 1.0

author: ultimodruido

Overview
--------

Control all your [Maerklin MyWorld](https://www.maerklin.de/de/lp/2020/willkommen-bei-my-world) 
trains from your PC.


Requirements
------------

You need a [circuitpython playground express](https://www.adafruit.com/product/3333) to transmit IR signals to the trains.


Usage
-----

Copy the content of `playground_firmware/transmitter_routine.py` in a file named `code.py` on the circuit playground, 
and the firmware will load automatically.
A copy of adafruit library `adafruit_irremote.py` can be found in the directory `playground_firmware/lib`. 
For a more recent version refer to the official 
[adafruit circuitpython](https://docs.circuitpython.org/en/latest/docs/index.html) website.

The latest working Windows executable file for the server is available in `./dist`

If the executable is not an option, follow these steps to run the server from the command line:

_clone the repository_
```
git clone https://github.com/ultimodruido/myworld_remote.git
cd myworld_remote
```
_create and activate a python environment_
```
python.exe -m venv venv
venv\Scripts\activate.bat (on Windows)
source venv/bin/activate (on Linux or MacOS)
```
_install the requirements_
```
python.exe -m pip install -r requirements.txt
```
_now you are good to start_
```
python myworld.py -p 8000
```

Default port is 5000, with the `-p` parameter a different port can be set.

Configuration
-------------

Example of a starting configuration file can be found in `./src/myworld.conf_example`
Rename the file in `myworld.conf` and place it in the same folder as the executable.

It is not a mandatory step, the program will create its own configuration file.

Refer to the [official documentation](https://myworld-remote.readthedocs.io) on read the doc for further details

Limitation
--

Only frequencies __G__ and __H__ are usable with the system, because I have no train with other frequencies to decode.

If you want to help, scan your remote and open an issue with your data in. 
I will try to decode and include it into the software. Follow the instructions 
in the [official roadmap](https://myworld-remote.readthedocs.io/en/latest/roadmap.html) to see how do I need the input.

UI
--

This project contains only the server and the board firmware.
A simple web interface is available in the [myworld_webui](https://github.com/ultimodruido/myworld_webui) repository.

Alternatively, you can also build your own ;)
