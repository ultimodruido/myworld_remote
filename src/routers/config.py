from fastapi import APIRouter, Request

"""
manage all endpoints related to the configuration of the system 
Module: router - config
"""
from server_deps import rolling_stock, remote, reply, Message
from server_lock import data_protection_lock

router = APIRouter()


######################
# Remote configuration
######################
@router.get("/remote_status", response_model=Message)
async def remote_status(request: Request):
    """
    Returns the configuration of the serial port:
    If status is True, the remote is active.
    The port key returns a string containing the port open for communication with the remote

    Example:

        {
          "entry_point": "/remote_status",
          "result": True,
          "data": {
            "port": "COM3",
            "status": True
          }
        }
    """
    return reply(request.url.path, True, port=remote.port, status=remote.ready)


@router.post("/register/remote/{port_name}", response_model=Message)
async def register_remote(port_name: str, request: Request):
    """
    Configure the serial port used used for the connection with the remote

    *port_name*: name of the serial port, example "COM3"

    The *result* key (bool) informs about the success of the operation

    Example:

        {
            "entry_point": "/register/remote/COM7",
            "result": false,
            "data": {}
        }
    """
    status = remote.configure(port_name)
    return reply(request.url.path, status)


######################
# Fleet configuration
######################
@router.post("/register/newtrain/{name}/{frequency}", response_model=Message)
async def register_train(name: str, frequency: str, request: Request):
    """
    Add a new train

    *name*: name to be used in the UIs to identify the train
    *frequency*: the frequency used to transmit commands to the train

    Example response:

        {
            "entry_point": "/register/newtrain/TGV/G",
            "result": true,
            "data": {}
        }
    """
    async with data_protection_lock:
        rolling_stock.add_train(name, frequency, remote.send)
    return reply(request.url.path, True)


@router.post("/register/train/{train_id}/name/{name}", response_model=Message)
async def set_train_name(train_id: str, name: str, request: Request):
    """
    Rename a registered train

    *train_id*: id number of the train as obtained from the '/train_list' command
    *name*: name to be used in the UIs to identify the train

    Example response:

        {
            "entry_point": "/register/train/1/name/TGV",
            "result": true,
            "data": {}
        }
    """
    result = False
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.set_name(name)
            result = True
    return reply(request.url.path, result)


@router.post("/register/train/{train_id}/frequency/{frequency}", response_model=Message)
async def set_train_frequency(train_id: str, frequency: str, request: Request):
    """
    Change frequency of a registered train

    *train_id*: id number of the train as obtained from the '/train_list' command
    *frequency*: the frequency used to transmit commands to the train

    Example response:

        {
            "entry_point": "/register/train/1/frequency/H",
            "result": true,
            "data": {}
        }
    """
    result = False
    async with data_protection_lock:
        train = rolling_stock.get_train_by_id(train_id)
        if train:
            train.set_frequency(frequency)
            result = True
    return reply(request.url.path, result)


@router.post("/register/train/{train_id}/box/{box_number}", response_model=Message)
async def set_train_box(train_id: str, box_number: str, request: Request):
    """
    Add a box number to a registered train

    *train_id*: id number of the train as obtained from the '/train_list' command
    *box_number*: the number on the box the train. It can be used for rendering purposes from the UI

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
            train.set_box(box_number)
            result = True
    return reply(request.url.path, result)


@router.post("/remove/train/{train_id}", response_model=Message)
async def remove_train(train_id: str, request: Request):
    """
    Remove a registered train

    *train_id*: id number of the train as obtained from the '/train_list' command

    Example response:

        {
            "entry_point": "/register/train/1",
            "result": true,
            "data": {}
        }
    """
    async with data_protection_lock:
        result = rolling_stock.remove_train(train_id)
    return reply(request.url.path, result)
