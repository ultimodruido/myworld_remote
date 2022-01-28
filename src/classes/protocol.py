"""
Module: protocol
Contains the binary codes conversion for each command given by the MyWorld remote.

Each remote has 7 speed commands: STOP, 3 forward speed and 3 backward speed
SPEED_SIGNALS = ['STOP', 'F1', 'F2', 'F3', 'B1', 'B2', 'B3']

In addition there are emergency commands (SOS) linghts, horn and 2 sounds.
COMMAND_SIGNALS = ['SOS', 'LIGHT', 'SOUND1', 'HORN', 'SOUND2']

The IR protocol pulses used by Maerklin is as follow:
4000 -> incipit
bit 0 -> 500 + 500
bit 1 -> 500 + 1500

!!! CORRECT WRONG DESCRIPTION !!!
To recreate the STOP signal for protocol H (binary: 10000000111111),
the signal starts with a pulse 4000 long and then use the above conversion
to get the pulses length:
bit 1 -> 500 + 1500
7 times bit 0 -> 500 + 500
6 times bit 1 -> 500 + 1500

Result:
Signals STOP: [4000, 500, 1500, 500, 500, 500, 500, 500, 500,
    500, 500,500, 500, 500, 500, 500, 500, 500, 1500,
    500, 1500, 500,1500, 500, 1500, 500, 1500, 500, 1500]

the protocol dictionary returns the desired protocol dictionary:

protocol['H']['STOP'] returns '10000000111111' as a string

The emergency command is different for each protocol but recognized by every
vehicle, so we can say it is protocol independent.
"""

SPEED_SIGNALS = ['STOP', 'F1', 'F2', 'F3', 'B1', 'B2', 'B3', 'SOS']
FUNCTION_SIGNALS = ['NO_FN', 'LIGHT', 'SOUND1', 'HORN', 'SOUND2']


FREQ = {
    'G': 0,
    'H': 1,
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
