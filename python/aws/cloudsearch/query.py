#!/usr/bin/env python

import boto3

cloudsearch = boto3.client(
    'cloudsearchdomain',
    endpoint_url='https://ENDPOINT.us-east-1.cloudsearch.amazonaws.com'
)

paginator = cloudsearch.get_paginator('search')

pages = paginator.paginate(
    query='word1 word2 word3',
)

for page in pages:
    print page
