# This file is placed in the Public Domain.


"console"


import readline
import sys
import termios
import time


from .cli   import CLI
from .disk  import skel
from .event import Event
from .log   import debug
from .main  import Cfg, enable, init, scan
from .parse import parse
from .run   import fleet
from .utils import forever, modnames


from . import modules, user


class Console(CLI):

    "Console"

    def __init__(self, outer, inner, prompt="> "):
        CLI.__init__(self, outer)
        self.inner = inner
        self.prompt = prompt
        fleet.register(self)

    def announce(self, txt):
        "echo text"
        self.raw(txt)

    def callback(self, evt):
        "wait for callback."
        CLI.callback(self, evt)
        evt.wait()

    def poll(self):
        "poll console and create event."
        evt = Event()
        evt.txt = self.inner(self.prompt)
        evt.type = "command"
        return evt


def wrap(func):
    "restore console."
    old2 = None
    try:
        old2 = termios.tcgetattr(sys.stdin.fileno())
    except termios.error:
        pass
    try:
        func()
    except (KeyboardInterrupt, EOFError):
        sys.stdout.write("\n")
        sys.stdout.flush()
    finally:
        if old2:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old2)



def console():
    "start console"
    parse(Cfg, " ".join(sys.argv[1:]))
    skel()
    if "a" in Cfg.opts:
        Cfg.mod = ",".join(modnames(modules, user))
    if "v" in Cfg.opts:
        enable(print)
        dte = " ".join(time.ctime(time.time()).replace("  ", " ").split()[1:])
        debug(f'{dte} {Cfg.name.upper()} {Cfg.opts.upper()} {Cfg.mod.upper()}')
    scan(Cfg.mod, modules, user)
    if "i" in Cfg.opts:
        thrs = init(Cfg.mod, modules, user)
        for thr in thrs:
            thr.join()
    csl = Console(print, input)
    csl.start()
    forever()


def main():
    "wrap main."
    readline.redisplay()
    wrap(console)


if __name__ == "__main__":
    main()
    