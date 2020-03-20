#!/usr/bin/env python3

from setuptools import setup

setup(
    name='ipshow',
    version='0.1',
    description='Nicely-Formatted IP Information',
    scripts=['ipshow'],
    author='Mihail Georgiev',
    author_email='misho88@gmail.com',
    install_requires=[
        'netifaces',
        'blessed',
    ],
)
