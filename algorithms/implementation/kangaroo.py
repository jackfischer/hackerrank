#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

'''
def checker():
    if x1 == x2:
        return True
    elif x1 < x2 and v1 < v2:
        return False
    elif x1 > x2 and v1 > v2:
        return False
    else:
        return None

    
while True:
    check = checker()
    if check == True:
        print("YES")
        break
    if check == False:
        print("NO")
        break
    x1 += v1
    x2 += v2
'''


if v2 == v1:
    if x1 != x2:
        print("NO")
    else:
        print("YES")
else:
    n = (x1 - x2) / (v2 - v1)
    if n.is_integer() and n > 0:
        print("YES")
    else:
        print("NO")
    
    
    