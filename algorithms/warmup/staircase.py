#!/bin/python3

import sys


n = int(input().strip())

pounds = 1
while pounds <= n:
    print(' '*(n-pounds) + ('#'*pounds))
    pounds += 1
    
    
    
    
    