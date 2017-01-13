#!/usr/bin/env bash

aws iam list-policies | jq -r '.Policies[] | .Arn'
