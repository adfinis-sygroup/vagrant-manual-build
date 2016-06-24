#!/usr/bin/env python
import sys
from os.path import exists


def make(condition, function):
    """Emulate make"""
    if not condition:
        function()


def driver(distro, arg):
    """Do the build"""
    print(arg)


def debian(distro, arg):
    """Debian and ubuntu build"""


def centos(distro, arg):
    """Centos build"""

[driver(sys.argv[1], arg) for arg in sys.argv[2:]]
