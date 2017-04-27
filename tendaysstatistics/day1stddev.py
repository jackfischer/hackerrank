N = int(input())
X = [int(x) for x in input().strip().split()]

u = sum(X) / len(X)

sigma = pow( sum( map(lambda x: pow(x - u, 2), X) ) / N, 1/2)
print("%.1f" % sigma)