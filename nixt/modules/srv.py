# This file is placed in the Public Domain.


"create service file."


import getpass
import os


NAME = __file__.split(os.sep)[-3]
TITLE = "you have been {NAME}t!"


def srv(event):
    "create service file (pipx)."
    if event.args:
        user = event.args[0]
    else:
        user  = getpass.getuser()
    txt = f"""[Unit]
Description={TITLE}
Requires=network-online.target
After=network-online.target

[Service]
Type=simple
User={user}
Group={user}
WorkingDirectory=/home/{user}/.{NAME}
ExecStart=/home/{user}/.local/pipx/venvs/{NAME}/bin/{NAME}d
ExitType=cgroup
RemainAfterExit=yes

[Install]
WantedBy=default.target"""
    event.reply(txt)


srv.target = "cli"
