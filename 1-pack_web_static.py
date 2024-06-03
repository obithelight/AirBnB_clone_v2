#!/usr/bin/python3
# Generate a tgz archive from the contents of AirBnB web_static

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Create a tar archive of the directory web_static
    """

    dt = datetime.now()
    file_name = (f"versions/web_static_{dt.year}{dt.month}{dt.day}"
                 f"{dt.hour}{dt.minute}{dt.second}.tgz")

    if not os.path.isdir("versions"):
        if local("mkdir versions").failed:
            return None
    if local(f"tar -cvzf {file_name} web_static").failed:
        return None
    return file_name
