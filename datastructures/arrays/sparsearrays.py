#!/bin/python3

N = int(input())
strings = [input() for _ in range(N)]
Q = int(input())
queries = [input() for _ in range(Q)]

counts = {}
for s in strings:
    if s in counts:
        counts[s] += 1
    else:
        counts[s] = 1
        
for q in queries:
    print(counts[q] if q in counts else 0)
