import sys

def vector_multiply(a,b):
    return [ai*bi for ai,bi in zip(a,b)]

X, Y = zip(*[map(int, tuple(line.split())) for line in sys.stdin])
n = len(X)

b = (n*sum(vector_multiply(X,Y)) - sum(X)*sum(Y)) / (n*sum(vector_multiply(X,X)) - sum(X)**2)

a = (sum(Y) / n) - (sum(X) / n)*b

x = 80
print(a + x*b)
