#!/usr/bin/python3
"""Generates a `.tgz` archive using fabric"""
from fabric.api import local
from datetime import datetime


def do_pack():
    '''generates a .tgz archive from the contents of the web_static folder'''
    local("mkdir -p versions")
    archive_path = ("versions/web_static_{}.tgz"
                    .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(archive_path))

    if result.failed:
        return None
    return archive_path
