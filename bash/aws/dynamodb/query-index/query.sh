#!/usr/bin/env bash

aws dynamodb query \
    --table-name 'table' \
    --index-name 'index' \
    --projection-expression 'key1, key2' \
    --key-condition-expression 'key1 = :v1 and key2 > :v2' \
    --filter-expression "col1 = :v2" \
    --expression-attribute-values '{":v1":{"S": "value1"}, ":v2":{"N": "0"}}'
    #--expression-attribute-values 'file://expression-attributes.json'
