# This file is placed in the Public Domain.


"modules"


import importlib
import os


from nixt.lib.default import Default
from nixt.lib.object  import keys


mods = Default()


for fnm in os.listdir(os.path.dirname(__file__)):
    if fnm.startswith("__"):
        continue
    if fnm.endswith("~"):
        continue
    name = fnm[:-3]
    mname = f"mods.{name}"
    mod = importlib.import_module(mname, "mods")
    setattr(mods, name, mod)


def __dir__():
    return sorted(keys(mods))
