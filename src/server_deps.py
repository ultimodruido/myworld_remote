import asyncio

from time import strftime

from submodules.remote import Remote
from submodules.rolling_stock import RollingStock
from submodules.settings import load_settings, save_settings
from server_lock import data_protection_lock

remote = Remote()
rolling_stock = RollingStock()


########################
# Main loop for updating status transmission
########################
async def main_loop():
    """Maerklin MyWorld trains are configured to automatically shutdown if no command is sent for a longer period.
    With a simple infinite loop that transmits the train status every few seconds we ensure that every train is
    running as desired.
    """
    while True:
        # get the lock to avoid concurrent writing on train values
        async with data_protection_lock:
            print(f"running main_loop {strftime('%H:%M:%S')}")
            for train in rolling_stock:
                print(f"updating train: {train}")
                train.update()

        await asyncio.sleep(5)


########################
# Start & Stop events handlers
########################
async def startup():
    """Grab the uvicorn event loop to add the main_loop function as a task.
    Load previous settings if available"""

    loop = asyncio.get_event_loop()
    loop.create_task(main_loop())

    saved_config = load_settings()
    if saved_config:

        for train in saved_config['rolling_stock']:
            rolling_stock.add_train(**train, update_callback=remote.send)

        remote.configure(saved_config['port'])


async def shutdown():
    """Store settings to file, and properly close the serial communication."""
    save_settings(remote.port, rolling_stock.get_train_list())
    remote.close()


########################
# Communication messages
########################
def reply(value: bool, **kwargs) -> dict:
    kwargs["reply"] = value
    return kwargs
