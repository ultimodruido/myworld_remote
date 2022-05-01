from dataclasses import dataclass, field
from typing import Optional, List

from .train import Train


class UnknownTrainError(Exception):
    message: str = "Train not found"


@dataclass
class RollingStock:
    """Collection of registered trains"""
    trains: List[Train] = field(default_factory=list)

    def __getitem__(self, item):
        """Make class indexable"""
        return self.trains[item]

    def add_train(self, name: str, frequency: str, box: str, update_callback: callable) -> Train:
        train = Train(name, frequency, box, update_callback)
        self.trains.append(train)
        return train

    def import_train_list(self, train_list: List[Train]) -> None:
        self.trains = train_list

    def get_train_by_id(self, train_id: int) -> Train:
        try:
            return self.trains[train_id]
        except IndexError:
            raise UnknownTrainError

    def get_train_list(self) -> List[Train]:
        # train_collection = {idx: train for idx, train in enumerate(self.trains)}
        train_collection = [train.get_dict_repr() for train in self.trains]
        return train_collection

    def remove_train(self, train_id: int) -> None:
        try:
            self.trains.pop(train_id)
        except IndexError:
            raise UnknownTrainError
