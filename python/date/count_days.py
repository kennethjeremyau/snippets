#!/usr/bin/env python

from datetime import date

d0 = date(2017, 8, 23)
d1 = date(2017, 6, 1)
delta = d0 - d1
print delta.days
