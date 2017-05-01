#Geometric distribution is special case of negative binomial where number of desired successes is 1
p_success = 1 / 3
n = 5
p_failure = 1 - p_success
p_n = p_failure ** (n-1) * p_success
print(round(p_n, 3))