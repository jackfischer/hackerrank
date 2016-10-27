from collections import Counter

def number_needed(a, b):
    cA = Counter(a)
    cB = Counter(b)
    deltaA = cA - cB
    deltaB = cB - cA
    return sum(deltaA.values()) + sum(deltaB.values())


a = input().strip()
b = input().strip()

print(number_needed(a, b))
