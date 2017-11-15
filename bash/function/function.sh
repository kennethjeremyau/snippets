#!/usr/bin/env bash

function e {
    echo "$1"
    return 1
}

VAR=$(e hello\ world)
echo $VAR
