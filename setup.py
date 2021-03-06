#!/usr/bin/env python

from setuptools import setup, find_packages
import os.path

setup(name='tap-outbrain',
      version='0.3.2',
      description='Singer.io tap for extracting data from the Outbrain API',
      author='Fishtown Analytics',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_outbrain'],
      install_requires=[
          'singer-python>=5.0.4',
          'backoff>=1.3.2',
          'requests>=2.20.0',
          'python-dateutil>=2.6.0'
      ],
      entry_points='''
          [console_scripts]
          tap-outbrain=tap_outbrain:main
      ''',
      packages=['tap_outbrain']
)
