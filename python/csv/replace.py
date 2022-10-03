#!/usr/bin/env python3

import csv

with open('input.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        for i in range(0, len(row)):
            row[i] = row[i].replace(',', '')
        print(','.join(row))
