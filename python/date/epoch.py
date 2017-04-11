#!/usr/bin/env python

# Using datetime.
from datetime import datetime
print int((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds())

# Using time.
import time
print int(time.time())
