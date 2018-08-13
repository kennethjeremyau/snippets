#!/usr/bin/env python

import boto3

s3 = boto3.client('s3')
paginator = s3.get_paginator('list_objects')
pages = paginator.paginate(Bucket='bucket')

for page in pages:
    for obj in page['Contents']:
        print obj['Key']
