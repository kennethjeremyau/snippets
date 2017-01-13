#!/usr/bin/env bash

aws iam put-user-policy --user-name $1 --policy-name $2 --policy-document file://user-policy.json
