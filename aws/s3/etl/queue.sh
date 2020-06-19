#!/bin/sh

SQS_QUEUE_PREFIX="$1"

[ -z "$SQS_QUEUE_PREFIX" ] && {
    echo FATAL: missing sqs queue prefix 1>&2
    exit 1
}

FAILED_QUEUE_URL=$(aws sqs create-queue \
    --queue-name "$SQS_QUEUE_PREFIX-failed" \
    --query QueueUrl \
    --output text)

FAILED_QUEUE_ARN=$(aws sqs get-queue-attributes \
    --queue-url "$FAILED_QUEUE_URL" \
    --attribute-names QueueArn \
    --query Attributes.QueueArn \
    --output text)

QUEUE_URL=$(aws sqs create-queue \
    --queue-name "$SQS_QUEUE_PREFIX" \
    --attributes "RedrivePolicy=\"{
        \\\"deadLetterTargetArn\\\":\\\"$FAILED_QUEUE_ARN\\\",
        \\\"maxReceiveCount\\\":\\\"20\\\"
    }\"" \
    --query QueueUrl \
    --output text)

while read line; do
    aws sqs send-message \
        --queue-url "$QUEUE_URL" \
        --message-body "$line" > /dev/null
    echo "$line"
done
