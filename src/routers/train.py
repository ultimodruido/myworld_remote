"""
Module: router - trains
manage all endpoints related to train control
"""
from fastapi import APIRouter, Request, Path
from enum import Enum

from server_deps import rolling_stock, reply, Message
from server_lock import data_protection_lock
from server_exceptions import UnknownTrainError

from .params_docstring import param_doc

router = APIRouter()


@router.get("/train_list", response_model=Message)
async def train_list(request: Request):
    """
    Return the list of the known trains.

    Example::

        {
          "entry_point": "/train_list",
          "result": true,
          "data": {
            "train_list": [
                {
                    "name": "Airport Express",
                    "frequency": "H",
                    "box": "29307"
                },
                {
                    "name": "Vectron",
                    "frequency": "G",
                    "box": "29342"
                },
                {
                    "name": "InOui",
                    "frequency": "G",
                    "box": "29406"
                }
            ]
          }
        }
    """
    # what to do here? how to handle with events?
    return reply(request.url.path, True, train_list=rolling_stock.get_train_list())


class ModelSpeedValue(str, Enum):
    """Validation model for speed_value parameter"""
    STOP = "STOP"
    F1 = "F1"
    F2 = "F2"
    F3 = "F3"
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"

    def __str__(self):
        return self.value


@router.post("/train/{train_id}/speed/{speed_value}", response_model=Message)
async def set_train_speed(request: Request,
                          train_id: int = Path(..., description=param_doc['train_id']),
                          speed_value: ModelSpeedValue = Path(..., description=param_doc['speed_value'])
                          ):
    """
    Change speed of a train
    """
    async with data_protection_lock:
        try:
            train = rolling_stock.get_train_by_id(train_id)
            # store the speed as a string to comply with typehint
            train.update(speed=str(speed_value))
            return reply(request.url.path, True, train=train.get_dict_repr(full_export=True))
        except UnknownTrainError as e:
            return reply(request.url.path, False, error=e.message)


@router.post("/train/{train_id}/light", response_model=Message)
async def toggle_train_light(request: Request,
                             train_id: int = Path(..., description=param_doc['train_id'])
                             ):
    """
    Toggle the light of a train
    """
    async with data_protection_lock:
        try:
            train = rolling_stock.get_train_by_id(train_id)
            train.toggle_light()
            return reply(request.url.path, True, train=train.get_dict_repr(full_export=True))
        except UnknownTrainError as e:
            return reply(request.url.path, False, error=e.message)


@router.post("/train/{train_id}/horn", response_model=Message)
async def blow_train_horn(request: Request,
                          train_id: int = Path(..., description=param_doc['train_id'])
                          ):
    """
    Blow the horn of a train
    """
    async with data_protection_lock:
        try:
            train = rolling_stock.get_train_by_id(train_id)
            train.horn()
            return reply(request.url.path, True, train=train.get_dict_repr(full_export=True))
        except UnknownTrainError as e:
            return reply(request.url.path, False, error=e.message)


@router.post("/train/{train_id}/sound1", response_model=Message)
async def train_sound1(request: Request,
                       train_id: int = Path(..., description=param_doc['train_id'])
                       ):
    """
    Play sound 1
    """
    async with data_protection_lock:
        try:
            train = rolling_stock.get_train_by_id(train_id)
            train.play_sound('SOUND1')
            return reply(request.url.path, True, train=train.get_dict_repr(full_export=True))
        except UnknownTrainError as e:
            return reply(request.url.path, False, error=e.message)


@router.post("/train/{train_id}/sound2", response_model=Message)
async def train_sound2(request: Request,
                       train_id: int = Path(..., description=param_doc['train_id'])
                       ):
    """
    Play sound 2
    """
    async with data_protection_lock:
        try:
            train = rolling_stock.get_train_by_id(train_id)
            train.play_sound('SOUND2')
            return reply(request.url.path, True, train=train.get_dict_repr(full_export=True))
        except UnknownTrainError as e:
            return reply(request.url.path, False, error=e.message)
