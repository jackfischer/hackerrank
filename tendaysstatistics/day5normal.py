from math import erf, sqrt

mu, sigma = [int(x) for x in input().split()]
lt = float(input().strip())
x1, x2 = [int(x) for x in input().split()]
"""
mu = 20
sigma = 2
"""
phi = lambda x: (1 + erf( (x-mu) / (sigma * sqrt(2)) )) / 2

print("%.3f" % phi(lt))
center = phi(x2) - phi(x1)
print("%.3f" % center)

