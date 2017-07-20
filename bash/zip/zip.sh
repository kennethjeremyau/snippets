#!/usr/bin/env bash

# Zip with parent folder.
zip -r9 build.zip build

# Zip without parent folder.
cd build; zip -r9 ../build_contents.zip *
