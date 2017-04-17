#!/usr/bin/env python

import re

match = re.search("f[^\s]+ " + ".e", "can you find me?")
print match.group()
