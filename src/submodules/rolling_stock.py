from dataclasses import dataclass, field
from typing import Optional, List

from .train import Train


@dataclass
class RollingStock:
    trains: List[Train] = field(default_factory=list)

    def __getitem__(self, item):
        """Make class indexable"""
        return self.trains[item]

    def add_train(self, name: str, frequency: str, box: str, update_callback: callable) -> Train:
        train = Train(name, frequency, box, update_callback)
        self.trains.append(train)
        return train

    def import_train_list(self, train_list: List[Train]):
        self.trains = train_list

    def get_train_by_id(self, train_id: int) -> Optional[Train]:
        try:
            return self.trains[train_id]
        except IndexError:
            return None

    def get_train_list(self) -> list:
        # train_collection = {idx: train for idx, train in enumerate(self.trains)}
        train_collection = [train.get_dict_repr() for train in self.trains]
        return train_collection

    def remove_train(self, train_id) -> bool:
        try:
            self.trains.pop(train_id)
        except IndexError:
            return False
        return True
