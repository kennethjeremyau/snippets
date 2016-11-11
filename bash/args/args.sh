#!/usr/bin/env bash

HELP="false"
NUMBER=0

while [[ $# -gt 0 ]]; do
    arg="$1"
    case $arg in
    -h|--help)
        HELP="true"
        ;;
    -n|--number)
        NUMBER="$2"
        shift
        ;;
    *)
        # Unknown option
        ;;
    esac
    shift
done
echo HELP = "${HELP}"
echo NUMBER = "${NUMBER}"
