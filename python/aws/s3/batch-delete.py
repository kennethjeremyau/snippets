#!/usr/bin/env python

import boto3
import sys

BUCKET = 'bucket'
s3 = boto3.client('s3')


def batched_keys(limit=1000):
    keys = []
    for line in sys.stdin:
        key = line.rstrip()
        keys.append(key)
        if len(keys) == limit:
            yield keys
            keys = []
    if len(keys):
        yield keys


for keys in batched_keys():
    kwargs = {
        'Bucket': BUCKET,
        'Delete': {
            'Objects': [{'Key': key} for key in keys],
            'Quiet': True
        }
    }
    s3.delete_objects(**kwargs)
