import logging

from page_loader import cli
from page_loader import logger

URL = 'https://ru.hexlet.io/courses'
OUTPUT = '/test'
LEVEL = 'debug'

test_logger = logging.getLogger()


def test_get_args():
    args = cli.parser.parse_args(['-o', OUTPUT, '-l', LEVEL, URL])
    assert args.url == URL
    assert args.output == OUTPUT
    assert args.level == LEVEL


def test_set_logger_debug():
    logger.set_logger('debug')
    assert logging.Logger.getEffectiveLevel(test_logger) == logging.getLevelName('DEBUG')  # noqa: E501
