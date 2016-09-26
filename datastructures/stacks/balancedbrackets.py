#!/bin/python3

import sys


t = int(input().strip())
corresponds = {'(': ')', '{': '}', '[': ']'}

for _ in range(t):
    s = input().strip()
    #print(s)
    stack = list()
    
    for c in s:
        if c in corresponds: #left bracket
            stack.append(c)
        elif len(stack) != 0: #right bracket
            left = stack.pop()
            if corresponds[left] != c:
                print("NO")
                break
        else: #not enough left elements
            print("NO")
            break
    else:
        if len(stack) == 0: #normal correct completion
            print("YES")
        else: #left over left elements
            print("NO")
            
    
    
  