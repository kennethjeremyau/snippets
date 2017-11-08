#!/usr/bin/env bash

function e {
    echo "$1"
    return 1
}

e hello\ world
echo $?
