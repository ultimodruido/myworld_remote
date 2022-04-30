"""
manage all endpoints related to the configuration of the system
Module: router - config
"""
from fastapi import APIRouter, Request, Path

from server_deps import rolling_stock, remote, reply, Message
from server_lock import data_protection_lock
from submodules.rolling_stock import UnknownTrainError

from .params_docstring import param_doc


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
async def register_remote(request: Request,
                          port_name: str = Path(..., description=param_doc['port_name'])
                          ):
    """
    Configure the serial port used used for the connection with the remote

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
@router.post("/register/newtrain/{train_name}/{frequency}", response_model=Message)
async def register_train(request: Request,
                         train_name: int = Path(..., description=param_doc['train_name']),
                         frequency: str = Path(..., description=param_doc['frequency'])
                         ):
    """
    Add a new train
    """
    async with data_protection_lock:
        rolling_stock.add_train(train_name, frequency, remote.send)
    return reply(request.url.path, True)


@router.post("/register/train/{train_id}/name/{train_name}", response_model=Message)
async def set_train_name(request: Request,
                         train_id: int = Path(..., description=param_doc['train_id']),
                         train_name: str = Path(..., description=param_doc['train_name'])
                         ):
    """
    Rename a registered train
    """
    async with data_protection_lock:
        try:
            train = rolling_stock.get_train_by_id(train_id)
            train.set_name(train_name)
            return reply(request.url.path, True)
        except UnknownTrainError as e:
            return reply(request.url.path, False, error=e.message)


@router.post("/register/train/{train_id}/frequency/{frequency}", response_model=Message)
async def set_train_frequency(request: Request,
                              train_id: int = Path(..., description=param_doc['train_id']),
                              frequency: str = Path(..., description=param_doc['frequency'])
                              ):
    """
    Change communication frequency of a registered train
    """
    async with data_protection_lock:
        try:
            train = rolling_stock.get_train_by_id(train_id)
            train.set_frequency(frequency)
            return reply(request.url.path, True)
        except UnknownTrainError as e:
            return reply(request.url.path, False, error=e.message)


@router.post("/register/train/{train_id}/box/{box_number}", response_model=Message)
async def set_train_box(request: Request,
                        train_id: int = Path(..., description=param_doc['train_id']),
                        box_number: str = Path(..., description=param_doc['box_number'])
                        ):
    """
    Add a box number to a registered train
    """
    async with data_protection_lock:
        try:
            train = rolling_stock.get_train_by_id(train_id)
            train.set_box(box_number)
            return reply(request.url.path, True)
        except UnknownTrainError as e:
            return reply(request.url.path, False, error=e.message)


@router.post("/remove/train/{train_id}", response_model=Message)
async def remove_train(request: Request,
                       train_id: int = Path(..., description=param_doc['train_id'])):
    """
    Remove a registered train
    """
    async with data_protection_lock:
        try:
            rolling_stock.remove_train(train_id)
            return reply(request.url.path, True)
        except UnknownTrainError as e:
            return reply(request.url.path, False, error=e.message)
