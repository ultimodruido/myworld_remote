"""
Module: emergency
Provides a 'emergency class' to stop all fleet in case of problems
"""
from fastapi import APIRouter, Request

from server_deps import Message, reply
from server_deps import remote, lock
from submodules.protocol import FREQ


router = APIRouter()


@router.get("/sos", response_model=Message)
async def train_sos(request: Request):
    """
    Send SOS signal to all trains and lock the transmission.
    """
    await lock(request.app).acquire()
    for frequency in FREQ:
        remote(request.app).send(frequency, 'SOS', 'NO_FN')
    return reply(request.url.path, True)


@router.get("/sos_release", response_model=Message)
async def train_sos_release(request: Request):
    """
    Release the SOS signal.
    """
    lock(request.app).release()
    return reply(request.url.path, True)
