#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static folder of
an AirBnB Clone repo, using the function do_pack
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Return:
        returns the archive path if the archive has been correctly generated
        return None otherwise
    """

    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))

    return filename if result.succeeded else None
