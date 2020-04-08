#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages
import os

# Allow to run setup.py from another directory.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

version = '0.0.1.dev0'

setup(
    name='arjun_ra',
    version=version,
    packages=find_packages(
        exclude=(
            '.*',
            'EGG-INFO',
            '*.egg-info',
            '_trial*',
            '*.tests',
            '*.tests.*',
            'tests.*',
            'tests',
            'examples.*',
            'examples*',
            )
        ),
    include_package_data=True,
    install_requires=[
        'bpprov',
        'rasdk',
        'rpsdk[ra]',
        ],
    entry_points={
        'console_scripts': [
            'arjun_ra = arjun_ra.main:main',
            ]
        },
    tests_require=[
        'mock',
        'nose',
        ],
    test_suite='nose.collector',
)
