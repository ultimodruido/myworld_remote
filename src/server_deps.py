import asyncio

from time import strftime
from pydantic import BaseModel
from fastapi import FastAPI

from server_lock import LoggingLock
from submodules.remote import Remote
from submodules.rolling_stock import RollingStock
from submodules.settings import load_settings, save_settings


# helper functions
def lock(app: FastAPI) -> LoggingLock:
    """Return the instance of the lock in the server"""
    return app.state.data_protection_lock


def rolling_stock(app: FastAPI) -> RollingStock:
    """Return the instance of the rolling_stock in the server"""
    return app.state.rolling_stock


def remote(app: FastAPI) -> Remote:
    """Return the instance of the remote in the server"""
    return app.state.remote


########################
# Main loop for updating status transmission
########################
async def main_loop(app: FastAPI) -> None:
    """Maerklin MyWorld trains are configured to automatically shutdown if no command is sent for a longer period.
    With a simple infinite loop that transmits the train status every few seconds we ensure that every train is
    running as desired.
    """
    while True:
        # get the lock to avoid concurrent writing on train values
        async with lock(app):
            print(f"[I] Server: running main_loop {strftime('%H:%M:%S')}")
            for train in rolling_stock(app):
                print(f"[I] Server: updating train: {train}")
                train.update()

        await asyncio.sleep(3)


########################
# Start & Stop events handlers
########################
async def startup(app: FastAPI) -> None:
    """Grab the uvicorn event loop to add the main_loop function as a task.
    Load previous settings if available"""

    # store state variables
    app.state.remote = Remote()
    app.state.rolling_stock = RollingStock()
    app.state.data_protection_lock = LoggingLock()

    # add task to event loop with
    loop = asyncio.get_event_loop()
    loop.create_task(main_loop(app))

    saved_config = load_settings()
    if saved_config:

        for train in saved_config['rolling_stock']:
            rolling_stock(app).add_train(**train, update_callback=remote(app).send)

        remote(app).configure(saved_config['port'])


async def shutdown(app: FastAPI) -> None:
    """Store settings to file, and properly close the serial communication."""
    save_settings(remote(app).port, rolling_stock(app).get_train_list())
    remote(app).close()


########################
# Communication messages
########################
class Message(BaseModel):
    """Creates the data structure transmitted in the reply.
    Has 3 keys:
     - entry_point -> API address requested
     - result -> bool value to inform about the outcome of the request
     - data -> additional data to be transmitted"""
    entry_point: str
    result: bool
    data: dict


def reply(entry_point: str, result: bool, **kwargs) -> Message:
    """Support function to instantiate the Message reply"""
    return Message(entry_point=entry_point, result=result, data=kwargs)
