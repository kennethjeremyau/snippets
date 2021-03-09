#!/usr/bin/env python

import re

res = re.sub(r'\|\d+', '', 'test|000')
print(res)
