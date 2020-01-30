#!/bin/sh

redis-cli --cluster create \
    `dig +short cluster_redis_1`:6379 \
    `dig +short cluster_redis_2`:6379 \
    `dig +short cluster_redis_3`:6379 \
    `dig +short cluster_redis_4`:6379 \
    `dig +short cluster_redis_5`:6379 \
    `dig +short cluster_redis_6`:6379 \
    --cluster-replicas 1 \
    --cluster-yes

tail -f /dev/null
