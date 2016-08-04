#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)


diff = 0
for i in range(n):
    row = a[i]
    diff += row[i]
    diff -= row[-i-1]
    
if diff < 0:
    diff = diff * -1

print(diff)
    
    
