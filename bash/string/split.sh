#!/usr/bin/env bash

IN='test|0'
IFS='|' read -ra ARRAY <<< "$IN"
for i in "${ARRAY[@]}"; do
    echo "$i"
done
