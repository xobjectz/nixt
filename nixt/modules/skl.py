# This file is placed in the Public Domain.


"skel the working directory."


import getpass
import os


from ..disk  import skel
from ..utils import privileges


def skl(event):
    "create service file (pipx)."
    privileges(getpass.getuser())
    skel()
