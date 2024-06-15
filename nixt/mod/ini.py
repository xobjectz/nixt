# This file is placed in the Public Domain.


"init"


from nixt.run.thread import launch


try:
    import mods
except ModuleNotFoundError:
    mods = None


def ini(event):
    if not event.args:
        event.reply("ini <name>")
        return
    for name in event.args:
        mod = getattr(mods, name)
        if "init" in dir(mod):
            launch(mod.init)
 