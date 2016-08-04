#!/bin/python3

import sys


T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    q = [int(q_temp) for q_temp in input().strip().split(' ')]
    # your code goes here
    bribes = [0]*n
    correct = [_ for _ in range(1,n+1)]
    finbase = 0
    overflow = False
    while True:
        for i in range(finbase, n-1):
            if q[i] > q[i+1]:
                bribes[q[i]-1] += 1
                if bribes[q[i]-1] == 3:
                    overflow = True
                    break
                finbase = max((i-1,0))
                q[i+1], q[i] = q[i], q[i+1] #swap
                break
        else:
            print(sum(bribes))
            break
        
        if overflow:
            print("Too chaotic")
            break
    
    