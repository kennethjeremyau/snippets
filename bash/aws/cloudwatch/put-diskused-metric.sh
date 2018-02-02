#!/bin/bash

AWS_REGION=$(curl -s http://169.254.169.254/latest/dynamic/instance-identity/document | jq .region -r)
NAMESPACE="EC2"
NAME="DiskUsedPercent"
VALUE=$(df / | awk 'END{print gensub(/%/, "", "", $5)}')
UNIT="Percent"
DIMENSIONS="Tag=impressions"
AWS_DEFAULT_REGION=$AWS_REGION aws cloudwatch put-metric-data \
    --namespace $NAMESPACE \
    --metric-name $NAME \
    --unit $UNIT \
    --value $VALUE \
    --dimensions $DIMENSIONS
