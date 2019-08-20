#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """Creates archive from web_static directory"""
    local("mkdir -p versions")
    f = 'versions/web_static_{}.tgz'\
        .format(datetime.strftime(datetime.now(), "%Y%m%d%I%M%S"))
    s = 'tar -cvzf {} web_static'.format(f)
    r = local(s)
    if r.failed:
        return None
    return f
