#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())

#result = [((ord(i)+k) % 122) + 96 for i in s ]

result = []
for i in map(ord, s):
    if i >= 97 and i <= 122: #lowercase
        temp = (((i - 97) + k) % 26) + 97
    elif i >= 65 and i <= 90: #uppercase
        temp = (((i - 65) + k) % 26) + 65
    else: #non alpha character
        temp = i
    result.append(chr(temp))

print(''.join(result))
