#!/usr/bin/env python

import re
from os import path
import codecs
from distutils.core import setup

init_path = path.join(path.dirname(__file__), 'tiling', '__init__.py')
with codecs.open(init_path, 'r', 'utf-8') as fd:
    VERSION = re.search("__version__ = '([^']+)'", fd.read().strip()).group(1)

setup(name='Tiling',
      version=VERSION,
      description='Tilings of regular polygons',
      long_description=codecs.open('README.rst', 'r', 'utf-8').read(),
      author='Michael Fogleman',
      author_email='michael.fogleman@gmail.com',
      url='https://github.com/fogleman/Tiling',
      install_requires=['cairocffi'],
      packages=['tiling'],
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: "
        "GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Multimedia :: Graphics"]
     )