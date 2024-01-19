#!/bin/bash

# Simple argument parsing.
# Limitations:
#   - Doesn't handle positional arguments.  All arguments uses flags..
#   - No long flags.

function usage {
    echo "Usage: $(basename $0) [-h] [-a <arg>]" >&2
}

while getopts ":ha:" opt; do
    case $opt in
        a)
            arg=${OPTARG}
            echo "Argument: $arg"
            ;;
        h)
            usage
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            ;;
    esac
done
