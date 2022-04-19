Roadmap
-------
At the moment the API is fairly complete for a real time control of the trains.

The first step will be to expand the protocol to include other frequencies.

.. IMPORTANT ::
    Please use the *decode.py* code as explained in the **Circuit playground firmware** section to decode
    other frequencies and post them in the issue section.

Please fill a table like the following with the frequency you want to submit.
In addition the signal for the emergency button is also necessary. Thanks for the help.


.. list-table:: Example of all command combinations
   :widths: 25 25 25 25 25 25
   :header-rows: 1

   * - Frequency (H)
     - No function
     - Light
     - Horn
     - Sound 1
     - Sound 2

   * - STOP
     - 1 000 000  0 111 111
     - 1 000 100  0 111 011
     - 1 000 001  0 111 110
     - 1 000 010  0 111 101
     - 1 000 011  0 111 100

   * - Forward 1
     - 1 001 000  0 110 111
     - 1 001 100  0 110 011
     - 1 001 001  0 110 110
     - 1 001 010  0 110 101
     - 1 001 011  0 110 100

   * - Forward 2
     - ???
     - ???
     - ???
     - ???
     - ???

   * - Forward 3
     - ???
     - ???
     - ???
     - ???
     - ???

   * - Backward 1
     - ???
     - ???
     - ???
     - ???
     - ???
   * - Backward 2
     - ???
     - ???
     - ???
     - ???
     - ???

   * - Backward 3
     - ???
     - ???
     - ???
     - ???
     - ???

At last please post one full command as reported by the circuit playground.
This will be helpful to decode the pulses length::

    Received:  [3998, 493, 1515, 507, 490, 502, 496, 497, 491, 501, 498, 505, 493, 500, 498, 495, 493, 501, 1488, 533, 1514, 499, 1508, 512, 1516, 495, 1512, 511, 1518]
    Decoded: 0x 0x203f
    Decoded: b 10000000111111


Additional ideas (but no concrete plan) are:

* develop an identification solution based on the RFid technology
* map track sections and (eventually) control turnouts