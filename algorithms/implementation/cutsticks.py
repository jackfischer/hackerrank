#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr.sort(reverse=True)

while arr:
    print(len(arr))
    curr = arr.pop()
    arr = [i-curr for i in arr]
    arr = [i for i in arr if i > 0]
    
    