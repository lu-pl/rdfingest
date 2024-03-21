"""Pytest entry point for CLI tests."""

from sys import flags
import pytest

import requests

import rdfingest.ingest as ingest

from unittest import mock

from typer.testing import CliRunner
from rdfingest.main import app


runner = CliRunner()


@pytest.mark.parametrize(
    "flags",
    (
        [],
        ["-c", "dne_config.yaml"],
        ["-r", "dne_registry.yaml"],
        ["--config", "dne_config.yaml"],
        ["--registry", "dne_registry.yaml"],
        ["-c", "dne_config.yaml", "-r", "dne_registry.yaml"],
        ["--config", "dne_config.yaml", "--registry", "dne_registry.yaml"],
        ["-c", "dne_config.yaml", "--registry", "dne_registry.yaml"],
        ["--config", "dne_config.yaml", "-r", "dne_registry.yaml"]
    )
)
def test_cli_fail_no_files(flags):
    """Check if the CLI fails when config files don't exists."""
    result = runner.invoke(app, flags)
    assert result.exit_code == 2
