#!/usr/bin/env bash

awk '{print gsub(/a/,"")}' input.txt
