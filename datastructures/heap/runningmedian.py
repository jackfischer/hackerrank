# Enter your code here. Read input from STDIN. Print output to STDOUT

import heapq


N = int(input())
left = [] #max heap
right = [] #min heap

for _ in range(N):
    new = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -new)
    else:
        heapq.heappush(right, new)
        
    if right and -left[0] > right[0]: #Crossed
        temp = heapq.heapreplace(right, -heapq.heappop(left))
        heapq.heappush(left, -temp)
        
    if len(left) > len(right):
        print(float(-left[0]))
    else:
        print(float(-left[0] + right[0]) / 2)
        
    