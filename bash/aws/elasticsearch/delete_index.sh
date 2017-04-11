#!/usr/bin/env bash

# Endpoint is first argument.
# Index name is second argument.
curl -XDELETE "$1/$2"
