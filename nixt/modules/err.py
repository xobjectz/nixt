# This file is placed in the Public Domain.
# pylint: disable=W0622


"deferred exception handling"


from ..defer import all, format
from ..event import reply


def err(event):
    "show errors."
    nmr = 0
    for exc in all():
        txt = format(exc)
        for line in txt.split():
            reply(event, line)
        nmr += 1
    if not nmr:
        reply(event, "no errors")
        return
    reply(event, f"found {nmr} errors.")
