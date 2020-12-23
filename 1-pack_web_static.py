#!/usr/bin/python3
from fabric.api import *


def do_pack():
    """Fabric script that generates a .tgz archive from the
    contents of the web_static folder of your AirBnB Clone repo,
    using the function do_pack.
    """
    dest = "versions/web_static_$(date '+%Y%m%d%H%M%S').tgz"
    local("mkdir -p versions")
    local("tar -czvf {} web_static/".format(dest))
    archive_path = local("ls -t versions/ | head -1",
                         capture=True)
    if archive_path is None or archive_path == "":
        return None
    else:
        archive_path = "versions/" + archive_path
        return archive_path
