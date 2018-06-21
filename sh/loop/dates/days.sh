#!/bin/sh

d=2017-04-06
while [ "$d" != 2017-07-31 ]; do 
    echo $d
    d=$(date -d @$(( $(date -d $d +%s) + 86400 )) +%Y-%m-%d)
done
