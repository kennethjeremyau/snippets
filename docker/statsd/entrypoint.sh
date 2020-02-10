#!/bin/sh

while true; do
    echo -n "example:$((RANDOM % 100))|c" | nc -w 1 -u statsd 8125;
done
