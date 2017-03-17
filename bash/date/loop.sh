#!/usr/bin/env bash

d="2017-02-14T07:00:00+00:00"
while [ "$d" != "2017-03-08T23:00:00+00:00" ]; do 
    echo $(gdate -d "$d" "+%Y-%m-%d-%H-%M-%S")
    d=$(TZ=UTC gdate -Iseconds -d "$d + 1 hour")
done
