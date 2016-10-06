
"""
1 1
3 4
7 44
"""

s = int(input().strip())

table = {1: 1, 0: 1}

def stairs(n): #Memoized version of recursive stair-possibilities 
    if n in table:
        #print("hit table[" + str(n) + "]")
        return table[n]
    
    result = 0
    if n >= 3:
        result += stairs(n-3)
    if n >= 2:
        result += stairs(n-2)
    if n >= 1:
        result += stairs(n-1)
    
    table[n] = result
    #print("table[" + str(n) + "] = " + str(result))
    return result
    
for a0 in range(s):
    n = int(input().strip())
    result = stairs(n)
    print(result)
