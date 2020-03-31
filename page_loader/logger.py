import logging


# Create and configure logger
def set_logger(level):
    logging.basicConfig(format='[%(levelname)s]: %(message)s')
    logger = logging.getLogger()
    if level == 'debug':
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
