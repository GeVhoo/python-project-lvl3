import logging

from page_loader import logger


def test_set_logger_debug():
    test_logger = logging.getLogger()
    logger.set_logger('debug')
    assert logging.Logger.getEffectiveLevel(test_logger) == logging.getLevelName('DEBUG')  # noqa: E501
