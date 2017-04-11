#!/usr/bin/env bash

# Endpoint is first argument.
# Index name is second argument.
# JSON to add is third argument.
curl -XPUT '%1/%2' -d '%3'
