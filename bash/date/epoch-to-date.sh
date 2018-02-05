#!/usr/bin/env bash

date -d @"$@" 2>/dev/null || date -r $@
