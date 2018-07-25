#!/bin/sh

date -d @$(( $(date +%s) - 86400 )) +%Y-%m-%d
