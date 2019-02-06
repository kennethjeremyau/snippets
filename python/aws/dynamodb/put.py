#!/usr/bin/env python

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TABLE')
try:
    table.put_item(
        Item={ 'id': 'ID' },
        ConditionExpression='attribute_not_exists(id)',
    )
except Exception as e:
    if e.response['Error']['Code'] != 'ConditionalCheckFailedException':
        raise e
