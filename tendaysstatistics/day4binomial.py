from math import factorial

def nchoosek(n: int, k: int) ->int:
    return factorial(n) / (factorial(k) * factorial(n-k))

def f(x: int, n: int, p: float) -> float:
    return nchoosek(n, x) * (p**x) * ((1-p)**(n-x))

def F(x: int, n: int, p: float) -> float:
    return sum( f(i, n, p) for i in range(x+1) )

boys_to_girls = 1.09
p = boys_to_girls / (boys_to_girls+1)
result = 1 - F(2, 6, p)
print(round(result, 3))
