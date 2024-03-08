#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
* Filename: setup.py
* Description:
* Time: 2020.11.27
* Author: liuf5
*/
"""
from setuptools import setup

from zoomeyehk import __version__


DEPENDENCIES = open('requirements.txt', 'r', encoding='utf-8').read().split('\n')
README = open('README.rst', 'r', encoding='utf-8').read()

setup(
    name='zoomeyehk',
    version=__version__,
    description='Python library and command-line tool for ZoomEye.HK (https://www.zoomeye.hk/doc)',
    long_description=README,
    long_description_content_type='text/x-rst',
    author='ZoomEye.HK',
    url='https://github.com/zoomeye-hk/zoomeye-python',  #
    packages=['zoomeyehk'],
    entry_points={'console_scripts': ['zoomeyehk=zoomeyehk.cli:main']},
    install_requires=DEPENDENCIES,
    keywords=['security tool', 'zoomeye', 'zoomeyehk', 'command tool'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
