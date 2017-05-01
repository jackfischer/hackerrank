from math import exp, factorial

lambda_ = 2.5
x = 5

def f(lambda_: float, x: int) -> float:
    return lambda_**x * exp(-lambda_) / factorial(x)

print(round(f(lambda_, x), 3))