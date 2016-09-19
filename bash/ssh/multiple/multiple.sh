#!/usr/bin/env bash

SERVERS=servers.txt
while read server; do
    ssh -T $server < ./remote.sh >> stdout.txt
done < "$SERVERS"
