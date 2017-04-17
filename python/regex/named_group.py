#!/usr/bin/env python

import re

match = re.search(r"(?P<group1>hello)", "say hello")
print match.group('group1')
