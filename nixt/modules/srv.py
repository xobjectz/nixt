# This file is placed in the Public Domain.


"create service file."


import getpass


TITLE = "you have been nixt!"
PROG  = "nixt"


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
WorkingDirectory=/home/{user}/.{PROG}
ExecStart=/home/{user}/.local/pipx/venvs/{PROG}/bin/{PROG}d
ExitType=cgroup
RemainAfterExit=yes

[Install]
WantedBy=default.target"""
    event.reply(txt)


srv.target = "cli"
