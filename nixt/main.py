# This file is placed in the Public Domain.
# pylint: disable=W0718


"main"


import getpass
import os


from .cfg    import Config
from .cli    import CLI
from .cmds   import command
from .defer  import Errors
from .disk   import Persist
from .event  import Event
from .launch import launch
from .log    import Logging
from .utils  import skip, spl


from .cmds import scan as scancmd
from .disk import scan as scancls


Cfg         = Config()
Cfg.mod     = "cmd,err,mod,thr"
Cfg.name    = __file__.split(os.sep)[-2]
Cfg.user    = getpass.getuser()
Cfg.wdr     = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.pidfile = os.path.join(Cfg.wdr, f"{Cfg.name}.pid")


Persist.workdir = Cfg.wdr


def cmnd(txt, outer):
    "do a command using the provided output function."
    if not txt:
        return None
    cli = CLI(outer)
    evn = Event()
    evn.txt = txt
    command(cli, evn)
    evn.wait()
    return evn


def enable(outer):
    "enable printing."
    CLI.out = Errors.out = Logging.out = outer


def init(modstr, *pkgs, disable=None):
    "scan modules for commands and classes"
    thrs = []
    for mod in spl(modstr):
        if disable and mod in spl(disable):
            continue
        for pkg in pkgs:
            modi = getattr(pkg, mod, None)
            if not modi:
                continue
            if "init" not in dir(modi):
                continue
            thrs.append(launch(modi.init))
            break
    return thrs


def scan(modstr, *pkgs, disable=""):
    "scan modules for commands and classes"
    mds = []
    for modname in spl(modstr):
        if skip(modname, disable):
            continue
        for pkg in pkgs:
            module = getattr(pkg, modname, None)
            if not module:
                continue
            scancmd(module)
            scancls(module)
    return mds


def __dir__():
    return (
        'Cfg',
        'cmnd',
        'enable',
        'init',
        'scan'
    )
