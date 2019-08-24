#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py) that deletes out-of-date archives, using the function do_clean
"""

import os
from datetime import datetime
from fabric.api import *

env.hosts = ['35.196.224.3', '34.73.218.30']

def do_clean(number=0):
    """
    deletes out-of-date archives, using the function do_clean
    """
    if number < 2:
        number = 1
    number += 1
    number = str(number)
    with lcd("versions"):
        local("ls -1t | grep web_static_.*\.tgz | tail -n +" +
              number + " | xargs -I {} rm -- {}")
    with cd("/data/web_static/releases"):
        run("ls -1t | grep web_static_ | tail -n +" +
            number + " | xargs -I {} rm -rf -- {}")
