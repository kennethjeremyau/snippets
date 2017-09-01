#!/usr/bin/env python

from multiprocessing import Pool

WORKERS=3

def f(x):
    print x

def main():
    jobs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    work = [jobs[i:i + len(jobs) / WORKERS + 1]
        for i in xrange(0, len(jobs), len(jobs) / WORKERS + 1)]
    pool = Pool(processes=WORKERS)
    pool.map(f, work)

if __name__ == '__main__':
    main()
