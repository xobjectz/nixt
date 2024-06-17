# This file is placed in the Public Domain.


"runtime"


import os
import sys


from nixt.run.commands import command, scan
from nixt.lib.config   import Config
from nixt.run.broker   import Broker
from nixt.run.event    import Event
from nixt.run.handler  import CLI
from nixt.run.persist  import Persist, skel
from nixt.run.utils    import parse, wrap


Cfg         = Config()
Cfg.dis     = ""
Cfg.mod     = "cmd,err,fnd,log,mod,tdo,thr,tmr"
Cfg.opts    = ""
Cfg.name    = "nixt"
Cfg.version = "5"
Cfg.wdr     = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.moddir  = os.path.join(Cfg.wdr, "mods")
Cfg.pidfile = os.path.join(Cfg.wdr, f"{Cfg.name}.pid")


Persist.workdir = Cfg.wdr


import nixt.mod as modules


if os.path.exists(Cfg.moddir):
    sys.path.insert(0, Cfg.moddir)
    import mods
else:
    mods = None


broker = Broker()


def cmnd(txt, outer):
    "do a command using the provided output function."
    cli = CLI()
    cli.out = outer
    evn = Event()
    evn.txt = txt
    command(cli, evn)
    evn.wait()
    return evn


def wrapped():
    "wrap main."
    wrap(main)


def main():
    "main"
    Cfg.mod = ",".join(dir(modules))
    skel()
    parse(Cfg, " ".join(sys.argv[1:]))
    Cfg.mod += "," + ",".join(dir(mods))
    if "v" in Cfg.opts:
        dte = " ".join(time.ctime(time.time()).replace("  ", " ").split()[1:])
        print(f'{dte} {Cfg.name.upper()} {Cfg.opts.upper()} {Cfg.mod.upper()}'.replace("  ", " "))
    if "d" in Cfg.opts:
        Cfg.mod  = ",".join(dir(modules))
        Cfg.user = getpass.getuser()
        daemon(Cfg.pidfile, "-v" in sys.argv)
        privileges(Cfg.user)
        scan(modules, Cfg.mod)
        cmnd(Cfg.otxt, print)
        while 1:
            time.sleep(1.0)
        return
    scan(modules, Cfg.mod)
    scan(mods, Cfg.mod)
    if "c" in Cfg.opts:
        csl = Console()
        csl.out = print
        csl.start()
        cmnd(Cfg.otxt, print)
        while 1:
            time.sleep(1.0)
    elif Cfg.otxt:
        cmnd(Cfg.otxt, print)


def __dir__():
    return (
        'Cfg',
        'broker',
        'cmnd',
        'main',
        'wrapped'
    )
