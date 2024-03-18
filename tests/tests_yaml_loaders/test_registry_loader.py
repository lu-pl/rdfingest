"""Pytest entry point for the YAML Registry loader."""


from pydantic import ValidationError
import pytest

from rdfingest.models import InvalidRegistryEntry
from rdfingest.yaml_loaders import registry_loader, YAMLValidationError
from tests.tests_yaml_loaders.yaml_loaders_data import (
    fail_registry_yamls,
    pass_registry_yamls
)


@pytest.mark.parametrize("yaml_path", pass_registry_yamls)
def test_pass_yaml_loaders(yaml_path):
    assert registry_loader(yaml_path)


@pytest.mark.parametrize("yaml_path", fail_registry_yamls)
def test_fail_yaml_loaders(yaml_path):
    with pytest.raises(YAMLValidationError):
        registry_loader(yaml_path)
