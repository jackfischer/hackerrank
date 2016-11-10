#!/bin/python3

import sys

s = input().strip()

words = 1
for i in s:
    if i.isupper():
        words += 1
        
if s:
    print(words)
else:
    print("0")
    
    