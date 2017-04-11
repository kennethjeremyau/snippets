#!/usr/bin/env bash

ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o ProxyCommand="ssh $1 nc %h %p" $2
