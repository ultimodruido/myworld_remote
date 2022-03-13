"""
Module: train
Provides a class Train that describes a Maerklin MyWorld toy
It stores the information about active protocol and speed setting.
"""
from dataclasses import dataclass, field

EXPORT_FIELDS = ['name', 'frequency', 'box']


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

    async def update(self, speed=None, command=None):
        """
        Update the status of the train. speed and other commands are kept separate,
        because the train stops if for example lights are toggled.
        So the speed needs to be tranferred again every time

        :param speed:
        :type port: str

        :param command:
        :type port: str
        """
        if speed:
            self.speed = speed
        # self.status(command, speed)
        await self.update_callback(self.frequency, self.speed, command)

    async def toggle_light(self):
        await self.update(command='LIGHT')

    async def play_sound(self, sound):
        if sound in ['SOUND1', 'SOUND2']:
            await self.update(command=sound)

    async def horn(self):
        await self.update(command='HORN')

    def set_name(self, name: str):
        self.name = name

    def set_frequency(self, frequency: str):
        self.frequency = frequency

    def set_box(self, box):
        self.box = box

    def get_dict_repr(self):
        """Returns a simplified dictionary suitable for JSON export"""
        return {key: value for key, value in self.__dict__.items() if key in EXPORT_FIELDS}
