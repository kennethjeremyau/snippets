#!/usr/bin/env bash

d=$(date -I -d "2017-01-01 - 1 month" 2>/dev/null || date -jf "%Y-%m-%d" -v -1m 2017-01-01)
echo $d

IFS=" :-" read Y M D h m s <<<"YYYY-MM-DD hh:mm:ss"
d="$Y-$M-$D $h:$m:$s"
echo $d
