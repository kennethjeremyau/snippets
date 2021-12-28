#!/usr/bin/env python

import sys

if not sys.stdin.isatty():
    stdin = sys.stdin.read()
    print('stdin: {}'.format(stdin))
else:
    print('nothing piped')
