# This file is placed in the Public Domain.


"list of commands."


from nixt.run.run import Cfg


def ver(event):
    "list commands."
    event.reply(f"{Cfg.name.upper()} {Cfg.version}")