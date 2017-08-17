#!/usr/bin/env bash

TABLE_NAME='table'
INDEX_NAME='index'
PROJECTION_EXPRESSION='key1, key2'
KEY_CONDITION_EXPRESSION='key1 = :key1 and key2 > :key2'
EXPRESSION_ATTRIBUTE_VALUES='file://expression-attributes.json'
aws dynamodb query --table-name "$TABLE_NAME" --index-name "$INDEX_NAME" --projection-expression "$PROJECTION_EXPRESSION" --key-condition-expression "$KEY_CONDITION_EXPRESSION" --expression-attribute-values "$EXPRESSION_ATTRIBUTE_VALUES"
