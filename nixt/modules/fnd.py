# This file is placed in the Public Domain.


"locate"


from ..event  import reply
from ..object import fmt
from ..disk   import find, long, skel, types


def fnd(event):
    "locate objects."
    skel()
    if not event.rest:
        res = sorted([x.split('.')[-1].lower() for x in types()])
        if res:
            reply(event, ",".join(res))
        return
    otype = long(event.args[0])
    nmr = 0
    for _fnm, obj in find(otype, event.gets):
        reply(event, f"{nmr} {fmt(obj)}")
        nmr += 1
    if not nmr:
        reply(event, "no result")
