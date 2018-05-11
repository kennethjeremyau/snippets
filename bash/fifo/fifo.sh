#!/bin/bash

f=pipe.fifo
trap "rm -f $f" EXIT HUP INT TERM
[ ! -p "$f" ] && mkfifo "$f"

# writer
echo transfer > "$f" &

# reader
while read -r line; do
    echo $line
done < "$f" &
