# This file is placed in the Public Domain.
# pylint: disable=R0903


"todo list"


import time


from ..object import Object
from ..disk   import find, sync
from ..event  import reply
from ..utils  import fntime, laps


class NoDate(Exception):

    "no matching date"


class Todo(Object):

    "Todo"

    def __init__(self):
        Object.__init__(self)
        self.txt = ''


def dne(event):
    "flag todo as done."
    if not event.args:
        reply(event, "dne <txt>")
        return
    selector = {'txt': event.args[0]}
    nmr = 0
    for fnm, obj in find('todo', selector):
        nmr += 1
        obj.__deleted__ = True
        sync(obj, fnm)
        reply(event, 'ok')
        break
    if not nmr:
        reply(event, "nothing todo")


def tdo(event):
    "add todo."
    if not event.rest:
        nmr = 0
        for fnm, obj in find('todo'):
            lap = laps(time.time()-fntime(fnm))
            reply(event, f'{nmr} {obj.txt} {lap}')
            nmr += 1
        if not nmr:
            reply(event, "no todo")
        return
    obj = Todo()
    obj.txt = event.rest
    sync(obj)
    reply(event, 'ok')
