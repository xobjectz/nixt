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
    name = f"mods.{fnm[:-3]}"
    mod = importlib.import_module(name)
    setattr(mods, name, mod)


def __dir__():
    return sorted(keys(mods))
