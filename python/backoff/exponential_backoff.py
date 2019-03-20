#!/usr/bin/env python

import functools
import time

def exponential_backoff(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        MAX_ATTEMPTS = 5
        attempt = 1
        while attempt <= MAX_ATTEMPTS:
            success = True
            try:
                output = func(*args, **kwargs)
            except Exception as e:
                success = False
            if success:
                break
            if attempt == MAX_ATTEMPTS:
                raise e
            print 'attempt {}'.format(attempt)
            time.sleep(2 ** attempt)
            attempt += 1
        return output
    return wrapper

@exponential_backoff
def func():
    raise Exception('SAMPLE ERROR')

func()
