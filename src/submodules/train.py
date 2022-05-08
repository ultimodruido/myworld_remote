"""
Module: train
Provides a class Train that describes a Maerklin MyWorld toy
It stores the information about active protocol and speed setting.
"""
from dataclasses import dataclass, field
from typing import TypeVar

from submodules import protocol

EXPORT_FIELDS = ['name', 'frequency', 'box']
TrainDict = TypeVar('TrainDict')


@dataclass
class Train:
    """
        Class used to handle the communication with the playground express and use it as a remote

        Create a simple button and move the train with protocol 'H' and toggle the lights::

            r = Remote()
            r.send('H', 'F1', 'LIGHT')

        :param port: the port name of the simulated serial port on the playground express
        :type port: str
    """
    name: str
    frequency: str
    box: str
    update_callback: callable = field(default=None, repr=False)
    speed: str = field(default="STOP", init=False)

    def update(self, speed=None, command=None) -> None:
        """
        Update the status of the train. speed and other commands are kept separate,
        because the train stops if for example lights are toggled.
        So the speed needs to be transferred again every time

        :param speed:
        :type speed: str

        :param command:
        :type command: str
        """
        if speed:
            self.speed = speed
        # self.status(command, speed)
        self.update_callback(self.frequency, self.speed, command)

    def toggle_light(self) -> None:
        self.update(command='LIGHT')

    def play_sound(self, sound) -> None:
        if sound in ['SOUND1', 'SOUND2']:
            self.update(command=sound)

    def horn(self) -> None:
        self.update(command='HORN')

    def set_name(self, name: str) -> None:
        self.name = name

    def set_frequency(self, frequency: str) -> None:
        if type(frequency) is not str:
            raise TypeError
        if frequency not in protocol.FREQ:
            raise protocol.UnknownFrequency
        self.frequency = frequency

    def set_box(self, box: str) -> None:
        self.box = box

    def get_dict_repr(self) -> TrainDict:
        """Returns a simplified dictionary suitable for JSON export"""
        return {key: value for key, value in self.__dict__.items() if key in EXPORT_FIELDS}
