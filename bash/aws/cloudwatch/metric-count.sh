#!/bin/sh

if [ $# -ne 3 ]; then
    echo "$0: Not enough arguments." 1>&2
    exit 2
fi

NAMESPACE="Namespace"
NAME="$2"
UNIT="Count"
VALUE="$3"
DIMENSIONS="$1"
aws cloudwatch put-metric-data \
    --namespace $NAMESPACE \
    --metric-name $NAME \
    --unit $UNIT \
    --value $VALUE \
    --dimensions $DIMENSIONS
