"""
Protocol
--------

Contains the binary codes conversion for each command given by the MyWorld remote.

Each remote has 8 speed commands: STOP, 3 forward speed and 3 backward speed and
emergency stop which seems to be recognized by frequency pairs (ex. G & H). ::

    SPEED_SIGNALS = ['STOP', 'F1', 'F2', 'F3', 'B1', 'B2', 'B3', 'SOS']

In addition, there are functionalities like lights, horn and 2 sounds.
An *empty* value is also needed to properly describe all possibilities. ::

    FUNCTION_SIGNALS = ['NO_FN', 'LIGHT', 'SOUND1', 'HORN', 'SOUND2']


The IR protocol pulses length used by Maerklin are as follow::

    incipit -> 4000
    bit 0 -> 500 + 500
    bit 1 -> 500 + 1500

.. WARNING ::
    At the moment only frequencies G, H, U and V have been decoded.

A signal is between 14 and 18 bits long, each signal is divided into 2 sequences of equal length.
The second sequence is just like the first one, but with each bit inverted.
In the following code snippets the meaning of each bit will be explained.

.. data:: 1 to 5 bits: frequency selector, obtained by the FREQ dictionary

::

FREQ = {
    'G': '0',
    'H': '1',
    'U': '00110',
    'V': '00111',
}

.. data:: 3 bits: speed selector, obtained by the SPEED dictionary

::

        SPEED = {
            'STOP': '000',
            'F1': '001',
            'F2': '010',
            'F3': '011',
            'B1': '100',
            'B2': '101',
            'B3': '110',
            'SOS': '111',
        }

.. data:: 3 bits: function selector, obtained by the FUNCTION dictionary

::

    FUNCTION = {
        'NO_FN': '000',
        'HORN': '001',
        'SOUND1': '010',
        'SOUND2': '011',
        'LIGHT': '100',
    }

To recreate the STOP signal for protocol H without function::

    code = f"{FREQ['H']}{SPEED['STOP']}{FUNCTION['NO_FN']}"
    code = 1 000 000

we need to add the second sequence with inverted bits ::

    neg_code = 0 111 111

and the result is ::

    transmission_code = 1 000 000   0 111 111

the signal starts with a pulse 4000 long and then uses the conversion explained
at the top of the page to get the pulses' length:

* bit 1 -> 500 + 1500
* 7 times bit 0 -> 500 + 500
* 6 times bit 1 -> 500 + 1500

Result::

    Signals STOP: [4000, 500, 1500, 500, 500, 500, 500, 500, 500,
        500, 500,500, 500, 500, 500, 500, 500, 500, 1500,
        500, 1500, 500,1500, 500, 1500, 500, 1500, 500, 1500]

Refer to the playground firmware to convert the bits into pulses.
"""


###############
# Constants
###############
SPEED_SIGNALS = ['STOP', 'F1', 'F2', 'F3', 'B1', 'B2', 'B3', 'SOS']
FUNCTION_SIGNALS = ['NO_FN', 'LIGHT', 'SOUND1', 'HORN', 'SOUND2']


FREQ = {
    'G': '0',
    'H': '1',
    'U': '00110',
    'V': '00111',
}

SPEED = {
    'STOP': '000',
    'F1': '001',
    'F2': '010',
    'F3': '011',
    'B1': '100',
    'B2': '101',
    'B3': '110',
    'SOS': '111',
}

FUNCTION = {
    'NO_FN': '000',
    'HORN': '001',
    'SOUND1': '010',
    'SOUND2': '011',
    'LIGHT': '100',
}

