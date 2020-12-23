#!/usr/bin/python3
from fabric.api import *
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy
env.hosts = ['35.231.13.133', '35.196.88.5']
env.user = "ubuntu"


def deploy():
    """Fabric script that creates and distributes an archive to web servers.
    """
    try:
        archive_path = do_pack()
        if archive_path is None:
            return False
        return do_deploy(archive_path)
    except Exception as e:
        return False
