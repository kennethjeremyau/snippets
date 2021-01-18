#!/usr/bin/env python

import boto3
import sys

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TABLE')

for line in sys.stdin:
    key = line.rstrip()

    try:
        table.delete_item(Key={ 'KEY': key })
    except Exception as e:
        sys.stderr.write('{}\n', key)
        continue

    print('{}'.format(key))
