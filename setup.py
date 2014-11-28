#!/usr/bin/python2
#
# Copyright (C) 2014 pytest-sourceorder contributors. See COPYING for license
#

from setuptools import setup
import io

with io.open('README.rst', 'rt', encoding='utf-8') as f:
    readme_contents = f.read()

setup_args = dict(
    name = "pytest-sourceorder",
    version = "0.1",
    description = "Test-ordering plugin for pytest",
    long_description = readme_contents,
    url = "https://fedorahosted.org/python-pytest-sourceorder/",
    license = "GPL",
    author = "Petr Viktorin",
    author_email = "pviktori@redhat.com",
    packages = ["pytest_sourceorder"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Quality Assurance',
    ],
    install_requires=['pytest'],  # (paramiko & PyYAML are suggested)
    entry_points = {
        'pytest11': [
            'sourceorder = pytest_sourceorder.plugin',
        ],
    },
)

if __name__ == '__main__':
    setup(**setup_args)
