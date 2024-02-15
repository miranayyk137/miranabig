from setuptools import setup, Extension

my_module = Extension('testm1',
                    sources=['testm1.cpp'])

setup(name='my_module',
      version='1.0',
      description='A simple example of a Python extension module written in C++',
      ext_modules=[my_module])