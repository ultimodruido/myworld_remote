import asyncio
from time import strftime
from submodules.remote import Remote
from submodules.rolling_stock import RollingStock
from submodules.settings import load_settings, save_settings

remote = Remote()
rolling_stock = RollingStock()


async def main_loop():
    while True:
        print(f"running main_loop {strftime('%H:%M:%S')}")
        for train in rolling_stock:
            print(f"updating train: {train}")
            train.update()

        await asyncio.sleep(3)


async def startup():
    """Grab the uvicorn event loop to add the main_loop function as a task.
    Load previous settings if available"""

    loop = asyncio.get_event_loop()
    loop.create_task(main_loop())

    saved_config = load_settings()
    if saved_config:

        for train in saved_config['rolling_stock']:
            rolling_stock.add_train(**train, update_callback=remote.send)
        #await asyncio.sleep(2)
        remote.configure(saved_config['port'])


async def shutdown():
    save_settings(remote.port, rolling_stock.get_train_list())
    remote.close()
