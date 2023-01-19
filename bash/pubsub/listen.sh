#!/bin/bash

tail -f -n 0 topic | while read line; do echo $line; done
