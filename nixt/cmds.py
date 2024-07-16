# This file is placed in the Public Domain.
# pylint: disable=R0903


"commands"


import inspect


from .event  import ready
from .object import Object, add, fqn
from .parse  import parse


class Commands:

    "Commands"


def command(bot, evt):
    "check for and run a command."
    parse(evt)
    func = getattr(Commands, evt.cmd, None)
    if func and evt.txt:
        if "target" not in dir(func) or func.target in fqn(bot):
            func(evt)
            bot.show(evt)
    ready(evt)


def scan(mod) -> None:
    "scan module for commands."
    for key, cmd in inspect.getmembers(mod, inspect.isfunction):
        if key.startswith("cb"):
            continue
        if 'event' in cmd.__code__.co_varnames:
            add(Commands, cmd)


def __dir__():
    return (
        'Commands',
        'add',
        'command',
        'scan'
    )
