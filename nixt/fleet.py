# This file is placed in the Public Domain.


"list of bots."


from .object import Object, values


rpr = object.__repr__


class Fleet(Object):

    "Fleet"

    bots = []

    def all(self):
        "return all objects."
        return self.bots

    def announce(self, txt):
        "announce on all bots."
        for bot in self.bots:
            if "announce" in dir(bot):
                bot.announce(txt)

    def get(self, orig):
        "return bot."
        for x in self.bots:
            if rpr(x) == orig:
                return x

    def register(self, obj):
        "add bot."
        self.bots.append(obj)


def __dir__():
    return (
        'Fleet',
    )
