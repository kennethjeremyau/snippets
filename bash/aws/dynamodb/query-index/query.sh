#!/usr/bin/env bash

TABLE_NAME='table'
INDEX_NAME='index'
PROJECTION_EXPRESSION='key1, key2'
KEY_CONDITION_EXPRESSION='key1 = :v1 and key2 > :v2'
FILTER_EXPRESSION='col1 = :v2'
EXPRESSION_ATTRIBUTE_VALUES='{":v1":{"S": "value1"}, ":v2":{"N": "0"}}'
#EXPRESSION_ATTRIBUTE_VALUES='file://expression-attributes.json'
aws dynamodb query --table-name "$TABLE_NAME" --index-name "$INDEX_NAME" --projection-expression "$PROJECTION_EXPRESSION" --key-condition-expression "$KEY_CONDITION_EXPRESSION" --filter-expression "$FILTER_EXPRESSION" --expression-attribute-values "$EXPRESSION_ATTRIBUTE_VALUES"
