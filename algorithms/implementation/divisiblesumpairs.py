#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

result = 0
for i in range(n):
    for j in range(i):
        if (a[i]+a[j]) % k == 0:
            result += 1

print(result)