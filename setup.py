#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import with_statement, division, absolute_import

try:
    from setuptools import setup, Command, find_packages
except ImportError:
    from distutils.core import setup, Command


def get_version():
    """Get current version from VERSION file"""
    with open("VERSION") as f:
        return f.readline().strip()


def get_description():
    """Get current package description"""
    with open("DESCRIPTION") as f:
        return f.read()


def get_package_name():
    """Automatically figure out current package name"""
    import os.path
    with open("PACKAGE_NAME") as f:
        package_name = f.readline().strip()
    dir_name = package_name.replace("-", "_")  # reverse PyPI name normalization
    package_exists = os.path.exists(os.path.join(dir_name, "__init__.py"))
    assert package_exists, "Cannot get package name automatically"  # package name should be in the current dir as well!
    return package_name, dir_name


def get_requirements():
    with open("requirements.txt") as f:
        return [line.strip() for line in f]


def main():
    __package_name__, __dir_name__ = get_package_name()
    __version__ = get_version()
    __description__ = get_description()
    __packages__ = find_packages()
    __requirements__ = get_requirements()

    setup(
        name=__package_name__,
        version=__version__,
        author="Andrew Carter",
        author_email="andrewjcarter@gmail.com",
        description=__description__,
        long_description=open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
        license="MIT",
        keywords="example documentation tutorial",
        url="http://lightningwolf.net/an_example_pypi_project",
        packages=__packages__,
        install_requires=__requirements__,
        platforms=['unix', 'linux', 'osx'],
        classifiers=[
            "Development Status :: 3 - Alpha",
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Natural Language :: Polish',
            'Topic :: Server :: Utilities',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
        ],
    )


if __name__ == '__main__':
    main()