# -*- coding: utf-8 -*-
# @Author: root
# @Date:   2016-05-24 16:50:06
# @Last Modified by:   drinks
# @Last Modified time: 2016-05-24 23:24:52

from setuptools import setup, find_packages

VERSION = '0.2.2'

setup(name='colorfulprinter',
      version=VERSION,
      description="A drop in replacement for python built-in pprint package",
      long_description='just enjoy',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
      ],
      keywords='python pprint color console terminal unicode',
      author='drink',
      author_email='drinksober@foxmail.com',
      url='https://github.com/drinksober/colorfulprinter',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[],
      )