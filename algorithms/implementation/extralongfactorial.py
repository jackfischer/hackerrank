#!/bin/python3

import sys


n = int(input().strip())

accum = 1
for i in range(1,n):
    accum *= i

print(accum * n)