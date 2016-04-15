#!/usr/bin/env python
import setuptools

version = '0.9.5dev'

setuptools.setup(
    name='fastimport',
    description='VCS fastimport/fastexport parser',
    author='Canonical Ltd',
    version=version,
    author_email='bazaar@lists.canonical.com',
    license='GNU GPL v2 or later',
    url='https://launchpad.net/python-fastimport',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: GNU GPL v2 or later',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='git parser',
    packages=[
        'fastimport',
        'fastimport.processors'
    ],
    install_requires=['future'],
    extras_require={
        'dev': ['unittest2'],
    },
)
