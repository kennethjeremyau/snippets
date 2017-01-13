#!/usr/bin/env bash

aws opsworks describe-instances --layer-id $1 | jq -r '.Instances[] | .Hostname + " (" + .Ec2InstanceId + ")"'
