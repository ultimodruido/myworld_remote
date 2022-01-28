import asyncio

from classes.remote import Remote
from classes.rolling_stock import RollingStock
from classes.settings import load_settings, save_settings

remote = Remote()
rolling_stock = RollingStock()


async def main_loop():
    while True:
        for train in rolling_stock:
            print(f"updating train: {train}")
            train.update()
        print("running main_loop")
        await asyncio.sleep(3)


async def startup():
    """Grab the uvicorn event loop to add the main_loop function as a task.
    Load previous settings if available"""

    loop = asyncio.get_event_loop()
    loop.create_task(main_loop())

    saved_config = load_settings()
    if saved_config:
        remote.configure(saved_config['port'])
        for train in saved_config['rolling_stock']:
            rolling_stock.add_train(**train, update_callback=remote.send)


async def shutdown():
    remote.close()
    save_settings(remote.port, rolling_stock.get_train_list())