n, k = input().strip().split(' ')
n = int(n)
k = int(k)
a = [int(i) for i in input().strip().split(' ')]

comps = [i % k for i in a]
comp_accum = [0] * k #list of frequencies of occurances of comps
for i in comps:
    comp_accum[i] += 1

total = 1 if comp_accum[0] == 1 else 0 #zeros, always compatible
upperbound = ((k-1)//2)+1
for i in range(1, upperbound): #calculate midpoint
    #print(i)
    total += max( (comp_accum[i], comp_accum[k-i]) )

if k % 2 == 0:
    total += comp_accum[upperbound]
print(total)
