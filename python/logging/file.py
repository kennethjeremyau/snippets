#!/usr/bin/env python3

import collections
import logging
import module
import logstash

logging.basicConfig(filename='./example.log', level=logging.DEBUG)
logging.debug('this is a debug message')
logging.info('this is an info message')
logging.warning('this is a warning message')
logging.error('this is an error message')

logger = logging.getLogger(__name__)
logger.debug('using a named logger')
module.func()

fh = logging.FileHandler('separate.log')
logger = logging.getLogger('separate')
logger.propagate = False
logger.addHandler(fh)
logger.debug('separate')

logstash.debug(logger, logstash.Log(key='hi'))
