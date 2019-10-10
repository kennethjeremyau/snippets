#!/bin/bash

aws cloudsearchdomain --endpoint-url "$ENDPOINT" search \
    --search-query "$QUERY" \
    --query-options '{"defaultOperator": "or"}' \
    --return '_no_fields' \
    --size '10000'
