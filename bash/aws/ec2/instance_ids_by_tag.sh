#!/usr/bin/env bash

aws ec2 describe-instances --filters Name=tag-key,Values="Name",Name=tag-value,Values="$1" | jq -r '.[][][][]?["InstanceId"]'
