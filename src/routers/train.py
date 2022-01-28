"""
Module: router - trains
manage all endpoints related to train control
"""
from fastapi import APIRouter
from server_deps import rolling_stock

router = APIRouter()


@router.get("/train_list")
async def train_list():
    # what to do here? how to handle with events?
    print(rolling_stock.get_train_list())
    return rolling_stock.get_train_list()


@router.post("/train/{train_id}/light")
async def toggle_train_light(train_id: int):
    train = rolling_stock.get_train_by_id(train_id)
    if train:
        train.toggle_light()


@router.post("/train/{train_id}/speed/{speed_value}")
async def set_train_speed(train_id: int, speed_value: str):
    train = rolling_stock.get_train_by_id(train_id)
    if train:
        train.update(speed=speed_value)
    return {"message": "OK"}
