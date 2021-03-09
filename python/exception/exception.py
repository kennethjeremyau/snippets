#!/usr/bin/env python

import sys
import traceback

def inner():
    raise Exception('an exception message')

try:
    inner()
except Exception as e:
    sys.stderr.write('ERROR {}\n'.format(e))
    traceback.print_exc()
