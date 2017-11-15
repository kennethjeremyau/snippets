#!/usr/bin/env python

from boto import dynamodb2
from boto.dynamodb2.table import Table

table = Table('tablename', connection=dynamodb2.connect_to_region('us-east-1'))
for row in table.scan():
    print row['id']
