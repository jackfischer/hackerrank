
n = int(input())
queries = [ [int(i) for i in input().split(' ')] for _ in range(n)]

stack = list()
maxes = [float("-inf")]

for q in queries:
    if q[0] == 1:
        stack.append(q[1])
        if q[1] > maxes[-1]:
            maxes.append(q[1])
        else:
            maxes.append(maxes[-1])
            
    if q[0] == 2:
        stack.pop()
        maxes.pop()
        
    if q[0] == 3:
        print(maxes[-1])
        
