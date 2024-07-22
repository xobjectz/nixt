# This file is placed in the Public Domain.


"Worker"


import queue
import threading
import time


from .errors import later
from .thread import named


rpr = object.__repr__


class Worker(threading.Thread):

    "Worker Thread"

    def __init__(self):
        super().__init__(None, self.run, named(self), (), {}, daemon=True)
        self.current  = ""
        self.workq    = queue.Queue()
        self.running  = threading.Event()
        self.throttle = 0.01

    def __iter__(self):
        return self

    def __next__(self):
        yield from dir(self)

    def size(self):
        return self.workq.qsize()

    def work(self, func, *args):
        self.workq.put_nowait((func, args))

    def run(self):
        "loop to run this thread's payload."
        while 1:
            self.running.clear()
            func, args = self.workq.get()
            self.running.set()
            time.sleep(self.throttle)
            self.current = named(func)
            try:
                self._result = func(*args)
            except Exception as ex:
                later(ex)
                try:
                    args[1].ready()
                except IndexError:
                    pass


def __dir__():
    return (
        'Worker',
    )
