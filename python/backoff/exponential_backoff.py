#!/usr/bin/env python

import time

MAX_ATTEMPTS = 5

attempt = 1
while attempt <= MAX_ATTEMPTS:
    print attempt
    time.sleep(2 ** attempt)
    attempt += 1
