#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the "web_static" folder of my
AirBnB Clone repo.

"""
from fabric.api import run


def do_pack():
    """Generate .tgz archive."""
    run('echo "test"')
