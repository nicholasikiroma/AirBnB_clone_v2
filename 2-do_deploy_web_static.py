#!/usr/bin/python3
"""     Fabric script (based on the file 1-pack_web_static.py)
        that distributes an archive to your web servers,
        using the function do_deploy"""
from fabric.api import run, put, env, runs_once
from datetime import datetime
import os


env.hosts = ['18.204.15.114', '52.90.22.244']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


@runs_once
def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    dir_name = file_name.replace(".tgz", "")
    dir_path = "/data/web_static/releases/{}/".format(dir_name)
    status = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(dir_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, dir_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(dir_path, dir_path))
        run("rm -rf {}web_static".format(dir_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dir_path))
        print('New version Deployed Successfully!')
        status = True
    except Exception:
        status = False
    return status
