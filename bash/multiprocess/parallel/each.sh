#!/bin/bash

while read line; do
    echo "$line"
    sleep 10
    { flock -x 200; echo "$line" >> output.txt; } 200> lockfile
done
