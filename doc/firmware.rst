Circuit playground firmware
---------------------------

In the folder ``./playground_firmware`` are two scripts:

* decode.py
* transmitter_routine.py

just rename the one you want to load as ``code.py`` and copy it
in the circuit playground, the routine will start automatically.
For details refer to the official
`help page <https://learn.adafruit.com/adafruit-circuit-playground-express?view=all>`__
.
The library ``adafruit_irremote.py`` is required. A copy is available in the ``playground_firmware/lib`` directory.
.. data:: decode.py

This script is used to decode the signals from the remote.
An example of the output printed when pressing a button on the original remote  is::

    Received:  [3998, 493, 1515, 507, 490, 502, 496, 497, 491, 501, 498, 505, 493, 500, 498, 495, 493, 501, 1488, 533, 1514, 499, 1508, 512, 1516, 495, 1512, 511, 1518]
    Decoded: 0x 0x203f
    Decoded: b 10000000111111


.. data:: transmitter_routine.py

This script convert the received bis over serial link into pulses for the IR transmitter.
It blinks the red led when transmitting.
