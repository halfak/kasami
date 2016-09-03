try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    description='An implementation a basic PCFG parser/scorer in Python',
    author='Arthur Tilley',
    url='https://github.com/aetilley/pcfg',
    author_email='aetilley@gmail.com',
    version='0.0.1',
    install_requires=[],
    packages=['pcfg'],
    scripts=[],
    name='pcfg'
)
