"""Pytest entry point for Registry Model tests."""

import pytest
from pydantic import ValidationError

from rdfingest.models import RegistryEntry, InvalidRegistryEntry

from tests.tests_models.model_test_data import registry_model_test_data as registry_data


@pytest.mark.parametrize("data", registry_data.pass_data)
def test_pass_registry(data):
    assert RegistryEntry(**data)


@pytest.mark.parametrize("data", registry_data.fail_data_invalid_registry)
def test_fail_invalid_registry(data):
    with pytest.raises(InvalidRegistryEntry):
        RegistryEntry(**data)


@pytest.mark.parametrize("data", registry_data.fail_data_validation_error)
def test_fail_validation_registry(data):
    with pytest.raises(ValidationError):
        RegistryEntry(**data)
