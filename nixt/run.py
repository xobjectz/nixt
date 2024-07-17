# This file is placed in the Public Domain.


"runtime"


from .cache import Cache
from .fleet import Fleet

cache = Cache()
fleet = Fleet()


def announce(txt):
    "announce on all bots."
    print(dir(fleet))
    for bot in all(fleet):
        print(dir(bot))
        if "announce" in dir(bot):
            bot.announce(txt)



def __dir__():
    return (
        'announce',
        'broker',
        'fleet'
    )
