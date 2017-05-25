from math import sqrt

n = int(input())
X = [float(x) for x in input().split()]
Y = [float(y) for y in input().split()]

mu = lambda V: sum(V) / len(V)

def cov(X: list, Y: list) -> float:
    assert(len(X) == len(Y))
    mu_x = mu(X)
    mu_y = mu(Y)
    return sum((x-mu_x) * (y-mu_y) for x,y in zip(X,Y)) / len(X)

def variance(V: list) -> float:
    mu_v = mu(V)
    return sum((v - mu_v) ** 2 for v in V) / len(V)

pearson = cov(X, Y) / (sqrt(variance(X)) * sqrt(variance(Y)))

print("%.3f" % pearson)

