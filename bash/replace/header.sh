#!/bin/bash

[ $# -eq 0 ] && { echo "$0: Not enough arguments." 1>&2; exit 2; }
for f in $@; do
    DIR=$(basename $(dirname $(realpath $f)))
    NAME=$(basename $f)
    # Multiple hacks to get sed to insert newlines.
    head -1 $f | grep -q '^# .\+/.\+$' \
        || sed -i '' '1 s/^/# '"$DIR\/$NAME"'\'$'\n\\\n/' $f
done
