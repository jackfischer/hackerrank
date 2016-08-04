#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

rounds = n // k
thunders = [c[k*i] for i in range(rounds)]
result = 100 - (sum(thunders)*2) - rounds
print(result)
