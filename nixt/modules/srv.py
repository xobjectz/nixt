# This file is placed in the Public Domain.


"create service file."


import getpass
import sys


TITLE = "you have been nixt!"
PROG  = "nixt"

def srv(event):
    if event.args:
        global USER
        USER = event.args[0]
    else:
       USER  = getpass.getuser()
    TXT = f"""[Unit]
Description={TITLE}
Requires=network-online.target
After=network-online.target

[Service]
Type=simple
User={USER}
Group={USER}
WorkingDirectory=/home/{USER}/.{PROG}
ExecStart=/home/{USER}/.local/pipx/venvs/{PROG}/bin/{PROG}d
ExitType=cgroup
RemainAfterExit=yes

[Install]
WantedBy=default.target"""
    event.reply(TXT)
