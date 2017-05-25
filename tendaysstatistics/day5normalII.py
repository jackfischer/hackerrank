from math import erf, sqrt

mu, sigma = [int(x) for x in input().split()]
gt = int(input())
passing = int(input())

phi = lambda x: 100 * (1 + erf( (x-mu) / (sigma * sqrt(2)) )) / 2

print("%.2f" % (100-phi(gt)))
print("%.2f" % (100-phi(passing)))
print("%.2f" % phi(passing))
