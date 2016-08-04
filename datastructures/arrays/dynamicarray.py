import sys

N, Q = input().strip().split(' ')
N, Q = int(N), int(Q)
sl = [[] for _ in range(N)]
ql = [input().strip().split(' ') for _ in range(0,Q)]
ql = [[int(i) for i in q] for q in ql]
lastAns = 0

for q in ql:
    i, x, y = q
    index = (x ^ lastAns) % N
    if i == 1:
        sl[index].append(y)
    else:
        lastAns = sl[index][ y % len(sl[index]) ]
        print(lastAns)
    

