#!/bin/sh

SQS_QUEUE_PREFIX="$1"
S3_BUCKET="$2"

[ -z "$SQS_QUEUE_PREFIX" ] && {
    echo FATAL: missing sqs queue prefix 1>&2
    exit 1
}

[ -z "$S3_BUCKET" ] && {
    echo FATAL: missing s3 bucket 1>&2
    exit 1
}

QUEUE_URL=$(aws sqs get-queue-url \
    --queue-name "$SQS_QUEUE_PREFIX" \
    --query QueueUrl \
    --output text)

while true; do

    MESSAGE=$(aws sqs receive-message \
        --queue-url "$QUEUE_URL" \
        --wait-time-seconds 20)

    REMOTE_FILE=$(echo "$MESSAGE" | jq -r '.Messages[0].Body')

    LOCAL_FILE=$(echo "$MESSAGE" | jq -r '.Messages[0].MessageId')

    aws s3api get-object \
        --bucket "$S3_BUCKET" \
        --key "$REMOTE_FILE" \
        "$LOCAL_FILE" > /dev/null

    # Unzip if gzipped.
    file "$LOCAL_FILE" | grep 'gzip compressed data' > /dev/null && {
        gunzip < "$LOCAL_FILE" > "$LOCAL_FILE.gunzip"
        mv "$LOCAL_FILE.gunzip" "$LOCAL_FILE"
    }

    # Delete lines with content_code "EU".
    sed '/"continent_code":"EU"/d' "$LOCAL_FILE" > "$LOCAL_FILE.gdpr"

    gzip "$LOCAL_FILE.gdpr"

    # Upload.
    aws s3api put-object \
        --bucket "gdpr.gfycat.com" \
        --key "$REMOTE_FILE" \
        --body "$LOCAL_FILE.gdpr.gz" > /dev/null

    # Cleanup.
    rm "$LOCAL_FILE"*

    SQS_RECEIPT_HANDLE=$(echo "$MESSAGE" | jq -r '.Messages[0].ReceiptHandle')

    aws sqs delete-message \
        --queue-url "$QUEUE_URL" \
        --receipt-handle "$SQS_RECEIPT_HANDLE"

    echo "$REMOTE_FILE"

done
