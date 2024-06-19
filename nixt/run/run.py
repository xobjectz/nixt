# This file is placed in the Public Domain.


"runtime"


import os


from nixt.lib.config  import Config
from nixt.run.broker  import Broker
from nixt.run.persist import Persist


Cfg         = Config()
Cfg.dis     = ""
Cfg.mod     = "cmd,err,ini,mod,thr"
Cfg.opts    = ""
Cfg.name    = "nixt"
Cfg.version = "6"
Cfg.wdr     = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.moddir  = os.path.join(Cfg.wdr, "mods")
Cfg.pidfile = os.path.join(Cfg.wdr, f"{Cfg.name}.pid")


Persist.workdir = Cfg.wdr


broker = Broker()


def __dir__():
    return (
        'Cfg',
        'broker'
    )
