#!/usr/bin/env python

from boto import dynamodb2
from boto.dynamodb2.table import Table
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--segment', default=0, type=int)
parser.add_argument('--total-segments', default=1, type=int)
args = parser.parse_args()

table = Table('tablename', connection=dynamodb2.connect_to_region('us-east-1'))
for row in table.scan(segment=args.segment, total_segments=args.total_segments):
    print row['id']
