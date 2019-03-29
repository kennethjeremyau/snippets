#!/bin/sh

mkdir staging
cd staging
cat ../data.csv | split -l 2
