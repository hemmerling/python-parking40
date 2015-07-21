#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
#  @package   parking40
#  @file      setup.py
#  @brief     Python application "Parking 4.0"
#  @author    Rolf Hemmerling <hemmerling@gmx.net>
#  @version   1.00
#  @date      2015-03-08
#  @copyright GNU LESSER GENERAL PUBLIC LICENSE, Version 2.1
#
#  parking40 - Python application "Parking 4.0"
#
#  Copyright 2015 Rolf Hemmerling
#
#  Licensed under the GNU LESSER GENERAL PUBLIC LICENSE, Version 2.1
#  (the "License"); you may not use this file except in compliance with
#  the License. You may obtain a copy of the License at
#
#  http://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""

# From ez_setup import use_setuptools
# use_setuptools()
from distutils.core import setup

# Patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

# Setup for distutils_foo
setup(name='parking40',
      version='1.0',
      description=\
      'Parking 4.0',
      long_description=\
      'Parking 4.0',
      author='Rolf Hemmerling',
      author_email='hemmerling@gmx.net',
      # maintainer='Rolf Hemmerling',
      # maintainer_email='hemmerling@gmx.net',
      url='http://www.github.com/hemmerling/parking40',
      download_url='http://www.github.com/hemmerling/parking40',
      license='Apache License, Version 2.0',
      platforms=['Python 2.7 on Windows and Linux'],
      classifiers=['Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Development Status :: 1',
                   'Environment :: GUI',
                   'Intended Audience :: Car drivers',
                   'License :: Apache License, Version 2.0',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: Linux :: Ubuntu'],
      data_files=[('Lib/site-packages/parking40_package',\
                   ['AUTHORS', 'COPYING', 'README.md']),
                  ('Scripts',\
                   ['Scripts/parking40.bat', \
                    'Scripts/parking40.sh'])
                 ],
      scripts=['Scripts/parking40-script.py'],
      py_modules=['Scripts/parking40-script', 'parking40'],
      package_dir={'parking40_package': 'src/c_implementation/steps'},
      packages=['parking40'],
      requires=['required_module'],
      provides=['provided_module'],
      obsoletes=['obsolete_module'],
      keywords=['Parking 4.0', 'parking'])
