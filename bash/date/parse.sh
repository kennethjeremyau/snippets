#!/usr/bin/env bash

# Uses GNU date which is not available by default on Mac.
d=$(date -I -d "2017-01-01 - 1 month")
echo $d

IFS=" :-" read Y M D h m s <<<"YYYY-MM-DD hh:mm:ss"
d="$Y-$M-$D $h:$m:$s"
echo $d
