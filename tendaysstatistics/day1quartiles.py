N = int(input())
X = [int(x) for x in input().strip().split()]
X.sort()

def median(X):
    if len(X) % 2 == 1:
        return X[len(X) // 2]
    else:
        mid = len(X) // 2
        return (X[mid] + X[mid - 1]) // 2

Q1 = median(X[:len(X) // 2])
Q2 = median(X)
Q3 = median(X[len(X) // 2 + len(X) % 2:])

print(Q1)
print(Q2)
print(Q3)