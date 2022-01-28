from fastapi import APIRouter
"""
manage all endpoints related to configuration of the system 
Module: router - config
"""
from server_deps import rolling_stock, remote

router = APIRouter()


@router.get("/remote_status")
async def remote_status():
    return {"message": f"Remote status: {remote.ready}"}


@router.post("/register/remote/{port_name}")
async def register_remote(port_name: str):
    remote.configure(port_name)
    return {"message": "OK"}


@router.post("/register/train/{name}/{frequency}")
async def register_train(name: str, frequency: str):
    rolling_stock.add_train(name, frequency, remote.send)
    return {"message": "OK"}