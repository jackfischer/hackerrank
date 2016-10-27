n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

grandtotal = 0
for i in range(n):
    total = 0
    for j in range(n - 1):
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]
            total += 1
    if total == 0:
        break
    grandtotal += total

print("Array is sorted in %d swaps." % grandtotal)
print("First Element: %d" % a[0])
print("Last Element: %d" % a[n-1])
