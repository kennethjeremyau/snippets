#!/bin/bash

N=5
for i in $(seq 1 "$N"); do
    split -n "l/$i/$N" data.csv | cat &
done
wait
