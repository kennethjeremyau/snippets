#!/usr/bin/env python

from boto.s3.connection import S3Connection

conn = S3Connection()
bucket = conn.get_bucket('bucket')
for key in bucket.list():
    print key.name.encode('utf-8')
