#!/usr/bin/python3
"""
Fabric script that generates deploys an archive to the web
servers
"""
from fabric.api import run, put, env
from datetime import datetime
from os.path import isfile, basename

env.hosts = ['18.204.15.114', '52.90.22.244']


def do_deploy(archive_path):
    """Deploys archive to web servers"""
    if not isfile(archive_path):
        return False
    file_name = basename(archive_path)
    try:
        no_ext = file_name.split(".")[0]
        put(archive_path, "/tmp/")
        path = "/data/web_static/releases/{}".format(no_ext)
        run("mkdir -p {}".format(path))
        run("tar xzf /tmp/{} -C {}".format(file_name, path))
        run("rm /tmp/{}".format(file_name))
        run("mv {0}/web_static/* {0}/".format(path))
        run("rm -rf {0}/web_static/".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path))
        return True
    except Exception:
        return False
