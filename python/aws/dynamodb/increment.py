#!/usr/bin/env python

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TABLE')
try:
    res = table.update_item(
        Key={ 'id': 'ID' },
        UpdateExpression='ADD #n :v',
        ExpressionAttributeNames={ '#id': 'id', '#n': 'ATTRIBUTE_NAME' },
        ExpressionAttributeValues={ ':v': 1 },
        ConditionExpression='attribute_exists(#id)',
        ReturnValues='UPDATED_NEW',
    )
    if res['Attributes']['ATTRIBUTE_NAME'] >= 10:
        print('MAX')
except Exception as e:
    if e.response['Error']['Code'] != 'ConditionalCheckFailedException':
        raise e
