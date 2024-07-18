# This file is placed in the Public Domain.


"console"


from ..event  import Event, wait
from ..object import register


from .cli import CLI
from .    import fleet


class Console(CLI):

    "Console"

    def __init__(self, outer, inner, prompt="> "):
        CLI.__init__(self, outer)
        self.inner = inner
        self.prompt = prompt
        register(fleet, self)

    def announce(self, txt):
        "echo text"

    def callback(self, evt):
        "wait for callback."
        CLI.callback(self, evt)
        wait(evt)

    def poll(self):
        "poll console and create event."
        evt = Event()
        evt.txt = self.inner(self.prompt)
        evt.type = "command"
        return evt


def __dir__():
    return (
        'Console',
    )
