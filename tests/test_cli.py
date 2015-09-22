# -*- coding: utf-8 -*-
# Copyright (c) 2015 Spotify AB

from __future__ import absolute_import, division, print_function

import pytest

from griffin.cli import build
from griffin.config import setup_config


@pytest.fixture(scope="session")
def raml(EXAMPLES):
    """RAML file"""
    return EXAMPLES / "spotify.raml"


@pytest.fixture(scope="session")
def config(CONFIG):
    """Config file for griffin"""
    return setup_config((CONFIG / "simple_config.yaml").strpath)


def test_build(raml, config, tmpdir):
    tmp_output = tmpdir / "output"

    assert not tmp_output.exists()

    build(raml.strpath, config, tmp_output.strpath)

    # TODO: test the existance of assets & asset dirs

    # TODO: test the existance of genderated HTML & parent dirs
    assert tmp_output.exists()
    index = tmp_output / "index.html"
    assert index.exists()
    exp_text = "Auto-generated documentation from Griffin"
    assert exp_text in index.read_text("utf-8")
