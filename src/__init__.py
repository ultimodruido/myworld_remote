"""
Maerklin MyWorld universal remote
=================================

Control all your Maerlin `MyWorld`_ trains from a centralized interface.

The software requires a `circuitpython playground express`_ to transmit IR signals to the trains.

The software consists of multiple components:

* Firmware to be downloaded on the playground express.
* Web framework API (based on `FastAPI`_) to receive inputs from multiple UIs.

.. note::
    A UI is not included. If you are looking for a UI, check for example `MyWorld UI`_

.. warning::
    The software can at the moment replicate only frequencies G, H, U, V, W and X.
    See the *Protocol* section for details.

.. _circuitpython playground express: https://www.adafruit.com/product/3333
.. _MyWorld: https://www.maerklin.de/de/lp/2020/willkommen-bei-my-world
.. _FastAPI: https://fastapi.tiangolo.com
.. _MyWorld UI: https://github.com/ultimodruido/myworld_webui
"""