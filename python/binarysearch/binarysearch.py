#!/usr/bin/env python

from bisect import bisect_left


def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    pos = bisect_left(a, x, lo, hi)
    return (pos if pos != hi and a[pos] == x else -1)


a = [1, 2, 3]
print binary_search(a, 2)
