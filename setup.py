#!/usr/bin/env python
""" Setuptools setup file for FCpy. """
from setuptools import setup, find_packages
setup(
       name="FCpy",
       version="0.1.3",
       packages=find_packages(),
       python_requires=">=3.8",
       install_requires=[
           "numpy",
           "scipy",
           # optionally other deps
       ],
)
