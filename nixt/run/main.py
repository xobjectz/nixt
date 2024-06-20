# This file is placed in the Public Domain.
#
# pylint: disable=W0212,W0718


"main"


import getpass
import os
import pathlib
import pwd
import readline
import sys
import termios
import time


from nixt.run.cli      import CLI
from nixt.run.commands import Commands, command
from nixt.run.console  import Console
from nixt.run.errors   import errors, later
from nixt.run.event    import Event
from nixt.run.help     import __doc__ as helpstring
from nixt.run.parse    import parse
from nixt.run.persist  import skel
from nixt.run.run      import Cfg
from nixt.run.utils    import spl


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


def daemon(pidfile, verbose=False):
    "switch to background."
    pid = os.fork()
    if pid != 0:
        os._exit(0)
    os.setsid()
    pid2 = os.fork()
    if pid2 != 0:
        os._exit(0)
    if not verbose:
        with open('/dev/null', 'r', encoding="utf-8") as sis:
            os.dup2(sis.fileno(), sys.stdin.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as sos:
            os.dup2(sos.fileno(), sys.stdout.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as ses:
            os.dup2(ses.fileno(), sys.stderr.fileno())
    os.umask(0)
    os.chdir("/")
    if os.path.exists(pidfile):
        os.unlink(pidfile)
    path = pathlib.Path(pidfile)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(pidfile, "w", encoding="utf-8") as fds:
        fds.write(str(os.getpid()))


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


def inited(modstr):
    "init services."
    init(nixt.srv, modstr)
    init(nixt.usr, modstr)


def scan(pkg, modstr, disable=None):
    "scan modules for commands and classes"
    mds = []
    for modname in spl(modstr):
        if disable and modname in spl(disable):
            continue
        module = getattr(pkg, modname, None)
        if not module:
            continue
        Commands.scan(module)
    return mds


def scanned(modstr, disable=None):
    "scan modules."
    scan(nixt.mod, modstr, disable)
    scan(nixt.srv, modstr, disable)
    scan(nixt.usr, modstr, disable)


def modnames():
    "list all modules."
    return dir(nixt.mod) + dir(nixt.srv) + dir(nixt.usr)


def privileges(username):
    "drop privileges."
    pwnam = pwd.getpwnam(username)
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)


def wrap(func):
    "reset terminal."
    old3 = None
    try:
        old3 = termios.tcgetattr(sys.stdin.fileno())
    except termios.error:
        pass
    try:
        func()
    except (KeyboardInterrupt, EOFError):
        print("")
    finally:
        if old3:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old3)


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
        modstr = ",".join(modnames())
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
        inited(Cfg.mod)
        wait = True
    elif "c" in Cfg.opts:
        csl = Console()
        inited(Cfg.mod)
        csl.start()
        wait = True
    scanned(Cfg.mod, Cfg.sets.dis)
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
