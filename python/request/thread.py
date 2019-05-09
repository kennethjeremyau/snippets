#!/usr/bin/env python

import requests
import threading

def post(arg):
    def worker(arg):
        requests.post('url')
    t = threading.Thread(target=worker, args=(arg,))
    t.daemon = True
    t.start()

post('test')
