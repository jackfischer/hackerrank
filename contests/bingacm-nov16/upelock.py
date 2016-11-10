from math import sqrt

data = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ],
    [ None, 0, None ]
    ]

locs = dict()
for i in range(len(data)):
    for j in range(len(data[i])):
        locs[data[i][j]] = (i,j)

def dist(a: int, b: int) -> float:
    a1, a2 = locs[a]
    b1, b2 = locs[b]
    delta1 = abs(a1-b1)
    delta2 = abs(a2-b2)
    return sqrt((delta1 * delta1) + (delta2 * delta2))
    
    
nums = [int(i) for i in input()]
total = 0.0
for i in range(len(nums) - 1):
    total += dist(nums[i], nums[i+1])
    
print("%.2fin" % total)

"""
categories:
immediate 1
diagonal immediate root(2)
square diag root(8)
narrow diag root(5)

"""
