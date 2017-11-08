#!/usr/bin/env bash

# Uses GNU date which is not available by default on Mac.

d=2017-04-06
while [ "$d" != 2017-07-31 ]; do 
    echo $d
    d=$(date -I -d "+1 day")
done
