#!/usr/bin/env python

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# See "LICENSE.GPL" in the source distribution for more information.

# Headers in this file shall remain intact.
from setuptools import setup, find_packages


NAME = 'featdjango'

VERSION = '1.0.0'
DESCRIPTION = 'F3AT and Django integration'
LONG_DESC = DESCRIPTION
AUTHOR = 'Marek Kowalski',
AUTHOR_EMAIL = 'mkowalski@empaytech.com',
URL = 'https://github.com/mkowalski/featdjango'
LICENSE = "GPL"
PLATFORMS = ['any']
REQUIRES = ['twisted', 'twisted.web', 'json', 'feat']
SETUP_REQUIRES = ['setuptools>=0.6c9']
INSTALL_REQUIRES = ['Twisted>=10.1']
KEYWORDS = ['twisted', 'agent', 'framework']
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: No Input/Output (Daemon)',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 2.6',
    'Topic :: Software Development :: Libraries :: Application Frameworks']


setup(name = NAME,
      version = VERSION,
      description = DESCRIPTION,
      long_description = LONG_DESC,
      author = AUTHOR,
      author_email = AUTHOR_EMAIL,
      url = URL,
      license = LICENSE,
      platforms = PLATFORMS,
      setup_requires = SETUP_REQUIRES,
      install_requires = INSTALL_REQUIRES,
      requires = REQUIRES,
      package_dir = {'': 'src'},
      packages = find_packages('src'),
      include_package_data = True,
      keywords = KEYWORDS,
      classifiers = CLASSIFIERS)
