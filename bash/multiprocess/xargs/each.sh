#!/bin/bash

echo "$1"
sleep 60
{ flock -x 200; echo "$1" >> output.txt; } 200> lockfile
