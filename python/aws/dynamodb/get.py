#!/usr/bin/env python

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TABLE')
try:
    table.get_item(
        Key={ 'id': 'ID' },
        ProjectionExpression='#a',
        ExpressionAttributeNames={ '#a': 'ATTRIBUTE' },
    )
except Exception as e:
    print('ERROR {}'.format(e))
