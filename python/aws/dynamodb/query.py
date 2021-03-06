#!/usr/bin/env python

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TABLE')

try:
    res = table.query(
        # IndexName = 'INDEX'
        KeyConditionExpression = '#id = :id',
        # KeyConditionExpression = '#id = :id AND #sort <= :sort',
        # KeyConditionExpression = '#id = :id AND #sort BETWEEN :sort1 AND :sort2',
        # KeyConditionExpression = '#id = :id AND begins_with(#sort, :sort)',
        ExpressionAttributeNames = { '#id': 'id' },
        ExpressionAttributeValues = { ':id': 'ID' },
    )
    items = [ item['id'] for item in res['Items'] ]
    print (items)
except Exception as e:
    print ('ERROR {}'.format(e))
