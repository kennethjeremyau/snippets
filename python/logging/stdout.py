#!/usr/bin/env python3

import logging
import sys

stdout_handler = logging.StreamHandler(stream=sys.stdout)
stderr_handler = logging.StreamHandler(stream=sys.stderr)
handlers = [stdout_handler, stderr_handler]

logging.basicConfig(

    # Only logs with level INFO or greater will display.
    level=logging.INFO,

    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    format='%(asctime)s %(levelname)s %(name)s %(message)s',

    handlers=handlers,
)

logging.debug('this is a debug message')
logging.info('this is an info message')
logging.warning('this is a warning message')
logging.error('this is an error message')

logger = logging.getLogger(__name__)
logger.info('this is another info message')
