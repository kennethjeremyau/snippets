#!/usr/bin/env bash

aws iam list-users | jq -r '.Users[] | .Arn'
