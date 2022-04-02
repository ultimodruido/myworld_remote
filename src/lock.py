import inspect
from asyncio import Lock


class LoggingLock(Lock):
    def acquire(self):
        print([f"--> Enter Lock from {inspect.stack()[2][3]}"])
        return super().acquire()

    def release(self):
        print([f"<-- Exit Lock from {inspect.stack()[2][3]}"])
        return super().release()


data_protection_lock = LoggingLock()
