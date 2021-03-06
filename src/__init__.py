"""
Maerklin MyWorld universal remote
=================================

Control all your Maerlin `MyWorld`_ trains from a single interface.

The software uses a `circuitpython playground express`_ to transmit IR signals to the trains.

The system is made of multiple elements:

* Firmware to be downloaded on the playground express.
* Web framework API (based on `FastAPI`_) to receive inputs from multiple UIs.

.. note::
    A UI is not included.

.. warning::
    The software can at the moment replicate only frequencies G and H. See the *Protocol* section for details.

.. _circuitpython playground express: https://www.adafruit.com/product/3333
.. _MyWorld: https://www.maerklin.de/de/lp/2020/willkommen-bei-my-world
.. _FastAPI: https://fastapi.tiangolo.com
"""