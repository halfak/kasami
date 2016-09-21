import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def requirements(fname):
    return [line.strip()
            for line in open(os.path.join(os.path.dirname(__file__), fname))]

setup(
    name="kasami",
    version="0.0.1",  # change in pcfg/__init__.py
    author="Aaron Halfaker",
    author_email="ahalfaker@wikimedia.org",
    description=("A set of utilities for training probabilistic " +
                 "context-free grammars and scoring new sentences with them."),
    license="MIT",
    url="https://github.com/halfak/pcfg",
    packages=find_packages(),
    long_description=read('README.md'),
    install_requires=requirements('requirements.txt'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
