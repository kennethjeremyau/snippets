#!/usr/bin/env python

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TABLE')
table.update_item(
    Key={ 'id': 'ID' },
    UpdateExpression='ADD #n :v',
    ExpressionAttributeNames={ '#n': 'ATTRIBUTE_NAME' },
    ExpressionAttributeValues={ ':v': set('ITEM') },  # string set
    ReturnValues : "UPDATED_NEW"
)
