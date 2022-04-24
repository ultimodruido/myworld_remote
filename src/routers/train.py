"""
Module: router - trains
manage all endpoints related to train control
"""
from enum import Enum

from fastapi import APIRouter, Request
from server_deps import rolling_stock, reply, Message
from server_lock import data_protection_lock

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
async def set_train_speed(train_id: int, speed_value: str, request: Request):
    """
    Change speed of a train

    *train_id*: id number of the train as obtained from the '/train_list' command
    *speed_value*: speed code

    Example response:

        {
            "entry_point": "/register/train/1/box/22456",
            "result": true,
            "data": {}
        }
    """
    result = False
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.update(speed=speed_value)
            result = True
    return reply(request.url.path, result)


@router.post("/train/{train_id}/light", response_model=Message)
async def toggle_train_light(train_id: int, request: Request):
    """
    Toggle the light of a train

    *train_id*: id number of the train as obtained from the '/train_list' command

    Example response:

        {
            "entry_point": "/register/train/1/light",
            "result": true,
            "data": {}
        }
    """
    result = False
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.toggle_light()
            result = True
    return reply(request.url.path, result)


@router.post("/train/{train_id}/horn", response_model=Message)
async def blow_train_horn(train_id: int, request: Request):
    """
    Blow the horn of a train

    *train_id*: id number of the train as obtained from the '/train_list' command

    Example response:

        {
            "entry_point": "/register/train/1/horn",
            "result": true,
            "data": {}
        }
    """
    result = False
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.horn()
            result = True
    return reply(request.url.path, result)


@router.post("/train/{train_id}/sound1", response_model=Message)
async def train_sound1(train_id: int, request: Request):
    """
    Play sound 1

    *train_id*: id number of the train as obtained from the '/train_list' command

    Example response:

        {
            "entry_point": "/register/train/1/sound1",
            "result": true,
            "data": {}
        }
    """
    result = False
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.play_sound('SOUND1')
            result = True
    return reply(request.url.path, result)


@router.post("/train/{train_id}/sound2", response_model=Message)
async def train_sound2(train_id: int, request: Request):
    """
    Play sound 2

    *train_id*: id number of the train as obtained from the '/train_list' command

    Example response:

        {
            "entry_point": "/register/train/1/sound2",
            "result": true,
            "data": {}
        }
    """
    result = False
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.play_sound('SOUND2')
            result = True
    return reply(request.url.path, result)
