#!/usr/bin/env bash

wc -l < input.txt | awk '{print $1}'
