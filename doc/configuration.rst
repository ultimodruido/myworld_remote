Configuration
-------------
The program stores a configuration file during the shutdown phase.
It contains:

* the serial port used to communicate with the playground express
* the list of configured trains

As of release 0.1 each train has 3 settings:

* name:
* frequency: used frequency to communicate with the train
* box (optional): the number of the box can used from the UIs to render an image of the product

Example of configuration file::

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