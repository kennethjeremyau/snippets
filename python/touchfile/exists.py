#!/usr/bin/env python

import os

TOUCHFILE = 'touchfile'

def touchfile_exists():
    return os.path.isfile(os.path.join(os.getcwd(), TOUCHFILE))

print(touchfile_exists())
