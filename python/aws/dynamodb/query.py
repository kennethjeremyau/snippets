#!/usr/bin/env python

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TABLE')

try:
    res = table.query(
        KeyConditionExpression='#id = :id',
        ExpressionAttributeNames={ '#id': 'id' },
        ExpressionAttributeValues={ ':id': 'ID' },
    )
    items = [ item['id'] for item in res['Items'] ]
    print (items)
except Exception as e:
    print ('ERROR {}'.format(e))
