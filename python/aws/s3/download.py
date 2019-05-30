#!/usr/bin/env python

import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

try:
    s3.download_file('bucket', 'file.txt', './file.txt')
except ClientError as e:
    if e.response['Error']['Code'] == '403':
        print 'ERROR forbidden: {}'.format(e.response['Error']['Message'])
    elif e.response['Error']['Code'] == '404':
        print 'ERROR not found: {}'.format(e.response['Error']['Message'])
    else:
        raise e
