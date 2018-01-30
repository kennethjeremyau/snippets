#!/bin/bash

BUCKET='bucket'
PREFIX='prefix'
aws s3api list-objects --bucket $BUCKET --prefix $PREFIX --query 'Contents[].[Key]' --output text
