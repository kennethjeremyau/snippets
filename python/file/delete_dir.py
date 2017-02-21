#!/usr/bin/env python

import os
import shutil

try:
    shutil.rmtree(os.getcwd() + '/path/to/folder')
except:
    pass
