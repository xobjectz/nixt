# This file is placed in the Public Domain.
# pylint: disable=C0413,W0212,E0401


"main"


import os
import sys


sys.path.insert(0, os.getcwd())


from nixt.cfg   import Config
from nixt.defer import errors
from nixt.disk  import Persist
from nixt.main  import cmnd, enable, scan
from nixt.parse import parse
from nixt.utils import modnames


from nixt import modules
from nixt import user


Cfg         = Config()
Cfg.dis     = ""
Cfg.mod     = "mod,cmd,err,thr"
Cfg.name    = "nixt"
Cfg.opts    = ""
Cfg.wdr     = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.pidfile = os.path.join(Cfg.wdr, f"{Cfg.name}.pid")


Persist.workdir = Cfg.wdr


def main():
    "main"
    enable(print)
    parse(Cfg, " ".join(sys.argv[1:]))
    if "h" in Cfg.opts:
        return cmnd("hlp", print)
    Cfg.dis = Cfg.sets.dis
    Cfg.mod = ",".join(modnames(modules, user))
    scan(Cfg.mod, modules, user)
    return cmnd(Cfg.otxt, print)


if __name__ == "__main__":
    main()
    errors()
