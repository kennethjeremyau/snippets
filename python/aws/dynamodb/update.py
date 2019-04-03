#!/usr/bin/env python

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TABLE')
try:
    table.update_item(
        Item={ 'id': 'ID' },
        UpdateExpression='SET attr = 1',
        ConditionExpression='attribute_exists(id)',
    )
except Exception as e:
    if e.response['Error']['Code'] != 'ConditionalCheckFailedException':
        raise e
