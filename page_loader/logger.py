import logging

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO
}


# Create and configure logger
def set_logger(level):
    logging.basicConfig(format='[%(levelname)s]: %(message)s')
    logger = logging.getLogger()
    logger.setLevel(LEVELS[level])
