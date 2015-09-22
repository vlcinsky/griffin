# -*- coding: utf-8 -*-
# Copyright (c) 2015 Spotify AB
from __future__ import absolute_import, division, print_function

import pytest
from py.path import local


@pytest.fixture(scope="session")
def PAR_DIR():
    """Root tests directory"""
    return local("tests")


@pytest.fixture(scope="session")
def SPOTIFY(PAR_DIR):
    """Directory with spotify include files"""
    return PAR_DIR / "cli_input" / "spotify"


@pytest.fixture(scope="session")
def CONFIG(PAR_DIR):
    """Directory with config files"""
    return PAR_DIR / "cli_input" / "config"


@pytest.fixture(scope="session")
def EXAMPLES(PAR_DIR):
    """Directory with examples"""
    return PAR_DIR / "cli_input"


@pytest.fixture(scope="session")
def GRIFFIN():
    """Path to `griffin` executable"""
    path = local.sysfind("griffin")
    assert path.exists()
    return path
