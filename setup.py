#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 Spotify AB
import io
import os
import re
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand  # NOQA


NAME = "griffin"
META_PATH = os.path.join("griffin", "__init__.py")


HERE = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for fl in filenames:
        with io.open(fl, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


def install_requires():
    install_requires = ["ramlfications", "jinja2"]
    if sys.version_info[:2] == (2, 6):
        install_requires.append("ordereddict")
    return install_requires


long_description = read("README.rst", "docs/changelog.rst")


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args or [] + ["tests"])
        sys.exit(errno)

setup(
    name=NAME,
    version=find_meta("version"),
    description=find_meta("description"),
    long_description=long_description,
    url=find_meta("uri"),
    license=find_meta("license"),
    author=find_meta("author"),
    author_email=find_meta("email"),
    keywords=["raml", "rest"],
    packages=find_packages(exclude=["tests*"]),
    entry_points={
        'console_scripts': [
            'griffin = griffin.__main__:main'
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=install_requires(),
    tests_require=[
        "pytest"
    ],
    cmdclass={
        "test": PyTest,
    }
)
