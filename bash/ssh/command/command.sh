#!/usr/bin/env bash

ssh $1 "nohup $2 > nohup.out 2>&1 &"
