import logging

from page_loader import logger

test_logger = logging.getLogger()


def test_set_logger_debug():
    logger.set_logger('debug')
    assert logging.Logger.getEffectiveLevel(test_logger) == logging.getLevelName('DEBUG')  # noqa: E501
