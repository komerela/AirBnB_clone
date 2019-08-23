#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
import os
from datetime import datetime
from fabric.api import *

env.hosts = ['35.196.224.3', '34.73.218.30']


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


def do_deploy(archive_path):
    """Deploys an archive"""
    if not os.path.exists(archive_path):
        return False
    arch = archive_path.split('/')[1]
    name = arch.split('.')[0]
    r = put(archive_path, '/tmp/{}'.format(arch))
    if r.failed:
        return False
    r = sudo('mkdir -p /data/web_static/releases/{}'.format(name))
    if r.failed:
        return False
    r = sudo('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
             .format(arch, name))
    if r.failed:
        return False
    r = sudo('rm /tmp/{}'.format(arch))
    if r.failed:
        return False
    s = 'mv /data/web_static/releases/{0}/web_static/*'
    s += ' /data/web_static/releases/{0}/'
    r = sudo(s.format(name))
    if r.failed:
        return False
    r = sudo('rm -rf /data/web_static/releases/{}/web_static'.format(name))
    if r.failed:
        return False
    r = sudo('rm -rf /data/web_static/current')
    if r.failed:
        return False
    r = sudo('ln -s /data/web_static/releases/{}/ /data/web_static/current'
             .format(name))
    if r.failed:
        return False
    print('New version deployed!')
    return True


def deploy():
    """ Fabric
    """
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
