#!/usr/bin/python3
"""
Generate a tgz archive from the contents of AirBnB web_static
"""


import os
from datetime import datetime
from fabric.api import local

def do_pack():
    """
    Create a tar archive of the directory web_static
    """

    dt = datetime.now()
    file = f"versions/web_static_{dt.year}{dt.month}{dt.day}{dt.hour}{dt.minute}{dt.second}.tgz"

    if os.path.isdir("versions") is False:
        if local("mkdir versions").failed is True:
            return None
    if local(f"tar -cvzf {file} web_static").failed is True:
        return None
    return file
