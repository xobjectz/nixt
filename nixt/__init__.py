# This file is placed in the Public Domain.


"package"


from . import mod, usr


def getmod(name):
    mods = getattr(mod, name, None)
    if not mods:
        mods = getattr(usr, name, None)
    return mods
