#!/usr/bin/env python

import os
import shutil

shutil.rmtree(os.getcwd() + '/path/to/folder', ignore_errors=True)
