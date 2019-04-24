#!/usr/bin/env python

from Queue import Queue
from threading import Thread

NUM_WORKERS = 10


def worker():
    while True:
        item = q.get()
        print item
        q.task_done()

q = Queue()
for i in range(NUM_WORKERS):
    t = Thread(target=worker)
    t.daemon = True
    t.start()

for i in range(100):
    q.put(i)

q.join()
