#!/usr/bin/env bash

find ./input -type f -name '*.gz' -exec gunzip "{}" \;
