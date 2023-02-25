#!/usr/bin/env bash

HELP="false"

while [ "$#" -gt 0 ]; do
    case $1 in
    -h|--help)
        HELP="true"
        ;;
    -n|--number)
        NUMBER="$2"
        shift
        ;;
    -*|--*)
        echo "ERROR unknown option $1" 1>&2
        exit 1
        ;;
    esac
    shift
done

[ -z "$NUMBER" ] && {
    echo ERROR number required 1>&2
    exit 1
}

echo HELP = "${HELP}"
echo NUMBER = "${NUMBER}"
