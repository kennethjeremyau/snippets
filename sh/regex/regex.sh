#!/bin/sh

echo 1 | grep -Eq '^[0-9]+$' && echo true || echo false
