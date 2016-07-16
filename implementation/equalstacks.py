#!/bin/python3

import sys


n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]
h1.reverse()
h2.reverse()
h3.reverse()

top = 0
current = [0,0,0]
pos = [0,0,0]
blocks = [h1, h2, h3]
#print(blocks)
for i_ in range(2*sum((n1,n2,n3))):
    i = i_ % 3
    if current[i] < max(current) or (current[0] == current[1] and current[1] == current[2]):
        if pos[i] < len(blocks[i]):
            current[i] += blocks[i][pos[i]]
            pos[i] += 1

    if (current[0] == current[1] and current[1] == current[2]):
        top = current[0]
    #print((c1,c2,c3))
        
print(top)



