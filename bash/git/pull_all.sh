#!/usr/bin/env bash

find . -type d -maxdepth 1 | xargs -I{} bash -c 'pushd {}; git pull origin master; popd;'
