# -*- coding: utf-8 -*-
# Copyright (c) 2015 Spotify AB

from __future__ import absolute_import, division, print_function

import pytest
import py


@pytest.fixture()
def raml_file(EXAMPLES):
    """RAML file"""
    return EXAMPLES / "spotify.raml"


@pytest.fixture()
def config_file(CONFIG):
    """Griffin config file"""
    return CONFIG / "simple_config.yaml"


def test_build(raml_file, config_file, GRIFFIN, tmpdir):
    """Test successful build"""
    output_dir = tmpdir / "output"

    cmd = ["build",
           "--ramlfile", raml_file.strpath,
           "--config", config_file.strpath,
           "--output", output_dir.strpath]
    result = GRIFFIN.sysexec(*cmd)
    # status code != 0 would raise an exception
    assert result == ""


def test_bad_invocation(raml_file, config_file, GRIFFIN, tmpdir):
    """Test invalid invocation"""
    output_dir = tmpdir.mkdir("output")

    cmd = ["i_want_to_fail",
           "--ramlfile", raml_file.strpath,
           "--config", config_file.strpath,
           "--output", output_dir.strpath]
    with pytest.raises(py.process.cmdexec.Error) as excinfo:
        GRIFFIN.sysexec(*cmd)

    e = excinfo.value
    assert e.status == 2
    assert e.err == """Usage: griffin [OPTIONS] COMMAND [ARGS]...

Error: No such command "i_want_to_fail".
"""
