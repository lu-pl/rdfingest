"""Pytest entry point for the YAML Config loaders."""

from pydantic import ValidationError
import pytest

from rdfingest.yaml_loaders import config_loader, YAMLValidationError
from tests.tests_yaml_loaders.yaml_loaders_data import pass_yamls, fail_yamls


@pytest.mark.parametrize("yaml_path", pass_yamls)
def test_pass_yaml_loaders(yaml_path):
    assert config_loader(yaml_path)


@pytest.mark.parametrize("yaml_path", fail_yamls)
def test_fail_yaml_loaders(yaml_path):
    with pytest.raises(YAMLValidationError):
        config_loader(yaml_path)
