Configuration
-------------
The program stores a configuration file during the shutdown phase.
It contains:

* the serial port used to communicate with the playground express
* the list of configured trains

As of release 1.0 each train has 3 settings:

* name: transmitted to the UI for identification purposes
* frequency: used frequency to communicate with the train
* box (optional): the number of the box can used from the UIs to render an image of the product

Example of a starting configuration file can be found in ``./src/myworld.conf_example`` ::

        {
          "port": "COM3",
          "rolling_stock": [
            {
              "name": "Airport Express",
              "frequency": "H",
              "box": "29307"
            },
            {
              "name": "Vectron",
              "frequency": "G",
              "box": "29342"
            },
            {
              "name": "InOui",
              "frequency": "G",
              "box": "29406"
            }
          ]
        }

