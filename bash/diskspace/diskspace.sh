#!/bin/bash

df / | awk 'END{str=$5; sub(/%/, "", str); print str}'
