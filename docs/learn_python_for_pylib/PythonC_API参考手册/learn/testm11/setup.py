from setuptools import setup, Extension

testmm1 = Extension('testm1',
                    sources=['testm1.cpp'])

setup(name='testmm1',
      version='1.0',
      description='A simple example of a Python extension module written in C++',
      ext_modules=[testmm1])
