import sys

import pkg_resources
import subprocess


def check_package(package_name):
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    return package_name in installed_packages


def install_package(package_name):
    if not check_package(package_name):
        subprocess.run([sys.executable, "-m", "pip", "install", package_name], check=True)
