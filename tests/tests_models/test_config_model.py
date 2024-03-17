"""Pytest entry point for Config Model tests."""

import pytest

from pydantic import ValidationError

from rdfingest.models import ConfigModel
from tests.tests_models.model_test_data import config_model_test_data as config_data


@pytest.mark.parametrize("data", config_data.pass_data)
def test_pass_config(data):
    assert ConfigModel(**data)


@pytest.mark.parametrize("data", config_data.fail_data)
def test_fail_config(data):
    with pytest.raises(ValidationError):
        ConfigModel(**data)
