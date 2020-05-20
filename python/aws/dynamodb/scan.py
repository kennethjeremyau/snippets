#!/usr/bin/env python

import argparse
import boto3

parser = argparse.ArgumentParser()
parser.add_argument('--segment', default=0, type=int)
parser.add_argument('--total-segments', default=1, type=int)
args = parser.parse_args()

dynamodb = boto3.client('dynamodb', region_name='us-east-1')
table = dynamodb.get_paginator('scan')

for page in table.paginate(
    TableName='tablename',
    ExpressionAttributeNames={ '#a': 'a', '#b': 'b' },
    ExpressionAttributeValues={ ':c': {'N': '1'}, ':d': {'S': 'd'} },
    FilterExpression='#a >= :c and #b = :d',
    ProjectionExpression="#a,#b",
    Segment=args.segment,
    TotalSegments=args.total_segments
):
    for item in page['Items']:
        print str(item['id']['S'])
