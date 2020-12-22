#!/usr/bin/python3
from fabric.api import *
env.hosts = ['35.231.13.133', '35.196.88.5']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Fabric script that distributes an archive to web servers."""
    try:
        test = put(archive_path, "/tmp/", use_sudo=True)
        lista = archive_path.split('/')
        folder = lista[-1][:lista[-1].find(".")]
        dest = "/data/web_static/releases/" + folder
        sudo("mkdir -p {}".format(dest))
        sudo("tar -xzf {} -C {}".format(test[0], dest))
        sudo("rm {}".format(test[0]))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s /data/web_static/releases/{} /data/web_static/current".
             format(folder))
        return True
    except Exception as e:
        return False
