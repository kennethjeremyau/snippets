#!/usr/bin/env bash

INPUT=input.txt
while read line; do
    echo $line
done < "$INPUT"
