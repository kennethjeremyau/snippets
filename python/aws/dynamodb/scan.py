#!/usr/bin/env python

from boto import dynamodb2
from boto.dynamodb2.table import Table


def scan(tablename, callback, region='us-east-1', *args, **kwargs):
    connection = dynamodb2.connect_to_region(region)
    table = Table(tablename, connection=connection)
    items = table.scan()

    retries = 0
    while 1:
        try:
            item = next(items)
        except dynamodb2.exceptions.ProvisionedThroughputExceededException:
            backoff = min(60, (2 ** retries) / 10)
            time.sleep(backoff)
            item = None
            retries += 1 if retries < 10 else 0
        except StopIteration:
            break
        callback(item, *args, **kwargs)


def callback(item):
    print item['id']


scan('tablename', callback)
