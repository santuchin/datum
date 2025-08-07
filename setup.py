from setuptools import setup, Extension

module = Extension('datum', sources=['main.c'])

setup(
    name='datum',
    version='0.1',
    ext_modules=[module]
)
