# This file is placed in the Public Domain.


"list of commands"


from ..cmds   import Commands
from ..event  import reply
from ..object import keys


def cmd(event):
    "list commands."
    reply(event, ",".join(sorted([x for x in keys(Commands) if not x.startswith("__")])))
