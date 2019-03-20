#!/usr/bin/env python

import time

MAX_ATTEMPTS = 5

attempt = 1
while attempt <= MAX_ATTEMPTS:
    success = True
    try:
        raise Exception('SAMPLE ERROR')
    except:
        success = False
    if success:
        break
    if attempt == MAX_ATTEMPTS:
        print 'FINISHED'
        break
    print attempt
    time.sleep(2 ** attempt)
    attempt += 1
