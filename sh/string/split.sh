#!/bin/sh

str="test|0"
f1=$(echo $str | cut -d '|' -f1)
f2=$(echo $str | cut -d '|' -f2)
echo "$f1, $f2"
