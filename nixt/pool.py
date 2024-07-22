# This file is placed in the Public Domain,


"threadpool"


import time


from .work import Worker


class Pool:

    "Pool of Threads."

    def __init__(self, nr):
        self.workers = []

    def work(self, func, *args, **kwargs):
        "put function to an available thread."
        if not self.workers:
            worker = Worker()
            worker.start()
            self.workers.append(worker)
        for worker in self.workers:
            if not worker.size() and not worker.running.is_set():
                worker.work(func, *args)
                break
