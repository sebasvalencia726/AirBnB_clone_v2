#!/usr/bin/python3
from fabric.api import *
env.hosts = ['35.231.13.133', '35.196.88.5']
env.user = "ubuntu"
env.key_filename = '~/.ssh/holberton'


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


def do_deploy(archive_path):
    """Fabric script that distributes an archive to web servers."""
    try:
        test = put(archive_path, "/tmp/")
        lista = archive_path.split('/')
        folder = lista[-1][:lista[-1].find(".")]
        dest = "/data/web_static/releases/" + folder
        run("mkdir -p {}".format(dest))
        run("tar -xzf {} -C {}".format(test[0], dest))
        run("rm {}".format(test[0]))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(folder, folder))
        run("rm -rf /data/web_static/releases/{}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current".
            format(folder))
        return True
    except Exception:
        return False


def deploy():
    """Fabric script that creates and distributes an archive to web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    toReturn = do_deploy(archive_path)
    return toReturn
