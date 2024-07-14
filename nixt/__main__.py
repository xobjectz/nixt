# This file is placed in the Public Domain.
# pylint: disable=C0413,W0212,E0401


"main"


import sys


from .main  import Cfg, cmnd, enable, scan
from .parse import parse
from .utils import modnames


from . import modules
from . import user


def main():
    "main"
    parse(Cfg, " ".join(sys.argv[1:]))
    enable(print)
    if "h" in Cfg.opts:
        cmnd("hlp", print)
        return
    Cfg.dis = Cfg.sets.dis
    Cfg.mod = ",".join(modnames(modules, user))
    scan(Cfg.mod, modules, user)
    cmnd(Cfg.otxt, print)


if __name__ == "__main__":
    main()
