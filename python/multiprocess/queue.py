#!/usr/bin/env python

import Queue
import threading

NUM_WORKERS = 10


def worker(done):
    while not done.is_set():
        try:
            item = q.get_nowait()
            print item
            q.task_done()
        except Queue.Empty:
            pass
    print 'thread exiting'


q = Queue.Queue()
done_event = threading.Event()
for i in range(NUM_WORKERS):
    t = threading.Thread(target=worker, args=(done_event,))
    # Can use daemon instead of events if it is ok to kill thread abruptly.
    #t.daemon = True
    t.start()

for i in range(100):
    q.put(i)

q.join()
print "thread count: {}".format(threading.active_count())

done_event.set()
