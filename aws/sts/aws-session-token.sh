#!/bin/sh

JSON="$(
    aws sts get-session-token \
        --profile __PROFILE__ \
        --serial-number __MFA_ARN__ \
        --token $1
)"

AWS_ACCESS_KEY_ID="$(echo $JSON | jq -r '.Credentials.AccessKeyId')"
AWS_SECRET_ACCESS_KEY="$(echo $JSON | jq -r '.Credentials.SecretAccessKey')"
AWS_SESSION_TOKEN="$(echo $JSON | jq -r '.Credentials.SessionToken')"

aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
aws configure set aws_session_token $AWS_SESSION_TOKEN

echo "$JSON"
