#!/usr/bin/env bash

FILES=./input/*
for f in $FILES; do
  echo "Processing $f file..."
  cat $f
done
