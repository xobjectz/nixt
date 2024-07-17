# This file is placed in the Public Domain.
# pylint: disable=R0902,R0903,W0212


"event"


import threading


from .dft    import Default
from .object import get


class Event(Default):

    "Event"


def ready(obj):
    "event is ready."
    if not get(obj, "_ready"):
        obj._ready = threading.Event()
    obj._ready.set()


def reply(obj, txt):
    "add text to the result"
    if not get(obj, "result"):
        obj.result = []
    obj.result.append(txt)


def wait(obj):
    "wait for event to be ready."
    if not get(obj, "result"):
        obj.result = []
    if not get(obj, "_ready"):
        obj._ready = threading.Event()
    obj._ready.wait()
    if get(obj, "_thr"):
        obj._thr.join()
    return obj.result


def __dir__():
    return (
        'Event',
        'ready',
        'reply',
        'wait'
    )
