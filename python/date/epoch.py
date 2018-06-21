#!/usr/bin/env python

# Datetime to epoch.
from datetime import datetime
print int((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds())

# Time to epoch.
import time
print int(time.time())

# Epoch to datetime.
from datetime import datetime
datetime.fromtimestamp(1284286794)
