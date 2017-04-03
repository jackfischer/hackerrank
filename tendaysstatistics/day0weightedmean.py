import functools

N = int(input())
X = [int(x) for x in input().strip().split()]
W = [int(x) for x in input().strip().split()]

result = functools.reduce(lambda accum, pair: accum + pair[0]*pair[1], zip(X,W), 0)
result /= sum(W)

print("%.1f" % result)

