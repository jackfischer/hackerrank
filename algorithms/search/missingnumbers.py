from collections import Counter

n1 = int(input())
A = [int(x) for x in input().split()]
n2 = int(input())
B = [int(x) for x in input().split()]

counter = Counter(A)
counter.subtract(Counter(B))
missing_letters = [k for k in counter if counter[k] != 0]
missing_letters.sort()
missing_letters = [str(x) for x in missing_letters]
result = " ".join(missing_letters)
print(result)


