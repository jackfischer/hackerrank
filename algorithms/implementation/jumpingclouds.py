#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

pos = 0
jumps = 0

while pos < (n-1):
    if (pos+2) < n and c[pos+2] == 0:
        pos += 2
        jumps += 1
    elif (pos+1) < n and c[pos+1] == 0:
        pos += 1
        jumps += 1
    else:
        raise ValueError('A very specific bad thing happened')

    if pos == (n-1):
        print(jumps)
        break
        