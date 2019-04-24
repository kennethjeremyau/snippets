#!/usr/bin/env python

import boto3

s3 = boto3.client('s3')

s3.download_file('bucket', 'file.txt', './file.txt')
