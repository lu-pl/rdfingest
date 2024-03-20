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


# @pytest.fixture()
# def mock_rdfingest():
#     """Fixture that provides a RDFIngest instance mock."""
#     with mock.patch.object(ingest, "RDFIngest") as MockRDFIngest:
#         yield MockRDFIngest.return_value


# @pytest.fixture()
# def mock_requests_post():
#     """Fixture that provides a requests.post mock."""
#     def _mocked_post(url, **kwargs):
#         kwargs.update({"url": url})
#         return kwargs

#     with mock.patch("requests.post") as mock_post:
#         mock_post.return_value = _mocked_post
#         result = runner.invoke(app, ["-c", "./test_config.yaml", "-r" "./test_registry.yaml"])

#         print("INFO: ", result.exit_code)
#         print(f"INFO: {mock_post.called}")
#         print(f"INFO: {mock_post.assert_called_with('')}")


# def test_fun(mock_requests_post):
#     pass


# def test_cli_rdfingest_object(mock_rdfingest):
#     pass
