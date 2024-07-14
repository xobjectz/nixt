# This file is placed in the Public Domain.
# pylint: disable=R0902,R0903


"configuration"


import getpass
import os


from .dft  import Default
from .disk import Persist


class Config(Default):

    "Config"


Cfg         = Config()
Cfg.name    = "nixt"
Cfg.user    = getpass.getuser()
Cfg.wdr     = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.pidfile = os.path.join(Cfg.wdr, f"{Cfg.name}.pid")


Persist.workdir = Cfg.wdr


def __dir__():
    return (
        'Cfg',
        'Config',
    )
