"""
Module: router - trains
manage all endpoints related to train control
"""
from fastapi import APIRouter
from server_deps import rolling_stock, reply
from server_lock import data_protection_lock

router = APIRouter()


@router.get("/train_list")
async def train_list():
    # what to do here? how to handle with events?
    return reply(True, train_list=rolling_stock.get_train_list())


@router.post("/train/{train_id}/speed/{speed_value}")
async def set_train_speed(train_id: int, speed_value: str):
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.update(speed=speed_value)
    return reply(True)


@router.post("/train/{train_id}/light")
async def toggle_train_light(train_id: int):
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.toggle_light()
    return reply(True)


@router.post("/train/{train_id}/horn")
async def toggle_train_light(train_id: int):
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.horn()
    return reply(True)


@router.post("/train/{train_id}/sound1")
async def toggle_train_light(train_id: int):
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.play_sound('SOUND1')
    return reply(True)


@router.post("/train/{train_id}/sound2")
async def toggle_train_light(train_id: int):
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.play_sound('SOUND2')
    return reply(True)
