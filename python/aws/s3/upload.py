#!/usr/bin/env python

import boto3

s3 = boto3.client('s3')

s3.upload_file('./file.txt', 'bucket', 'file.txt')
