#!/usr/bin/env bash

array=( one two three )
for i in "${array[@]}"
do
    echo $i
done
