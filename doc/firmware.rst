Circuit playground firmware
---------------------------

In the folder ``./playground_firmware`` there are two scripts:

* decode.py
* transmitter_routine.py

just rename them ``code.py`` and copy them in the circuit playground, the routine will start automatically

.. data:: decode.py

This script is used to decode the signals from the remote. An example of the output ::

    Received:  [4025, 498, 1531, 505, 1533, 494, 1524, 529, 1510, 502, 497, 503, 495, 512, 497, 504, 495, 504, 504, 494, 504, 504, 504, 497, 1532, 494, 1525, 512, 1526]
    Decoded: 0x3c07


.. data:: transmitter_routine.py

This script convert the received bis over serial link into pulses for the IR transmitter.
It blinks the red led when transmitting
