#!/usr/bin/env python
import sys
import os
import contextlib
from os.path import exists

redhat_based = set([
    'centos6',
    'centos7',
])
debian_based = set([
    'jessie',
    'wheezy',
    'trusty',
    'vivid',
    'xenial',
])


@contextlib.contextmanager
def chdir(directory):
    cwd = os.getcwd()
    os.chdir(directory)
    yield
    os.chdir(cwd)


def check_system(*args, **kwargs):
    """Return exception if system fails"""
    ret = os.system(*args, **kwargs)
    if ret != 0:
        raise OSError(
            "Command %s failed with %d" % (args[0], ret)
        )
    return ret


def which(file):
    """Check if a binary is installed"""
    for path in os.environ["PATH"].split(os.pathsep):
        if os.path.exists(os.path.join(path, file)):
                return os.path.join(path, file)
    return False


def make(condition, function):
    """Emulate make"""
    if not condition:
        function()


def repo(url):
    """Checkout a repository"""
    base = url.split(os.path.sep)[-1]
    make(
        exists(base),
        lambda: check_system("git clone %s" % url)
    )
    with chdir(base):
        check_system("git submodule update --init --recursive")
    return base


def driver(distro, arg):
    """Do the build"""
    if distro in debian_based:
        debian(distro, arg)
    elif distro in redhat_based:
        centos(distro, arg)
    else:
        raise ValueError("Unknown distro")


def build_depends():
    """Install build depends"""
    check_system("mk-build-deps")
    try:
        os.system("sudo dpkg -i *.deb")
        check_system("sudo apt-get install -f -y")
    finally:
        os.system("rm -rf *.deb")


def debian(distro, arg):
    """Debian and ubuntu build"""

    def git():
        check_system("sudo apt-get update")
        check_system("sudo apt-get install -y git")
    make(
        which("git"),
        git
    )
    make(
        which("dpkg-checkbuilddeps"),
        lambda: check_system(
            "sudo apt-get install -y build-essential"
        )
    )
    make(
        which("mk-build-deps"),
        lambda: check_system(
            "sudo apt-get install -y devscripts"
        )
    )
    make(
        which("equivs-build"),
        lambda: check_system(
            "sudo apt-get install -y equivs"
        )
    )
    base = repo(arg)
    with chdir(base):
        make(
            os.system("dpkg-checkbuilddeps") == 0,
            build_depends
        )
        check_system("make deb")
        os.system("sudo dpkg -i ../*.deb")
        check_system("sudo apt-get install -f -y")


def centos(distro, arg):
    """Centos build"""

[driver(sys.argv[1], arg) for arg in sys.argv[2:]]
