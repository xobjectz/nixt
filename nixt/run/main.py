# This file is placed in the Public Domain.
#
# pylint: disable=W0718


"main"


import getpass
import readline
import sys
import time


from nixt.run.cli      import CLI
from nixt.run.commands import command, scan
from nixt.run.console  import Console
from nixt.run.errors   import errors, later
from nixt.run.event    import Event
from nixt.run.help     import __doc__ as helpstring
from nixt.run.parse    import parse
from nixt.run.persist  import skel
from nixt.run.run      import Cfg
from nixt.run.utils    import daemon, privileges, spl, wrap


import nixt.mod
import nixt.srv
import nixt.usr


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
        Cfg.user = getpass.getuser()
        daemon(Cfg.pidfile, "-v" in sys.argv)
        privileges(Cfg.user)
        init(nixt.srv, Cfg.mod)
        wait = True
    elif "c" in Cfg.opts:
        csl = Console()
        init(nixt.srv, Cfg.mod)
        init(nixt.usr, Cfg.mod)
        csl.start()
        wait = True
    scan(nixt.mod, Cfg.mod)
    scan(nixt.srv, Cfg.mod)
    scan(nixt.usr, Cfg.mod)
    if Cfg.otxt:
        cmnd(Cfg.otxt, print)
    if wait or "w" in Cfg.opts:
        while 1:
            time.sleep(1.0)


def __dir__():
    return (
        'cmnd',
        'init',
        'main',
        'wrapped'
    )
