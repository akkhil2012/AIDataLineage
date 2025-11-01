"""Smoke tests for logging helpers."""

from aidatalineage.utils.logging import configure_logging


def test_configure_logging_returns_logger() -> None:
    logger = configure_logging()
    assert logger.name == "aidatalineage"
