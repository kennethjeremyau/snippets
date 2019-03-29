#!/bin/sh

for f in ./staging/x??; do
    nohup cat "$f" &
done
