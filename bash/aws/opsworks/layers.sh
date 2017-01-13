#!/usr/bin/env bash

aws opsworks describe-layers --stack-id $1 | jq -r '.[][] | .Name + " (" + .LayerId + ")"'

