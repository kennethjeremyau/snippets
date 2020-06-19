#!/bin/sh

S3_PREFIX_URI="$1"

[ -z "$S3_PREFIX_URI" ] && {
    echo FATAL: missing s3 uri parameter. 1>&2
    exit 1
}

echo WARNING: filenames with multiple consecutive spaces may be truncated. 1>&2
aws s3 ls --recursive "$S3_PREFIX_URI" | tr -s ' ' | cut -d ' ' -f 4-
