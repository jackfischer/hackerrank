#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

top = float('-inf')
for i in range(0, len(arr) - 2):
    for j in range(0, len(arr[i]) - 2):
        total = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
        if total > top:
            top = total

print(top)

