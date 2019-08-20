#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack"""
import os
from fabric.api import *


env.hosts = ['34.73.218.30', '35.196.224.3']


def do_pack():
    """Creates archive from web_static directory"""
    local("mkdir -p versions")
    s = 'tar -cvzf versions/$(date +"web_static_%Y%m%d%I%M%S.tgz") web_static'
    r = local(s)
    if r.failed:
        return None
    else:
        return r


def do_deploy(archive_path):
    """Deploys an archive"""
    if not os.path.exists(archive_path):
        return False
    arch = archive_path.split('/')[1]
    name = arch.split('.')[0]
    r = put(archive_path, '/tmp/{}'.format(arch))
    if r.failed:
        return False
    r = run('mkdir -p /data/web_static/releases/{}'.format(name))
    if r.failed:
        return False
    r = run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(arch, name))
    if r.failed:
        return False
    r = run('rm /tmp/{}'.format(arch))
    if r.failed:
        return False
    s = 'mv /data/web_static/releases/{0}/web_static/*'
    s += ' /data/web_static/releases/{0}/'
    r = run(s.format(name))
    if r.failed:
        return False
    r = run('rm -rf /data/web_static/releases/{}/web_static'.format(name))
    if r.failed:
        return False
    r = run('rm -rf /data/web_static/current')
    if r.failed:
        return False
    r = run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(name))
    if r.failed:
        return False
    print('New version deployed!')
    return True
