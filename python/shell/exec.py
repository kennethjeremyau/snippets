#!/usr/bin/env python

import subprocess

# simple
subprocess.check_call(['date'])

# pipes
subprocess.check_call('cat {} | sort > output.txt'.format('input.txt'), shell=True)
