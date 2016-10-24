#!/usr/bin/env python
import sys
import os
import contextlib
from os.path import exists

redhat_based = {
    'centos6': "06centos",
    'centos7': "07centos",
}
debian_based = {
    'jessie': "08jessie",
    'wheezy': "07wheezy",
    'trusty': "14trusty",
    'vivid':  "15vivid",
    'xenial': "16xenial",
}

all_distros = dict(debian_based.items() + redhat_based.items())

for env in [
        key for key in os.environ.keys()
        if key.startswith("LC_")
]:
    del os.environ[env]


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
    if base.endswith(".git"):
        base = base[:-4]
    make(
        exists(base),
        lambda: check_system("git clone %s" % url)
    )
    with chdir(base):
        check_system("git submodule update --init --recursive")
    return base


def driver(distro, arg):
    """Do the build"""
    suffix = all_distros[distro]
    os.environ["ADSY_VERSION_SUFFIX"] = "~%s+adsy" % suffix
    if distro in debian_based:
        debian(distro, arg)
    elif distro in redhat_based:
        centos(distro, arg)


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

    check_system("sudo apt-get update")
    if distro == "wheezy":
        check_system("sudo apt-get install -y ca-certificates")
    make(
        which("pip"),
        lambda: check_system("sudo apt-get install -y python-pip")
    )
    make(
        which("git"),
        lambda: check_system("sudo apt-get install -y git")
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
        check_system("sudo make log")
        check_system("sudo chown -R vagrant:vagrant .")
        check_system("make deb")
        if distro == "wheezy":
            os.system("rm ../python3-*.deb")
        os.system("sudo dpkg -i ../*.deb")
        check_system("sudo apt-get install -f -y")
    check_system("mkdir -p /vagrant/%s/" % distro)
    check_system("mv *.deb /vagrant/%s/" % distro)


def centos(distro, arg):
    """Centos build"""
    def pip():
        check_system("sudo yum install -y epel-release")
        check_system("sudo yum install -y python-pip")
        check_system("sudo pip install -U setuptools")
    if distro == "centos6":
        make(
            which("pip"),
            pip
        )
    make(
        which("git"),
        lambda: check_system("sudo yum install -y git")
    )
    base = repo(arg)
    make(
        which("rpmbuild"),
        lambda: check_system("sudo yum install -y rpm-build")
    )
    with chdir(base):
        check_system("make rpm")
    check_system("mkdir -p /vagrant/%s/" % distro)
    check_system("mv */dist/*.rpm /vagrant/%s/" % distro)

[driver(sys.argv[1], arg) for arg in sys.argv[2:]]
