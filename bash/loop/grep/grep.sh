#!/bin/sh

while cat touchfile | grep "NotReady" > /dev/null; do
    sleep 1
    echo "not ready"
done
