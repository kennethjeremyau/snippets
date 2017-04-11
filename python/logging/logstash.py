import collections

Log = collections.namedtuple('Log', 'key query subreddit user gfyname msg')

# set default value to '-'
Log.__new__.__defaults__ = ('-',) * len(Log._fields)

def debug(logger, log):
    logger.debug(' '.join('"{}"'.format(x) for x in log))

def info(logger, log):
    logger.info(' '.join(x for x in log))

def warning(logger, log):
    logger.warning(' '.join(x for x in log))

def error(logger, log):
    logger.error(' '.join(x for x in log))

def exception(logger, log):
    logger.exception(' '.join(x for x in log))

def critical(logger, log):
    logger.critical(' '.join(x for x in log))
