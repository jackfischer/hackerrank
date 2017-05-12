#!/bin/python3

from math import sqrt, floor, ceil
import sys

s = input().strip()
s = s.replace(' ', '')

rows = floor(sqrt(len(s)))
cols = ceil(sqrt(len(s)))

if rows*cols < len(s) and rows < cols:
    rows += 1

for col in range(cols):
    for row in range(rows):
        index = (cols * row) + col
        if index < len(s):
            print(s[index], end='')
    print(' ', end='')

