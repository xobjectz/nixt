# This file is placed in the Public Domain.


"uptime"


import time


from ..event import reply
from ..utils import laps


STARTTIME = time.time()


def upt(event):
    "show uptime."
    reply(event, laps(time.time() - STARTTIME))
