import logging

logger = logging.getLogger(__name__)

def func():
    logging.warning('from another module')
    logger.warning('again')
