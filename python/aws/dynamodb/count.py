#!/usr/bin/env python

import boto3

dynamodb = boto3.client('dynamodb')
table = dynamodb.get_paginator('scan')
for page in table.paginate(
    TableName='tableName',
    Select='COUNT',
    Segment=0,
    TotalSegments=1,
    FilterExpression='attribute_exists(#k) AND #k > :v',
    ExpressionAttributeNames={'#k': {'S': 'key'}},
    ExpressionAttributeValues={':v': {'N': '0'}},
):
    print(page['Count'])
