"""
Module: remote
Provides a class Remote that handle the serial connection with
the circuit express playground.
"""
from typing import Optional
from serial import Serial

from .protocol import FREQ, SPEED, FUNCTION, SPEED_SIGNALS, FUNCTION_SIGNALS


def _inverted_bit_char(c):
    """converts '1' into '0' & viceversa"""
    if c == '1':
        return '0'
    elif c == '0':
        return '1'
    else:
        return ''


class Remote:
    """
        Class used to handle the communication with the playground express and use it as a remote

        Create a simple button and move the train with protocol 'H' and toggle the lights::

            r = Remote('COM7')
            r.send('H', 'F1', 'LIGHT')

        :param port: the port name of the simulated serial port on the playground express
        :type port: str

    """

    def __init__(self, port: str = ''):
        self.serial: Optional[Serial] = None
        self.port: str = port
        self.ready: bool = False
        if self.port != '':
            self.configure(port)
        # self.lock: bool = False

    def configure(self, port: str) -> bool:
        """
        Change the port at which we are connecting

        :param port: port name, example 'COM3'
        :type port: str
        """

        try:
            self.serial = Serial(port, 115200)  # open serial port
            self.ready = True
            self.port = port
            print(f"[i] Remote: configured serial port {port}")
        except Exception as e:
            print(e)
            self.port = ''
            self.ready = False
            print(f"[E] Remote: impossible to configure serial port {port}")
        return self.ready

    def send(self, frequency: str, speed: str, command: Optional[str]) -> None:
        """
        Converts the instruction into binary code and transmits it.
        A double code will always be transmitted:
         [command] + [speed]
        For example if a toggle light command is sent, the actual speed
        status need to be transmitted again otherwise the train will stop.

        A transfer will start only if:
        . the serial port was opened correctly
        . [command] is one of the protocol.COMMAND_SIGNALS instructions
        . [speed] is one of the protocol.SPEED_SIGNALS instructions

        :param frequency: protocol frequency used for the conversion, example 'H'
        :type frequency: str

        :param speed: speed code you want to transmit
        :type speed: str

        :param command: port name, example 'COM3'
        :type command: str
        """
        # preliminary controls
        start_transfer = True
        if self.ready is False:
            start_transfer = False
        if command is None:
            command = 'NO_FN'
        if command not in FUNCTION_SIGNALS:
            start_transfer = False
        if speed not in SPEED_SIGNALS:
            start_transfer = False
        if start_transfer:
            self._send(frequency, speed, command)
        else:
            print("[E] Remote: transmission skipped, not ready")
    def _send(self, frequency: str, speed: str, function: str) -> None:

        try:
            pre_code = f"{FREQ[frequency]}{SPEED[speed]}{FUNCTION[function]}"
        except KeyError as e:
            # if the precode cannot be generated, probably unknown frequencies are being requested.
            # return and skip the transmission
            print("[E] Remote: error while building the code, transmission skipped")
            return
        # the second part of the code is inverted
        post_code = ''.join(_inverted_bit_char(c) for c in pre_code)

        cmd_code = f"C{pre_code}{post_code}!\n\r"

        # print(f"f: {frequency} - s: {speed} - fz: {function}")
        # print(f"playgroung code: {cmd_code}")
        print(f"[I] Remote: sending over serial: {frequency} - s: {speed} - fz: {function} ~~ code: {cmd_code[:-2]}")
        self.serial.write(cmd_code.encode())

    def close(self) -> None:
        if self.ready:
            self.serial.close()
        else:
            print("[E] Remote: transmission skipped: not ready")
