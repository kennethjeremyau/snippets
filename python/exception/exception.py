#!/usr/bin/env python

import sys
import traceback

try:
    raise Exception('an exception message')
except Exception as e:
    sys.stderr.write('ERROR {}\n'.format(e))
    traceback.print_last()
