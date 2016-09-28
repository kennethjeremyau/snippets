#!/usr/bin/env bash

KEYS=keys.txt
TABLENAME=table
KEYNAME=id
REGION=us-west-1
while read key; do
    echo "Downloading $key"
    aws dynamodb get-item --table-name $TABLENAME --key "{\"$KEYNAME\":{\"S\":\"$key\"}}" --region $REGION |
    python -c "import sys, json; print json.dumps(json.load(sys.stdin)['Item'])" > ./staging/$key.json
done < "$KEYS"
