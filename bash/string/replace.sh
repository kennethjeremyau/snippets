#!/bin/sh

TEXT="I love Suzy and Mary"
SUBSTRING="Sara"
echo "${TEXT/Suzy/$SUBSTRING}"
