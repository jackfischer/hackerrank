p_success = 1 / 3
p_failure = 1 - p_success

f = lambda n: p_failure ** (n-1) * p_success
terms = map(f , range(1, 6) )
p_total = round(sum(terms), 3)
print(p_total)