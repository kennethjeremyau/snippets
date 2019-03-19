#!/bin/bash

TABLE_NAME='table'
KEY_NAME='key'
VAL_NAME='value'

while read line; do
    KEY=$(echo "$line" | cut -d "," -f 1)
    VAL=$(echo "$line" | cut -d "," -f 2)
    aws dynamodb update-item \
        --table-name "$TABLE_NAME" \
        --key "{\"$KEY_NAME\":{\"S\":\"$KEY\"}}" \
        --update-expression "SET $VAL_NAME = :v" \
        --expression-attribute-values "{\":v\":{\"S\":\"$VAL\"}}" \
        --return-values ALL_NEW
done
