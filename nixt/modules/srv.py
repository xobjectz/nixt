#!/usr/bin/env python3


import getpass
import sys


USER  = getpass.getuser()
TITLE = "you have been nixt!"
PROG  = "nixt"


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
RemainAfterExit=yes

[Install]
WantedBy=default.target"""


def srv(event):
    event.reply(TXT)
