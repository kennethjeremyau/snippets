#!/usr/bin/env python

def is_file_ascii(path):
    with open(path) as f:
        try:
            f.read().encode('ascii')
        except UnicodeDecodeError:
            return False
        return True

if is_file_ascii('good.txt'):
    print 'good.txt has no non-ascii characters.'
else:
    print 'good.txt has non-ascii characters.'

if is_file_ascii('bad.txt'):
    print 'bad.txt has no non-ascii characters.'
else:
    print 'bad.txt has non-ascii characters.'
