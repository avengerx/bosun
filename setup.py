# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

import os
import sys
from distutils import log

long_desc = ''' '''
requires = ['Fabric', 'PyYAML', 'mom4-utils', 'python-dateutil']

setup(
    name='bosun',
    version='1.0',
    url='https://bitbucket.org/luizirber/bosun',
    download_url='https://bitbucket.org/luizirber/bosun',
    license='PSF',
    author='Luiz Irber, Guilherme Castelao',
    author_email='luiz.irber@gmail.com, castelao@gmail.com',
    description='',
    long_description=long_desc,
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Scientific/Engineering',
    ],
    platforms='any',
    scripts=["bin/bosun"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)
