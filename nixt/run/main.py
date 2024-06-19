# This file is placed in the Public Domain.
#
#


"main"


import readline
import sys
import time


from nixt.run.cli      import CLI
from nixt.run.commands import command, scan
from nixt.run.console  import Console
from nixt.run.errors   import errors, later
from nixt.run.event    import Event
from nixt.run.parse    import parse
from nixt.run.persist  import skel
from nixt.run.run      import Cfg
from nixt.run.utils    import spl, wrap


import nixt.mod
import nixt.srv


def cmnd(txt, outer):
    "do a command using the provided output function."
    cli = CLI()
    cli.out = outer
    evn = Event()
    evn.txt = txt
    command(cli, evn)
    evn.wait()
    return evn


def init(pkg, modstr):
    "scan modules for commands and classes"
    mds = []
    for mod in spl(modstr):
        module = getattr(pkg, mod, None)
        if not module:
            continue
        try:
            module.init()
        except Exception as ex:
            later(ex)
    return mds


def wrapped():
    "wrap main."
    wrap(main)
    errors()


def main():
    "main"
    readline.redisplay()
    skel()
    parse(Cfg, " ".join(sys.argv[1:]))
    if "a" in Cfg.opts:
        modstr = sorted(dir(nixt.mod) + dir(nixt.srv))
        Cfg.mod = ",".join(modstr)
    if "h" in Cfg.opts:
        print(helpstring)
        return
    if "v" in Cfg.opts:
        dte = " ".join(time.ctime(time.time()).replace("  ", " ").split()[1:])
        print(f'{dte} {Cfg.name.upper()} {Cfg.opts.upper()} {Cfg.mod.upper()}'.replace("  ", " "))
    wait = False
    if "d" in Cfg.opts:
        wait = True
        Cfg.user = getpass.getuser()
        daemon(Cfg.pidfile, "-v" in sys.argv)
        privileges(Cfg.user)
    elif "c" in Cfg.opts:
        wait = True
        csl = Console()
        csl.out = print
        csl.start()
    scan(nixt.mod, Cfg.mod)
    scan(nixt.srv, Cfg.mod)
    if Cfg.otxt:
        cmnd(Cfg.otxt, print)
        #wait = False
    if wait or "w" in Cfg.opts:
        init(nixt.srv, Cfg.mod)
        while 1:
            time.sleep(1.0)


def __dir__():
    return (
        'Cfg',
        'cmnd',
        'init',
        'main',
        'wrapped'
    )
