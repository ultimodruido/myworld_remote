from fastapi import APIRouter

"""
manage all endpoints related to configuration of the system 
Module: router - config
"""
from server_deps import rolling_stock, remote

router = APIRouter()


######################
# Remote configuration
######################
@router.get("/remote_status")
async def remote_status():
    """.. data:: route: GET /remote_status

    returns a dictionary containing serial port status (bool) and name (str)

    Example::

        {
          "ready": True,
          "port": "COM3"
        }
    """
    return {"ready": remote.ready,
            "port": remote.port}


@router.post("/register/remote/{port_name}")
async def register_remote(port_name: str):
    """.. data:: route: POST /register/remote/{port_name}

    configure the serial port used used for the connection with the remote

    :param port_name: name of the serial port, example "COM3"

    returns a dictionary containing serial port status (bool) and name (str)

    Example::

        {
          "ready": True,
          "port": "COM3"
        }
    """
    remote.configure(port_name)
    return {"ready": remote.ready,
            "port": remote.port}


######################
# Fleet configuration
######################
@router.post("/register/newtrain/{name}/{frequency}")
async def register_train(name: str, frequency: str):
    rolling_stock.add_train(name, frequency, remote.send)
    return {"message": True}


@router.post("/register/train/{train_id}/name/{name}")
async def register_train(train_id: str, name: str):
    train = rolling_stock.get_train_by_id(train_id)
    if train:
        train.set_name(name)
        return {"message": True}
    else:
        return {"message": False}


@router.post("/register/train/{train_id}/frequency/{frequency}")
async def register_train(train_id: str, frequency: str):
    train = rolling_stock.get_train_by_id(train_id)
    if train:
        train.set_frequency(frequency)
        return {"message": True}
    else:
        return {"message": False}


@router.post("/register/train/{train_id}/box/{box_number}")
async def register_train(train_id: str, box_number: str):
    train = rolling_stock.get_train_by_id(train_id)
    if train:
        train.set_box(box_number)
        return {"message": True}
    else:
        return {"message": False}


@router.post("/remove/train/{train_id}")
async def register_train(train_id: str):
    message = rolling_stock.remove_train(train_id)
    return {"message": message}
