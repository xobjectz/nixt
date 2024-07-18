# This file is placed in the Public Domain.
# pylint: disable=W0622


"runtime"


from ..cache  import Cache
from ..fleet  import Fleet
from ..object import all


cache = Cache()
fleet = Fleet()


def announce(txt):
    "announce on all bots."
    for _name, bot in all(fleet):
        if "announce" in dir(bot):
            bot.announce(txt)



def __dir__():
    return (
        'announce',
        'broker',
        'fleet'
    )
