#!/bin/bash

AWS_REGION="us-east-1"
NAMESPACE="Analytics"
NAME="diskspace"
VALUE=$(df / | awk 'END{str=$5; sub(/%/, "", str); print str}')
UNIT="Percent"
DIMENSIONS="App=viewcount"
AWS_DEFAULT_REGION=$AWS_REGION aws cloudwatch put-metric-data \
    --namespace $NAMESPACE \
    --metric-name $NAME \
    --unit $UNIT \
    --value $VALUE \
    --dimensions $DIMENSIONS
