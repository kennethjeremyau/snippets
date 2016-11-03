#!/usr/bin/env bash

FILES=staging/*
TABLENAME=table
REGION=us-east-1
for f in $FILES; do
    echo "Uploading $f"
    aws dynamodb put-item --table-name $TABLENAME --item file://$f --region $REGION
done
