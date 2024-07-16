# This file is placed in the Public Domain.
# pylint: disable=R0902


"event"


import threading


from .dft import Default


class Event(Default):

    "Event"


def ready(obj):
    "event is ready."
    if not obj._ready:
        obj._ready = threading.Event()
    obj._ready.set()


def reply(obj, txt):
    "add text to the result"
    if not obj.result:
        obj.result = []
    obj.result.append(txt)


def wait(obj):
    "wait for event to be ready."
    if not obj.result:
        obj.result = []
    if not obj._ready:
        obj._ready = threading.Event()
    obj._ready.wait()
    if obj._thr:
        obj._thr.join()
    return obj.result


def __dir__():
    return (
        'Event',
        'ready',
        'reply',
        'wait'
    )
