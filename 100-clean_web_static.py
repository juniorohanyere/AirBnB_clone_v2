#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder of
an AirBnB Clone repo, using the function do_pack
distributes an archive to your web servers, using the function do_deploy
creates and distributes an archive to a web server, using the function deploy
"""

import os
from fabric.api import *
from datetime import datetime


env.hosts = ["54.237.56.212", "54.196.44.164"]
env.user = "ubuntu"


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


def do_deploy(archive_path):
    """distribute an archive to a web server

    Args:
        archive_path (str): the full path of the archive to distribute

    Return:
        return True on success
        return False otherwise
    """

    if not os.path.exists(archive_path):
        return False

    try:
        filename = archive_path[9:]
        dfile = "/data/web_static/releases/" + filename[:-4]
        filename = "/tmp/" + filename

        put(archive_path, "/tmp")

        run("sudo mkdir -p {}".format(dfile))
        run("sudo tar -xzf {} -C {}".format(filename, dfile))
        run("sudo rm {}".format(filename))
        run("sudo mv {}/web_static/* {}".format(dfile, dfile))
        run("sudo rm -rf {}/web_static".format(dfile))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(dfile))

        print("New version deployed!")

        return True

    except Exception:
        return False


def deploy():
    """creates and distributes an archive to a web server
    """

    archive_path = do_pack()

    return do_deploy(archive_path) if os.path.exits(archive_path) else False


def do_clean(number=0):
    """deletes out-of-date archives of static files.

    Args:
        number: number of archives to keep
    """

    archives = os.listdir('versions/')
    archives.sort(reverse=True)
    start = int(number)

    if not start:
        start += 1
    if start < len(archives):
        archives = archives[start:]
    else:
        archives = []

    for archive in archives:
        os.unlink('versions/{}'.format(archive))

    cmd_parts = [
        "rm -rf $(",
        "find /data/web_static/releases/ -maxdepth 1 -type d -iregex",
        " '/data/web_static/releases/web_static_.*'",
        " | sort -r | tr '\\n' ' ' | cut -d ' ' -f{}-)".format(start + 1)
    ]

    run(''.join(cmd_parts))
