#!/usr/bin/env bash

aws opsworks describe-stacks | jq -r '.[][] | .Name + " (" + .StackId + ")"'
