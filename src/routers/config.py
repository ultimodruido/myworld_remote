from fastapi import APIRouter

"""
manage all endpoints related to the configuration of the system 
Module: router - config
"""
from server_deps import rolling_stock, remote, reply
from lock import data_protection_lock

router = APIRouter()


######################
# Remote configuration
######################
@router.get("/remote_status")
async def remote_status():
    """
    returns a dictionary containing serial port status (bool) and name (str)

    Example::

        {
          "reply": True,
          "port": "COM3"
        }
    """
    return reply(remote.ready, port=remote.port)


@router.post("/register/remote/{port_name}")
async def register_remote(port_name: str):
    """
    configure the serial port used used for the connection with the remote

    :param port_name: name of the serial port, example "COM3"

    returns a dictionary containing serial port status (bool) and name (str)

    Example::

        {
          "reply": True,
        }
    """
    status = remote.configure(port_name)
    return reply(status)


######################
# Fleet configuration
######################
@router.post("/register/newtrain/{name}/{frequency}")
async def register_train(name: str, frequency: str):
    async with data_protection_lock:
        rolling_stock.add_train(name, frequency, remote.send)
    return reply(True)


@router.post("/register/train/{train_id}/name/{name}")
async def register_train(train_id: str, name: str):
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.set_name(name)
            return reply(True)
        else:
            return reply(False)


@router.post("/register/train/{train_id}/frequency/{frequency}")
async def register_train(train_id: str, frequency: str):
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.set_frequency(frequency)
            return reply(True)
        else:
            return reply(False)


@router.post("/register/train/{train_id}/box/{box_number}")
async def register_train(train_id: str, box_number: str):
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.set_box(box_number)
            return reply(True)
        else:
            return reply(False)


@router.post("/remove/train/{train_id}")
async def register_train(train_id: str):
    async with data_protection_lock:
        result = rolling_stock.remove_train(train_id)
    return reply(result)
