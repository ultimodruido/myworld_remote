import inspect
from asyncio import Lock


class LoggingLock(Lock):
    """Extension of the asyncio.Lock class that prints the calling function tha acquires & releases the Lock"""
    def acquire(self):
        print(f"-->> Enter Lock from {inspect.stack()[2][3]}")
        return super().acquire()

    def release(self):
        print(f"<<-- Exit Lock from {inspect.stack()[2][3]}")
        return super().release()



