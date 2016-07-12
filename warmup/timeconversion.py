#!/bin/python3

import sys


time = input().strip()
t = time.split(':')
h = int(t[0])
m = t[1]
s = t[2][0:2]

if h == 12 and time[-2] == 'A':
    h = 0
if h != 12 and time[-2] == 'P':
    h += 12
    
if h < 10:
    h = '0'+str(h)
else:
    h = str(h)
    
#result = [str(i) for i in [h,m,s]]

print(':'.join((h, m, s)))
