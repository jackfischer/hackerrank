def traverseA(a, m):
    for i in range(len(a)):
        if a[i] < m:
            for j in range(i + 1, len(a)):
                #print("i is %d j is %d" % (i,j))
                if a[i] + a[j] == m:
                    return (str(i+1), str(j+1))        

t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = traverseA(a, m)
    print(" ".join(result))
    
        