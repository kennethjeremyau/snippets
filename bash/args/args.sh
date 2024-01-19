#!/bin/bash

function usage {
    echo "Usage: $(basename $0)" >&2
}

while [ "$#" -gt 0 ]; do
    case $1 in
    -h|--help)
        usage
        exit 0
        ;;
    -n|--number)
        NUMBER="$2"
        shift # past argument
        shift # past value
        ;;
    -*|--*)
        echo "ERROR unknown option $1" >&2
        exit 1
        ;;
    *)
        echo "POSITIONAL ARGUMENT $1"
        shift # past value
    esac
done

[ -z "$NUMBER" ] && {
    echo ERROR number required >&2
    exit 1
}

echo NUMBER = "${NUMBER}"
