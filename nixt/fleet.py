# This file is placed in the Public Domain.


"list of bots."


from .object import Object, values


rpr = object.__repr__


class Fleet(Object):

    "Fleet"


def announce(txt):
    "announce on all bots."
    for bot in all(Fleet):
        if "announce" in dir(bot):
            bot.announce(txt)


def __dir__():
    return (
        'Fleet',
        'announce'
    )
