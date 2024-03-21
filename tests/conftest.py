from unittest import mock

from rdfingest import ingest

import pytest
from loguru import logger
from _pytest.logging import LogCaptureFixture


@pytest.fixture
def caplog(caplog: LogCaptureFixture):
    """Override of the caplog fixture to provide loguru support.

    See https://loguru.readthedocs.io/en/stable/resources/migration.html#replacing-caplog-fixture-from-pytest-library.
    """
    handler_id = logger.add(
        caplog.handler,
        format="{message}",
        level=0,
        filter=lambda record: record["level"].no >= caplog.handler.level,
        enqueue=False,  # Set to 'True' if your test is spawning child processes.
    )
    yield caplog


@pytest.fixture()
def mock_rdfingest():
    """Fixture that provides a RDFIngest instance mock."""
    with mock.patch.object(ingest, "RDFIngest") as MockRDFIngest:
        yield MockRDFIngest.return_value
