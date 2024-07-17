# This file is placed in the Public Domain.


"deferred exception handling"


from ..defer import Errors
from ..event import reply


def err(event):
    "show errors."
    nmr = 0
    for exc in Errors.errors:
        txt = Errors.format(exc)
        for line in txt.split():
            reply(event, line)
        nmr += 1
    if not nmr:
        reply(event, "no errors")
        return
    reply(event, f"found {nmr} errors.")
