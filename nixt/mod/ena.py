# This file is placed in the Public Domain.


"init"


from nixt.run.commands import scan
from nixt.run.main     import Cfg, mods
from nixt.run.thread   import launch
from nixt.run.utils    import getmods, spl


def ena(event):
    "enable a  module."
    if not event.args:
        event.reply("ini <name>")
        return
    if not mods:
        event.reply("modules are not available")
        return
    for name in spl(event.args[0]):
        for nme in spl(name):
            mod = getattr(mods, nme, None)
            scan(mod)
            if "init" in dir(mod):
                event.reply(f"launched {nme}")
                launch(mod.init)
