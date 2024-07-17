# This file is placed in the Public Domain.
# pylint: disable=R0903,W0622


"list of bots."


from .object import Object, all


rpr = object.__repr__


class Fleet(Object):

    "Fleet"


def announce(txt):
    "announce on all bots."
    for bot in all(Fleet):
        print(bot, txt)
        if "announce" in dir(bot):
            bot.announce(txt)


def __dir__():
    return (
        'Fleet',
        'announce'
    )
