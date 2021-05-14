#!/bin/sh

seq 1 3 | xargs -I {} sh "./{}.sh"
