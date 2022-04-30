"""
Module: router - trains
manage all endpoints related to train control
"""
from fastapi import APIRouter, Request, Path

from server_deps import rolling_stock, reply, Message
from server_lock import data_protection_lock

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


@router.post("/train/{train_id}/speed/{speed_value}", response_model=Message)
async def set_train_speed(request: Request,
                          train_id: int = Path(..., description=param_doc['train_id']),
                          speed_value: str = Path(..., description=param_doc['speed_value'])
                          ):
    """
    Change speed of a train
    """
    result = False
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.update(speed=speed_value)
            result = True
    return reply(request.url.path, result)


@router.post("/train/{train_id}/light", response_model=Message)
async def toggle_train_light(request: Request,
                             train_id: int = Path(..., description=param_doc['train_id'])
                             ):
    """
    Toggle the light of a train
    """
    result = False
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.toggle_light()
            result = True
    return reply(request.url.path, result)


@router.post("/train/{train_id}/horn", response_model=Message)
async def blow_train_horn(request: Request,
                          train_id: int = Path(..., description=param_doc['train_id'])
                          ):
    """
    Blow the horn of a train
    """
    result = False
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.horn()
            result = True
    return reply(request.url.path, result)


@router.post("/train/{train_id}/sound1", response_model=Message)
async def train_sound1(request: Request,
                       train_id: int = Path(..., description=param_doc['train_id'])
                       ):
    """
    Play sound 1
    """
    result = False
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.play_sound('SOUND1')
            result = True
    return reply(request.url.path, result)


@router.post("/train/{train_id}/sound2", response_model=Message)
async def train_sound2(request: Request,
                       train_id: int = Path(..., description=param_doc['train_id'])
                       ):
    """
    Play sound 2
    """
    result = False
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.play_sound('SOUND2')
            result = True
    return reply(request.url.path, result)
