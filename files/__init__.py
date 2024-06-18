# This file is placed in the Public Domain.
#
#


"modules"


import importlib
import os


from nixt.lib.default import Default
from nixt.lib.object  import keys


mods = Default()
name = __file__.split(os.sep)[-2]


for fnm in os.listdir(os.path.dirname(__file__)):
    if fnm.startswith("__"):
        continue
    if fnm.endswith("~"):
        continue
    nme = fnm[:-3]
    mname = f"{name}.{nme}"
    mod = importlib.import_module(mname, name)
    setattr(mods, nme, mod)


def __dir__():
    return sorted(keys(mods))
